def binary_search(arr, l_index, h_index, search_ele):
    if h_index >= l_index:
        m_index = (h_index + l_index) // 2
        if arr[m_index] == search_ele:
            return m_index
        elif arr[m_index] > search_ele:
            return binary_search(arr, l_index, m_index - 1, search_ele)
        else:
            return binary_search(arr, m_index + 1, h_index, search_ele)
    else:
        return -1


a = [2, 5, 6, 8, 13, 17, 21]
x = 17
res = binary_search(a, 0, len(a) - 1, x)
if res != -1:
    print('present at pos', res)
else:
    print('not present')
