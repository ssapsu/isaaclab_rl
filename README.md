# IsaacLab with Kinova and Dobot Manipulators

## Installation

Follow the steps below to install Isaac Sim and IsaacLab:

### Prerequisites
Refer to the [IsaacLab Installation Guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html) and install Isaac Sim as follows:

```sh
conda create -n env_isaaclab python=3.10
conda activate env_isaaclab
pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121
pip install --upgrade pip
pip install isaacsim[all,extscache]==4.5.0 --extra-index-url https://pypi.nvidia.com
```

### Install IsaacLab
Activate the conda environment and install IsaacLab:

```sh
git clone https://github.com/isaac-sim/IsaacLab.git
sudo apt install cmake build-essential
cd IsaacLab
./isaaclab.sh --install # or "./isaaclab.sh -i"
```

### System Requirements
- **OS:** Ubuntu 22.04
- **GPU:** NVIDIA RTX 4090
- **Driver Version:** 535.183.01

---

## Customization for Kinova and Dobot Manipulators
IsaacLab by default includes Franka Emika. We modify it to support **Robotiq 2F-85 gripper with Dobot and Kinova manipulators**.

### Steps to Modify IsaacLab

1. Clone the repository containing the custom modifications:
   ```sh
   git clone https://github.com/ssapsu/isaaclab_rl.git source/isaaclab_tasks/isaaclab_tasks/manager_based
   ```
2. Move `kinova.py` and `dobot.py` to the robots folder:
   ```sh
   mv source/isaaclab_tasks/isaaclab_tasks/manager_based/kinova.py source/isaaclab_assets/isaaclab_assets/robots/
   mv source/isaaclab_tasks/isaaclab_tasks/manager_based/dobot.py source/isaaclab_assets/isaaclab_assets/robots/
   ```
3. Modify `__init__.py` to include Dobot:
   ```sh
   echo "from .dobot import *" >> source/isaaclab_assets/isaaclab_assets/robots/__init__.py
   ```

---

## Running the Training

### Train with Dobot
```sh
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py --task Isaac-Lift-Cube-Dobot-v0 --num_envs 512
```

### Train with Kinova
```sh
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py --task Isaac-Lift-Cube-Kinova-v0 --num_envs 512
```

---

## Training Demonstration
You can watch the training process in the following videos:

# IsaacLab with Kinova and Dobot Manipulators

## Installation

Follow the steps below to install Isaac Sim and IsaacLab:

### Prerequisites
Refer to the [IsaacLab Installation Guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html) and install Isaac Sim as follows:

```sh
conda create -n env_isaaclab python=3.10
conda activate env_isaaclab
pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121
pip install --upgrade pip
pip install isaacsim[all,extscache]==4.5.0 --extra-index-url https://pypi.nvidia.com
```

### Install IsaacLab
Activate the conda environment and install IsaacLab:

```sh
git clone https://github.com/isaac-sim/IsaacLab.git
sudo apt install cmake build-essential
cd IsaacLab
./isaaclab.sh --install # or "./isaaclab.sh -i"
```

### System Requirements
- **OS:** Ubuntu 22.04
- **GPU:** NVIDIA RTX 4090
- **Driver Version:** 535.183.01

---

## Customization for Kinova and Dobot Manipulators
IsaacLab by default includes Franka Emika. We modify it to support **Robotiq 2F-85 gripper with Dobot and Kinova manipulators**.

### Steps to Modify IsaacLab

1. Clone the repository containing the custom modifications:
   ```sh
   git clone https://github.com/ssapsu/isaaclab_rl.git source/isaaclab_tasks/isaaclab_tasks/manager_based
   ```
2. Move `kinova.py` and `dobot.py` to the robots folder:
   ```sh
   mv source/isaaclab_tasks/isaaclab_tasks/manager_based/kinova.py source/isaaclab_assets/isaaclab_assets/robots/
   mv source/isaaclab_tasks/isaaclab_tasks/manager_based/dobot.py source/isaaclab_assets/isaaclab_assets/robots/
   ```
3. Modify `__init__.py` to include Dobot:
   ```sh
   echo "from .dobot import *" >> source/isaaclab_assets/isaaclab_assets/robots/__init__.py
   ```

---

## Running the Training

### Train with Dobot
```sh
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py --task Isaac-Lift-Cube-Dobot-v0 --num_envs 512
```

### Train with Kinova
```sh
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py --task Isaac-Lift-Cube-Kinova-v0 --num_envs 512
```

---

## Training Demonstration
You can watch the training process in the following videos:

[![Dobot Training](https://img.youtube.com/vi/IZ1218bCFwY/0.jpg)](https://www.youtube.com/watch?v=IZ1218bCFwY)

[![Kinova Training](https://img.youtube.com/vi/jzSWpFRQUzo/0.jpg)](https://www.youtube.com/watch?v=jzSWpFRQUzo)
