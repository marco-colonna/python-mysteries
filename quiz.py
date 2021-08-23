# ask the candidate a question
activity = input("How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n")
if activity == "A":
    print("Reading a book, nice choice!")
elif activity == "B":
    print("Attending a party? Sounds fun!")
else:
    print("You must type A or B, let's just say you like to read.")
    activity = "A"

# ask the candidate a second question
job = input("What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n")
if job == "A":
    print("Curator? Sounds like a lot of responsibility...")
elif job == "B":
    print("Running a business? Sounds like a big investment...")
else:
    print("You must type A or B, let's just say you want to be a curator at the Smithsonian.")
    job = "A"

# ask the candidate a third question
value = input("What's more important?\n(A) Money\n(B) Love\n")
if value == "A":
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
elif value == "B":
    print("<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
else:
    print("You must type A or B, let's just say money is more important to you.")
    value = "A"

# ask the candidate a fourth question
decade = input("What's your favorite decade?\n(A) 1910s\n(B) 2010s\n")
if decade == "A":
    print("Yeah! World War 1 was great!")
elif decade == "B":
    print("Yeah! The War on Terror was great!")
else:
    print("You must type A or B, let's just say the 1910s is your favorite decade.")
    decade = "A"

# ask the candidate a fifth question
travel = input("What's your favorite way to travel?\n(A) Driving\n(B) Flying\n")
if travel == "A":
    print("Driving? I hope you like cars!")
elif travel == "B":
    print("Flying? I hope you like airplanes!")
else:
    print("You must type A or B, let's just say driving is your favorite way to travel.")
    travel = "A"

# print out their choices
print(f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")
