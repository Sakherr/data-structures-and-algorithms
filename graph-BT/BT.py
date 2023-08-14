def business_trip(graph, cities):

  costs = {}
  for city in cities:
    if city not in graph:
      return None
    costs[city] = float("inf")

  def dfs(city, path_cost):
    if city == cities[-1]:
      costs[city] = min(costs[city], path_cost)
      return

    for neighbor, cost in graph[city]:
      if costs[neighbor] > path_cost + cost:
        dfs(neighbor, path_cost + cost)

  dfs(cities[0], 0)
  return costs[cities[-1]] if costs[cities[-1]] != float("inf") else None
