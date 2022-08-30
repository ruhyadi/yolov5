cmake_minimum_required(VERSION 3.0.0)
project(openvino VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(inference inference_cpp.cpp)
target_link_libraries(inference
/opt/intel/openvino/extras/opencv/lib/libopencv_dnn.so
/opt/intel/openvino/extras/opencv/lib/libopencv_core.so
/opt/intel/openvino/extras/opencv/lib/libopencv_imgcodecs.so
/opt/intel/openvino/extras/opencv/lib/libopencv_imgproc.so
/opt/intel/openvino/runtime/lib/intel64/libopenvino.so
)
target_include_directories(inference PUBLIC 
/opt/intel/openvino/extras/opencv/include/
/opt/intel/openvino/runtime/include/
/opt/intel/openvino/runtime/include/ie/
)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
