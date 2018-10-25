import sys
from huff_tree import Tree, Node

# calc total freq value in 2d list of char-freq pairs
def total_freqs(data):
    total = 0
    for pair in data: 
        total += pair[1]
    return total


#build 
def build_tree(data):
    node = Node()

    if len(data) == 2: 
        node.l = Node(data[0])
        node.r = Node(data[1])

    elif len(data) == 1:
        node.val = data[0]

    else:
        # start with split point of 0
        split = 0
        # loop may sometimes need to loop all the way through data
        for _ in range(len(data)):
            # if both sides of splic equal, or wont be any better by moveing
            # split, split point has been found
            if (total_freqs(data[:split]) == total_freqs(data[split:])) or \
                    ((total_freqs(data[:split]) < total_freqs(data[split:])) and \
                    (total_freqs(data[:split+1]) > total_freqs(data[split+1:]))):

                    # found split point
                    node.r = build_tree(data[:split])
                    node.l = build_tree(data[split:])

            # if split not yet optimal, increase by one
            else: 
                split += 1

    return node



def main():
    # get message from first argument
    msg = sys.argv[1]

    # create msg_data and tree
    msg_data = []
    tree = Tree()


    # count frequencys
    for c in msg:
        found = False
        for char_pair in msg_data:
            if c == char_pair[0]:
                found = True
                char_pair[1] += 1

        if not found:
            char_pair = [c, 1]
            msg_data.append(char_pair)

    # sort chars by frequency
    msg_data = list(reversed(sorted(msg_data, key=lambda x: x[1])))

    # build out tree
    tree.root = build_tree(msg_data)

    

    

if __name__ == '__main__':
    main()

