# GAZEBO_SIM

## 1. 클론
```bash
git clone https://github.com/Carpediem324/GAZEBO_SIM.git
```

## 2. 빌드
```bash
cd ~/GAZEBO_SIM/ssafy_ws && colcon build
```

## 3. 소싱
```bash
source install/setup.bash
```

## 4. 모델 경로 설정
```bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/ubuntu/GAZEBO_SIM/ssafy_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/
```
위 내용에서 경로를 자신의 위치로 맞춰서 `~/.bashrc`에 추가하세요. 아래 예시

### 예시
```bash
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/ubuntu/GAZEBO_SIM/ssafy_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/' >> ~/.bashrc
source ~/.bashrc
```

## 5. 실행
```bash
ros2 launch turtlebot3_gazebo tb3_imu_lidar_gps_burger.launch.py
```


# Trouble Shooting

## 1. No module named 'catkin_pkg'

### 1) Conda를 사용하는 경우
```bash
conda install -c auto catkin_pkg
```

### 2) 일반 환경
```bash
pip install catkin_pkg
```