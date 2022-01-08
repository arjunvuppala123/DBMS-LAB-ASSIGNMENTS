import threading
import os

def task1():
 print(threading.current_thread().name)

def task2():
 print(threading.current_thread().name)


if __name__ == "__main__":

 # print ID of current process
 print("ID of process running main program:",os.getpid())

 # print name of main thread
 print("Main thread name:",threading.current_thread().name)
 # get the current thread object

 # creating threads
 t1 = threading.Thread(target=task1, name='t1')
 t2 = threading.Thread(target=task2, name='t2')

 # starting threads
 t1.start()
 t2.start()

 # wait until all threads finish
 t1.join()
 t2.join()