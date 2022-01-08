'''
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used the names P() and V() instead of acquire() and release())


A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().


import threading
import time
sem = threading.Semaphore()

def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)

t = threading.Thread(target = fun1)
t.start()
t2 = threading.Thread(target = fun2)
t2.start()
'''
import threading
from  time import sleep
sem = threading.Semaphore()
print(sem)
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
