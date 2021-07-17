cmake_minimum_required(VERSION 3.15)
project(crab2d LANGUAGES CXX)

include(CTest)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup()
else()
	message(ERROR
	    "conanbuildinfo.cmake doesn't exist. Please run conan install first")
endif()

file(GLOB sources src/*.cpp)

add_library(${PROJECT_NAME} "${sources}")
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
target_include_directories(${PROJECT_NAME} PUBLIC include)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# TODO: Figure out how to make PUBLIC_HEADER work.
install(
	TARGETS ${PROJECT_NAME}
	# PUBLIC_HEADER DESTINATION include/crab2d
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib)

# TODO: Why doesn't this install any files when doing a conan build?
install(DIRECTORY include
	DESTINATION include/crab2d
	FILES_MATCHING PATTERN "*.hpp")
