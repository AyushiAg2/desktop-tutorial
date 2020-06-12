import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval>=lowval:
        guess=lowval+(highval-lowval)//2
        #If guess is in the middle, it will be found
        if guess==randnum:
            return count
        elif guess>randnum:
            count=count+1
            return computerGuess(lowval,guess-1,randnum,count)
        else:
            count=count+1
            return computerGuess(guess+1,highval,randnum,count)
    else:
        return -1

randnum = random.randint(1,101)

count = 0
guess = -99
while guess!=randnum:
        guess = (int) (input("enter between 1 and 100:"))
        if guess < randnum:
            print("higher")
        elif guess > randnum:
            print("lower")
        else:
            print("found")
            break
        count = count + 1
#user guessed in:
print(count)
#computer guessed in:
print(computerGuess(0,100,randnum))