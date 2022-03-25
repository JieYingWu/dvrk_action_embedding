
# This is the script to convert the JHU recored data from rosbag format to video RGB images(.jpg) and kinematics files(.txt).


## Install:

ffmpeg is needed and can be installed on Ubuntu with:

    sudo apt install ffmpeg

ros and other stuff

    sudo apt install python3-roslib python3-sensor-msgs python3-opencv



## Usage:

### 1. Modify the path and name of the source data in 'recieve_data.py':
    save_root = {path_to_save_folder}

    bag_name = {rosbag_name}
    
    (other setting please refer to the code)
    
### 2. Initialize ROS
    roscore
    
### 3. Run the script
    python recieve_data.py

### 4. Play the rosbag file:
    rosbag play {rosbag_name}.bag


## Acknowledgement

Code modified from [rosbag2video](https://github.com/mlaiacker/rosbag2video/). Thanks for contributions
    
## Citation

      @inproceedings{
      long2021relational,
      title={Relational graph learning on visual and kinematics embeddings for accurate gesture recognition in robotic surgery},
      author={Long, Yonghao and Wu, Jie Ying and Lu, Bo and Jin, Yueming and Unberath, Mathias and Liu, Yun-Hui and Heng, Pheng Ann and Dou, Qi},
      booktitle={2021 IEEE International Conference on Robotics and Automation (ICRA)},
      pages={13346--13353},
      year={2021},
      organization={IEEE}
      }


