# Author: Zach Tatman
# Date: 6/11/2021

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import logging
import threading
import time

# Scheduler class
class Scheduler:
  def __init__(self):
    self.lock = threading.Lock()
    self.name = 0

  def job(self, funct, ms):
    name = self.name
    logging.info("Thread %s: starting job", name)
    logging.debug("Thread %s about to lock", name)
    with self.lock:
      logging.debug("Thread %s has lock", name)
      time.sleep(ms/1000)
      funct()
      logging.debug("Thread %s about to release lock", name)
    logging.debug("Thread %s after release", name)
    logging.info("Thread %s: finishing job", name)

# Job that adds two numbers
def add(a, b):
  def adder():
    print(a + b)
  return adder


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    shedule = Scheduler()
    shedule.job(add(1,2), 5000)
