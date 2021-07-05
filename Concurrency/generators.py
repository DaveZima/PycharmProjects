
from collections import deque
from types import coroutine

FRIENDS = deque(("Dave","Cecilia","Gabby"))



def countdown(n):
	while n > 0:
		yield n
		n -= 1

def gen_thread_exercise():

	print("******************************************")
	print("* Simulate Thread Queue Using Generators *")
	print("******************************************")

	tasks = [countdown(5),countdown(10),countdown(20)]

	while tasks:
		task = tasks[0]
		tasks.remove(task)
		# Call/Execute a generator
		try:
			x = next(task)
			print(x)
			tasks.append(task) # Add the generator back into the queue
		except StopIteration:
			print("Task finishied")

def yield_gen_from_gen_exercise():

	title_box("Yielding from another iterator in Python")

	friends_generator = get_friend()
	g = greet(friends_generator)
	print(next(g))
	print(next(g))

def recv_data_from_yield_exercise():

	title_box("Receiving data through yield")

	greeter = greet3(friend_upper())
	greeter.send(None)
	greeter.send("Hello")
	greeter.send("Hello")



def title_box(title):

	lgth = len(title) + 4
	print("*" * lgth)
	print("* " + title + " *")
	print("*" * lgth)

def get_friend():
	global FRIENDS
	yield from FRIENDS

def greet(g):

	while True:
		try:
			friend = next(g)
			yield f"HELLO {friend}"
		except StopIteration:
			pass

def greet2():
	friend = yield
	print(f"Hello {friend}")

@coroutine
def friend_upper():
	while FRIENDS:
		friend = FRIENDS.popleft().upper()
		greeting = yield
		print(f"{greeting} {friend}")

def greet3(g):

	# Could be yield from g  Core Routine
	g.send(None) # Prime generator
	while True:
		greeting = yield
		g.send(greeting)

async def greet4(g):

	await g


def main():

	title_box("The async and await keywords")

	greeter = greet4(friend_upper())
	greeter.send(None)
	greeter.send("Hello")
	greeter.send("Hello")


	title_box("Python asynchronus development uses generators for threading")



##########
# Module #
##########

if __name__ == "__main__":
	main()

