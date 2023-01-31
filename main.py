import random as rn


class Guessing:
    def __init__(self):
        self.guess = rn.randint(0, 250)

    def game(self, num):
        self.num = num
        if self.num == self.guess:
            return
        inp = True
        while inp:
            try:
                x = int(input("Choose a type of hint:\n1) Smaller/greater\n2) Divisible by number\n3) Warm/cold\n"))
                inp = False
            except:
                print("Make a good input, please\n")
        if x == 1:
            if num > self.guess:
                print(f"The number {num} is greater")
            elif num < self.guess:
                print(f"The number {num} is smaller")
        if x == 2:
            if self.guess % num == 0:
                print("The number is divisible by your number")
            else:
                print("The number is not divisible by your number")
        if x == 3:
            if abs(num - self.guess) in (1, 2, 3):
                print("Very hot!")
            elif abs(num - self.guess) > 20:
                print("Very cold")
            elif abs(num - self.guess) > 10:
                print("Cold")
            elif abs(num - self.guess) > 5:
                print("A bit warm")
            elif abs(num - self.guess) > 4:
                print("Warm")


num_obj = Guessing()
var = True
game = True
while game:
    while var:
        inp = True
        while inp:
            try:
                num_obj.game(int(input("Print your guess:\n")))
            except:
                print("Make a good input, please\n")
        if num_obj.guess == num_obj.num:
            var = False

    print(f"Yes, the number was {num_obj.guess}!")
    again = input("Do you want to play again?\n")
    if again == 'Yes':
        var = True
        num_obj = Guessing()
    else:
        game = False
