# Strings in DSA (C++) — Interview Preparation Notes

Goal:
Learn how to solve string questions using **patterns**, not memorization.

---

# 1. How Strings are Stored

```cpp
string s = "coding";
```

Memory:

```text
c o d i n g
0 1 2 3 4 5
```

Access:

```cpp
s[i]
```

Time Complexity:

* Access → O(1)
* Traversal → O(N)
* Insert/Delete middle → O(N)
* Append → O(1) average

---

# 2. String Complexity You Must Know

| Operation   | Complexity |
| ----------- | ---------- |
| Access      | O(1)       |
| Compare     | O(N)       |
| Concatenate | O(N)       |
| Reverse     | O(N)       |
| Substring   | O(K)       |
| Find        | O(N)       |

Interviewers expect this.

---

# 3. Important STL Operations

## Reverse

```cpp
reverse(s.begin(), s.end());
```

---

## Sort

```cpp
sort(s.begin(), s.end());
```

Useful in:

* Anagram
* Lexicographical problems

---

## Find

```cpp
s.find("abc");
```

Returns index.

Example:

```cpp
string s="abcdef";

cout<<s.find("cd");
```

Output:

```text
2
```

If not found:

```text
string::npos
```

---

## Erase

```cpp
s.erase(start,length);
```

Example:

```cpp
string s="abcdef";

s.erase(2,2);

cout<<s;
```

Output:

```text
abef
```

---

## Insert

```cpp
s.insert(index,"xyz");
```

---

# 4. Pattern 1 → Frequency Array

Most important beginner interview pattern.

Works when:

* lowercase letters
* counting

Example:
Count characters.

```cpp
string s="banana";

vector<int> freq(26,0);

for(char c:s)
{
    freq[c-'a']++;
}
```

Complexity:

```text
O(N)
```

Questions:

* Valid Anagram
* Ransom Note
* First Unique Character

---

# 5. Pattern 2 → Hashing + String

Use when:

* large characters
* Unicode
* duplicates

Template:

```cpp
unordered_map<char,int> mp;

for(char c:s)
{
    mp[c]++;
}
```

Questions:

* Group Anagrams
* Character Frequency
* Longest Unique Substring

Complexity:

```text
O(N)
```

---

# 6. Pattern 3 → Two Pointers

Use when:

* compare both ends
* reverse
* palindrome

Template:

```cpp
int left=0;
int right=s.size()-1;

while(left<right)
{
    left++;
    right--;
}
```

Questions:

* Reverse String
* Valid Palindrome
* Reverse Words

---

# 7. Pattern 4 → Sliding Window ⭐⭐⭐

Very important.

Use when question contains:

```text
Longest
Shortest
Maximum
Minimum
Substring
Continuous
```

Template:

```cpp
int left=0;

for(int right=0;right<n;right++)
{
    while(condition)
    {
        left++;
    }
}
```

Example:
Longest substring without repeating.

```cpp
string s;

unordered_map<char,int> mp;

int left=0;
int ans=0;

for(int right=0;right<s.size();right++)
{
    mp[s[right]]++;

    while(mp[s[right]]>1)
    {
        mp[s[left]]--;
        left++;
    }

    ans=max(ans,right-left+1);
}
```

Complexity:

```text
O(N)
```

---

# 8. Pattern 5 → Expand Around Center

Used in palindrome problems.

Idea:

```text
Move left and right outward.
```

Template:

```cpp
while(left>=0 &&
right<n &&
s[left]==s[right])
{
    left--;
    right++;
}
```

Questions:

* Longest Palindrome
* Count Palindromes

Complexity:

```text
O(N²)
```

---

# 9. Pattern 6 → String + Stack

Useful for:

```text
remove
decode
brackets
undo
```

Template:

```cpp
stack<char> st;
```

Questions:

* Remove Adjacent Duplicates
* Decode String
* Valid Parentheses

---

# 10. Pattern 7 → KMP (Advanced)

Use:

```text
Pattern Matching
Search substring
```

Problem:

Find pattern efficiently.

Complexity:

```text
O(N+M)
```

Concept:
Build LPS array.

Template:

```cpp
vector<int> lps(m);
```

Questions:

* Implement strStr()
* Pattern Search

---

# 11. Pattern 8 → Rolling Hash (Advanced)

Use:

```text
Repeated substring
duplicate detection
```

Questions:

* Repeated DNA Sequence
* Rabin Karp

Complexity:

```text
O(N)
```

---

# 12. Pattern Recognition Sheet

| If Question Says  | Use            |
| ----------------- | -------------- |
| Frequency         | Array / Hash   |
| Reverse           | Two Pointer    |
| Longest Substring | Sliding Window |
| Palindrome        | Two Pointer    |
| Pattern Search    | KMP            |
| Remove            | Stack          |
| Group             | Hash Map       |

---

# Top LeetCode String Questions (Do in Order)

## Level 1 — Foundation

1. Reverse String
2. Valid Palindrome
3. Valid Anagram
4. Longest Common Prefix
5. First Unique Character
6. Implement strStr()

Goal:
Finish in 3–4 days.

---

## Level 2 — Core Interview

1. Longest Substring Without Repeating Characters ⭐⭐⭐
2. Group Anagrams ⭐⭐⭐
3. String Compression ⭐⭐⭐
4. Decode String ⭐⭐⭐
5. Palindromic Substrings
6. Partition Labels
7. Remove Duplicate Letters

Goal:
Finish in 1 week.

---

## Level 3 — Strong DSA Level

1. Minimum Window Substring ⭐⭐⭐
2. Longest Palindromic Substring ⭐⭐⭐
3. Edit Distance ⭐⭐⭐
4. Regular Expression Matching
5. Rabin Karp
6. KMP

Goal:
2 weeks.

---

# Interview Strategy

For every string problem ask:

Step 1:

```text
Brute Force?
```

Step 2:

```text
Can hashing reduce complexity?
```

Step 3:

```text
Can sliding window help?
```

Step 4:

```text
Can two pointers help?
```

Step 5:

```text
Can preprocessing help?
```

---

# Final Checklist

Before interviews you should solve:

□ 10 Easy
□ 20 Medium
□ 5 Hard

Must know:

* Sliding Window
* Hashing
* Two Pointer
* KMP
* Stack + String
* Palindrome Logic

If these are strong, most string interviews become manageable.



<!-- s.find("abc")	Returns the starting index if found
string::npos	Means "not found"
== string::npos	The substring is not present
!= string::npos	The substring is present -->