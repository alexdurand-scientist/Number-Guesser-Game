import random

def main():
    print('Welcome to the number guesser game!')
    name = input('What is your name? ')
    print('Well, ' + name +', lets see if you can guess the correct number.')
    lower, upper, rand = num_range()
    total_guesses = max_guess(lower, upper)
    evaluate_guess(rand, total_guesses)

def num_range():
    print('Please select a range in which you would like to guess.')    
    while True:
        try:
            Lower_limit = int(input('Enter the lower limit: '))
        except ValueError:
            print('Please enter a number!')
            continue
        else:
            break
            print('Your lower limit is %d' % (Lower_limit))
    while True:
        try:    
            Upper_limit = int(input('Enter the upper limit: '))  
        except ValueError:
            print('Please enter a number!')
            continue 
        if Upper_limit <= Lower_limit:
            print('Your upper limit needs to be above your lower limit!')
            continue 
        else:
            break
        print('Your upper limit is %d' % (Upper_limit))
    random_number = random.randint(Lower_limit, Upper_limit)
    return Lower_limit, Upper_limit, random_number

def max_guess(low, high):
    total_numbers = (high - low) + 1
    total_guesses = 0
    while (2**total_guesses) < total_numbers:
        total_guesses += 1
    print ("You have a total of %d guesses\n"
           "in your range from %d to %d"
           % (total_guesses, low, high))
    return total_guesses

def evaluate_guess(random_number, total_guesses):
    guess_count = 0
    while guess_count < total_guesses:
        guess = int(input('Guess a number: '))
        if guess > random_number:
            print('Try lower!')
            guess_count += 1
        elif guess < random_number:
            print('Try higher!')
            guess_count += 1
        elif guess == random_number:
            print('That is correct, my number is %d' % (random_number)) 
            break 
    else:
        print('Sorry, you ran out of guesses. My number was %d. \nTry again next time.' % (random_number))
if __name__ == "__main__":
    main()

