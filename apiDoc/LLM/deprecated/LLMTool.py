```python
#!/usr/bin/env python3

"""
LLMTool.py
==========

Autonomous Lua/Python API assistant and migration agent.

Uses an LLM through OpenRouter and a local or remote API
documentation repository.

Example:

    py LLMTool.py "convert the script with name xxx that is attached to object yyy to the current version of the software"

Force API index regeneration:

    py LLMTool.py --reset-index "find all deprecated API calls in the project"

The API documentation is expected to contain:

    context.txt

    categories.cat

    *.category

    *.method

    *.property

    list.deprecated

    *.deprecated


The agent currently deals with Lua and Python API usage.
"""


# ============================================================
# CONFIGURATION
# ============================================================

# ------------------------------------------------------------
# API documentation location
# ------------------------------------------------------------

# Local example:
API_ROOT = r"D:\CoppeliaSim\api"

# Remote example:
#
# API_ROOT = "https://example.com/coppeliasim/api/"


# ------------------------------------------------------------
# Project directory
# ------------------------------------------------------------

PROJECT_ROOT = r"D:\MyProject"


# ------------------------------------------------------------
# OpenRouter model
# ------------------------------------------------------------

# OpenRouter API key is read from the environment:
#
#     OPENROUTER_API_KEY
#
# PowerShell:
#
#     $env:OPENROUTER_API_KEY="sk-or-..."
#
# CMD:
#
#     set OPENROUTER_API_KEY=sk-or-...

MODEL = "openai/gpt-5"


# ------------------------------------------------------------
# API index
# ------------------------------------------------------------

# Rebuild the index when this much time has elapsed since
# the previous invocation of LLMTool.py.
#
# Examples:
#
#     3600        = 1 hour
#     86400       = 1 day
#     604800      = 1 week
#
# Set to 0 to rebuild every time.

INDEX_TIMEOUT_SECONDS = 7 * 24 * 60 * 60


# The persistent index is stored next to this script.

INDEX_FILENAME = "LLMTool_api_index.json"


# ------------------------------------------------------------
# Agent
# ------------------------------------------------------------

MAX_ITERATIONS = 50

# Maximum size of a single file that may be read.

MAX_FILE_SIZE = 2 * 1024 * 1024

# Maximum number of project files returned by list_files().

MAX_LIST_FILES = 3000

# Maximum number of search results.

MAX_SEARCH_RESULTS = 300


# ============================================================
# IMPORTS
# ============================================================

import os
import sys
import json
import time
import argparse
import subprocess

from pathlib import Path
from urllib.parse import urljoin

import requests
from openai import OpenAI


# ============================================================
# GLOBAL PATHS
# ============================================================

SCRIPT_DIR = Path(
    __file__
).resolve()

INDEX_PATH = (
    SCRIPT_DIR /
    INDEX_FILENAME
)

PROJECT_DIR = Path(
    PROJECT_ROOT
).resolve()

API_ROOT = (
    API_ROOT.rstrip("/")
    + "/"
)


# ============================================================
# OPENROUTER
# ============================================================

OPENROUTER_API_KEY = os.environ.get(
    "OPENROUTER_API_KEY"
)

if not OPENROUTER_API_KEY:

    print(
        "ERROR: OPENROUTER_API_KEY environment variable "
        "is not set.",
        file=sys.stderr
    )

    print(
        "\nPowerShell example:\n"
        '  $env:OPENROUTER_API_KEY="sk-or-..."',
        file=sys.stderr
    )

    sys.exit(1)


client = OpenAI(

    base_url=
        "https://openrouter.ai/api/v1",

    api_key=
        OPENROUTER_API_KEY,
)


# ============================================================
# API DOCUMENTATION ACCESS
# ============================================================

def api_is_url():

    return (
        API_ROOT.startswith(
            "http://"
        )
        or
        API_ROOT.startswith(
            "https://"
        )
    )


def api_root_identifier():

    return API_ROOT


def api_get(
    filename
):
    """
    Retrieve an API documentation file.

    Supports:

        local filesystem

    or:

        HTTP/HTTPS
    """

    filename = (
        filename
        .replace("\\", "/")
        .lstrip("/")
    )


    # --------------------------------------------------------
    # Remote
    # --------------------------------------------------------

    if api_is_url():

        url = urljoin(
            API_ROOT,
            filename
        )

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        return response.text


    # --------------------------------------------------------
    # Local
    # --------------------------------------------------------

    api_root_path = Path(
        API_ROOT
    ).resolve()

    path = (
        api_root_path /
        filename
    ).resolve()


    # Prevent path traversal.

    try:

        path.relative_to(
            api_root_path
        )

    except ValueError:

        raise ValueError(
            "API documentation path escapes API_ROOT."
        )


    if not path.is_file():

        raise FileNotFoundError(
            f"API documentation file not found: "
            f"{filename}"
        )


    if (
        path.stat().st_size
        > MAX_FILE_SIZE
    ):

        raise ValueError(
            f"API documentation file is too large: "
            f"{filename}"
        )


    return path.read_text(
        encoding="utf-8",
        errors="replace"
    )


# ============================================================
# CONTEXT
# ============================================================

def read_context():

    return api_get(
        "context.txt"
    )


# ============================================================
# CATEGORIES
# ============================================================

def parse_categories():
    """
    Parse categories.cat.

    Example:

        name: object
        description: object
        file: object.category

        name: app
        description: app
        file: app.category
    """

    text = api_get(
        "categories.cat"
    )

    categories = []

    current = {}


    def finish():

        nonlocal current

        if current and "file" in current:

            categories.append(
                current
            )

        current = {}


    for line in text.splitlines():

        stripped = line.strip()

        if not stripped:

            finish()

            continue


        if ":" not in line:

            continue


        key, value = line.split(
            ":",
            1
        )

        current[
            key.strip()
        ] = value.strip()


    finish()

    return categories


def parse_category_entries(
    category_text,
    category_filename
):
    """
    Parse a *.category file.

    Only methods and properties are indexed.
    """

    entries = []

    current = {}


    def finish():

        nonlocal current

        if not current:

            return


        entry_type = (
            current.get(
                "type",
                ""
            )
            .strip()
            .lower()
        )

        filename = (
            current.get(
                "file",
                ""
            )
            .strip()
        )


        if entry_type not in {
            "method",
            "property"
        }:

            current = {}

            return


        if not (
            filename.endswith(
                ".method"
            )
            or
            filename.endswith(
                ".property"
            )
        ):

            current = {}

            return


        current["category"] = (
            category_filename
        )

        entries.append(
            current
        )

        current = {}


    for line in category_text.splitlines():

        stripped = line.strip()

        if not stripped:

            finish()

            continue


        if ":" not in line:

            continue


        key, value = line.split(
            ":",
            1
        )

        current[
            key.strip()
        ] = value.strip()


    finish()

    return entries


# ============================================================
# DEPRECATED API PARSING
# ============================================================

def parse_deprecated_file(
    text
):
    """
    Parse a .deprecated file.

    Example:

        name: sim.writeCustomStringData
        description: Deprecated. See properties instead
        luaSynopsis: ...
        pythonSynopsis: ...

        inputs:
        1. objectHandle: ...
        2. tagName: ...
        3. data: ...

        outputs:
        1. result: ...

        replacedBy:
        - name: setStringProperty, class: object,
          object_setStringProperty.method,
          note: "use a 'customData.'-prefix..."
    """

    result = {

        "name":
            "",

        "description":
            "",

        "luaSynopsis":
            "",

        "pythonSynopsis":
            "",

        "inputs":
            [],

        "outputs":
            [],

        "replacedBy":
            []
    }


    lines = text.splitlines()

    section = None


    for line in lines:

        stripped = line.strip()

        if not stripped:

            continue


        # ----------------------------------------------------
        # Top-level fields
        # ----------------------------------------------------

        if stripped.startswith(
            "name:"
        ):

            result["name"] = (
                stripped[
                    len("name:"):
                ].strip()
            )

            section = None

            continue


        if stripped.startswith(
            "description:"
        ):

            result["description"] = (
                stripped[
                    len("description:"):
                ].strip()
            )

            section = None

            continue


        if stripped.startswith(
            "luaSynopsis:"
        ):

            result["luaSynopsis"] = (
                stripped[
                    len("luaSynopsis:"):
                ].strip()
            )

            section = None

            continue


        if stripped.startswith(
            "pythonSynopsis:"
        ):

            result["pythonSynopsis"] = (
                stripped[
                    len("pythonSynopsis:"):
                ].strip()
            )

            section = None

            continue


        # ----------------------------------------------------
        # Sections
        # ----------------------------------------------------

        if stripped == "inputs:":

            section = "inputs"

            continue


        if stripped == "outputs:":

            section = "outputs"

            continue


        if stripped == "replacedBy:":

            section = "replacedBy"

            continue


        # ----------------------------------------------------
        # Inputs / outputs
        # ----------------------------------------------------

        if section in {
            "inputs",
            "outputs"
        }:

            value = stripped


            # Remove "-".
            if value.startswith("-"):

                value = (
                    value[1:]
                    .strip()
                )


            # Remove numeric prefix:
            #
            # 1. objectHandle: ...

            if value and value[0].isdigit():

                dot = value.find(".")

                if dot >= 0:

                    value = (
                        value[
                            dot + 1:
                        ]
                        .strip()
                    )


            if ":" in value:

                name, description = (
                    value.split(
                        ":",
                        1
                    )
                )

                result[
                    section
                ].append({

                    "name":
                        name.strip(),

                    "description":
                        description.strip()
                })


            continue


        # ----------------------------------------------------
        # replacedBy
        # ----------------------------------------------------

        if section == "replacedBy":

            if not stripped.startswith("-"):

                continue


            value = (
                stripped[1:]
                .strip()
            )


            replacement = {}


            # ------------------------------------------------
            # We parse the known fields.
            #
            # This is intentionally tolerant rather than
            # trying to implement a complete YAML parser.
            # ------------------------------------------------

            fields = [
                "name",
                "class",
                "file",
                "note"
            ]


            positions = []

            for field in fields:

                marker = (
                    field + ":"
                )

                position = value.find(
                    marker
                )

                if position >= 0:

                    positions.append(
                        (
                            position,
                            field,
                            len(marker)
                        )
                    )


            positions.sort()


            for i, item in enumerate(
                positions
            ):

                position, field, marker_length = (
                    item
                )


                start = (
                    position
                    + marker_length
                )


                if i + 1 < len(
                    positions
                ):

                    end = (
                        positions[
                            i + 1
                        ][0]
                    )

                    # Usually preceded by comma.
                    field_value = (
                        value[
                            start:end
                        ]
                        .strip()
                        .strip(",")
                        .strip()
                    )

                else:

                    field_value = (
                        value[start:]
                        .strip()
                        .strip(",")
                        .strip()
                    )


                # Remove surrounding quotes.

                if (
                    len(field_value) >= 2
                    and
                    (
                        (
                            field_value[0]
                            == '"'
                            and
                            field_value[-1]
                            == '"'
                        )
                        or
                        (
                            field_value[0]
                            == "'"
                            and
                            field_value[-1]
                            == "'"
                        )
                    )
                ):

                    field_value = (
                        field_value[1:-1]
                    )


                replacement[field] = (
                    field_value
                )


            if replacement:

                result[
                    "replacedBy"
                ].append(
                    replacement
                )


    return result


def parse_deprecated_entries():
    """
    Parse list.deprecated and enrich each entry with the
    corresponding .deprecated documentation.
    """

    text = api_get(
        "list.deprecated"
    )

    entries = []


    for line in text.splitlines():

        line = line.strip()

        if not line:

            continue

        if "-->" not in line:

            continue


        old_name, filename = (
            line.split(
                "-->",
                1
            )
        )


        old_name = (
            old_name.strip()
        )

        filename = (
            filename.strip()
        )


        if not old_name or not filename:

            continue


        entry = {

            "name":
                old_name,

            "file":
                filename,

            "deprecated":
                True
        }


        # ----------------------------------------------------
        # Read detailed deprecated file
        # ----------------------------------------------------

        try:

            detailed_text = api_get(
                filename
            )

            details = (
                parse_deprecated_file(
                    detailed_text
                )
            )


            entry["name"] = (
                old_name
            )


            for key in [

                "description",

                "luaSynopsis",

                "pythonSynopsis",

                "inputs",

                "outputs",

                "replacedBy"
            ]:

                value = details.get(
                    key
                )

                if value:

                    entry[key] = value


        except Exception as e:

            print(
                f"  WARNING: could not read "
                f"{filename}: {e}"
            )


        entries.append(
            entry
        )


    return entries


# ============================================================
# API INDEX
# ============================================================

def build_api_index():

    print()
    print("=" * 60)
    print("BUILDING API INDEX")
    print("=" * 60)
    print()

    start_time = time.time()


    # --------------------------------------------------------
    # Categories
    # --------------------------------------------------------

    categories = parse_categories()

    print(
        f"Found {len(categories)} API categories."
    )


    # --------------------------------------------------------
    # Current API
    # --------------------------------------------------------

    entries = []


    for number, category in enumerate(
        categories,
        1
    ):

        category_name = category.get(
            "name",
            ""
        )

        category_file = category.get(
            "file",
            ""
        )


        if not category_file:

            continue


        print(
            f"[{number}/{len(categories)}] "
            f"{category_name}"
        )


        try:

            text = api_get(
                category_file
            )

        except Exception as e:

            print(
                f"  WARNING: cannot read "
                f"{category_file}: {e}"
            )

            continue


        category_entries = (
            parse_category_entries(
                text,
                category_file
            )
        )


        entries.extend(
            category_entries
        )


    # --------------------------------------------------------
    # Deprecated API
    # --------------------------------------------------------

    print()
    print(
        "Reading deprecated API documentation..."
    )


    try:

        deprecated = (
            parse_deprecated_entries()
        )

    except Exception as e:

        print(
            f"WARNING: could not read "
            f"list.deprecated: {e}"
        )

        deprecated = []


    # --------------------------------------------------------
    # Construct index
    # --------------------------------------------------------

    now = time.time()


    index = {

        "version":
            3,

        "api_root":
            api_root_identifier(),

        "created":
            now,

        "last_used":
            now,

        "categories":
            categories,

        "entries":
            entries,

        "deprecated":
            deprecated
    }


    # --------------------------------------------------------
    # Atomic write
    # --------------------------------------------------------

    temporary_path = (
        INDEX_PATH.with_suffix(
            ".tmp"
        )
    )


    temporary_path.write_text(

        json.dumps(
            index,
            ensure_ascii=False,
            indent=2
        ),

        encoding="utf-8"
    )


    temporary_path.replace(
        INDEX_PATH
    )


    elapsed = (
        time.time()
        - start_time
    )


    print()
    print(
        f"Indexed {len(entries)} "
        f"current methods/properties."
    )

    print(
        f"Indexed {len(deprecated)} "
        f"deprecated APIs."
    )

    print(
        f"Index created in "
        f"{elapsed:.2f} seconds."
    )

    print(
        f"Index file: {INDEX_PATH}"
    )

    print()


    return index


def load_api_index():

    if not INDEX_PATH.is_file():

        return None


    try:

        return json.loads(
            INDEX_PATH.read_text(
                encoding="utf-8"
            )
        )

    except Exception as e:

        print(
            f"WARNING: could not load API index: "
            f"{e}"
        )

        return None


def index_needs_rebuild(
    index
):

    if index is None:

        return True


    # Different documentation source.

    if (
        index.get("api_root")
        != api_root_identifier()
    ):

        print(
            "API_ROOT changed. "
            "Rebuilding index."
        )

        return True


    # Old index version.

    if (
        index.get(
            "version",
            0
        )
        < 3
    ):

        print(
            "Old API index format detected. "
            "Rebuilding index."
        )

        return True


    if "entries" not in index:

        return True


    if "deprecated" not in index:

        return True


    # Rebuild every invocation.

    if (
        INDEX_TIMEOUT_SECONDS == 0
    ):

        return True


    last_used = index.get(
        "last_used"
    )


    if last_used is None:

        return True


    elapsed = (
        time.time()
        - last_used
    )


    if (
        elapsed
        >= INDEX_TIMEOUT_SECONDS
    ):

        print(
            f"API index has expired "
            f"({elapsed:.0f} seconds old)."
        )

        return True


    return False


def update_index_last_used(
    index
):

    index["last_used"] = (
        time.time()
    )


    INDEX_PATH.write_text(

        json.dumps(
            index,
            ensure_ascii=False,
            indent=2
        ),

        encoding="utf-8"
    )


def reset_api_index():

    if INDEX_PATH.exists():

        INDEX_PATH.unlink()

        print(
            f"Deleted API index: "
            f"{INDEX_PATH}"
        )

    else:

        print(
            "No existing API index."
        )


def initialize_api_index(
    force_reset=False
):

    if force_reset:

        print(
            "Manual API index reset requested."
        )

        reset_api_index()

        return build_api_index()


    index = load_api_index()


    if index_needs_rebuild(
        index
    ):

        return build_api_index()


    update_index_last_used(
        index
    )


    print(
        f"Using existing API index "
        f"({len(index['entries'])} "
        f"current methods/properties, "
        f"{len(index['deprecated'])} "
        f"deprecated APIs)."
    )


    return index


# ============================================================
# API SEARCH
# ============================================================

def api_search(
    query,
    index
):
    """
    Search current and deprecated API information.
    """

    query = (
        query
        .lower()
        .strip()
    )


    if not query:

        return []


    words = [
        word
        for word in query.split()
        if word
    ]


    results = []


    # --------------------------------------------------------
    # Current API
    # --------------------------------------------------------

    for entry in index.get(
        "entries",
        []
    ):

        name = entry.get(
            "name",
            ""
        )

        api_class = entry.get(
            "class",
            ""
        )

        entry_type = entry.get(
            "type",
            ""
        )

        description = entry.get(
            "description",
            ""
        )


        searchable = " ".join([

            name,

            api_class,

            entry_type,

            description

        ]).lower()


        score = 0


        if query in searchable:

            score += 20


        if query == name.lower():

            score += 100


        if query in name.lower():

            score += 50


        for word in words:

            if word in name.lower():

                score += 20

            elif word in api_class.lower():

                score += 10

            elif word in description.lower():

                score += 5


        if score > 0:

            results.append({

                "name":
                    name,

                "class":
                    api_class,

                "type":
                    entry_type,

                "description":
                    description,

                "file":
                    entry.get(
                        "file",
                        ""
                    ),

                "category":
                    entry.get(
                        "category",
                        ""
                    ),

                "deprecated":
                    False,

                "score":
                    score
            })


    # --------------------------------------------------------
    # Deprecated API
    # --------------------------------------------------------

    for entry in index.get(
        "deprecated",
        []
    ):

        name = entry.get(
            "name",
            ""
        )

        description = entry.get(
            "description",
            ""
        )

        lua_synopsis = entry.get(
            "luaSynopsis",
            ""
        )

        python_synopsis = entry.get(
            "pythonSynopsis",
            ""
        )

        replaced_by = entry.get(
            "replacedBy",
            []
        )


        searchable = " ".join([

            name,

            description,

            lua_synopsis,

            python_synopsis,

            json.dumps(
                replaced_by
            )

        ]).lower()


        score = 0


        if query in name.lower():

            score += 200

        elif query in searchable:

            score += 40


        for word in words:

            if word in name.lower():

                score += 30

            elif word in description.lower():

                score += 10

            elif word in searchable:

                score += 5


        if score > 0:

            results.append({

                "name":
                    name,

                "description":
                    description,

                "luaSynopsis":
                    lua_synopsis,

                "pythonSynopsis":
                    python_synopsis,

                "file":
                    entry.get(
                        "file",
                        ""
                    ),

                "replacedBy":
                    replaced_by,

                "deprecated":
                    True,

                "score":
                    score
            })


    results.sort(

        key=lambda x:
            x.get(
                "score",
                0
            ),

        reverse=True
    )


    return results[:30]


def api_deprecated(
    query,
    index
):
    """
    Explicit search of deprecated APIs.
    """

    query = (
        query
        .lower()
        .strip()
    )


    if not query:

        return []


    results = []


    for entry in index.get(
        "deprecated",
        []
    ):

        name = entry.get(
            "name",
            ""
        )


        searchable = json.dumps(
            entry,
            ensure_ascii=False
        ).lower()


        if query in searchable:

            results.append({

                "name":
                    name,

                "file":
                    entry.get(
                        "file",
                        ""
                    ),

                "description":
                    entry.get(
                        "description",
                        ""
                    ),

                "luaSynopsis":
                    entry.get(
                        "luaSynopsis",
                        ""
                    ),

                "pythonSynopsis":
                    entry.get(
                        "pythonSynopsis",
                        ""
                    ),

                "replacedBy":
                    entry.get(
                        "replacedBy",
                        []
                    ),

                "deprecated":
                    True
            })


    return results[:50]


def api_category(
    category,
    index
):
    """
    List current API methods/properties in a category.
    """

    category = (
        category
        .lower()
        .strip()
    )


    if not category.endswith(
        ".category"
    ):

        category += ".category"


    results = []


    for entry in index.get(
        "entries",
        []
    ):

        if (
            entry.get(
                "category",
                ""
            ).lower()
            ==
            category
        ):

            results.append(
                entry
            )


    return results


def api_file(
    filename
):
    """
    Read detailed current .method or .property documentation.
    """

    filename = (
        filename
        .replace("\\", "/")
        .strip()
    )


    if not (
        filename.endswith(
            ".method"
        )
        or
        filename.endswith(
            ".property"
        )
    ):

        raise ValueError(
            "Only .method and .property files "
            "can be accessed."
        )


    return api_get(
        filename
    )


def api_deprecated_file(
    filename
):
    """
    Read detailed .deprecated documentation.
    """

    filename = (
        filename
        .replace("\\", "/")
        .strip()
    )


    if not filename.endswith(
        ".deprecated"
    ):

        raise ValueError(
            "Only .deprecated files can be accessed."
        )


    return api_get(
        filename
    )


# ============================================================
# FIND REPLACEMENT
# ============================================================

def find_replacement(
    old_api,
    index
):
    """
    Find the documented replacement(s) for a deprecated API
    and automatically read the complete current documentation
    of those replacements.

    This is deliberately a high-level operation.

    Example:

        find_replacement(
            "sim.writeCustomStringData",
            index
        )

    can return:

        old API
        deprecated description
        old synopsis
        replacement:
            setStringProperty
            class: object
            note: use customData. prefix
            current documentation: ...

    This allows the LLM to migrate an API call without
    manually performing several separate tool calls.
    """

    query = (
        old_api
        .lower()
        .strip()
    )


    if not query:

        return {
            "error":
                "Empty API name."
        }


    candidates = []


    # --------------------------------------------------------
    # Find deprecated entry
    # --------------------------------------------------------

    for entry in index.get(
        "deprecated",
        []
    ):

        name = entry.get(
            "name",
            ""
        )


        if (
            query == name.lower()
            or
            query in name.lower()
            or
            name.lower() in query
        ):

            candidates.append(
                entry
            )


    if not candidates:

        # Try general search as fallback.

        search_results = (
            api_deprecated(
                old_api,
                index
            )
        )

        candidates = search_results


    if not candidates:

        return {

            "found":
                False,

            "oldApi":
                old_api,

            "message":
                "No deprecated API entry was found."
        }


    output = []


    for old_entry in candidates:

        replacement_results = []


        for replacement in old_entry.get(
            "replacedBy",
            []
        ):

            replacement_name = (
                replacement.get(
                    "name",
                    ""
                )
            )

            replacement_class = (
                replacement.get(
                    "class",
                    ""
                )
            )

            replacement_file = (
                replacement.get(
                    "file",
                    ""
                )
            )

            replacement_note = (
                replacement.get(
                    "note",
                    ""
                )
            )


            item = {

                "name":
                    replacement_name,

                "class":
                    replacement_class,

                "file":
                    replacement_file,

                "note":
                    replacement_note
            }


            # ------------------------------------------------
            # Find matching current API entry in index
            # ------------------------------------------------

            current_entry = None


            for candidate in index.get(
                "entries",
                []
            ):

                candidate_name = (
                    candidate.get(
                        "name",
                        ""
                    )
                )

                candidate_class = (
                    candidate.get(
                        "class",
                        ""
                    )
                )

                candidate_file = (
                    candidate.get(
                        "file",
                        ""
                    )
                )


                name_match = (

                    replacement_name
                    and
                    candidate_name.lower()
                    ==
                    replacement_name.lower()
                )


                class_match = (

                    not replacement_class
                    or
                    candidate_class.lower()
                    ==
                    replacement_class.lower()
                )


                file_match = (

                    not replacement_file
                    or
                    candidate_file.lower()
                    ==
                    replacement_file.lower()
                )


                if (
                    name_match
                    and
                    class_match
                    and
                    file_match
                ):

                    current_entry = (
                        candidate
                    )

                    break


            # ------------------------------------------------
            # Read authoritative current documentation
            # ------------------------------------------------

            if replacement_file:

                try:

                    current_doc = api_file(
                        replacement_file
                    )

                    item[
                        "currentDocumentation"
                    ] = current_doc

                except Exception as e:

                    item[
                        "documentationError"
                    ] = str(e)


            elif current_entry:

                try:

                    current_doc = api_file(
                        current_entry.get(
                            "file",
                            ""
                        )
                    )

                    item[
                        "currentDocumentation"
                    ] = current_doc

                except Exception as e:

                    item[
                        "documentationError"
                    ] = str(e)


            if current_entry:

                item[
                    "currentIndexEntry"
                ] = current_entry


            replacement_results.append(
                item
            )


        output.append({

            "oldApi":
                old_entry.get(
                    "name",
                    old_api
                ),

            "deprecatedFile":
                old_entry.get(
                    "file",
                    ""
                ),

            "description":
                old_entry.get(
                    "description",
                    ""
                ),

            "luaSynopsis":
                old_entry.get(
                    "luaSynopsis",
                    ""
                ),

            "pythonSynopsis":
                old_entry.get(
                    "pythonSynopsis",
                    ""
                ),

            "inputs":
                old_entry.get(
                    "inputs",
                    []
                ),

            "outputs":
                old_entry.get(
                    "outputs",
                    []
                ),

            "replacements":
                replacement_results
        })


    return {

        "found":
            True,

        "oldApi":
            old_api,

        "results":
            output
    }


# ============================================================
# PROJECT FILE ACCESS
# ============================================================

def safe_project_path(
    relative_path
):

    path = (
        PROJECT_DIR /
        relative_path
    ).resolve()


    try:

        path.relative_to(
            PROJECT_DIR
        )

    except ValueError:

        raise ValueError(
            "Access outside PROJECT_ROOT is forbidden."
        )


    return path


def list_files(
    directory="."
):

    path = safe_project_path(
        directory
    )


    if not path.is_dir():

        raise ValueError(
            f"Not a directory: {directory}"
        )


    result = []


    for p in path.rglob("*"):

        if not p.is_file():

            continue


        result.append(
            str(
                p.relative_to(
                    PROJECT_DIR
                )
            )
        )


        if (
            len(result)
            >= MAX_LIST_FILES
        ):

            break


    return result


def read_file(
    path
):

    p = safe_project_path(
        path
    )


    if not p.is_file():

        raise FileNotFoundError(
            path
        )


    if (
        p.stat().st_size
        > MAX_FILE_SIZE
    ):

        raise ValueError(
            f"File exceeds maximum size "
            f"of {MAX_FILE_SIZE} bytes."
        )


    return p.read_text(
        encoding="utf-8",
        errors="replace"
    )


def write_file(
    path,
    content
):

    p = safe_project_path(
        path
    )


    p.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    p.write_text(
        content,
        encoding="utf-8"
    )


    return {

        "success":
            True,

        "file":
            str(
                p.relative_to(
                    PROJECT_DIR
                )
            )
    }


def search_code(
    pattern
):

    pattern = (
        pattern
        .lower()
    )


    results = []


    extensions = {

        ".lua",
        ".py",

        ".txt",
        ".md",
        ".json",
        ".xml",

        ".c",
        ".cc",
        ".cpp",
        ".cxx",

        ".h",
        ".hh",
        ".hpp",
        ".hxx"
    }


    for p in PROJECT_DIR.rglob("*"):

        if not p.is_file():

            continue


        if (
            p.suffix.lower()
            not in extensions
        ):

            continue


        try:

            text = p.read_text(
                encoding="utf-8",
                errors="replace"
            )

        except Exception:

            continue


        for line_number, line in enumerate(
            text.splitlines(),
            1
        ):

            if pattern in line.lower():

                results.append({

                    "file":
                        str(
                            p.relative_to(
                                PROJECT_DIR
                            )
                        ),

                    "line":
                        line_number,

                    "text":
                        line
                })


                if (
                    len(results)
                    >= MAX_SEARCH_RESULTS
                ):

                    return results


    return results


# ============================================================
# SHELL COMMAND
# ============================================================

def run_command(
    command
):
    """
    Run a shell command in PROJECT_ROOT.

    The LLM can use this for syntax checking, tests, etc.
    """

    result = subprocess.run(

        command,

        shell=True,

        cwd=PROJECT_DIR,

        capture_output=True,

        text=True,

        timeout=120
    )


    return {

        "returncode":
            result.returncode,

        "stdout":
            result.stdout[-15000:],

        "stderr":
            result.stderr[-15000:]
    }


# ============================================================
# TOOL DEFINITIONS
# ============================================================

tools = [

    # ========================================================
    # Context
    # ========================================================

    {
        "type":
            "function",

        "function": {

            "name":
                "read_context",

            "description":
                "Read context.txt containing general information "
                "about the application/software.",

            "parameters": {

                "type":
                    "object",

                "properties":
                    {}
            }
        }
    },


    # ========================================================
    # Current API
    # ========================================================

    {
        "type":
            "function",

        "function": {

            "name":
                "api_search",

            "description":
                "Search the current Lua/Python API for methods "
                "and properties. Also finds relevant deprecated "
                "APIs and marks them as deprecated.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "query": {

                        "type":
                            "string",

                        "description":
                            "API name or functionality to search for."
                    }
                },

                "required":
                    ["query"]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "api_category",

            "description":
                "List current Lua/Python methods and properties "
                "in an API category such as object, app, scene, "
                "joint, etc.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "category": {

                        "type":
                            "string",

                        "description":
                            "Category name, for example app or object."
                    }
                },

                "required":
                    ["category"]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "api_file",

            "description":
                "Read the complete authoritative documentation "
                "for a current .method or .property file. "
                "Use this before generating or migrating code "
                "when the exact API semantics matter.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "filename": {

                        "type":
                            "string",

                        "description":
                            "Current API documentation filename."
                    }
                },

                "required":
                    ["filename"]
            }
        }
    },


    # ========================================================
    # Deprecated API
    # ========================================================

    {
        "type":
            "function",

        "function": {

            "name":
                "api_deprecated",

            "description":
                "Search deprecated Lua/Python APIs and their "
                "migration information. Deprecated entries may "
                "contain descriptions, synopses, inputs, outputs "
                "and explicit replacement APIs.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "query": {

                        "type":
                            "string",

                        "description":
                            "Deprecated API name or functionality."
                    }
                },

                "required":
                    ["query"]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "api_deprecated_file",

            "description":
                "Read the complete detailed documentation of a "
                "deprecated API.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "filename": {

                        "type":
                            "string",

                        "description":
                            "A .deprecated filename."
                    }
                },

                "required":
                    ["filename"]
            }
        }
    },


    # ========================================================
    # Replacement discovery
    # ========================================================

    {
        "type":
            "function",

        "function": {

            "name":
                "find_replacement",

            "description":
                "Given a deprecated Lua/Python API function, find "
                "its documented replacement(s), migration notes "
                "and the complete current API documentation for "
                "each replacement. Prefer this tool when migrating "
                "a known deprecated API because it combines "
                "deprecated information and current replacement "
                "documentation in one operation.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "old_api": {

                        "type":
                            "string",

                        "description":
                            "Deprecated API name, e.g. "
                            "sim.writeCustomStringData."
                    }
                },

                "required":
                    ["old_api"]
            }
        }
    },


    # ========================================================
    # Project
    # ========================================================

    {
        "type":
            "function",

        "function": {

            "name":
                "list_files",

            "description":
                "List files in the project directory.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "directory": {

                        "type":
                            "string",

                        "description":
                            "Relative project directory. "
                            "Defaults to '.'."
                    }
                }
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "read_file",

            "description":
                "Read a project source or text file.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "path": {

                        "type":
                            "string",

                        "description":
                            "Relative path inside PROJECT_ROOT."
                    }
                },

                "required":
                    ["path"]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "write_file",

            "description":
                "Write or replace a project source file.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "path": {

                        "type":
                            "string"
                    },

                    "content": {

                        "type":
                            "string"
                    }
                },

                "required":
                    [
                        "path",
                        "content"
                    ]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "search_code",

            "description":
                "Search project source files for a text pattern. "
                "Useful for locating scripts, object names, "
                "deprecated API calls and related code.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "pattern": {

                        "type":
                            "string"
                    }
                },

                "required":
                    ["pattern"]
            }
        }
    },


    {
        "type":
            "function",

        "function": {

            "name":
                "run_command",

            "description":
                "Run a shell command in PROJECT_ROOT for syntax "
                "checks, tests, builds or other validation.",

            "parameters": {

                "type":
                    "object",

                "properties": {

                    "command": {

                        "type":
                            "string"
                    }
                },

                "required":
                    ["command"]
            }
        }
    }
]


# ============================================================
# TOOL DISPATCH
# ============================================================

API_INDEX = None


def execute_tool(
    name,
    arguments
):

    if name == "read_context":

        return read_context()


    if name == "api_search":

        return api_search(
            arguments["query"],
            API_INDEX
        )


    if name == "api_category":

        return api_category(
            arguments["category"],
            API_INDEX
        )


    if name == "api_file":

        return api_file(
            arguments["filename"]
        )


    if name == "api_deprecated":

        return api_deprecated(
            arguments["query"],
            API_INDEX
        )


    if name == "api_deprecated_file":

        return api_deprecated_file(
            arguments["filename"]
        )


    if name == "find_replacement":

        return find_replacement(
            arguments["old_api"],
            API_INDEX
        )


    if name == "list_files":

        return list_files(
            arguments.get(
                "directory",
                "."
            )
        )


    if name == "read_file":

        return read_file(
            arguments["path"]
        )


    if name == "write_file":

        return write_file(
            arguments["path"],
            arguments["content"]
        )


    if name == "search_code":

        return search_code(
            arguments["pattern"]
        )


    if name == "run_command":

        return run_command(
            arguments["command"]
        )


    raise ValueError(
        f"Unknown tool: {name}"
    )


# ============================================================
# SYSTEM PROMPT
# ============================================================

def create_system_prompt(
    context
):

    return f"""
You are an autonomous software-engineering assistant for
the application described below.

============================================================
APPLICATION CONTEXT
============================================================

{context}


============================================================
TWO PRIMARY USE CASES
============================================================

You have two major purposes.

1. NEW CODE

   Help the user understand and use the CURRENT Lua/Python
   API when creating new code.

2. CODE MIGRATION

   Analyze existing Lua/Python code and migrate it from old
   or deprecated APIs to the CURRENT API.


============================================================
SUPPORTED API LANGUAGES
============================================================

Only Lua and Python API usage is currently supported.

Do not perform API migration for C, C++, or other languages.


============================================================
AUTHORITATIVE API DOCUMENTATION
============================================================

API documentation root:

{API_ROOT}

The documentation is indexed before the task starts.

The index contains:

    - API categories
    - current methods
    - current properties
    - deprecated APIs
    - deprecated API migration information


============================================================
CURRENT API
============================================================

Use:

    api_search()

to search the current API.

Use:

    api_category()

to inspect a category.

Use:

    api_file()

to read complete authoritative documentation for a
specific current method or property.

The detailed documentation may contain:

    - name
    - class
    - description
    - Lua synopsis
    - Python synopsis
    - inputs
    - outputs


============================================================
DEPRECATED API
============================================================

Deprecated APIs have detailed .deprecated documentation.

This documentation can contain:

    - description
    - Lua synopsis
    - Python synopsis
    - inputs
    - outputs
    - replacedBy
    - migration notes

The deprecated documentation is valuable both for:

    - migrating existing code
    - understanding functionality for new code


============================================================
FINDING REPLACEMENTS
============================================================

When you know that an API is deprecated, prefer:

    find_replacement()

This tool can directly provide:

    old API
    deprecated description
    old Lua/Python synopsis
    old inputs/outputs
    replacement API(s)
    replacement class
    migration note
    complete current replacement documentation

For example, a deprecated entry might contain:

    name:
        sim.writeCustomStringData

    description:
        Deprecated. See properties instead

    replacedBy:

        setStringProperty
        class: object
        file: object_setStringProperty.method
        note:
            use a 'customData.'-prefix for the property name

Do not blindly perform a textual name replacement.

Read and understand the current replacement documentation.


============================================================
MIGRATION RULES
============================================================

When migrating old code:

    1. Identify the old API call.
    2. Determine whether it is deprecated.
    3. Use find_replacement() when appropriate.
    4. Read the current API documentation.
    5. Compare:
         - arguments
         - return values
         - calling convention
         - semantics
         - property names
         - classes
    6. Modify the code correctly.
    7. Re-read the modified code.
    8. Search for remaining deprecated APIs.
    9. Validate the result.
   10. Fix any problems discovered.


============================================================
NEW CODE
============================================================

When creating new code, reason about the requested
functionality first.

Then:

    1. Search the current API.
    2. Inspect relevant categories if useful.
    3. Read the complete documentation of candidate APIs.
    4. Choose the API that best matches the requested
       functionality.
    5. Generate code using CURRENT APIs.

Do not recommend deprecated APIs for new code.

However, deprecated documentation may be used as a bridge
when it reveals the modern replacement for functionality
that used to exist.


============================================================
PROJECT
============================================================

Project root:

{PROJECT_DIR}

You may:

    - list project files
    - search project files
    - read project files
    - modify project files
    - run validation commands

Never access files outside PROJECT_ROOT.


============================================================
SCRIPT IDENTIFICATION
============================================================

If the user requests something like:

    "convert the script named xxx attached to object yyy"

do not blindly modify the first matching filename.

Instead:

    - search for xxx
    - identify candidate files
    - search for yyy if useful
    - determine which script is actually relevant
    - read it
    - then modify it


============================================================
AUTONOMOUS OPERATION
============================================================

You are expected to perform multi-step tasks autonomously.

Do not stop after discovering what should be done.

If the user asks you to modify code, actually modify it.

Do not merely provide instructions for the user to perform
the modification themselves.


============================================================
CODE MODIFICATION
============================================================

Preserve existing behavior unless the task requires
otherwise.

Do not make unrelated refactorings.

Do not introduce APIs that are not established by the
documentation.

When the documentation provides an explicit migration note,
take it seriously.


============================================================
VALIDATION
============================================================

After modifying code:

    - re-read modified files
    - search for remaining deprecated API calls
    - perform syntax checks when practical
    - run relevant project tests/checks when practical

If validation finds a problem:

    investigate
    fix
    validate again


============================================================
UNCERTAINTY
============================================================

Never invent API names, arguments or behavior.

Prefer the supplied API documentation over general knowledge.

If the documentation does not establish something, say so.

When several APIs could satisfy a request, inspect their
documentation before deciding.


============================================================
USER TASK
============================================================

The user's task is contained in the user message.
"""


# ============================================================
# AGENT LOOP
# ============================================================

def run_agent(
    task
):

    print()
    print("=" * 60)
    print("LLMTool")
    print("=" * 60)

    print(
        f"Project : {PROJECT_DIR}"
    )

    print(
        f"API     : {API_ROOT}"
    )

    print(
        f"Model   : {MODEL}"
    )

    print()
    print("Task:")
    print(task)
    print()


    # --------------------------------------------------------
    # Context
    # --------------------------------------------------------

    try:

        context = read_context()

    except Exception as e:

        print(
            f"WARNING: could not read context.txt: {e}"
        )

        context = ""


    system_prompt = create_system_prompt(
        context
    )


    messages = [

        {
            "role":
                "system",

            "content":
                system_prompt
        },

        {
            "role":
                "user",

            "content":
                task
        }
    ]


    # --------------------------------------------------------
    # Agent loop
    # --------------------------------------------------------

    for iteration in range(
        1,
        MAX_ITERATIONS + 1
    ):

        print()
        print("=" * 60)
        print(
            f"AGENT ITERATION {iteration}"
        )
        print("=" * 60)


        try:

            response = (
                client.chat.completions.create(

                    model=
                        MODEL,

                    messages=
                        messages,

                    tools=
                        tools,

                    tool_choice=
                        "auto"
                )
            )

        except Exception as e:

            print()
            print(
                "ERROR communicating with OpenRouter:"
            )

            print(e)

            return


        message = (
            response.choices[0].message
        )


        # ----------------------------------------------------
        # Store assistant response
        # ----------------------------------------------------

        messages.append(
            message
        )


        # ----------------------------------------------------
        # Final response
        # ----------------------------------------------------

        if not message.tool_calls:

            print()
            print("=" * 60)
            print("AGENT RESULT")
            print("=" * 60)
            print()

            print(
                message.content
                or "(no final response)"
            )

            return


        # ----------------------------------------------------
        # Execute tool calls
        # ----------------------------------------------------

        for tool_call in (
            message.tool_calls
        ):

            name = (
                tool_call.function.name
            )


            try:

                arguments = json.loads(
                    tool_call.function.arguments
                )

            except Exception as e:

                result = {

                    "error":
                        "Invalid JSON tool arguments.",

                    "details":
                        str(e)
                }


                messages.append({

                    "role":
                        "tool",

                    "tool_call_id":
                        tool_call.id,

                    "content":
                        json.dumps(
                            result
                        )
                })


                continue


            print()
            print(
                f"TOOL: {name}"
            )

            print(
                json.dumps(
                    arguments,
                    indent=2,
                    ensure_ascii=False
                )
            )


            # ------------------------------------------------
            # Execute
            # ------------------------------------------------

            try:

                result = execute_tool(
                    name,
                    arguments
                )

            except Exception as e:

                result = {

                    "error":
                        str(e)
                }


            # ------------------------------------------------
            # Convert result
            # ------------------------------------------------

            if isinstance(
                result,
                str
            ):

                result_text = result

            else:

                result_text = json.dumps(

                    result,

                    ensure_ascii=False
                )


            print(
                f"Result: "
                f"{len(result_text)} characters"
            )


            # ------------------------------------------------
            # Return to LLM
            # ------------------------------------------------

            messages.append({

                "role":
                    "tool",

                "tool_call_id":
                    tool_call.id,

                "content":
                    result_text
            })


    # --------------------------------------------------------
    # Iteration limit
    # --------------------------------------------------------

    print()
    print(
        f"ERROR: Agent reached maximum "
        f"of {MAX_ITERATIONS} iterations."
    )


# ============================================================
# COMMAND LINE
# ============================================================

def main():

    parser = argparse.ArgumentParser(

        description=
            "Autonomous Lua/Python API assistant "
            "and migration agent."
    )


    parser.add_argument(

        "--reset-index",

        action=
            "store_true",

        help=
            "Delete and rebuild the API index before "
            "executing the task."
    )


    parser.add_argument(

        "task",

        nargs=
            "*",

        help=
            "Task or question for the LLM."
    )


    args = parser.parse_args()


    # --------------------------------------------------------
    # Validate project
    # --------------------------------------------------------

    if not PROJECT_DIR.exists():

        print(

            f"ERROR: PROJECT_ROOT does not exist:\n"
            f"  {PROJECT_DIR}",

            file=sys.stderr
        )

        sys.exit(1)


    if not PROJECT_DIR.is_dir():

        print(

            f"ERROR: PROJECT_ROOT is not a directory:\n"
            f"  {PROJECT_DIR}",

            file=sys.stderr
        )

        sys.exit(1)


    # --------------------------------------------------------
    # Initialize API index
    # --------------------------------------------------------

    global API_INDEX


    API_INDEX = initialize_api_index(

        force_reset=
            args.reset_index
    )


    # --------------------------------------------------------
    # Require task
    # --------------------------------------------------------

    if not args.task:

        print()
        print(
            "No task supplied."
        )

        print()
        print(
            "Example:"
        )

        print()

        print(
            '  py LLMTool.py '
            '"convert the script with name xxx that is '
            'attached to object yyy to the current version"'
        )

        print()

        print(
            "Force API index rebuild:"
        )

        print()

        print(
            '  py LLMTool.py --reset-index '
            '"your task"'
        )

        sys.exit(1)


    task = " ".join(
        args.task
    )


    # --------------------------------------------------------
    # Run agent
    # --------------------------------------------------------

    run_agent(
        task
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
```
