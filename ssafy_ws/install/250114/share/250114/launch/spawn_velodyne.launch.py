from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = '250114'
    package_share_dir = get_package_share_directory(package_name)

    # 정확한 URDF 경로를 설정
    urdf_file_path = os.path.join(package_share_dir, 'models', 'test.urdf')

    # 파일 존재 여부를 확인하는 로그 출력
    print(f"URDF file path: {urdf_file_path}")
    if not os.path.exists(urdf_file_path):
        raise FileNotFoundError(f"URDF file not found at {urdf_file_path}")

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', urdf_file_path,
                '-entity', 'test'
            ],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzserver',
            arguments=['--verbose'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            output='screen'
        )
    ])
