#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of these characters: ., ? and : '''


def text_indentation(text):
    '''text_indentation'''
    l = len(text)
    c=0
    while c!=l:
        if text[c] in '.:?' or text[c] == '\n':
            print(text[c], end='')
            print('\n')
            c+=2
        else:
            print(text[c], end='')
            c+=1
