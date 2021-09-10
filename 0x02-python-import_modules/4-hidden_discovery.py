#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    l = dir(hidden_4)
    l_len = len(l)
    for i in range(l_len):
        if l[i].startswith('_'):
            continue
        else:
            print(l[i])
