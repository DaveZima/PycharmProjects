
user = {"user": "Jose", "access_level": "admin"}

# This is a decorator receives function and returns function
def user_has_permission(func):
	def secure_func():
		if user.get("access_level") == "admin":
			return func()
	return secure_func()

# Example function that does nothing really
@user_has_permission
def my_function():
	"""
	my_function doc str
	"""
	return "password for admin panel is 1234."

def another():
	pass

# Show the result
print(my_function().__name__)