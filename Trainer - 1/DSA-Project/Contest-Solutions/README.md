# 🏆 How to Add Contest Solutions

Guide for organizing and tracking your contest solutions.

---

## Contest Solutions Structure

```
Contest-Solutions/
├── README.md
├── LeetCode/
│   ├── Weekly-Contest-XXX/
│   │   ├── Problem-1.cpp
│   │   ├── Problem-2.cpp
│   │   └── Results.md
│   └── Biweekly-Contest-XX/
│       ├── Problem-1.cpp
│       ├── Problem-2.cpp
│       └── Results.md
└── Codeforces/
    ├── Round-XXX/
    │   ├── ProblemA.cpp
    │   ├── ProblemB.cpp
    │   ├── ProblemC.cpp
    │   └── Results.md
    └── Div2-Round-XXX/
        ├── ProblemA.cpp
        ├── ProblemB.cpp
        ├── ProblemC.cpp
        └── Results.md
```

---

## LeetCode Contest Format

### Create Contest Folder

When LeetCode Weekly Contest #XXX starts:

```bash
mkdir "Contest-Solutions/LeetCode/Weekly-Contest-XXX"
# or for biweekly
mkdir "Contest-Solutions/LeetCode/Biweekly-Contest-XX"
```

### Problem File Format

```cpp
// Problem: [Problem Name]
// LeetCode Weekly Contest #XXX
// Problem Number: [1/2/3/4]
// Difficulty: [Easy/Medium/Hard]
// Solved: [Yes/No/Partial]
// Time: [X minutes]

#include <bits/stdc++.h>
using namespace std;

// Solution code
class Solution {
public:
    // ... code ...
};

/*
Analysis:
- Approach: 
- Time: 
- Space: 
- Issues: 
*/
```

### Results.md Template

```markdown
# Weekly Contest #XXX Results

**Date:** [Date]
**Rank:** [Your Rank]/[Total Participants]
**Score:** [Score]
**Solved:** [X/4 problems]

## Problem Breakdown

### Problem 1: [Name]
- Status: ✓ Accepted
- Time: 5 min
- Complexity: O(n)
- Approach: [Brief description]

### Problem 2: [Name]
- Status: ✓ Accepted
- Time: 15 min
- Complexity: O(n²)
- Approach: [Brief description]

### Problem 3: [Name]
- Status: ✗ Wrong Answer
- Time: 25 min
- Issue: Off-by-one error
- Fix: [What you'll do next time]

### Problem 4: [Name]
- Status: ✗ Did Not Attempt
- Reason: Time constraint

## Learnings
- [ ] Insight 1
- [ ] Insight 2

## Next Steps
- [ ] Solve Problem 3 correctly
- [ ] Practice similar problems
```

---

## Codeforces Contest Format

### Create Contest Folder

When new Codeforces round starts:

```bash
mkdir "Contest-Solutions/Codeforces/Round-XXX"
# or
mkdir "Contest-Solutions/Codeforces/Div2-Round-XXX"
```

### Problem File Format

```cpp
// Problem: [Problem Name]
// Codeforces [Round Type] Round #XXX
// Problem: [A/B/C/D/E/F]
// Difficulty: [1000-2500]
// Verdict: [Accepted/WA/TLE/RTE]
// Time: [X seconds]

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // Solution code
    
    return 0;
}

/*
Approach:
1. ...
2. ...

Time: O(...)
Space: O(...)

Key Idea:
- ...

Why it failed (if applicable):
- ...
*/
```

### Results.md Template

```markdown
# Codeforces Div 2 Round #XXX

**Date:** [Date]
**Rating:** [Your Rating] → [New Rating]
**Change:** [+/-XX]
**Solved:** [X/6 problems]

## Problem Results

| Problem | Verdict | Time | Language |
|---------|---------|------|----------|
| A | AC | 2:15 | C++ |
| B | AC | 8:30 | C++ |
| C | WA | 35:00 | C++ |
| D | TLE | 45:00 | C++ |

## Analysis

### Problem A
- ✓ Solved
- Approach: [Brief]
- Difficulty: Easy

### Problem B
- ✓ Solved
- Approach: [Brief]
- Difficulty: Medium

### Problem C
- ✗ Wrong Answer
- Issue: [What went wrong]
- Fix: [How to solve]

### Problem D
- ✗ Time Limit Exceeded
- Approach: Brute force O(n²)
- Optimization: Need O(n log n) with [data structure]

## Key Takeaways
1. [Learning 1]
2. [Learning 2]
3. [Learning 3]
```

---

## Tracking Template

Create `Contest-Solutions/README.md`:

```markdown
# Contest Solutions Archive

Organized collection of solutions from competitive programming contests.

## Statistics

### LeetCode
- Weekly Contests: [X]
- Biweekly Contests: [X]
- Total Solved: [X/Y]
- Participation Rate: [%]

### Codeforces
- Contests: [X]
- Current Rating: [XXXX]
- Peak Rating: [XXXX]
- Contests: [Count]

## Recent Contests

### LeetCode Weekly Contest #XXX
- Date: [Date]
- Rank: [Rank]
- Solved: 2/4
- [Link to folder](./LeetCode/Weekly-Contest-XXX/)

### Codeforces Div 2 Round #XXX
- Date: [Date]
- Rating Change: +50
- Solved: 3/6
- [Link to folder](./Codeforces/Div2-Round-XXX/)

## Contest Participation Timeline

| Date | Contest | Platform | Rank | Solved | Status |
|------|---------|----------|------|--------|--------|
| 2026-06-24 | Weekly #XXX | LC | 5000 | 2/4 | ✓ |

## Weak Areas from Contests

- [ ] Observation-based problems
- [ ] Greedy proofs
- [ ] Number theory
- [ ] Data structure combinations

## Improvements Needed

1. **Time Management** - Spend more time on observation
2. **Prewriting** - Always verify approach before coding
3. **Edge Cases** - Test thoroughly before submitting
4. **Practice** - More upsolving after contests
```

---

## After Each Contest

### Immediate Steps (Same Day)
1. [ ] Copy all attempted solutions
2. [ ] Create Results.md with current status
3. [ ] Document verdicts (AC/WA/TLE/etc)
4. [ ] Add to statistics

### Analysis (Within 24 Hours)
1. [ ] Solve unsolved/partial problems
2. [ ] Understand correct approaches
3. [ ] Note where you went wrong
4. [ ] Add key insights

### Learning (Within 1 Week)
1. [ ] Practice similar problems
2. [ ] Master weak patterns
3. [ ] Update weak areas list
4. [ ] Commit solutions

---

## Commit Examples

```bash
# After contest
git add Contest-Solutions/LeetCode/Weekly-Contest-XXX/
git commit -m "Contest: LeetCode Weekly #XXX - 2/4 solved"
git push

# After upsolving
git add Contest-Solutions/LeetCode/Weekly-Contest-XXX/Problem-3.cpp
git commit -m "Upsolved: LeetCode #XXX Problem 3 - Wrong approach fixed"
git push

# Rating change
git add Contest-Solutions/Codeforces/Round-XXX/
git commit -m "Contest: CF Round #XXX - Rating 1500→1600 (+100)"
git push
```

---

## Tips for Contest Success

### Before Contest
- [ ] Review weak topics
- [ ] Make sure environment set up
- [ ] Have templates ready
- [ ] Read all problems first

### During Contest
- [ ] Spend 10 min reading all problems
- [ ] Start with easier problems
- [ ] Code cleanly (important for debugging)
- [ ] Test before submitting
- [ ] Don't overthink - submit and iterate

### After Contest
- [ ] Analyze all problems (even unsolved)
- [ ] Understand official solution
- [ ] Practice similar problems
- [ ] Update weak areas tracking

---

## Resources for Contest Prep

### Upsolving Platforms
- **LeetCode** - LeetCode problems for contest practice
- **Codeforces** - Browse by difficulty/tags
- **AtCoder** - Daily practice contests

### Editorials
- **LeetCode Discuss** - Community solutions
- **Codeforces Blog** - Official editorials
- **YouTube** - Solution walkthroughs

---

## Contests to Join

### Regular Participation
- LeetCode: Weekly Sunday (2:30 PM UTC)
- LeetCode: Biweekly alternating (2:30 PM UTC)
- Codeforces: ~2 rounds per week

### Goal
- Participate in 1 contest every week
- Gradually improve ranking
- Master all problem types

