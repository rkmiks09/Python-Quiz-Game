print("Welcome to My Quiz Game!")
playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play : ")
print("Use Proper Space While givng the Answers")
score = 0

answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of GPU? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of ALU? ")
if answer.lower() == "arithematic logical unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print ("You got " + str(score)+ " Questions Correct!")
print ("You got " + str((score / 4)* 100)+ "%")

