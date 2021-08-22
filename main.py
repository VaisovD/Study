# a = str(input("Input first string: "))
# b = str(input("Input first string: "))
# if a==b:
#     print("Two strings are identical.")
# else:
#     print("Two strings are different.")

# Lesson 2
num1 = int(input("Input first number: "))

num2 = int(input("Input second number: "))

num3 = int(input("Input third number: "))

num4 = int(input("Input fourth number: "))

if num1>=num2>=num3>=num4:
    print("The numbers are in order of ", num1, ">=", num2, ">=", num3, ">=", num4, "." )
elif num1>=num2>=num4>=num3:
    print("The numbers are in order of ", num1, ">=", num2, ">=", num4, ">=", num3, "." )
elif num1>=num3>=num2>=num4:
    print("The numbers are in order of ", num1, ">=", num3, ">=", num2, ">=", num4, "." )
elif num1>=num3>=num4>=num2:
    print("The numbers are in order of ", num1, ">=", num3, ">=", num4, ">=", num2, "." )
elif num1>=num4>=num2>=num3:
    print("The numbers are in order of ", num1, ">=", num4, ">=", num2, ">=", num3, "." )
elif num1>=num4>=num3>=num2:
    print("The numbers are in order of ", num1, ">=", num4, ">=", num3, ">=", num2, "." )
elif num2>=num1>=num3>=num4:
    print("The numbers are in order of ", num2, ">=", num1, ">=", num3, ">=", num4, "." )
elif num2>=num1>=num4>=num3:
    print("The numbers are in order of ", num2, ">=", num1, ">=", num4, ">=", num3, "." )
elif num2>=num3>=num1>=num4:
    print("The numbers are in order of ", num2, ">=", num3, ">=", num1, ">=", num4, "." )
elif num2>=num3>=num4>=num1:
    print("The numbers are in order of ", num2, ">=", num3, ">=", num4, ">=", num1, "." )
elif num2>=num4>=num1>=num3:
    print("The numbers are in order of ", num2, ">=", num4, ">=", num1, ">=", num3, "." )
elif num2>=num4>=num3>=num1:
    print("The numbers are in order of ", num2, ">=", num4, ">=", num3, ">=", num1, "." )
elif num3>=num2>=num1>=num4:
    print("The numbers are in order of ", num3, ">=", num2, ">=", num1, ">=", num4, "." )
elif num3>=num2>=num4>=num1:
    print("The numbers are in order of ", num3, ">=", num2, ">=", num4, ">=", num1, "." )
elif num3>=num1>=num2>=num4:
    print("The numbers are in order of ", num3, ">=", num1, ">=", num2, ">=", num4, "." )
elif num3>=num1>=num4>=num2:
    print("The numbers are in order of ", num3, ">=", num1, ">=", num4, ">=", num2, "." )
elif num3>=num4>=num2>=num1:
    print("The numbers are in order of ", num3, ">=", num4, ">=", num2, ">=", num1, "." )
elif num3>=num4>=num1>=num2:
    print("The numbers are in order of ", num3, ">=", num4, ">=", num1, ">=", num2, "." )
elif num4>=num2>=num3>=num1:
    print("The numbers are in order of ", num4, ">=", num2, ">=", num3, ">=", num1, "." )
elif num4>=num2>=num1>=num3:
    print("The numbers are in order of ", num4, ">=", num2, ">=", num1, ">=", num3, "." )
elif num4>=num3>=num2>=num1:
    print("The numbers are in order of ", num4, ">=", num3, ">=", num2, ">=", num1, "." )
elif num4>=num3>=num1>=num2:
    print("The numbers are in order of ", num4, ">=", num3, ">=", num1, ">=", num2, "." )
elif num4>=num1>=num2>=num3:
    print("The numbers are in order of ", num4, ">=", num1, ">=", num2, ">=", num3, "." )
elif num4>=num1>=num3>=num2:
    print("The numbers are in order of ", num4, ">=", num1, ">=", num3, ">=", num2, "." )
# List = []
# List[1]=num1
# List[2]=num2
# List[3]=num3
# List[4]=num4
# for i in range (3):
#     for j in range(3):
#         if List[i] > List[j+1]:
#             temp = List[j]
#             List[j] = List[j+1]
#             List[j+1] = temp
# print("The numbers are in order of: ", List[1], "<=", List[2], "<=", List[3], "<=", List[4])
