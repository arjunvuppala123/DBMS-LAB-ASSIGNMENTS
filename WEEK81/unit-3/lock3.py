import threading
def worker1(v):
    	#with v.get_lock():
	for i in range(1000000):
		ctypes_int.value += 1

def worker2(v):
    	#with v.get_lock():
	for i in range(1000000):
		ctypes_int.value += 2
	
ctypes_int = threading.Value("i", 0)
print(ctypes_int.value)
process1 = threading.Thread(
    target=worker1, args=[ctypes_int])
process2 = threading.Thread(
    target=worker2, args=[ctypes_int])

process1.start()
process2.start()
process1.join()
process2.join()

print (ctypes_int.value)
