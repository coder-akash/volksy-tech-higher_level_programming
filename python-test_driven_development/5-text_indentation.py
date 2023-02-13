#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of
these characters: ., ? and : '''


def text_indentation(text):
    '''text_indentation'''
    l = text.split()
    for i in range(len(l)):
        if l[i][-1] in ".:?":
            print(l[i] + '\n')
        else:
            print(l[i], end=' ')
