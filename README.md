# doom-ai
A programming to build a Doom AI
- http://vizdoom.cs.put.edu.pl
- https://github.com/mwydmuch/ViZDoom

````bash
git clone https://github.com/HackTheNight/doom-ai.git
cd doom-ai/
git clone https://github.com/mwydmuch/ViZDoom.git
````


o get all dependencies (except JDK) on Ubuntu execute the following commands in the shell (requires root access):

# ZDoom dependencies
sudo apt-get install build-essential zlib1g-dev libsdl2-dev libjpeg-dev \
nasm tar libbz2-dev libgtk2.0-dev cmake git libfluidsynth-dev libgme-dev \
libopenal-dev timidity libwildmidi-dev

# Boost libraries
sudo apt-get install libboost-all-dev

# Python 2 dependencies
sudo apt-get install python-dev python-pip
pip install numpy
# or install Anaconda 2 and add it to PATH

# Lua binding dependencies
sudo apt-get install liblua5.1-dev

dependancies
sudo apt-get install g++ make cmake libsdl2-dev git zlib1g-dev libbz2-dev \
libjpeg-dev libfluidsynth-dev libgme-dev libopenal-dev libmpg123-dev \
libsndfile1-dev libwildmidi-dev libgtk-3-dev timidity nasm tar chrpath
