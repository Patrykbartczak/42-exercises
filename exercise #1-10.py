import random,sys

            # 1. Hello World!

# print('Hello World')
# print("What's your name: ?")
# my_name = input()
# print(f"Hello {my_name}")

            # 2. Temp conversion

def convertofahrenheit(cel):
    #Calculate and return the degrees Fahrenheit:
    return cel * (9/5) + 32
def converttocelsius(fah):
    #Calculate and return the degrees celsius:
    return (fah - 32) * (5/9)

            # 3. Odd & even

def isOdd(num):
    # Return whether number mod 2 is 1:
    return num % 2 == 1
def isEven(num):
    # Return whether number mod (modulo) 2 is 0:
            return num % 2 == 0

            # 4. Area & volume

def area (lenght, width):
    #Return the product of the length and width:
    return lenght * width
def perimeter (lenght, width):
    #Return the sum of the length twice and the width twice:
    return (2 * lenght) + (2 * width)
def volume (lenght, width, height):
    #Return the product of the length, width, and height
    return lenght * width * height
def surfaceArea(lenght, widht, height):
    #Return the sum of the area of each of the six sides
    return ((lenght * widht) + (lenght * height) + (widht * height)) * 2


            # 5. Fizz Buzz
def FizzBuzz(upTo):
    for num in range(1,upTo +1): # Will always add 1 to indicated num
        # If the loop is divisible by 3 and 5 make it 15 as least common multiple
        if num % 15 == 0:
            print('FizzBuzz', end= ' ')
        # If the lopp is divisible by 3
        elif num % 3 == 0:
            print('Fizz', end= ' ')
        # If the loop is divisible by 5
        elif num % 5 == 0:
            print('Buzz', end= ' ')
        # If not, print number
        else:
            print(num, end= ' ')
# print(FizzBuzz(99))


            # 6. Ordinal suffix

def ordinalSuffix(num):
    numberStr = str(num)
    #11,12,13 have the suffix "th"


            # 7. Rock, paper, scissor
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s loses, %s ties' %(wins,losses,ties))
    while True:
        print('Podaj swój wybór: (k)amień, (p)apier, (n)ożyce lub (w)yjście') # ruch gracza
        player_move = input()
        if player_move == 'w':
            sys.exit() # koniec gry
        elif player_move == 'k' or player_move == 'p' or player_move == 'n':
            break
        print('Wpisz litere k,p,n,w jako swój wybór: ')

    if player_move == 'k':
        print('Kamień vs..')
    elif player_move == 'p':
        print('Papier vs...')
    elif player_move == 'n':
        print('Nożyce vs..')

    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'k'
        print('Kamień!')
    elif random_number == 2:
        computer_move = 'p'
        print('Papier!')
    elif random_number == 3:
        computer_move = 'n'
        print('Nożyce!')
    if player_move == computer_move:
        print('Mamy remis!')
        ties += 1
    elif player_move == 'k' and computer_move == 'n':
        print('Wygrałeś!')
        wins += 1
    elif player_move == 'n' and computer_move == 'k':
        print('Przegrałeś!')
        losses += 1
    elif player_move == 'k' and computer_move == 'p':
        print('Przegrałeś!')
        losses += 1
    elif player_move == 'n' and computer_move == 'p':
        print('Wygrałeś!')
        wins += 1
    elif player_move == 'p' and computer_move == 'k':
        print('Wygrałeś!')
        wins += 1
    elif player_move == 'p' and computer_move == 'n':
        print('Przegrałeś')
        losses += 1
