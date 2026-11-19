cmake_minimum_required(VERSION 3.21)

project(CoppeliaSimManual
    VERSION 1.0.0
    DESCRIPTION "CoppeliaSim user manual: Markdown sources and static HTML site"
    LANGUAGES NONE
)

# ---------------------------------------------------------------------------
# Options
# ---------------------------------------------------------------------------
option(MANUAL_VERIFY
    "Run verify.py (link/image/fence checks) before rendering the site" ON)
option(MANUAL_PORTABLE
    "Build a self-contained site with relative URLs (openable from file://)" ON)

# Deliberately *not* ${CMAKE_BINARY_DIR}/html: when this project is added with
# add_subdirectory(html) that path is CMake's own binary directory for this
# subproject, and installing it would copy CMakeFiles/, Makefile, node_modules
# and the rest of the build tree into the install prefix.
set(MANUAL_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/manual_html"
    CACHE PATH "Directory receiving the generated static site")

# Older configurations cached ${CMAKE_BINARY_DIR}/html (or .../site), which is
# CMake's own binary directory when this project is built as a subdirectory —
# installing it would copy CMakeFiles/, node_modules and the rest of the build
# tree into the install prefix. Fall back to the dedicated default if a cached
# value points at a binary directory.
if(MANUAL_OUTPUT_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR
   OR MANUAL_OUTPUT_DIR STREQUAL CMAKE_BINARY_DIR)
    message(STATUS
        "Ignoring stale MANUAL_OUTPUT_DIR=${MANUAL_OUTPUT_DIR}, using the default")
    set(MANUAL_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/manual_html"
        CACHE PATH "Directory receiving the generated static site" FORCE)
endif()

set(MANUAL_NPM_CACHE "${CMAKE_BINARY_DIR}/npm-cache"
    CACHE PATH "npm cache directory (kept out of \$HOME for hermetic builds)")
set(MANUAL_PORT "5173"
    CACHE STRING "Port used by the 'serve' target")
set(MANUAL_BASE "/"
    CACHE STRING "Base URL path of the site, e.g. /manual/ for GitHub Pages (hosted builds only)")

set(MANUAL_ROOT "${CMAKE_CURRENT_SOURCE_DIR}")
set(MANUAL_DOCS "${MANUAL_ROOT}/../docs")
set(MANUAL_SITE_STAMP "${CMAKE_BINARY_DIR}/site.stamp")

# A portable build uses a relative base and drops the client bundle, so the
# site can be opened straight from the file system.
if(MANUAL_PORTABLE)
    set(MANUAL_EFFECTIVE_BASE "./")
    set(MANUAL_PORTABLE_ENV "MANUAL_PORTABLE=1")
else()
    set(MANUAL_EFFECTIVE_BASE "${MANUAL_BASE}")
    set(MANUAL_PORTABLE_ENV "MANUAL_PORTABLE=0")
endif()

# ---------------------------------------------------------------------------
# Toolchain
# ---------------------------------------------------------------------------
find_program(NODE_EXECUTABLE NAMES node nodejs
    DOC "Node.js executable (>= 18) used by VitePress")
find_program(NPM_EXECUTABLE NAMES npm npm.cmd
    DOC "npm executable used to install and run VitePress")

if(NOT NODE_EXECUTABLE)
    message(FATAL_ERROR
        "Node.js was not found. Install Node.js >= 18 (https://nodejs.org) "
        "or pass -DNODE_EXECUTABLE=/path/to/node")
endif()
if(NOT NPM_EXECUTABLE)
    message(FATAL_ERROR
        "npm was not found. Install npm or pass -DNPM_EXECUTABLE=/path/to/npm")
endif()

execute_process(
    COMMAND "${NODE_EXECUTABLE}" --version
    OUTPUT_VARIABLE MANUAL_NODE_VERSION
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE MANUAL_NODE_RESULT
)
if(NOT MANUAL_NODE_RESULT EQUAL 0)
    message(FATAL_ERROR "Cannot run ${NODE_EXECUTABLE} --version")
endif()
string(REGEX REPLACE "^v" "" MANUAL_NODE_VERSION "${MANUAL_NODE_VERSION}")
if(MANUAL_NODE_VERSION VERSION_LESS 18.0)
    message(FATAL_ERROR
        "VitePress requires Node.js >= 18, found ${MANUAL_NODE_VERSION}")
endif()

# Python is only used by verify.py (standard library only).
set(MANUAL_PYTHON "" CACHE FILEPATH
    "Python interpreter for verify.py (default: found on PATH)")
if(MANUAL_PYTHON)
    set(Python3_EXECUTABLE "${MANUAL_PYTHON}")
else()
    find_package(Python3 COMPONENTS Interpreter QUIET)
endif()

if(NOT EXISTS "${MANUAL_DOCS}/index.md")
    message(FATAL_ERROR
        "Markdown pages not found in ${MANUAL_DOCS}: this does not look like "
        "the manual source tree.")
endif()

# ---------------------------------------------------------------------------
# npm dependencies (installed in the build tree; the source tree stays clean)
# ---------------------------------------------------------------------------
set(MANUAL_NODE_MODULES "${CMAKE_BINARY_DIR}/node_modules")
set(MANUAL_CACHE_DIR "${CMAKE_BINARY_DIR}/vitepress-cache")
# The stamp lives inside node_modules, so deleting the packages forces a
# reinstall instead of leaving a stale stamp behind.
set(MANUAL_NPM_STAMP "${MANUAL_NODE_MODULES}/.cmake-installed")
# VitePress loads its config and theme from <root>/.vitepress (html/), which
# must be able to resolve "vitepress" and "vue". A link keeps that working
# while the packages themselves stay in the build tree.
set(MANUAL_LINKED_MODULES "${MANUAL_ROOT}/node_modules")

set(MANUAL_NPM_DEPS "${MANUAL_ROOT}/package.json")
if(EXISTS "${MANUAL_ROOT}/package-lock.json")
    set(MANUAL_NPM_INSTALL "${NPM_EXECUTABLE}" ci --no-audit --no-fund)
    list(APPEND MANUAL_NPM_DEPS "${MANUAL_ROOT}/package-lock.json")
else()
    set(MANUAL_NPM_INSTALL "${NPM_EXECUTABLE}" install --no-audit --no-fund)
endif()

# npm runs against copies of the manifests in the build directory, so its
# node_modules lands there instead of next to the sources.
set(MANUAL_NPM_COPIES
    COMMAND "${CMAKE_COMMAND}" -E copy_if_different
            "${MANUAL_ROOT}/package.json" "${CMAKE_BINARY_DIR}/package.json")
if(EXISTS "${MANUAL_ROOT}/package-lock.json")
    list(APPEND MANUAL_NPM_COPIES
        COMMAND "${CMAKE_COMMAND}" -E copy_if_different
                "${MANUAL_ROOT}/package-lock.json" "${CMAKE_BINARY_DIR}/package-lock.json")
endif()

if(WIN32)
    set(MANUAL_LINK_COMMAND cmd /c mklink /J
        "${MANUAL_LINKED_MODULES}" "${MANUAL_NODE_MODULES}")
else()
    set(MANUAL_LINK_COMMAND "${CMAKE_COMMAND}" -E create_symlink
        "${MANUAL_NODE_MODULES}" "${MANUAL_LINKED_MODULES}")
endif()

add_custom_command(
    OUTPUT "${MANUAL_NPM_STAMP}"
    ${MANUAL_NPM_COPIES}
    COMMAND "${CMAKE_COMMAND}" -E chdir "${CMAKE_BINARY_DIR}"
            ${MANUAL_NPM_INSTALL} --cache "${MANUAL_NPM_CACHE}"
    COMMAND "${CMAKE_COMMAND}" -E touch "${MANUAL_NPM_STAMP}"
    DEPENDS ${MANUAL_NPM_DEPS}
    COMMENT "Installing VitePress dependencies (out of source)"
    VERBATIM
)

add_custom_command(
    OUTPUT "${MANUAL_LINKED_MODULES}"
    COMMAND "${CMAKE_COMMAND}" -E rm -rf "${MANUAL_LINKED_MODULES}"
    COMMAND ${MANUAL_LINK_COMMAND}
    DEPENDS "${MANUAL_NPM_STAMP}"
    COMMENT "Linking node_modules into the source tree"
    VERBATIM
)

add_custom_target(manual-deps DEPENDS "${MANUAL_NPM_STAMP}" "${MANUAL_LINKED_MODULES}")

# ---------------------------------------------------------------------------
# Build steps
# ---------------------------------------------------------------------------
# The steps are collected first: putting "COMMAND" keywords inside the list
# keeps add_custom_command from mistaking an argument for an output file.
set(MANUAL_BUILD_STEPS "")

# Check the Markdown before rendering it.
if(MANUAL_VERIFY AND Python3_EXECUTABLE)
    list(APPEND MANUAL_BUILD_STEPS
        COMMAND "${Python3_EXECUTABLE}" "${MANUAL_ROOT}/verify.py" "${MANUAL_DOCS}")
endif()

list(APPEND MANUAL_BUILD_STEPS
    COMMAND "${CMAKE_COMMAND}" -E env
            "MANUAL_BASE=${MANUAL_EFFECTIVE_BASE}" "${MANUAL_PORTABLE_ENV}"
            "MANUAL_CACHE_DIR=${MANUAL_CACHE_DIR}"
            "${NPM_EXECUTABLE}" run build -- --outDir "${MANUAL_OUTPUT_DIR}")
if(MANUAL_PORTABLE)
    list(APPEND MANUAL_BUILD_STEPS
        COMMAND "${NODE_EXECUTABLE}" "${MANUAL_ROOT}/tools/portable.mjs"
                "${MANUAL_OUTPUT_DIR}")
endif()
list(APPEND MANUAL_BUILD_STEPS
    COMMAND "${CMAKE_COMMAND}" -E touch "${MANUAL_SITE_STAMP}")

# ---------------------------------------------------------------------------
# Static site
# ---------------------------------------------------------------------------
file(GLOB_RECURSE MANUAL_MARKDOWN CONFIGURE_DEPENDS "${MANUAL_DOCS}/*.md")
file(GLOB_RECURSE MANUAL_IMAGES CONFIGURE_DEPENDS "${MANUAL_DOCS}/images/*")
file(GLOB_RECURSE MANUAL_SITE_CONFIG CONFIGURE_DEPENDS
    "${MANUAL_ROOT}/.vitepress/*.mts"
    "${MANUAL_ROOT}/.vitepress/theme/*"
)

add_custom_command(
    OUTPUT "${MANUAL_SITE_STAMP}"
    ${MANUAL_BUILD_STEPS}
    WORKING_DIRECTORY "${MANUAL_ROOT}"
    DEPENDS
        "${MANUAL_NPM_STAMP}"
        "${MANUAL_ROOT}/tools/portable.mjs"
        ${MANUAL_MARKDOWN}
        ${MANUAL_IMAGES}
        ${MANUAL_SITE_CONFIG}
        # The sidebar is read from the table of contents at build time.
        "${MANUAL_DOCS}/index.md"
    COMMENT "Rendering the manual with VitePress into ${MANUAL_OUTPUT_DIR}"
    VERBATIM
)

add_custom_target(manual ALL DEPENDS "${MANUAL_SITE_STAMP}")
add_dependencies(manual manual-deps)

if(MANUAL_VERIFY AND Python3_EXECUTABLE)
    # Convenience target; the same check also runs as part of the site build.
    add_custom_target(verify
        COMMAND "${Python3_EXECUTABLE}" "${MANUAL_ROOT}/verify.py" "${MANUAL_DOCS}"
        WORKING_DIRECTORY "${MANUAL_ROOT}"
        COMMENT "Checking the Markdown sources"
        USES_TERMINAL
    )
endif()

# ---------------------------------------------------------------------------
# Development server (run explicitly: cmake --build build --target serve)
# ---------------------------------------------------------------------------
add_custom_target(serve
    COMMAND "${CMAKE_COMMAND}" -E env "MANUAL_CACHE_DIR=${MANUAL_CACHE_DIR}"
            "${NPM_EXECUTABLE}" run dev -- --port ${MANUAL_PORT}
    WORKING_DIRECTORY "${MANUAL_ROOT}"
    COMMENT "Starting the VitePress dev server on http://localhost:${MANUAL_PORT}"
    USES_TERMINAL
)
add_dependencies(serve manual-deps)

# ---------------------------------------------------------------------------
# Install / summary
# ---------------------------------------------------------------------------
install(DIRECTORY "${MANUAL_OUTPUT_DIR}/" DESTINATION ".")

message(STATUS "CoppeliaSim manual site")
message(STATUS "  node            : ${NODE_EXECUTABLE} (v${MANUAL_NODE_VERSION})")
message(STATUS "  npm             : ${NPM_EXECUTABLE}")
message(STATUS "  markdown pages  : ${MANUAL_DOCS}")
message(STATUS "  site output     : ${MANUAL_OUTPUT_DIR}")
message(STATUS "  base URL        : ${MANUAL_EFFECTIVE_BASE}")
message(STATUS "  portable        : ${MANUAL_PORTABLE}")
if(Python3_EXECUTABLE)
    message(STATUS "  python          : ${Python3_EXECUTABLE}")
else()
    message(STATUS "  python          : not found (verify target disabled)")
endif()
