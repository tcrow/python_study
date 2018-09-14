class Node:
    def __init__(self):
        self.data = {}
        self.next = None


def find(point, find_list):
    for data in find_list:
        if data[0] == point:
            return data
    return None



first_line = input().split()
word_list = []
for i in range(0,int(first_line[1])):
    try:
        word = input()
        arr = word.split()
        word_list.append(arr)
    except EOFError:
        break

def create_node(point, init_list):
    node = Node()
    node.data = find(point, init_list)
    if node.data[2] != '-1':
        node.next = create_node(node.data[2], init_list)
    return node


def reverse(node, k):
    k = int(k)
    if k == 1:
        return node
    if not node.next:
        return node
    temp_list = []
    i = 0
    next_node = None
    while True:
        if i < k and i < int(first_line[1]):
            temp_list.append(node)
            node = node.next
        else:
            next_node = node
            break
        i += 1
    head_node = None
    while len(temp_list) > 0:
        node = temp_list.pop()
        if head_node:
            if len(temp_list) > 0:
                node.data[2] = temp_list[len(temp_list) - 1].data[0]
                node.next = temp_list[len(temp_list) - 1]
            else:
                if next_node:
                    node.data[2] = next_node.data[0]
                    node.next = next_node
                else:
                    node.data[2] = '-1'
                    node.next = None
        else:
            head_node = node
            head_node.data[2] = temp_list[len(temp_list) - 1].data[0]
            head_node.next = temp_list[len(temp_list) - 1]
    return head_node


head = create_node(first_line[0], word_list)

head = reverse(head, first_line[2])

loop_node = head

while True:
    print(' '.join(loop_node.data))
    if loop_node.next:
        loop_node = loop_node.next
    else:
        break
