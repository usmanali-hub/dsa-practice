"""Number of Islands (medium).

``grid`` is a 2D array of ``"1"`` (land) and ``"0"`` (water). An island is a maximal group of land cells connected
4-directionally (up/down/left/right, not diagonally). Count the islands.

Approach: scan every cell; on an unvisited land cell, flood-fill (DFS, iterative with an explicit stack to avoid
recursion-depth limits on a large grid) to mark every connected land cell visited, and count that as one island.
Time O(rows * cols) (every cell visited once), space O(rows * cols) worst case (a grid that is entirely one island,
for the stack).
"""


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = [[False] * cols for _ in range(rows)]

    def flood_fill(start_r: int, start_c: int) -> None:
        stack = [(start_r, start_c)]
        seen[start_r][start_c] = True
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not seen[nr][nc]
                    and grid[nr][nc] == "1"
                ):
                    seen[nr][nc] = True
                    stack.append((nr, nc))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not seen[r][c]:
                islands += 1
                flood_fill(r, c)
    return islands
