prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break  # exit the program
    else:
        print("I'd love to go to " + city.title() + "!")
