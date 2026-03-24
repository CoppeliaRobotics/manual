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
        --objects-xml=${CMAKE_CURRENT_BINARY_DIR}/objects.xml
        --enums-xml=${CMAKE_CURRENT_BINARY_DIR}/enums.xml
        --functions-xml=${CMAKE_SOURCE_DIR}/apiDoc/functions.xml
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
coppeliasim_add_manual(apiDoc/functions.xml SUBDIR apiDoc)

add_custom_command(
    OUTPUT
        ${CMAKE_CURRENT_BINARY_DIR}/objects.xml
    COMMAND ${COPPELIASIM_EXECUTABLE_TEMP} --headless
        --param addOns.autoLoad=false
        --addon ${CMAKE_SOURCE_DIR}/apiDoc/extract_objects_properties.lua
        --param output_xml=${CMAKE_CURRENT_BINARY_DIR}/objects-properties.xml
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_SOURCE_DIR}/apiDoc/merge_objects_properties_methods.py
        ${CMAKE_CURRENT_BINARY_DIR}/objects-properties.xml
        ${CMAKE_SOURCE_DIR}/apiDoc/objects-methods.xml
        ${CMAKE_CURRENT_BINARY_DIR}/objects.xml
    DEPENDS
        ${CMAKE_SOURCE_DIR}/apiDoc/objects-methods.xml
        ${CMAKE_SOURCE_DIR}/apiDoc/extract_objects_properties.lua
        ${CMAKE_SOURCE_DIR}/apiDoc/merge_objects_properties_methods.py
    COMMENT "Generating merged objects.xml"
)
add_custom_target(genObjectsXML DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/objects.xml)
coppeliasim_add_manual(${CMAKE_CURRENT_BINARY_DIR}/objects.xml SUBDIR apiDoc)
add_dependencies(genRegularApi genObjectsXML)

add_custom_command(
    OUTPUT
        ${CMAKE_CURRENT_BINARY_DIR}/enums.xml
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/apiDoc/extract_enums.py ${COPPELIASIM_INCLUDE_DIR}/simLib/simConst.h > ${CMAKE_CURRENT_BINARY_DIR}/enums.xml
    DEPENDS
        ${CMAKE_CURRENT_SOURCE_DIR}/apiDoc/extract_enums.py
        ${COPPELIASIM_INCLUDE_DIR}/simLib/simConst.h
    COMMENT "Generating enums.xml"
)
add_custom_target(genEnumsXML DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/enums.xml)
coppeliasim_add_manual(${CMAKE_CURRENT_BINARY_DIR}/enums.xml SUBDIR apiDoc)
add_dependencies(genRegularApi genEnumsXML)
