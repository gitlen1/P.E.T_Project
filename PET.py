import mysql.connector

pet_user = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2195",
  database="pet"

)

print(pet_user)

tempuser = {

}

while True:
    fname = input("First name: ")
    if fname != None and fname != "":
        tempuser["first_name"] = fname 
        break
    else:
        continue

while True:
    lname = input("Last name: ")
    if lname != None and lname != "":
        tempuser["last_name"] = lname
        break
    else:
        continue

while True:
    age = int(input("Age: "))
    if age != None:
        tempuser["age"] = age
        break
    else:
        continue

while True:
    email = input("Email adress: ")
    if email != None and email != "":
        tempuser["email"] = email
        break
    else:
        continue

while True:      
    from getpass import getpass
    password = getpass("Password: ")
    if password != None and password != "":
        tempuser["password"] = password
        break
    else:
        continue

while True:
    address = input("Address: ")
    if address != None and address != "":
        tempuser["address"] = address
        break
    else:
        continue



    
curs = pet_user.cursor()

sql = "INSERT INTO users (user_id, first_name, last_name, age, email, password, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (1, tempuser["first_name"], tempuser["last_name"], tempuser["age"], tempuser["email"], tempuser["password"], tempuser["address"])
curs.execute(sql, val)

pet_user.commit()

curs = pet_user.cursor()
