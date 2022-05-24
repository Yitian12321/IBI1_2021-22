#creat a class and use _init_ to identify the attributes.
class Staff():
  def __init__(self, first_name, last_name, location, role):
    self.first_name = first_name
    self.last_name = last_name
    self.location = location
    self.role = role
#Create a function to combine and show the basic information.
  def information(self):
    print("Full name:",self.first_name, self.last_name," Location:",self.location," Role:",self.role)
#example
a=Staff('Robert','Young','Edinburgh','faculty')
a.information()
#result
#Full name: Robert Young  Location: Edinburgh  Role: faculty
