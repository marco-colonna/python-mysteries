# stores the quiz questions
questions = ["How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n",
            "What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n",
            "What's more important?\n(A) Money\n(B) Love\n",
            "What's your favorite decade?\n(A) 1910s\n(B) 2010s\n",
            "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n"]
# stores the candidate's answers to each question
answers = []
# stores the responses if the candidate chooses "A"
response_A = ["Reading a book, nice choice!\n",
            "Curator? Sounds like a lot of responsibility...\n",
            "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n",
            "Great decade! Save for World War 1...\n",
            "Driving? I hope you like cars!\n"]
# stores the responses if the candidate chooses "B"
response_B = ["Attending a party? Sounds fun!\n",
            "Running a business? Sounds like a big investment...\n",
            "<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3\n",
            "Great decade! Save for Donald Trump...\n",
            "Flying? I hope you like airplanes!\n"]

# ask the candidate each question of the quiz
for index, question in enumerate(questions):
    answer = input(question)
    if answer == "A":
        print(response_A[index])
    elif answer == "B":
        print(response_B[index])
    else:
        print("You must type A or B, let's just say you chose A.\n")
        answer = "A"
    answers += answer

# print out their choices
print(f"You chose {answers[0]}, then {answers[1]}, then {answers[2]}, then {answers[3]}, then {answers[4]}.\n")

# create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# update scoring variables based on the activity choice
if answers[0] == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

# update scoring variables based on the job choice
if answers[1] == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the value choice
if answers[2] == "A":
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the decade choice
if answers[3] == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# update scoring variables based on the travel choice
if answers[4] == "A":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

# print the results depending on the score
if sam_like >= 3:
    print( "You're most like Sharp-Eyed Sam!" )
elif cam_like >= 3:
    print( "You're most like Curious Cam!" )
elif kai_like >= 3:
    print( "You're most like Keen Kai!" )
else:
    print( "You're most like Inquisitive Indy!" )

# More challenges for your quiz code
# As an added challenge, you can start exploring how you might:
#   Reduce the number of if, elif, and else statements in your code. -> DONE
#   Allow users to select a new choice if they didn't enter A or B.
