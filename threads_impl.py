import threading
import time
import psutil

class new_thread(threading.Thread):
	
	def __init__(self, thread_id, name, delay):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.name = name
		self.delay = delay

	def run(self):
		running_times = 3
		print(self.name + " starts")
		print_usage(self.name, self.delay, running_times)
		print(self.name + " finishes")

def print_usage(threadName, delay, running_times):
   while running_times:
      time.sleep(delay)
      print(threadName, psutil.virtual_memory())

      running_times = running_times -  1

thread1 = new_thread(1, "Thread 1", 1)
thread2 = new_thread(2, "Thread 2", 1)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Process finished.")
		