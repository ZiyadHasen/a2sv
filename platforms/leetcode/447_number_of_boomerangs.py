class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            cnt = {}
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                d2 = dx*dx + dy*dy
                cnt[d2] = cnt.get(d2, 0) + 1
            for c in cnt.values():
                ans += c * (c - 1)
        return ans