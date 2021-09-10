#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    m_list = dir(hidden_4)
    l_len = len(m_list)
    for i in range(l_len):
        if m_list[i].startswith('_'):
            continue
        else:
            print(m_list[i])
