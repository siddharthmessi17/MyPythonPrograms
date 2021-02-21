def merge(larr, rarr):
    result = []
    i, j = 0, 0
    while(i < len(larr) and j < len(rarr)):
        if(larr[i] < rarr[j]):
            result.append(larr[i])
            i += 1
        else:
            result.append(rarr[j])
            j += 1
    result += larr[i:]
    result += rarr[j:]
    return result

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    mid = int(len(arr)//2)
    larr = merge_sort(arr[:mid])
    rarr = merge_sort(arr[mid:])
    return merge(larr, rarr)

arr = [1,6, 81,5, 66,71,89]
print(merge_sort(arr))


