# GAZEBO_SIM

이 저장소는 Gazebo에서 IMU, GPS, 3D LiDAR와 같은 다양한 센서를 사용하기 위한 시뮬레이션 환경을 포함하고 있습니다.

## 📂 저장소

[GAZEBO_SIM GitHub 저장소](https://github.com/Carpediem324/GAZEBO_SIM.git)

## 📜 설명

이 프로젝트는 Gazebo에서 다양한 센서를 사용하기 위해 만들어졌습니다. 포함된 센서들은 다음과 같습니다:
- **IMU** (관성 측정 장치)
- **GPS** (위성 위치 확인 시스템)
- **3D LiDAR** (광 탐지 및 거리 측정)

저장소를 탐색하고 프로젝트에 기여해 주세요.

## 🚀 시작하기

이 프로젝트를 시작하려면 다음 명령어를 사용하여 저장소를 클론하세요:

```bash
git clone https://github.com/Carpediem324/GAZEBO_SIM.git
```

## 🛠 사용법

Gazebo에서 센서를 사용하는 방법에 대한 지침은 저장소에 제공될 예정입니다.

---

## bashrc에 추가해야함.모델경로
```
export TURTLEBOT3_MODEL=burger	
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/shh/ssafy_gazeboy/ssafy_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/
```