guessed_letters=""
word="mjasjsmad"
len_word=len(word)
letter="m"
num_tries=0
i=0
print(letter)
for i in range(len_word):
    if word[i] is letter:
        guessed_letters=guessed_letters+letter
    else:
        guessed_letters=guessed_letters+"_ "
    i+=1
print(guessed_letters)
