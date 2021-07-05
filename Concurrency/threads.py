import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

#from multiprocessing import Process

def ask_user():
	start = time.time()
	user_input = input("Enter your name: ")
	greet = f"Hello {user_input}"
	print(greet)
	print(f"ask_user() BLOCKING total time: {time.time() - start} seconds")

def complex_calculation():
	start = time.time()
	print("Started calculation ...")
	[x**2 for x in range(20000000)]
	print(f"complex_calculation() total time: {time.time() - start} seconds")

def thread_exercise1():

	start = time.time()
	# ask_user()
	# complex_calculation()

	# Main thread is the app

	thread1 = Thread(target=complex_calculation)
	thread2 = Thread(target=ask_user)

	thread1.start()
	thread2.start()

	# Join child threads to parent thread so the parent waits before exiting

	thread1.join()
	thread2.join()

	print(f"Single thread total time: {time.time() - start} seconds")

	print("***********************************")
	print("Threading with non-blocking threads")
	print("***********************************")

	start = time.time()

	thread1 = Thread(target=complex_calculation)
	thread2 = Thread(target=complex_calculation)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print(f"Proof that Python threads do not run in parallel total time: {time.time() - start} seconds")

def thread_pool_exercise():

	print("**************************")
	print("* concurrent thread pool *")
	print("**************************")

	start = time.time()

	# Will wait until finish so no need to join thread to main
	with ThreadPoolExecutor(max_workers=2) as pool:
		pool.submit(complex_calculation)
		pool.submit(ask_user)

	# context manager eliminates need for pool.shutdown()

	print(f"concurrent total time: {time.time() - start} seconds")

def concurrency_exercise():

	print("**************************")
	print("* concurrent thread pool *")
	print("**************************")


	start = time.time()

	# Will wait until finish so no need to join thread to main
	with ThreadPoolExecutor(max_workers=2) as pool:
		pool.submit(complex_calculation)
		pool.submit(ask_user)

	# context manager eliminates need for pool.shutdown()

	print(f"concurrent total time: {time.time() - start} seconds")

def main():

	print("*******************")
	print("* Multiprocessing *")
	print("*******************")


	start = time.time()

	ask_user()
	complex_calculation()

	print(f"Single thread total time: {time.time() - start} seconds")

	with ProcessPoolExecutor(max_workers=2) as pool:
		pool.submit(complex_calculation)
		pool.submit(complex_calculation)


	print(f"Two processes total time: {time.time() - start} seconds")

##########
# Module #
##########

if __name__ == "__main__":
	main()