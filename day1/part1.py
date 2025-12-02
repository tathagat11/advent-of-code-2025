input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

current = 50
password = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction == "R":
        current += distance
    else:
        current -= distance

    current = current % 100

    if current == 0:
        password += 1

print("Answer =", password)
