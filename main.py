#Write your code below this row 👇

even = 0
for number in range(1, 103, 2):
  # print(number-1)
  even += number-1
print(even)

even2 = 0
for number in range(2, 101, 2):
  even2 += number
print(even2)

even3 = 0
for number in range(1, 101):
  if number % 2 == 0:
    even3 += number
print(even3)