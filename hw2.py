usersPasswordict = { 
    "user1": "password1", 
    "user2": "password2", 
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10", 
}

username = input("Enter username:")
password = input("Enter password:")
  
if usersPasswordict[username] == password: 
    print("You are now logged in") 
else: 
    print("Invalid username or password") 

textbooks = {
    "physics": 300,
    "maths": 400,
    "english": 200,
    "biology": 600,
    "chemistry": 350    
}

print(textbooks)

#change physics textbook price
textbooks["physics"] = 200
print(textbooks)

#add in two more textbooks
textbooks["geography"] = 550
textbooks["history"] = 450

print(textbooks)

#print cost of books
x = textbooks.values()
print(x)

#print cost of books and costs
for x,y in textbooks.items():
    print(x,y)