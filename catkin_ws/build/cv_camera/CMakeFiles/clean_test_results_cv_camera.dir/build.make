# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\opt\ros\melodic\x64\lib\site-packages\cmake\data\bin\cmake.exe

# The command to remove a file.
RM = C:\opt\ros\melodic\x64\lib\site-packages\cmake\data\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\yahoo\hack\mr_robotarm\catkin_ws\src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build

# Utility rule file for clean_test_results_cv_camera.

# Include the progress variables for this target.
include cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\progress.make

cv_camera\CMakeFiles\clean_test_results_cv_camera:
	cd C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build\cv_camera
	C:\opt\ros\melodic\x64\python.exe C:/opt/ros/melodic/x64/share/catkin/cmake/test/remove_test_results.py C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/test_results/cv_camera
	cd C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build

clean_test_results_cv_camera: cv_camera\CMakeFiles\clean_test_results_cv_camera
clean_test_results_cv_camera: cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\build.make

.PHONY : clean_test_results_cv_camera

# Rule to build all files generated by this target.
cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\build: clean_test_results_cv_camera

.PHONY : cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\build

cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\clean:
	cd C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build\cv_camera
	$(CMAKE_COMMAND) -P CMakeFiles\clean_test_results_cv_camera.dir\cmake_clean.cmake
	cd C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build
.PHONY : cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\clean

cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" C:\Users\yahoo\hack\mr_robotarm\catkin_ws\src C:\Users\yahoo\hack\mr_robotarm\catkin_ws\src\cv_camera C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build\cv_camera C:\Users\yahoo\hack\mr_robotarm\catkin_ws\build\cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : cv_camera\CMakeFiles\clean_test_results_cv_camera.dir\depend

