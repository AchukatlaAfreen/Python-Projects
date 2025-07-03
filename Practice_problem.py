#arr = [10,20,30,40,50,70]
#max_num = arr[0]
#for num in arr:
    #if num > max_num:
        #max_num = num
#print("The maximum number is:",max_num)
arr = [2,4,6,8,12,80]
even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:",even_sum)

arr=[1,2,3,4,5]
n = len(arr)
for i in range(n):
    print(arr[i], end = " ")
print()


age = 10
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

marks = 54

if marks < 25:
    print("Grade: F")
elif marks >= 25 and marks <= 44:
    print("Grade: E")
elif marks >= 45 and marks <=49:
    print("Grade: D")
elif marks >=50 and marks <=59:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: B")
elif marks >=70:
    print("Grade: A")
marks = int(input("Enter your marks:"))


day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("Invalid")


x = 10
y = 5
result = x+ y
if result == 15:
    print("Result is 15.")
elif result == 20:
    print("Result is 20.")
else:
    print("No match found")


grade = 'B'

if grade == 'A':
    print("Excellent")
elif grade == 'B':
    print("Good!")
elif grade == 'c':
    print("Not satisfied")
else:
    print("Not specified.")


day = 2

if day == 1:
    print("Monday.")
elif day == 2:
    print("Tuesday.")
else:
    print("Invalid day.")


x = 2
y = 3
if x == 1:
    print("x is 1.")
    if y == 1:
        print("Y is 1.")
    else:
        print("y is not 1.")
else:
    print("x is not 1.")


