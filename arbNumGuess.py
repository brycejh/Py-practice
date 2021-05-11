def NumGuess(numTop, numBot=0):
    difference = numTop - numBot
    half = difference // 2
    guess = numBot + half
    lololol = "Is your number Higher(H), Lower(L), or Exactly(E) " + str(guess) + ": "
    HLE = input(lololol)
    if HLE == "H":
        return NumGuess(numTop, guess)
    elif HLE == "L":
        return NumGuess(guess, numBot)
    elif HLE == "E":
        return True
    else:
        print("Please use the given input parameters")
        return NumGuess(numTop, numBot)


print("Time to play a game.....")
print("Think of any positive integer and store it in your mind")
higherThan = input(
    "Now please type any integer that is higher than the one you have selected: "
)
if NumGuess(numTop=int(higherThan)):
    print("I WIN!!!")
else:
    print("YOU BEAT ME!!!!!!!!!!!!!!! HOWWWWW!!!!!!!!!!!!!!")
