#Joshua Jaja ID:1543343 Zylab 14.11
def selection_sort_descend_trace(b):
    for i in range(len(b)-1):
        ind = i
        for j in range(i + 1, len(b)):
            if b[ind] < b[j]:
                ind = j
        b[i], b[ind] = b[ind], b[i]
        for x in b:
            print(x,end=" ")
        print()
    return b

if __name__ == '__main__':
    n = [int(x) for x in input().split()]
    selection_sort_descend_trace(n)