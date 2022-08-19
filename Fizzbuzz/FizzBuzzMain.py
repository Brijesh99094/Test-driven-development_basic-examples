

class FizzBuzz : 
    def __init__(self):
        pass

    def fizz_buzz_or_number(self,number):
        if number % 3 == 0 and number % 5 == 0 : return "FizzBuzz"
        elif number % 5 == 0: return "Buzz"
        elif number % 3 == 0 : return "Fizz"
        else : return str(number) 


if __name__ == "__main__":
    fb = FizzBuzz()
    print(fb.fizz_buzz_or_number(50))
    print(fb.fizz_buzz_or_number(9))
    print(fb.fizz_buzz_or_number(15))
    print(fb.fizz_buzz_or_number(11))