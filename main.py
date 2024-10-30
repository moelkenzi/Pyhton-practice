# checks if the number is positve or not 
# num = int(input("enter random number \n")) 

# if num > 0:
#     print("number is positive")                                     

# elif num >= -3: # else
#     print("number is -3")

# elif num == 0: # else
#     print("number is neutral")

# else :
#     print("number is negative")
    
# # checking studdent marks

# mark = int(input("enter your marks"))
# if mark > 70:
#     print("you passed")
# else :
#     print("your failed ")



# Day = "wednesday"

# day = input("what is today: \n")
# if day == "wednesday":
#     print("Yes it is ")
# else:
#     print(f"no it is not, it's {Day}")





# Grade calculation based on student marks in the Minstary of Education of The 2024 Std

# name = input('Enter your name: ')
# marks = float(input('Enter your marks: '))

# if marks >= 90:
#     print('Your grade is A')
# elif marks >= 80:
#     print('Your grade is B')
# elif marks >= 70:
#     print('Your grade is C')
# elif marks >= 60:
#     print('Your grade is D')
# else:
#     print('Waa dhacday')
    


# Loop That Prints from 1 to 10

# count = 1
# while count < 11:
#     print(count)
#     count = count + 1
  
  # ask the user to input a number
  # check if the number is even or odd
  # print its odd or even


# while True:
#   num = int(input('Hey, Please Enter a random number: '))
#   if num % 2 == 0:
#       print('This is an even number ')
      # num = int(input('Hey, Please Enter another random number: '))


# we have secret code which is B5B
# ask the user to enter the secret code 
# grant permission if he provides correctly 
# else permission denied

# secret_code = "B5B"

# user = input('Please enter the secret code to Continue: ')
# if user == "B5B":
#   print("Succesfully permitted")
# else:
#   print("Permission Denied")


# ask the user to enter his age 
# if he's younger than 13 tell him he's too young
# if he's younger than 25 tell him he's a boy
# if he's younger than 50 tell him he's a man
# if he's older than 50 tell him he's an adult


# user = int(input("Please enter your age: "))
# if user <= 13:
#     print("You are too young")
# elif user <= 25:
#     print("You are a boy")
# elif user <= 50:
#     print("You are a man")
# else:
#     print("You are an adult")


# ask the user name to input his grade
# give Grade A if its grade equal  90 or above
# give Grade B if its grade equal  80 or above
# give Grade C if its grade equal  70 or above
# otherwise give it D

# grade = int(input("Please enter your grade: \n"))
# if grade >= 90:
#     print("Your grade is A")
# elif grade >= 80:
#     print("Your grade is B")
# elif grade >= 70:
#     print("Your grade is C")
# else:
#     print("Your grade is D")

# make a while loop that prints from 10 to 20

# count = 0
# num = int(input("Start: "))
# loop = int(input("Loop: "))
# # steps = int(input("Steps: "))
# while steps > loop:
#     print(num)
#     steps = steps + 1
#     num = num - 1


# Ask the user to enter the start num
# Ask the user to enter the end num
# print from the start to end steps 


## Up increasing
# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# while start < end:
#     start += 1
#     print(start)

    
   
## Down decreasing

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# while start >= end:
#     start -= 1
#     print(start)




# Ask the user to enter the start point
# Ask the user to enter the end point
# add them all
# print the total

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# total = 0
# while start < end:
#     start += 1
#     print(start)
#     total = start + 1




start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
total = 0 
while start < end:
    start += 1
    total = total + start 
print(total)