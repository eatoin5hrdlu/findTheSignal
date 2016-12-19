#!/bin/bash
nohup /home/pi/src/findTheSignal/audio/capcom.sh "default" /home/pi/src/findTheSignal/audio/orange_lightning.wav >/dev/null &
nohup /home/pi/src/findTheSignal/audio/capcom.sh "plughw:Set,0" /home/pi/src/findTheSignal/audio/eagle_flash.wav >/dev/null &
nohup /home/pi/src/findTheSignal/audio/capcom.sh "plughw:Set_1,0" /home/pi/src/findTheSignal/audio/oddity_landing.wav >/dev/null &
