#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import subprocess

class MavlinkRouterNode(Node):
    def __init__(self):
        super().__init__('mavlink_router_node')
        self.declare_parameter('endpoint', '127.0.0.1:14550') #default endpoint value
        self.declare_parameter('device', '/dev/ttyACM0') #default device value
        self.declare_parameter('baudrate', 921600) #default device baudrate value

        endpoint = self.get_parameter('endpoint').get_parameter_value().string_value
        device = self.get_parameter('device').get_parameter_value().string_value
        baudrate = self.get_parameter('baudrate').get_parameter_value().integer_value

        self.process = None
        self.start_mavlink_router(endpoint, device, baudrate)
        self.get_logger().info('Mavlink Router Node started')

    def start_mavlink_router(self, endpoint, device, baudrate):
        command = ['mavlink-routerd', '-e', endpoint, f'{device}:{baudrate}']
        self.process = subprocess.Popen(command)

    def destroy_node(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = MavlinkRouterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
