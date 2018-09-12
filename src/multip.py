p1 = input().split()
p2 = input().split()


def append(inp):
    arr = []
    for i in range(1, len(inp), 2):
        arr.append(inp[i] + "," + inp[i + 1])
    return arr


# 去除重复项
def removal(arr):
    arr = to_int(arr)
    new_arr = []
    for i in range(0, len(arr), 2):
        base = arr[i]
        if base == 0:
            continue
        index = arr[i + 1]
        for j in range(i + 3, len(arr), 2):
            _index = arr[j]
            if index == _index:
                base += arr[j - 1]
                arr[j - 1] = 0
        if base != 0:
            new_arr.append(base)
            new_arr.append(index)
    if len(new_arr) == 0:
        return '0 0'
    return ' '.join(to_string(new_arr))


# 多项式相乘法
def multip(arr1, arr2):
    m = []
    for p in arr2:
        p_arr = to_int(p.split(','))
        base = p_arr[0]
        index = p_arr[1]
        for pp in arr1:
            pp_arr = to_int(pp.split(','))
            _base = pp_arr[0] * base
            _index = pp_arr[1] + index
            m.append(_base)
            m.append(_index)
    return removal(m)


def to_int(arr):
    new_arr = []
    for s in arr:
        new_arr.append(int(s))
    return new_arr


def to_string(arr):
    new_arr = []
    for s in arr:
        new_arr.append(str(s))
    return new_arr


# 多项式相加
def addition(arr1, arr2):
    m = []
    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            node2 = to_int(arr2[j].split(','))
            m.append(node2[0])
            m.append(node2[1])
            break

        if j >= len(arr2):
            node1 = to_int(arr1[i].split(','))
            m.append(node1[0])
            m.append(node1[1])
            break

        node1 = to_int(arr1[i].split(','))
        node2 = to_int(arr2[j].split(','))
        if node1[1] == node2[1]:
            if node1[0] + node2[0] != 0:
                m.append(node1[0] + node2[0])
                m.append(node1[1])
            i += 1
            j += 1
        elif node1[1] > node2[1]:
            m.append(node1[0])
            m.append(node1[1])
            i += 1
        elif node1[1] < node2[1]:
            m.append(node2[0])
            m.append(node2[1])
            j += 1
    return removal(m)


arr1 = append(p1)
arr2 = append(p2)
print(multip(arr1, arr2))
print(addition(arr1, arr2))
