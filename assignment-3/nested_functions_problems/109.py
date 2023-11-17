name = input('enter your name: ')

def greeting_generator(name):

    def message(name):
        return f"Hello, {name}! How are you today?"
    
    return message(name)

print(greeting_generator(name))