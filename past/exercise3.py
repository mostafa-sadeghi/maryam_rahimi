# from random import choices
from random import choice, randrange, shuffle
from string import ascii_lowercase


# def randomLetter():
#     indexes = [ord(l) for l in ascii_lowercase]
#     print(indexes)
#     return chr(choice(indexes))

# print(randomLetter())

# def randomSequence(n):
#     indexes = [ord(l) for l in ascii_lowercase]
#     shuffle(indexes)
#     length = randrange(1,n)
#     indexes = indexes[:length]
#     result = [chr(i) for i in indexes]
#     return "".join(result)


# print(randomSequence(10))

# def randomSequence(n):
#     return choices(ascii_lowercase, k=n)

# print("".join(randomSequence(5)))


def scoreMCQ(attempt, correct):
    score = 0
    attempt_len = len(attempt)
    correct_len = len(correct)
    if attempt_len != correct_len:
        raise Exception("Error")
       
    if not attempt and not correct:
        return 0
    for i in range(attempt_len):
        if attempt[i] == correct[i]:
            score += 1
    return score


assert(scoreMCQ("","")==0), "First test failed"
assert(scoreMCQ("TFTF","TTTT")==2), "Second test failed"
assert(scoreMCQ("TFTT","TTTT")==4), "Third test failed"
assert(scoreMCQ("CCCC","ABCD")==1), "Fourth test failed"
print("All tests succesfull")
