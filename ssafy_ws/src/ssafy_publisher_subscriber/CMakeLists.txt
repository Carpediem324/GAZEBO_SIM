cmake_minimum_required(VERSION 3.8)
project(ssafy_publisher_subscriber)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(ssafy_publisher src/ssafy_publisher.cpp)
ament_target_dependencies(ssafy_publisher rclcpp std_msgs)

add_executable(ssafy_subscriber src/ssafy_subscriber.cpp)
ament_target_dependencies(ssafy_subscriber rclcpp std_msgs)

install(TARGETS
  ssafy_publisher
  ssafy_subscriber
  DESTINATION lib/${PROJECT_NAME})

ament_package()