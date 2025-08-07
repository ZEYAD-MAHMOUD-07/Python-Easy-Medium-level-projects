print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")


answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")


print("You got " + str(score) + "/3 questions correct!")
