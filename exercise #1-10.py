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