# A2SV Competitive Programming Solutions

This is a **public repository** documenting my journey with **A2SV**. It is meant to help anyone who is trying to get into **competitive programming**.

## Organization

- **Platforms**: Problems are grouped by platform (`LeetCode`, `Codeforces`, `HackerRank`).
- **Topics**: Within each platform, problems are organized by topic:
  - `arrays`
  - `strings`
  - `hashing`
  - `linked-list`

- **Contests**: Time-based contests are stored separately under the `contests` folder.
- **Notes**: Brief insights, mistakes, or key ideas are added for each problem to help future reference.

## File Naming Rules

- **One problem per file**
- File name format: `problemNumber_problemName.py` (e.g., `268_missing_number.py`)
- Use **snake_case** for names
- Include a **short comment at the top** with:
  - Problem name & platform
  - Difficulty (optional)
  - Key idea or approach
  - Notes for future reference

### Example

```python
# Problem: 268. Missing Number
# Platform: LeetCode
# Idea: Use XOR of 0..n with array to find missing number
# Note: Works because a ^ a = 0

class Solution:
    def missingNumber(self, nums):
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for n in nums:
            res ^= n
        return res
```

## Contribution Tips

- Add **new problems only under the correct platform and topic**
- **Do not mix topics**; pick the dominant idea
- Use **notes** to explain tricky parts or mistakes
- Keep files **clean, readable, and minimal**
- Contests go under `contests` with a folder per contest

## Quick Placement Cheat Sheet

| Problem Type                              | Folder                               |
| ----------------------------------------- | ------------------------------------ |
| Array manipulations, sums, rotations      | `arrays`                             |
| String operations, parsing, substrings    | `strings`                            |
| Dicts, sets, frequency counts             | `hashing`                            |
| Linked list operations (nodes & pointers) | `linked-list`                        |
| Time-based contest problems               | `contests/<platform>/<contest-name>` |

**Rule of thumb:**

- Pick the **dominant idea** of the problem for the topic folder.
- If a problem involves multiple topics, choose the one that **unlocks the solution** fastest.
