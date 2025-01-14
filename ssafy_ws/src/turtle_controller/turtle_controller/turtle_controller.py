import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        
        # Create a publisher that will send messages to the /turtle1/cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Set a timer to call the method send_velocity every 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_velocity)
        
        # Define the Twist message that will be sent
        self.velocity = Twist()
        self.velocity.linear.x = 2.0  # Move forward with a speed of 2.0
        self.velocity.angular.z = 1.0  # Rotate with a speed of 1.0

    def send_velocity(self):
        # Publish the velocity command
        self.publisher_.publish(self.velocity)
        self.get_logger().info('Publishing: linear.x: {:.2f}, angular.z: {:.2f}'.format(self.velocity.linear.x, self.velocity.angular.z))

def main(args=None):
    rclpy.init(args=args)
    
    turtle_controller = TurtleController()
    
    rclpy.spin(turtle_controller)
    
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
