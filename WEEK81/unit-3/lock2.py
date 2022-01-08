import time
from multiprocessing import Process, Value, Lock

def func(val, lock):
    for i in range(500):
        time.sleep(0.01)
        with lock:
            val.value += 1

if __name__ == '__main__':
    v = Value('i', 0)
    lock = Lock()
    procs=Process(target=func, args=(v, lock))

    procs.start()
    procs.join()

    print(v.value)
