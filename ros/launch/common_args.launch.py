from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "lidar_topic",
                description="",
            ),
            DeclareLaunchArgument(
                "use_2d_lidar",
                default_value="true",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "lidar_odometry_topic",
                default_value="lidar_odometry",
                description="",
            ),
            DeclareLaunchArgument(
                "lidar_odom_frame",
                default_value="odom",
                description="",
            ),
            DeclareLaunchArgument(
                "wheel_odom_frame",
                default_value="odom_wheel",
                description="",
            ),
            DeclareLaunchArgument(
                "base_frame",
                default_value="f1tenth_1",
                description="",
            ),
            DeclareLaunchArgument(
                "publish_odom_tf",
                default_value="true",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "invert_odom_tf",
                default_value="true",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "visualize",
                default_value="false",
                description="",
                choices=["true", "false"],
            ),
        ]
    )
