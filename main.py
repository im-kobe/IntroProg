filename = input("What do you want to name your file? ")

username = input("What is your name? " )
address = input("What is your street address? ")
number = input("What is your phone number? ")

with open(filename, 'w') as f:
  f.write(f"{username}, {address}, {number}")

with open(filename) as f:
  contents = f.read()

print(contents)