#!/usr/bin/python3
def weight_average(lst):
    if len(lst) == 0:
        return 0
    else:
        m_a = 0
        add = 0
        for i in range(len(lst)):
            mul = 1
            for j in range(len(lst[i])):
                print(lst[i])
                if j == 1:
                    add = add + lst[i][j]
                mul = mul * lst[i][j]
            m_a = m_a + mul
        res = m_a / add
        return res
