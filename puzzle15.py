from copy import deepcopy
from typing import Optional
from algorithms import breadth_first_search,depth_first_search
import functools
# [ 0 , 1 , 2   3]
# [ 4 , 5 , 6 , 7]
# [ 8 , 9 ,10, 11]
# [12 ,13 ,14, 15]


@functools.total_ordering
class State:
    puzzle:list[list[int]]
    value:int
    parent:Optional['State']
    previous_move:Optional[tuple[int]]
    zero_in:tuple[int]
    
    
    def __init__(self,state:list[list[int]],previous_move:Optional[tuple[int]],parent:Optional['State'],goal_state:'State')->None:
        self.puzzle = state
        self.parent = parent
        self.value = 0
        self.previous_move = previous_move
        self.zero_in = self.find_0()
        self.value = self.evaluate_state(goal_state)       

    def evaluate_state(self,goal_state:'State')->None:
        """Evaluates how bad is a state"""
        out_of_place = 0
        for i in range(4):
            for j in range(4):
                if self.puzzle[i][j] != goal_state[i][j]:
                    out_of_place += 1
        return out_of_place
    
    def find_0(self)-> tuple[int]:
        j = None
        for i,row in enumerate(self.puzzle):
            if 0 in row:
                j = row.index(0)
                return (i,j)
    
    def __lt__(self,other:'State')->bool:
        return self.value < other.value
    
    def __repr__(self)-> list[list[int]]:
        stra = ""
        for row in self.puzzle:
            stra += str(row)
            stra += "\n"          
        return f"Previous move: {self.previous_move}\nHeuristic Value: {self.value}\n" + stra
        
class Puzzle15Problem:
    initial_state:State
    goal_state:State
    
    def __init__(self,initial_state:list[list[int]],goal_state:list[list[int]])->None:
        self.initial_state = State(initial_state,None,None,goal_state)
        self.goal_state = State(goal_state,None,None,goal_state)
        
    def expand(self,state:State) -> list[State]:
        children:list[State] = list()
        moves = [(-1,0),(1,0),(0,1),(0,-1)] # Up,Down,Right,Left
        zero_i = state.zero_in
        for move in moves:
            new_zero_index = (zero_i[0] + move[0], zero_i[1] + move[1])
            if 0 <= new_zero_index[0] < 4 and 0 <= new_zero_index[1] < 4:
                child = deepcopy(state.puzzle)
                value = child[new_zero_index[0]][new_zero_index[1]]
                child[zero_i[0]][zero_i[1]] = value
                child[new_zero_index[0]][new_zero_index[1]] = 0
                children.append(State(child,move,state,self.goal_state.puzzle))       
        return children
    
    def is_goal(self,state: 'State') -> bool:
        return state.value == 0
    
def print_solution(state_sol:Optional[State|None])->None:
    if state_sol is None:
        print("Couldnt find a solution:")
    else:
        path = []
        current = state_sol
        while current != None:
            path.append(current)
            current = current.parent 
        print("Path:___________________")
        for i in range(len(path)-1,-1,-1):
            print(path[i])
    
def main()->None:
    # initial_state = [[5,1,12,3],
    #                  [13,9,6,4],
    #                  [2,11,15,0],
    #                  [14,10,8,7]]
    
    initial_state = [[1,2,3,0],
                  [4,5,6,7],
                  [8,9,10,11],
                  [12,13,14,15]]
    
    goal_state = [[0,1,2,3],
                  [4,5,6,7],
                  [8,9,10,11],
                  [12,13,14,15]]

    puzle15 = Puzzle15Problem(initial_state,goal_state)
    #solution = breadth_first_search(puzle15)
    solution = depth_first_search(puzle15)
    print_solution(solution)


if __name__ == "__main__":
    main()