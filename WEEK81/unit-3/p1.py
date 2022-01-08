import threading
import os 

def print_cube(num):
    print("cube of a number",num * num * num)
def print_square(num):
    print("cube of a number",num * num)
if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")