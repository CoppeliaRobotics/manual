cmake_minimum_required(VERSION 3.12)
project(manual)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

if(NOT COPPELIASIM_INCLUDE_DIR)
    if(DEFINED ENV{COPPELIASIM_ROOT_DIR})
        set(COPPELIASIM_INCLUDE_DIR $ENV{COPPELIASIM_ROOT_DIR}/programming/include)
    else()
        set(COPPELIASIM_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../include)
    endif()
endif()
list(APPEND CMAKE_MODULE_PATH ${COPPELIASIM_INCLUDE_DIR}/cmake)
find_package(CoppeliaSim 4.5.0.7 REQUIRED)

message(STATUS "COPPELIASIM_EXECUTABLE_TEMP=${COPPELIASIM_EXECUTABLE_TEMP}")
if(NOT EXISTS "${COPPELIASIM_EXECUTABLE_TEMP}")
    message(FATAL_ERROR "Please pass -DCOPPELIASIM_EXECUTABLE_TEMP=... pointing to a valid coppeliaSim executable.")
endif()

add_custom_target(genRegularApi ALL
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_BINARY_DIR}/generated
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/apiDoc/generate.py
        --objects-xml=${COPPELIASIM_INCLUDE_DIR}/sim/objects.xml
        --enums-xml=${COPPELIASIM_INCLUDE_DIR}/sim/enums.xml
        --functions-xml=${COPPELIASIM_INCLUDE_DIR}/sim/functions.xml
        --output-dir=${CMAKE_CURRENT_BINARY_DIR}/generated
    BYPRODUCTS ${CMAKE_CURRENT_BINARY_DIR}/generated/en
)

# Markdown counterparts of the sim-2 HTML pages (installed in docs/sim-2):
add_custom_target(genRegularApiMd ALL
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_BINARY_DIR}/generated/docs/sim-2
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/apiDoc/generate_md.py
        --objects-xml=${COPPELIASIM_INCLUDE_DIR}/sim/objects.xml
        --functions-xml=${COPPELIASIM_INCLUDE_DIR}/sim/functions.xml
        --docs-dir=${CMAKE_CURRENT_SOURCE_DIR}/docs
        --output-dir=${CMAKE_CURRENT_BINARY_DIR}/generated/docs/sim-2
    BYPRODUCTS ${CMAKE_CURRENT_BINARY_DIR}/generated/docs/sim-2
)

file(GLOB HELP_FILES CONFIGURE_DEPENDS *.html *.lua *.class *.css *.txt)
list(FILTER HELP_FILES EXCLUDE REGEX "/CMakeLists\\.txt$")
foreach(HELP_FILE IN LISTS HELP_FILES)
    coppeliasim_add_manual(${HELP_FILE} SUBDIR .)
endforeach()
coppeliasim_add_manual_directory(docs)
coppeliasim_add_manual_directory(en)
coppeliasim_add_manual_directory(index)
coppeliasim_add_manual_directory(wb_img)
coppeliasim_add_manual_directory(js)

coppeliasim_add_manual_directory(${CMAKE_CURRENT_BINARY_DIR}/generated/en)
coppeliasim_add_manual_directory(${CMAKE_CURRENT_BINARY_DIR}/generated/docs/sim-2 SUBDIR docs)
