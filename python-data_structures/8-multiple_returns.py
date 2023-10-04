#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        leng = 0
        first_char = None
        return (leng, first_char)
    else:
        leng = (len(tuple(sentence)))
        first_char = sentence[0]
        return (leng, first_char)
