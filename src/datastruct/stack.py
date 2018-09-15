# import sys
#
# sys.setrecursionlimit(200000)

import time;
time_start=time.time();

class Node:
    def __init__(self):
        self.data = {}
        self.next = None


# 二分查找法实现查找，需要先将数据进行排序
def find(point, find_list):
    low = 0
    high = len(find_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if int(point) < int(find_list[mid][0]):
            high = mid
        elif int(point) > int(find_list[mid][0]):
            low = mid + 1
        else:
            return find_list[mid]
    return None


first_line = input().split()
word_list = []
for i in range(0, int(first_line[1])):
    try:
        word = input()
        arr = word.split()
        word_list.append(arr)
    except EOFError:
        break

word_list.sort(key=lambda s: int(s[0]))

time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
print(time_end-time_start,'s')

head = find(first_line[0], word_list)
k = int(first_line[2])
node = head
stack_list = []
result_list = []
p_node = None
h_node = None
while node:
    if k == 1:
        h_node = head
        break
    stack_list.append(node)
    if node[2] != '-1':
        node = find(node[2], word_list)
    else:
        node = None
    if len(stack_list) == k:
        if p_node and p_node[2] == '-1':
            p_node[2] = stack_list[len(stack_list) - 1][0]
        while len(stack_list) > 0:
            if not h_node:
                h_node = stack_list.pop()
                h_node[2] = stack_list[len(stack_list) - 1][0]
            else:
                p_node = stack_list.pop()
                if len(stack_list) > 0:
                    p_node[2] = stack_list[len(stack_list) - 1][0]
                else:
                    p_node[2] = '-1'
if len(stack_list) > 0:
    p_node[2] = stack_list[0][0]

time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
print(time_end-time_start,'s')
# loop_node = h_node
# while True:
#     print(' '.join(loop_node))
#     if loop_node[2] != '-1':
#         loop_node = find(loop_node[2], word_list)
#     else:
#         break
