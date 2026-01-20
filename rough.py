# Method vs Function
# A method is a function that is associated with an object.
# A function is a standalone piece of code that performs a specific task.

from project1 import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

# method
# print(user1.get_name())  # Accessing the get_name method of the chatbook class
# user1.set_name("Atharv")
# print(user1.get_name())


# lst = [1, 2, 3, 4, 5]

# # function
# a1 = len(lst)
# print(a1)

