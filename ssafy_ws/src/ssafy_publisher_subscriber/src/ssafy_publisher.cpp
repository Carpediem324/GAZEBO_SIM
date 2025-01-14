#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class SSAFYPublisher : public rclcpp::Node
{
public:
  SSAFYPublisher() : Node("ssafy_publisher")
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("ssafy_topic", 10);
    timer_ = this->create_wall_timer(
      std::chrono::milliseconds(500),
      std::bind(&SSAFYPublisher::publish_message, this));
  }

private:
  void publish_message()
  {
    auto message = std_msgs::msg::String();
    message.data = "SSAFY";
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
  }

  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SSAFYPublisher>());
  rclcpp::shutdown();
  return 0;
}
