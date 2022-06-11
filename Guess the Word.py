# first we choose the secret word
secret_word = "COVID"
guess = ""
# the guess counter is 0
guess_count = 0
# number of times we want to let them guess
guess_limit = 3
out_of_guesses = False  
while guess != secret_word and not out_of_guesses:   # the condition appies if we have not guessed right word or we have guesses left 
    if guess_count < guess_limit:
        guess = input("Enter Guess :")
        guess_count += 1
        print(guess, "is wrong guess, Try again")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses,you lose!")   
else:
    print("YOU WIN!!!!")
