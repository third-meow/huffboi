import sys
from huff_node import Node


def main():
    # get message from first argument
    msg = sys.argv[1]

    # create msg_data
    msg_data = []


    # count frequencys and convert to Nodes
    for c in msg:
        found = False
        for node in msg_data:
            if c == node.val:
                found = True
                node.freq += 1

        if not found:
            new_node = Node(c, 1)
            msg_data.append(new_node)


    # build out tree
    while len(msg_data) > 1:
        # sort by freq
        msg_data.sort(key=lambda x: x.freq)

        # create node by extracting first two nodes in msg data
        new_node = Node()
        new_node.l = msg_data.pop(0)
        new_node.r = msg_data.pop(0)
        new_node.auto_freq_calc()

        # put new node back into msg_data
        msg_data.append(new_node)



    # call first node root
    root = msg_data[0]

    root.print_code()
    print('')




    

if __name__ == '__main__':
    main()

