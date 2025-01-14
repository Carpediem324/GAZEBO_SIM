from setuptools import setup
from glob import glob
import os

package_name = '250114'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/models', glob('models/*.urdf')),  # 모델 파일 복사
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shh',
    maintainer_email='gusgkr0324@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
