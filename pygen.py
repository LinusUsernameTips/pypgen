import secrets
import keyword 
import string

print("██╗     ██╗   ██╗████████╗███████╗    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗")
print("██║     ██║   ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
print("██║     ██║   ██║   ██║   ███████╗    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║")
print("██║     ██║   ██║   ██║   ╚════██║    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║")
print("███████╗╚██████╔╝   ██║   ███████║    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║")
print("╚══════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")                               
characters = string.printable.strip()
while True:
  while True:
   try:
    pass_len = int(input("How long you want the pass / passes to be? : "))
    break 
   except ValueError:
     print("Please enter a numeric value.")

  multiplepassq = str(input("Do you need multiple passes? Y/N : "))
  if multiplepassq.lower() == "y":
    while True:
     try:
      howmanypass = int(input("How many passes? : "))
      break
     except ValueError:
       print("Please enter a numeric value.")
    print("Ok!")
    for x in range(0, howmanypass):
     password2 = ""
     for x in range(0, pass_len):
      grabletter = secrets.choice(characters)
      password2   = password2 + grabletter
     print("Password : ", password2)
  if multiplepassq.lower() == "n":
     print("Ok!")
     password = ""
     for x in range(0, pass_len):
      grabletter = secrets.choice(characters)
      password  = password + grabletter
     print("Password : ", password)
