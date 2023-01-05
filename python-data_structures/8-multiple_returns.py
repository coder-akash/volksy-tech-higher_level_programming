#!/usr/bin/python3
def multiple_returns(sen):
    if len(sen) == 0:
        return len(sen), None
    else:
        return len(sen), sen[0]
