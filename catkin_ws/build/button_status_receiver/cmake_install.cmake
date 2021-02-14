# Install script for directory: C:/Users/yahoo/hack/mr_robotarm/catkin_ws/src/button_status_receiver

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/button_status_receiver/catkin_generated/installspace/button_status_receiver.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/button_status_receiver/cmake" TYPE FILE FILES
    "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/button_status_receiver/catkin_generated/installspace/button_status_receiverConfig.cmake"
    "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/button_status_receiver/catkin_generated/installspace/button_status_receiverConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/button_status_receiver" TYPE FILE FILES "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/src/button_status_receiver/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/button_status_receiver" TYPE PROGRAM FILES "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/button_status_receiver/catkin_generated/installspace/button_status_receiver_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/button_status_receiver" TYPE EXECUTABLE FILES "C:/Users/yahoo/hack/mr_robotarm/catkin_ws/build/button_status_receiver/catkin_generated/windows_wrappers/button_status_receiver_button_status_receiver_node.py_exec_install_python/button_status_receiver_node.exe")
endif()

