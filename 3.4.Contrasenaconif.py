user_1="pedro";
pass_1="1234";
user_2="angel"
pass_2="a4s1"

print("Empresa XY\n");
print("Login\n");

user=input("User: ")
passw=input("Password: ")

if(user.lower==user_1 and passw==pass_1) or (user.lower==user_2 and passw==pass_2):
    print("Acceso correcto");
else:
    print("Que aweonao se equivoco")