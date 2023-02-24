def greetings(lang):    #the remember part of the code
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    elif lang=='jp':
        print('Konichiwa')
    elif lang=='en':
        print('Hello')
    elif lang=='in':
        print('Namaskar')
    else:
        print('Sorry cannot read the language chosen')

name = input("Enter your name:")
x = input('Enter Language of your choice 1.es 2.fr 3.jp 4.en 5.in:')

greetings(x) #x is the arguement and the function gets invoked here
print(name)
