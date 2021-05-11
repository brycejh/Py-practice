def NumGuess(numTop=200, numBot=-200):
    difference = difCalc(numTop, numBot)
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


def difCalc(num_one, num_two):
    greater, smaller = bigger2Smaller(num_one, num_two)
    # print("Greater " + str(greater))
    # print("SMaller " + str(smaller))
    if isNeg(greater):
        return -1 * (smaller - greater)
    else:
        return greater - smaller


def isNeg(num):
    return True if num < 0 else False


def bigger2Smaller(num_one, num_two):
    # print("Number1 " + str(num_one) + "\nNum2 " + str(num_two))
    if num_one > num_two:
        return num_one, num_two
    elif num_one < num_two:
        return num_two, num_one
    else:
        return num_one, num_two


print("Time to play a game.....")
print("Think of any integer and store it in your mind")

if NumGuess():
    print("I WIN!!!")
else:
    print("YOU BEAT ME!!!!!!!!!!!!!!! HOWWWWW!!!!!!!!!!!!!!")
