from sensors import Sensors
from lid import Lid
from display import Display
from level import Level
import time
import threading

class Main:
    def run():

        while True:
            ts = threading.Thread(target=Sensors.run)
            ts.start()
            #Lid.run()
            tl = threading.Thread(target=Level.run)
            tl.start()
            td = threading.Thread(target=Display.run)
            td.start()
'''
if __name__ == '__main__':
    print("Starting up!")
    try:
        Main.run()
    except:
        print('Exit')
'''
def infiniteloop1():
    while True:
        print('Display is working!')
        time.sleep(10)

def infiniteloop2():
    while True:
        print('Sensors is working!')
        time.sleep(4)
def infiniteloop3():
    while True:
        print('Level sensing is working!')
        time.sleep(30)

try:
    thread1 = threading.Thread(target=infiniteloop1)
    thread1.start()

    thread2 = threading.Thread(target=infiniteloop2)
    thread2.start()

    thread3 = threading.Thread(target=infiniteloop3)
    thread3.start()
except:
    print('Ending')