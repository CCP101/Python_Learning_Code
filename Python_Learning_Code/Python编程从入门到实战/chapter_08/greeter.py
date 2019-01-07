def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


name = input('My name is:')
greet_user(name)
