PROJECT(lpod NONE)

cmake_minimum_required(VERSION 2.6)

SET(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

##
# Detect python version
##

EXECUTE_PROCESS(
  COMMAND
  python -c "from distutils import sysconfig; print sysconfig.get_python_version()"
  OUTPUT_VARIABLE PYTHON_VERSION
  OUTPUT_STRIP_TRAILING_WHITESPACE
  )

##
# Browse the scripts subdirectory
##


ADD_SUBDIRECTORY(open_formula)
ADD_SUBDIRECTORY(chart)

##
# Status
##

MESSAGE(STATUS "- - - -")
MESSAGE(STATUS "LPoD configured successfully")
MESSAGE(STATUS "Using ${CMAKE_INSTALL_PREFIX} for installation")
MESSAGE(STATUS "Python version ${PYTHON_VERSION}")
MESSAGE(STATUS "- - - -")

