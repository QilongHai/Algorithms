def enumerate(data):
    '''Generates an indexed series:  (0,coll[0]), (1,coll[1]) ...'''
    i = 0
    it = iter(data)
    while 1:
        yield (i, it.__next__())
        i += 1

if __name__ == '__main__':
    A = ['allen', 'lucas', 'bob', 'finch', 'susan', 'finch']
    for i, j in enumerate(A):
        print(i, j)