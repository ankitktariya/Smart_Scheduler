def detect_deadlock(allocation, request):
    graph = {}
    for task, res in allocation.items():
        graph[res] = [task]
    for task, res in request.items():
        graph.setdefault(task, []).append(res)

    visited = set()
    path = set()
    deadlocked = set()

    def dfs(node):
        if node in path:
            deadlocked.update(path)
            return
        if node in visited:
            return
        visited.add(node)
        path.add(node)
        for nei in graph.get(node, []):
            dfs(nei)
        path.remove(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return [x for x in deadlocked if x in allocation]
