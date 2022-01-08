'''import threading
import time
from threading import Thread

def i_am_thread():
	time.sleep(2)
	print("this is thread")
    
th = Thread(target= i_am_thread,name='fast')
th.start()
import time #main is executing
import threading
from threading import Thread

def i_am_thread():
	time.sleep(10)
	print("this is thread")
    
th = Thread(target= i_am_thread,name='fast')
th.start()
print("Current Thread count:",threading.active_count())
print("state:",th.is_alive())

import time
import threading
from threading import Thread

def i_am_thread():
	time.sleep(2)
	print("this is thread")
    
th = Thread(target= i_am_thread,name='fast')
th.start()
th.join()
print("Current Thread count:",threading.active_count())
print("state:",th.is_alive())
'''

import time
import threading
from threading import Thread

def i_am_thread():
	time.sleep(10)
	print("this is thread")
    
th = Thread(target= i_am_thread,name='fast')
th.start()
print("Current Thread count:",threading.active_count())
print("state:",th.is_alive())
th.join()
print("state:",th.is_alive())
print("get name:",th.getName())






