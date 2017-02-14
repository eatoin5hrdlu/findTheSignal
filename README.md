# findTheSignal
#
# remote login to this machine
# Raspberry Pi

1) DISABLE VNC option in:
    (Click on the Raspberry)
    Preferences->Raspberry Pi Configuration-> Interfaces

2) Add xrdp and vnc4server to standard Raspberry Pi configuration

     sudo apt-get install xrdp vnc4server

3) Restart xrdp
     sudo service xrdp --full-restart

4) To get a text with the IP when the system boots up, add the command:
     /home/pi/src/findTheSignal/audio/smstext.py <carrier> <phone-number>

(To be able to send texts)
5) Add your gmail login/password to "secrets.py" in findTheSignal/audio
 { 'login' : <login-in-quotes>, 'password' : <gmail password in quotes> }

Files in the audio directory are the current ones for Find The Signal

Source materials are in mp3,wav,ogg,m4r directories according to format.

Bash script launch.sh should be called from /etc/rc.local (or equivalent)
to start the three two-channel audio tracks playing on repeat.

For our purposes, we need six (five really) independent Cap-com sound bites and we accomplish this with only three instances of aplay by creating stereo wave files with two cap-com sound clips.

With Audacity, this was accomplished by Importing->Audio from one of the cap com files, Importing-Audio from the second cap com file.  Editing these two mono recordings so that they have approximately the same length.  Removing silence is easy, and if the lengths are very different, duplicate the shorter clip in the track since we are simply playing them on repeat mode anyway.

Then click on the top tracks track-name pulldown where the Create Stereo Track option is found. This will combine the two mono tracks into left and right audio for a single stereo track.  On my Audacity, previewing this file, I am unable to hear one of the channels, but if you Export->Audio as a wav file and then move it to the Linux system and listen with Aplay, the channels are both there.

Your version of Audacity may not be broken, like mine.

When you add the (USB) sound cards you will need to find their names with the command "aplay -L" and change the appropriate device names in launch.sh.
As you will see, you can plug in more sound cards and add lines to launch.sh for even more than six channels.  We are currently only using the built-in sound card and two USB sound cards from AdaFruit (recommended because they have a pigtail and therefore they don't crowd out your other USB ports.

