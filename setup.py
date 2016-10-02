from distutils.core import setup
from time import sleep
try:
    from termcolor import cprint
    cprint("Nice!, you have termcolor already!\n\n","green")
    cprint("INSTALLING "*6,"red")
except:
    print "######################\nTo use this module you'll need to download\n'Termcolor'\n######################\n\n"
    sleep(3)
    print "INSTALLING "*6
setup(
    name='pcf8574',
    version='0.5',
    packages=[''],
    url='',
    license='',
    author='Kacper Serewis',
    author_email='k4czp3r.dev@gmail.com',
    description='A python wrapper to turn on/off pins of pcf8574'
)
try:
    cprint("DONE "*10,"green")
except:
    print("DONE "*10)