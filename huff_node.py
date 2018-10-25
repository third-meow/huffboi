class Node():
    def __init__(self, val=None, freq=0):
        self.val = val
        self.l= None
        self.r = None
        self.freq = freq 

    def auto_freq_calc(self):
        self.freq = 0
        self.freq += self.l.freq
        self.freq += self.r.freq

    def print_children(self):
        if self.val != None:
            print(self.val, end=' ')
        else:
            print('*', end=' ')


        if self.l != None: 
            self.l.print_children()

        if self.r != None: 
            self.r.print_children()


        print('|', end=' ')


    def print_code(self, path=''):
        # if node has value 
        if self.val != None:
            # print path and value
            print('{} : {}'.format(path, self.val))
        else:
            if self.l != None: 
                self.l.print_code('{}0'.format(path))

            if self.r != None: 
                self.r.print_code('{}1'.format(path))


