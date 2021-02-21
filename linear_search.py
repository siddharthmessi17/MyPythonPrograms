def linear_search(arr, ele):
    l = len(arr)
    for i in range(0, l):
        if arr[i] == ele:
            return i
    return -1


n = int(input('Enter size of list'))
a = []
for i in range(0, n):
    ele = int(input('Enter element'))
    a.append(ele)
x = int(input('Enter the search element'))
result = linear_search(a, x)
if result == -1:
    print('Not Found')
else:
    print('Found at Position', result)
