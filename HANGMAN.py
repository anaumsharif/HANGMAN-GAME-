MAX_GUESSES = 10
tries = 0
word = "loop"
word = word.lower()
print(word)
while True :
    key = input("Guess the letter :")
    if key in word:
        print(" The word contains " +key)
        word = word.replace(key,"")
        print(f"Number of words left = {len(word)}")
        if len(word)== 0:
            print("YOU WIN ")
            break
    else:
        print("Wrong guess")
        tries = tries+1
        if tries>= MAX_GUESSES:
            print("YOU LOST ")
            break 