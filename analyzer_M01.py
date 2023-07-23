users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

name = input("zadej jmeno: ")
pass_u = input("zadej heslo: ")
#name = "bob"
#pass_u = "123"
print(f"username:{name}")
print(f"password:{pass_u}")
if name in users:
    if pass_u == users[name]:
        print("----------------------------------------")
        print(f"Welcome to the app, {name}")
    else:
        print("unregistered user, terminating the program")
else:
    print("unregistered user, terminating the program")
