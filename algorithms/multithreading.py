import time
from threading import Thread
from tqdm import tqdm


class A(Thread):
    def run(self):
        for i in tqdm(range(50)):
            print("Hello")


class B(Thread):
    def run(self):
        for i in tqdm(range(50)):
            # time.sleep(.3)
            print("Hi")


t1 = A()
t2 = B()
# t1.start()
# t2.start()


class Even(Thread):
    for i in range(100):
        if i % 2 == 0:
            print("even = ", i)
            time.sleep(3)


class Odd(Thread):
    for i in range(100):
        if i % 2 != 0:
            print("odd = ", i)
            # time.sleep()


e = Even()
o = Odd()
# e.run()
# o.run()
#
# # o.join()
# # e.join()

Thread.start(e)
Thread.start(o)