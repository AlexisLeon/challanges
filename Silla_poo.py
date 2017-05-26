import datetime as dt
class Person(object):
	def __init__(self, name, dob_y):
		self.name = name
		self.dob_y = dob_y

	def getAge(self):
		age = dt.datetime.now().year - self.dob_y
		return str(age) + ', you\'re old! ' if age >= 18 else age

class User(Person):
	def __init__(self, name, dob_y, email, phone):
		Person.__init__(self, name, dob_y)
		self.email = email
		self.phone = phone
	
	def bePolite(self):
		return 'Hi, ' + self.name

name = str(raw_input('name? '))
dob_y = int(raw_input('year? '))
email = str(raw_input('email? '))
phone = str(raw_input('phone? '))
user = User(name, dob_y, email, phone)
print user.bePolite()
print user.getAge()