def binary_tree(data, left=None, right=None):
    return [data, left, right]

def is_empty_bin_tree(bin_tree):
    return bin_tree is None

def root(bin_tree):
    return bin_tree[0]

def left(bin_tree):
    return bin_tree[1]

def right(bin_tree):
    return bin_tree[-1]  #  or return bin_tree[2]

def set_root(bin_tree, data):
    bin_tree[0] = data

def set_left(bin_tree, left):
    bin_tree[1] = left

def set_right(bin_tree, right):
    bin_tree[-1] = right