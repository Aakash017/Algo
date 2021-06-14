import time
from threading import Thread
from tqdm import tqdm


class A(Thread):
    def run(self):
        for i in tqdm(range(500)):
            print("Hello")


class B(Thread):
    def run(self):
        for i in tqdm(range(500)):
            time.sleep(.3)
            print("Hi")


t1 = A()
t2 = B()
t1.start()
t2.start()
