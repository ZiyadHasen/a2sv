class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target
        my_dist = abs(tx) + abs(ty)
        for x, y in ghosts:
            ghost_dist = abs(tx - x) + abs(ty - y)
            if ghost_dist <= my_dist:
                return False
        return True
        