my_maze = [
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1]
]
start = (0, 0)
end = (11, 13)
dirs = [(0, 1 ), (1, 0), (0, -1), (-1, 0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2  # if the position is visited, marked it = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()

def maze_solver_stack(maze, start, end):
    if start == end:
        print(start)
        return
    st = ArrayStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            next_pos = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if next_pos == end:
                print(start, end)
                while not st.is_empty():
                    print(st.pop())
            if passable(maze, next_pos):
                st.push((pos, i+1))
                mark(maze, next_pos)
                st.push((next_pos, 0))
                break
    print('no path found')


if __name__ == '__main__':
    maze_solver_stack(my_maze, start, end)