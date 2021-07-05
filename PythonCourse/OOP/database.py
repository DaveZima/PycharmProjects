
class Database:

	# Class variable not an instance variable so all objects have the same variable
	content = {"users":[]}

	@classmethod
	def insert(cls,data):    # cls = self
		cls.content["users"].append(data)

	@classmethod
	def remove(cls,finder):
		cls.content["users"] = [user for user in cls.content["users"] if not finder(user)]

	@classmethod
	def find(cls,finder):
		return [user for user in cls.content["users"] if finder(user) ]
