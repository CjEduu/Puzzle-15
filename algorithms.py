import heapq


def breadth_first_search(problem):
    frontier_length = 0 
    node = problem.initial_state
    if problem.is_goal(node):
        return node
    
    frontier = [node]
    heapq.heapify(frontier)
    reached = list()
    reached.append(node)
    
    while frontier:
        node = heapq.heappop(frontier)
        for child in problem.expand(node):
            if child not in reached:
                if problem.is_goal(child):
                    print (f"max frontier longitud = {frontier_length}")
                    return child
                reached.append((child))
                # frontier.append(child)
                heapq.heappush(frontier,child)
                if (frontier_length < len(frontier)):
                    frontier_length = len(frontier)
    return None


def depth_first_search(problem):
    stack = [problem.initial_state]
    reached = list()
    
    while stack:
        node = stack.pop()
        if problem.is_goal(node):
            return node
        if node not in reached:
            reached.append(node)
            children = problem.expand(node)
            stack.extend(children)
    return None