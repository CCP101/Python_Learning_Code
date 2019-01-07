height = input("How tall are you, in inches? ")
height = int(height)
if height >= 165:
    print("\nYou're tall enough to ride!")
elif height <=190:
    print("\nSorry ,you can not play this for safety!")
else:
    print("\nYou'll be able to ride when you're a little older.")
