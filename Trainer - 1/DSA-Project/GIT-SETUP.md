# Git Setup Guide

## Initial Repository Setup

### Step 1: Initialize Git (if not already done)

```bash
cd DSA-Project
git init
git add .
git commit -m "Initial CP Portfolio setup"
```

### Step 2: Create Remote Repository

1. Go to GitHub.com (or GitLab/Bitbucket)
2. Create new repository: `CP-Portfolio` or `DSA-Portfolio`
3. **Don't** add any files (README, .gitignore) yet

### Step 3: Connect to Remote

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CP-Portfolio.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## Regular Workflow

### After Solving a Problem

```bash
# 1. Add your solution file
git add Arrays/TwoSum.cpp

# 2. Commit with descriptive message
git commit -m "Add: Two Sum (LC #1) - HashMap approach"

# 3. Push to remote
git push
```

### Commit Message Format

```
[Add/Update/Fix]: [Topic] - [Problem] ([ID]) - [Brief description]

Examples:
- Add: Arrays - Two Sum (LC #1) - HashMap solution
- Update: Graphs - Number of Islands (LC #200) - Added BFS version
- Fix: DP - Climbing Stairs - Fixed edge case handling
```

### Weekly Update

```bash
# 1. Update progress
git add PROGRESS.md
git commit -m "Update: Weekly progress - Week 1 complete"

# 2. Push all weekly changes
git push
```

---

## Useful Git Commands

### View Status
```bash
git status
```

### View Commit History
```bash
git log --oneline -10
```

### View Changes
```bash
git diff
```

### Revert Last Commit (not pushed)
```bash
git reset HEAD~1
```

### Stash Changes (temporary save)
```bash
git stash
git stash pop
```

### Create a Branch
```bash
git branch feature/new-feature
git checkout feature/new-feature
# or use:
git checkout -b feature/new-feature
```

---

## .gitignore File

Create `.gitignore` in root:

```
# Compiled binaries
*.exe
*.o
*.out

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Temporary files
*.tmp
.DS_Store

# Build directories
build/
dist/
```

---

## GitHub Profile Tips

### 1. Add to Profile README

In your GitHub profile, mention:

```markdown
🎯 **CP Portfolio** - 300+ DSA problems solved
- Arrays, Strings, LinkedList
- Trees, Graphs, DP
- Leetcode: 4-star rating
- Codeforces: 1600+ rating
```

### 2. Make Repository Stand Out

- Update README regularly
- Add progress badges
- Keep commit history clean
- Pin to profile

### 3. Sample Progress Badge

```markdown
![Problems](https://img.shields.io/badge/Problems%20Solved-8%2B-blue)
![Progress](https://img.shields.io/badge/Progress-11.4%25-green)
```

---

## Collaboration (Optional)

### If Working with Others

1. Fork the repository
2. Create a feature branch: `git checkout -b add-graph-problems`
3. Make changes
4. Push to your fork
5. Create Pull Request

---

## Tips for Good Git History

✅ **Good:**
- Commit frequently (1-2 problems per commit)
- Write descriptive messages
- Update progress weekly
- Push regularly

❌ **Bad:**
- One giant commit with all problems
- Vague messages like "update" or "fix"
- Push only once at the end
- Irregular commits

---

## Troubleshooting

### "Your branch is behind by X commits"
```bash
git pull origin main
```

### "Changes conflict"
```bash
# Resolve conflicts manually in your editor
# Then:
git add .
git commit -m "Merge: Resolved conflicts"
git push
```

### "Accidentally committed sensitive data"
```bash
git rm --cached SENSITIVE_FILE.txt
echo "SENSITIVE_FILE.txt" >> .gitignore
git commit -m "Remove: Sensitive file"
git push
```

---

## Recommended Commit Schedule

### Daily (After solving problems)
```bash
git add .
git commit -m "Add: Solutions for Day X"
git push
```

### Weekly (Every Sunday)
```bash
git add PROGRESS.md
git commit -m "Update: Weekly progress report"
git push
```

### Monthly (End of month review)
```bash
git add README.md
git commit -m "Update: Monthly review and statistics"
git push
```

---

## GitHub Actions (Advanced)

Create `.github/workflows/lint.yml`:

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check code format
        run: |
          # Add linting commands here
```

This automatically runs checks on every push!

