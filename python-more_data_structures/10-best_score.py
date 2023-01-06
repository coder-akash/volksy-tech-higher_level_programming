#!/usr/bin/python3
def best_score(dic):
    if dic is None:
        return None
    else:
        for i in dic:
            if dic[i] == max(dic.values()):
                return i
