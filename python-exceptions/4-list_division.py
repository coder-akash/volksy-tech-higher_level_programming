#!/usr/bin/python3
def list_division(l1, l2, leng):
    div_l = []
    for i in range(leng):
        try:
            res = l1[i] / l2[i]
        except ZeroDivisionError:
            print('division by 0')
            res = 0
        except TypeError:
            print('wrong type')
            res = 0
        except IndexError:
            print('out of range')
            res = 0
        finally:
            div_l.append(res)
    return div_l
