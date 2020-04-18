'''
    File name: astar.py
    Author: Amir Mohammad Mirzaie
    Date created: April/11/2020
    Python Version: 3.7
'''
# Node object for using in the grid system
class Node(object):
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position # this position is a tuple of (n_row, n_col)

        self.g = 0 # cost value from the start_position of the graph
        self.h = 0 # euclidean distance between the node and the end_position
        self.f = 0 # sum of self.g and self.h

    def set_g(self, g):
        self.g = g

    def get_g(self):
        return self.g

    def set_h(self, h):
        self.h = h

    def get_h(self):
        return self.h

    def set_f(self, f):
        self.f = f

    def get_f(self):
        return self.f

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent


class astar():
    def __init__(self, maze, start_position, end_position):

        self.maze = maze
        self.start_node = Node(position=start_position)
        self.end_node = Node(position=end_position)
        self.start_position = start_position
        self.end_position = end_position

    def calculate_h(self, current_node):
        # TODO: use a faster approximation to calculate this value
        current_position = current_node.get_position()
        end_position = self.end_position
        h = ((current_position[0] - end_position[0]) ** 2 + (current_position[1] - end_position[1]) ** 2) ** 0.5
        current_node.set_h(h)
        return h

    def calculate_g(self, current_node):
        # TODO: use a faster approximation to calculate this value
        current_position = current_node.get_position()
        parent = current_node.get_parent()
        parent_position = parent.get_position()

        increment = ((current_position[0] - parent_position[0]) ** 2 + (
                    current_position[1] - parent_position[1]) ** 2) ** 0.5
        g = parent.get_g() + increment
        current_node.set_g(g)
        return g

    def calculate_f(self, current_node):
        f = current_node.get_h() + current_node.get_g()
        current_node.set_f(f)
        return f
    # possible directions one node can propagate
    def get_directions(self):
        directions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
        return directions

    # returns path list from end_position to the start position
    def print_path(self, node, positions_path=[]):
        if node.get_parent():
            positions_path.append(node.get_position())
            self.print_path(node.get_parent(), positions_path)
        else:
            positions_path.append(node.get_position())
        return positions_path

    # A* algorithm goes here.
    def find_path(self):

        open_list = [] # the list of open candidates to use in the later iterations
        closed_list = [] # the list of visited and assessed nodes

        self.start_node.set_g(0)
        self.calculate_h(self.start_node)
        self.calculate_f(self.start_node)

        open_list.append(self.start_node)

        # setting a "visited" matrix to keep track of closed nodes
        # we could do other ways to handle closed nodes.
        # However, I see this way to be better
        visited = [[0] * len(self.maze[0]) for _ in range (len(self.maze))]

        # calculating the maximum possible index for row and column
        rows_max = len(self.maze) - 1
        cols_max = len(self.maze[0]) - 1

        while open_list: # while we have something in our open_list
            current_node = open_list[0] # set the current node to the first element of the open_list

            # compare all other elements in the open_list with the current node
            # and find the best node and change the current_node to this node
            best_index = 0
            for i, item in enumerate(open_list):
                if item.get_f() <= current_node.get_f():
                    best_index = i
                    current_node = item

            open_list.pop(best_index)
            closed_list.append(current_node)
            current_position = current_node.get_position()

            # check if we have reached the end position
            if current_node.get_position() == self.end_position:
                print('we have reached the end_position')
                return current_node, self.print_path(current_node)

            # set visited for this node in the "visited" matrix
            visited[current_position[0]][current_position[1]] = 1

            # getting all possible directions to go to
            directions = self.get_directions()

            for direct in directions:

                # calculating the new row and col index
                # corresponding to the directions
                new_row = current_position[0] + direct[0]
                new_col = current_position[1] + direct[1]

                # if new row and new col index are in correct range
                # and if the new node corresponding to the new position is not a wall
                # and if the new node corresponding to the new position is not in the closed list
                if (0 <= new_row <= rows_max) and (0 <= new_col <= cols_max) and (self.maze[new_row][new_col] != 1) \
                    and not(visited[new_row][new_col]):

                    # create a new node related to this new position
                    neighbor_position = (new_row, new_col)
                    neighbor_node = Node(parent=current_node, position=neighbor_position)

                    # calculate its g, h and f
                    self.calculate_g(neighbor_node)
                    self.calculate_h(neighbor_node)
                    self.calculate_f(neighbor_node)

                    # append this node to the open list
                    open_list.append(neighbor_node)
        return -1


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# means the first row and the first column
start = (0, 0)

# means the 5th row and the 8th column
end = (5, 8)

# creating the astar object
ast = astar(maze, start, end)

# storing the path related to this astar algorithm
path = ast.find_path()










