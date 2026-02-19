class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for row in image:
            new_row = []
            
            # go from right to left (flip)
            for i in range(len(row) - 1, -1, -1):
                new_row.append(1 - row[i])  # invert
            
            result.append(new_row)

        return result
        