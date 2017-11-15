from collections import defaultdict


def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team) # append used instead of add, square brackets in append
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        visited.append(curr)
        if curr == dest:
            return True
        if curr in visited:  # visited[curr]
            return False
        return any(
            [is_reachable_dfs(graph, team, dest, visited) for team in graph[curr]]
        )

    return is_reachable_dfs(build_graph(), team_a, team_b)
