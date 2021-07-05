import time
import random
import queue
from threading import Thread
#from concurrent.futures import ThreadPoolExecutor
#from concurrent.futures import ProcessPoolExecutor

COUNTER = 0

# Create the JOB and COUNTER queues

JOB_QUEUE = queue.Queue()
COUNTER_QUEUE = queue.Queue()

""" Runs forever processing counter items in the COUNTER_QUEUE 
    incremented counter item is put in the PRINT_QUEUE """
def increment_manager():

	global COUNTER

	while True:
		increment = COUNTER_QUEUE.get() # waits for an item
		old_counter = COUNTER
		COUNTER = old_counter + 1
		JOB_QUEUE.put((f"New counter value is {COUNTER}","-------------"))
		COUNTER_QUEUE.task_done() # unlocks the queue

""" Runs forever processing print items in the PRINT_QUEUE """
def printer_manager():
	while True:
		for line in JOB_QUEUE.get():
			print(line)
		JOB_QUEUE.task_done()

""" Seed the COUNTER_QUEUE """
def increment_counter():

	COUNTER_QUEUE.put(1)

def main():

	print("*************************************")
	print("* Threads Queues with Shared States *")
	print("*************************************")
	""" Place one in the COUNTER_QUEUE and then use a function to
		update the global counter.  Use another queue to control the
		printing 
	"""
	# Start the COUNTER_QUEUE
	Thread(target=increment_manager, daemon=True).start()

	# Start the PRINT_QUEUE
	Thread(target=printer_manager,daemon=True).start()

	# Create 10 threads each containing 1
	worker_threads = [Thread(target=increment_counter) for thread in range(10)]

	for thread in worker_threads:
		thread.start()

	for thread in worker_threads:
		thread.join()

	COUNTER_QUEUE.join()
	JOB_QUEUE.join()



##########
# Module #
##########

if __name__ == "__main__":
	main()
