from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('endpoint', default_value='127.0.0.1:14550', description='Endpoint for mavlink-router'),
        DeclareLaunchArgument('device', default_value='/dev/ttyACM0', description='Device for mavlink-router'),
        DeclareLaunchArgument('baudrate', default_value='921600', description='Baudrate for device'),

        Node(
            package='mavlink_router_launcher',
            executable='mavlink_router_node',
            name='mavlink_router_node',
            parameters=[
                {'endpoint': LaunchConfiguration('endpoint')},
                {'device': LaunchConfiguration('device')},
                {'baudrate': LaunchConfiguration('baudrate')},
            ],
            output='screen'
        ),
    ])
