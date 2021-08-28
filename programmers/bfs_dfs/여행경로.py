def solution(tickets):
    routes = {}
    for ticket in tickets:
        routes[ticket[0]] = routes.get(ticket[0], []) + [ticket[1]]
    for route in routes:
        routes[route].sort(reverse=True)


    visited = ['ICN']
    path = []
    while visited:
        top = visited[-1]
        if top in routes and routes[top]:
            visited.append(routes[top].pop())
        else:
            path.append(visited.pop())
    return path[::-1]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))