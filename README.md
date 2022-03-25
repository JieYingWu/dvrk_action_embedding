
This is the script to convert the JHU dataset from rosbag format to video images(.png) and kinematics(.txt) file.


## install:

ffmpeg is needed and can be installed on Ubuntu with:

    sudo apt install ffmpeg

ros and other stuff

    sudo apt install python3-roslib python3-sensor-msgs python3-opencv



## usage:

#Play the rosbag file:
    pyhon

#Run the script

## example output:

    ./rosbag2video.py camera_and_state.bag

    rosbag2video, by Maximilian Laiacker 2020 and Abel Gabor 2019

    ############# COMPRESSED IMAGE  ######################
    /image_raw/compressed  with datatype: sensor_msgs/CompressedImage

    frame=   77 fps= 13 q=28.0 size=    1280kB time=00:00:00.96 bitrate=10922.2kbits/s speed=0.156x

## Acknowledgement

    Code modified from [rosbag2video](https://github.com/mlaiacker/rosbag2video/). Thanks for contributions


