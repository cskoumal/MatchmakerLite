# Conner Skoumal
# Matchmaker Lite

print("")
print("Matchmaker 2021")
print("")
print("[[Your instruction here.]]")
print("")

userResponse1 = int(input("Ironclad Robotics rocks!"))
desiredResponse1 = 5
compatibility1 = 5 - abs(userResponse1 - desiredResponse1)
print("Question 1 Compatibility: " + str(compatibility1))
print("")

userResponse2 = int(input("Sports are the best!"))
desiredResponse2 = 1
compatibility2 = 5 - abs(userResponse2 - desiredResponse2)
print("Question 2 Compatibility: " + str(compatibility2))
print("")

totalCompatibility = (compatibility1 + compatibility2) * 10
print("Total Compatability: " + str(totalCompatibility))
print("")
