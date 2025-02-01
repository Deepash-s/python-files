graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []
queue = []

def bfs(graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        element = queue.pop(0)
        print(element, end=" ")

        for neighbor in graph[element]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(graph,'5')