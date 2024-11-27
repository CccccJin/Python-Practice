# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

scores = input("Please enter your score: ")
try:
    a = float(scores)
    if a > 0.0 and a < 1.0:
        if a < 0.6:
            print("F")
        elif a >= 0.6 and a < 0.7:
            print("D")
        elif a >= 0.7 and a < 0.8:
            print("C")
        elif a >= 0.8 and a < 0.9:
            print("B")
        elif a >= 0.9 and a <= 1.0:
            print("A")
    else:
        print("Bad score")
except:
    print("Bad scores")