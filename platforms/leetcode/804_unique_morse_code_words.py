class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        seen = set()

        for word in words:
            code = ""
            for ch in word:
                idx = ord(ch) - ord('a')
                code += morse[idx]
            seen.add(code)

        return len(seen)
        