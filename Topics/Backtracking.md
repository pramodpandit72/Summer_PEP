# Backtracking (C++) - Beginner Notes

> Goal: Learn **Backtracking** for LeetCode and Coding Interviews.

---

# 1. What is Backtracking?

Backtracking is a technique where we

- Make a choice
- Explore that choice
- Undo the choice (Backtrack)
- Try another choice

Think of it as trying every possible path.

Example:

```
Choose A
|
|-- Choose B
|   |
|   |-- Result
|
Undo B
|
Choose C
|
|-- Result
```

The important part is **undoing the previous choice** before trying another one.

---

# 2. When to use Backtracking?

If the question asks

- Generate all possibilities
- Find all combinations
- Find all permutations
- Subsets
- Sudoku
- N Queens
- Maze paths
- Word Search

Think:

> **Backtracking**

Keywords:

- All possible answers
- Every combination
- Every permutation
- Every path
- Can we place?

---

# 3. Basic Backtracking Steps

```
1. Make a choice

2. Move forward (Recursive Call)

3. Undo the choice
```

This is called

> Choose → Explore → Unchoose

---

# 4. General Template

```cpp
void backtrack(...) {

    // Base Case
    if(condition){
        // store answer
        return;
    }

    for(all possible choices){

        // Choose
        ...

        // Explore
        backtrack(...);

        // Undo (Backtrack)
        ...
    }
}
```

---

# 5. Example 1 : Generate All Subsets

Input

```
nums = [1,2]
```

Output

```
[]
[1]
[2]
[1,2]
```

Tree

```
                []
             /      \
           1          skip
         /   \
      2      skip
```

Code

```cpp
class Solution {
public:

    vector<vector<int>> ans;
    vector<int> path;

    void solve(int index, vector<int>& nums){

        if(index==nums.size()){
            ans.push_back(path);
            return;
        }

        // Take
        path.push_back(nums[index]);
        solve(index+1, nums);

        // Backtrack
        path.pop_back();

        // Don't Take
        solve(index+1, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums) {

        solve(0, nums);
        return ans;
    }
};
```

---

# Dry Run

```
path = []

Take 1

path = [1]

Take 2

path = [1,2]

Store

Backtrack

path = [1]

Don't Take 2

Store

Backtrack

path = []

Take 2

Store

Don't Take 2

Store
```

---

# 6. Example 2 : Permutations

Input

```
[1,2,3]
```

Output

```
123
132
213
231
312
321
```

Idea

Choose every unused number.

Use

```cpp
visited[]
```

Template

```cpp
for(int i=0;i<n;i++){

    if(visited[i]) continue;

    visited[i]=true;
    path.push_back(nums[i]);

    solve();

    path.pop_back();
    visited[i]=false;
}   
```

---

# 7. Example 3 : Combination Sum

Input

```
candidates = [2,3,6,7]

target = 7
```

Output

```
[2,2,3]
[7]
```

Choice

Take current number again

OR

Move to next number

---

# 8. Example 4 : N Queens

Choice

Can we place queen here?

If yes

```
Place Queen

↓

Go to next row

↓

Remove Queen
```

---

# 9. Example 5 : Sudoku Solver

For every empty cell

Try

```
1

2

3

...

9
```

If valid

```
Place

↓

Solve

↓

Remove
```

---

# 10. Example 6 : Word Search

Move

```
Up

Down

Left

Right
```

Mark cell visited

Explore

Unmark

---

# Backtracking Pattern

```
Choose

↓

Recursive Call

↓

Undo
```

Always remember this.

---

# 11. Common Data Structures

### Current Path

```cpp
vector<int> path;
```

### Final Answer

```cpp
vector<vector<int>> ans;
```

### Visited Array

```cpp
vector<bool> visited(n,false);
```

### Directions

```cpp
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
```

---

# 12. Time Complexity

Usually

```
O(2^N)
```

or

```
O(N!)
```

because we explore many possibilities.

Backtracking is generally exponential.

---

# 13. How to Identify Backtracking?

Question says

✅ Generate all

✅ Print all

✅ Every possible

✅ All paths

✅ All combinations

✅ Can we place?

Think

> Backtracking

---

# 14. Mistakes Beginners Make

### 1. Forgetting Base Case

Wrong

```cpp
solve();
```

Correct

```cpp
if(condition){
    return;
}
```

---

### 2. Forgetting Backtracking

Wrong

```cpp
path.push_back(x);

solve();
```

Correct

```cpp
path.push_back(x);

solve();

path.pop_back();
```

---

### 3. Forgetting visited=false

Wrong

```cpp
visited[i]=true;

solve();
```

Correct

```cpp
visited[i]=true;

solve();

visited[i]=false;
```

---

### 4. Passing by Value Unnecessarily

Wrong

```cpp
solve(vector<int> nums)
```

Correct

```cpp
solve(vector<int>& nums)
```

---

# 15. Master Template

```cpp
vector<vector<int>> ans;
vector<int> path;

void solve(...){

    if(base_case){
        ans.push_back(path);
        return;
    }

    for(each choice){

        if(choice not valid)
            continue;

        // Choose
        ...

        // Explore
        solve(...);

        // Undo
        ...
    }
}
```

Remember:

```
Choose

↓

Explore

↓

Undo
```

---

# 16. LeetCode Questions (Must Do)

## Easy

- 78. Subsets ⭐⭐⭐⭐⭐
- 257. Binary Tree Paths
- 401. Binary Watch

---

## Medium (Most Important)

- 46. Permutations ⭐⭐⭐⭐⭐
- 47. Permutations II ⭐⭐⭐⭐
- 39. Combination Sum ⭐⭐⭐⭐⭐
- 40. Combination Sum II ⭐⭐⭐⭐⭐
- 77. Combinations ⭐⭐⭐⭐⭐
- 90. Subsets II ⭐⭐⭐⭐⭐
- 17. Letter Combinations of a Phone Number ⭐⭐⭐⭐
- 22. Generate Parentheses ⭐⭐⭐⭐⭐
- 79. Word Search ⭐⭐⭐⭐⭐
- 131. Palindrome Partitioning ⭐⭐⭐⭐⭐
- 216. Combination Sum III ⭐⭐⭐⭐
- 93. Restore IP Addresses ⭐⭐⭐
- 491. Non-decreasing Subsequences ⭐⭐⭐⭐

---

## Hard

- 37. Sudoku Solver ⭐⭐⭐⭐⭐
- 51. N-Queens ⭐⭐⭐⭐⭐
- 52. N-Queens II ⭐⭐⭐⭐
- 212. Word Search II ⭐⭐⭐⭐⭐

---

# 17. Frequently Asked in Interviews

These backtracking problems are commonly asked (or have close variants) in interviews at companies like Amazon, Microsoft, Google, Adobe, Atlassian, Walmart Global Tech, Flipkart, Goldman Sachs, and many product-based companies.

### Must Practice

- Subsets
- Subsets II
- Permutations
- Permutations II
- Combination Sum
- Combination Sum II
- Generate Parentheses
- Word Search
- Palindrome Partitioning
- Letter Combinations of Phone Number
- N Queens
- Sudoku Solver

---

# 18. Practice Order (Recommended)

Week 1

1. Subsets
2. Combinations
3. Combination Sum
4. Combination Sum II

Week 2

5. Permutations
6. Permutations II
7. Subsets II
8. Generate Parentheses

Week 3

9. Letter Combinations
10. Word Search
11. Palindrome Partitioning

Week 4

12. N Queens
13. Sudoku Solver
14. Word Search II

---

# 19. Quick Revision

```
Backtracking = Try every possibility.

Algorithm

Choose

↓

Recursive Call

↓

Undo Choice

↓

Try Next Choice
```

### Template

```cpp
for(each choice){

    Choose

    solve()

    Undo
}
```

---

# 20. Final Checklist

Before solving a backtracking problem, ask yourself:

- Is the question asking for **all possible answers**?
- What is my **choice** at each step?
- What is the **base case**?
- How do I **undo** the choice?
- Do I need a **visited** array?
- Do I need to **store the current path**?

If the answer to the first question is **yes**, backtracking is likely the correct approach.