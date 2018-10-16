import sys

msg = sys.argv[1]
msg_data = []


class Node():
    def __init__(self, val=None):
        self.l= None
        self.r = None
        self.val = val

class Tree():
    def __init__():
        self.root = Node()




for c in msg:
    found = False
    for char_pair in msg_data:
        if c == char_pair[0]:
            found = True
            char_pair[1] += 1

    if not found:
        char_pair = [c, 1]
        msg_data.append(char_pair)

msg_data.sort(key=lambda x: x[1])


print(msg_data)

for char_set in msg_data:
    print(char_set[0])
    char_set.append(Node(char_set[0]))


print(msg_data)





        
with open('encoded.txt', 'w') as f:
    pass

with open('plain.txt', 'w') as f:
    f.write(msg)
