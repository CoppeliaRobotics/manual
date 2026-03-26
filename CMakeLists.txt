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
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/apiDoc/generate.py
        --objects-xml=${COPPELIASIM_INCLUDE_DIR}/sim/objects-methods.xml
        --enums-xml=${COPPELIASIM_INCLUDE_DIR}/sim/enums.xml
        --functions-xml=${COPPELIASIM_INCLUDE_DIR}/sim/functions.xml
)

file(GLOB HELP_FILES CONFIGURE_DEPENDS *.html *.lua *.class *.css *.txt)
list(FILTER HELP_FILES EXCLUDE REGEX "/CMakeLists\\.txt$")
foreach(HELP_FILE IN LISTS HELP_FILES)
    coppeliasim_add_manual(${HELP_FILE} SUBDIR .)
endforeach()
coppeliasim_add_manual_directory(en)
coppeliasim_add_manual_directory(index)
coppeliasim_add_manual_directory(wb_img)
coppeliasim_add_manual_directory(js)
