users = []
for i in range(5):
    user = input("Enter your username")
    pwd = input("Enter your password")
    login = user, pwd
    users.append(login)
print(users)

