import time
from functools import wraps
import multiprocessing

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class DegreeSeeker():

    def neighbors_for_person(self, person_id, df):
        self.person_id = person_id
        self.df = df

        movies_id = self.df.loc[self.df['person_id']==self.person_id]['movie_id'].tolist()
        neighbors = set()
        for movie_id in movies_id:
            for person_id in self.df.loc[self.df['movie_id']==movie_id]['person_id'].tolist():
                neighbors.add((movie_id,person_id))
        return neighbors
    
    def shortest_path(self,source, target, df, time_limit):
        self.source = source
        self.target = target
        self.df = df
        # 
        num_explored = 0

        start = Node(state=self.source, parent=None, action=None)
        # Choosing BFS to find fastest path
        frontier = QueueFrontier()
        frontier.add(start)

        # Create a set to future explored nodes
        explored = set()
        start_time = time.time()

        # Keep looking until find path
        while True:
            if frontier.empty():
                return 0
            
            current_time = time.time()
            if current_time - start_time > time_limit:
                return -1

            # Get initial node => initial state
            node = frontier.remove()
            # Keep track of explored nodes
            num_explored += 1

            # Bringing neighbors tuples from person_id = node.state
            neighbors = self.neighbors_for_person(node.state, df)
            
            explored.add(node.state)
            
            for movie, actor in neighbors:
                if actor == self.target:
                    path = []
                    path.append((movie,actor))
                    while node.parent is not None:
                        path.append((node.action, node.state))
                        node=node.parent
                    path.reverse()
                    return len(path)
                
                elif actor not in explored and not frontier.contains_state(actor):
                    child = Node(state=actor, action=movie, parent=node)
                    frontier.add(child)
