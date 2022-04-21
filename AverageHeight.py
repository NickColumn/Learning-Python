# Getting the values from user and calculating an average from them.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


# First step - calculating the sum of our heights.
studentSumHeights = 0
for n in student_heights:
    studentSumHeights += n
# Second step - calculating how many students there are.
studentTotal = 0
for n in student_heights:
    studentTotal += 1
# Third step - doing the math to calculate the average height and printing the result.
result = round(studentSumHeights / studentTotal)
print(result)