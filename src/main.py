#! ../bin/python3
import sys, subprocess, getpass, linecache, pip, os
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
x = ''
if len(sys.argv) == 1:
    x = input()
else:
    x = sys.argv[1]
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice','english+f4')
    engine.setProperty('rate',175)
    engine.setProperty('volume',1.0)
    for i in range(len(x)):
        engine.say(linecache.getline('values.txt',ord(x[i])+1))
    engine.runAndWait()
    engine.stop()
except OSError:
    print('Install espeak for your system.')
    if sys.platform == 'win32':
        print('Go here to install espeak : http://espeak.sourceforge.net/download.html')
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        print('Ubuntu (or Debian-based distros): $ sudo apt-get install espeak -y\nFedora (or any RHEL based distros): $ sudo yum install espeak -y\nArch (or any arch based distros : $ sudo pacman -S espeak')
    else:
        print('Use homebrew to install espeak.')
                