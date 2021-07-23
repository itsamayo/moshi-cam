# Moshi Cam

Live stream of Moshis home with temp and humidity stats for both cool and warm sides of the enclosure

## How it works
The Pi streams the output of the camera module over the web via Flask. Temperature and humidity data for both sides of the enclosure are received from a Firebase RealtimeDB that gets updates from 2 DHT22 modules inside the enclosure.

```
<raspberry_pi_ip:5001> 
```

## Requirements (Recommendations)
* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Raspbian OS recommended for best compatibility
* Python 3 recommended.

## Library dependencies
Install the following dependencies to create camera stream.

```
sudo apt-get update 
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install imutils
sudo pip3 install opencv-python
sudo pip3 install firebase-admin


```
