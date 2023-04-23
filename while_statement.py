secrete_word = "sky"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secrete_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = str(input("enter word: "))
        guess_count+=1
    else:
        out_of_guess = True

if out_of_guess:
    print("out of guessess, YOU LOSE!")
else:
    print("you win!")


