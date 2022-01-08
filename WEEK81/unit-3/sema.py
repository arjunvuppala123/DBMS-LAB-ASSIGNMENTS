import threading
from  time import sleep
sem = threading.Semaphore()
def fun1():
    print("fun1 starting")
    sem.acquire()
    for loop in range(1,3):
        print("Fun1 Working {}".format(loop))
        sleep(1)
    sem.release()
    print("fun1 finished")
def fun2():
    print("fun2 starting")
    while not sem.acquire(blocking=False):
        print("Fun2 No Semaphore available")
        sleep(1)
    else:
        print("Got Semphore")
        for loop in range(1, 3):
            print("Fun2 Working {}".format(loop))
            sleep(1)
    sem.release()
t1 = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)
t1.start()
t2.start()
t1.join()
t2.join()
print("All Threads done Exiting")
