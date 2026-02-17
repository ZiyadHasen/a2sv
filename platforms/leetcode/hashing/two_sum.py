class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {}
        players = set()

        for w, l in matches:
            players.add(w)
            players.add(l)
            loss[l] = loss.get(l, 0) + 1
            if w not in loss:
                loss.setdefault(w, 0)

        zero = []
        one = []

        for p in players:
            if loss.get(p, 0) == 0:
                zero.append(p)
            elif loss[p] == 1:
                one.append(p)

        return [sorted(zero), sorted(one)]
        