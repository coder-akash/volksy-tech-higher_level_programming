#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of
these characters: ., ? and : '''


def text_indentation(text):
    '''text_indentation'''
    
    if type(text) != str:
        raise TypeError('text must be a string')
    l = text.split()
    print(l)
    for i in range(len(l)):
        if l[i][-1] in ".:?":
            print(l[i]+'\n')
        else:
            if i == len(l)-1:
                print(l[i])
            else:
                print(l[i],end=' ')
