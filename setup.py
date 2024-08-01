from setuptools import setup
import os
from glob import glob

package_name = 'mavlink_router_launcher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Atar Babgei',
    maintainer_email='atarbabgei@gmail.com',
    description='ROS 2 wrapper around mavlink-routerd command',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'mavlink_router_node = mavlink_router_launcher.mavlink_router_node:main',
        ],
    },
)