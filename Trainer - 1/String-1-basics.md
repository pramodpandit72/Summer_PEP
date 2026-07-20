# Strings in DSA (C++) — Beginner Notes

## 1. What is a String?

A **string** is a sequence of characters.

Example:

```cpp
string name = "Hello";
```

Characters:

```
H e l l o
0 1 2 3 4
```

Index starts from **0**.

---

# 2. Declaration and Input

### Create String

```cpp
string s = "coding";
```

### Input

```cpp
string s;
cin >> s;
```

Input:

```
hello
```

Output:

```
hello
```

### Input with spaces

```cpp
string s;
getline(cin, s);
```

Input:

```
hello world
```

Output:

```
hello world
```

---

# 3. Important String Functions

## Length

```cpp
string s = "apple";

cout << s.length();
```

Output:

```
5
```

---

## Access Character

```cpp
cout << s[0];
```

Output:

```
a
```

---

## Add Character / String

```cpp
string s = "Hello";

s += " World";

cout << s;
```

Output:

```
Hello World
```

---

## Remove Last Character

```cpp
s.pop_back();
```

---

## Add Last Character

```cpp
s.push_back('A');
```

---

## Substring

```cpp
string s = "abcdef";

cout << s.substr(2,3);
```

Output:

```
cde
```

Format:

```cpp
substr(start,length)
```

---

## Reverse String

```cpp
reverse(s.begin(), s.end());
```

Need:

```cpp
#include <algorithm>
```

---

## Sort String

```cpp
sort(s.begin(), s.end());
```

Example:

```
dcba
↓
abcd
```

---

# 4. Traversing String

### Using Loop

```cpp
for(int i=0;i<s.length();i++)
{
    cout<<s[i];
}
```

### Range Loop

```cpp
for(char ch : s)
{
    cout<<ch;
}
```

---

# 5. String Comparison

```cpp
string a="abc";
string b="abc";

if(a==b)
{
    cout<<"Equal";
}
```

Output:

```
Equal
```

---

# 6. Convert Case

## Lowercase

```cpp
tolower(ch)
```

## Uppercase

```cpp
toupper(ch)
```

Example:

```cpp
string s="HELLO";

for(char &c:s)
{
    c=tolower(c);
}
```

Output:

```
hello
```

---

# 7. Frequency Count (Very Important)

Count characters.

```cpp
string s="banana";

int freq[26]={0};

for(char c:s)
{
    freq[c-'a']++;
}
```

Output:

```
a → 3
b → 1
n → 2
```

---

# 8. Two Pointer Pattern (Important)

Used in:

* Reverse
* Palindrome
* Remove spaces

Example:

```cpp
int left=0;
int right=s.size()-1;

while(left<right)
{
    swap(s[left],s[right]);

    left++;
    right--;
}
```

---

# 9. Sliding Window (Important for Interviews)

Used for:

* Longest substring
* Distinct characters
* Maximum length problems

Basic idea:

* Expand right
* Shrink left

---

# 10. Hashing + String (Very Important)

```cpp
unordered_map<char,int> mp;

for(char c:s)
{
    mp[c]++;
}
```

Used for:

* Frequency
* Anagram
* Unique characters

---

# 11. Important Interview Patterns

### Pattern 1 — Frequency Array

Examples:

* Anagram
* Character count

---

### Pattern 2 — Two Pointer

Examples:

* Reverse
* Palindrome

---

### Pattern 3 — Sliding Window

Examples:

* Longest substring

---

### Pattern 4 — Hash Map

Examples:

* Duplicate detection

---

# Must Practice Questions (LeetCode)

## Easy (Do First)

1. Two Sum
2. Valid Palindrome
3. Reverse String
4. Valid Anagram
5. Length of Last Word
6. First Unique Character in a String
7. Roman to Integer
8. Longest Common Prefix
9. Implement strStr()
10. Merge Strings Alternately

---

## Medium (Interview Important)

1. Longest Substring Without Repeating Characters ⭐
2. Group Anagrams ⭐
3. Longest Palindromic Substring ⭐
4. String Compression ⭐
5. Decode String
6. Generate Parentheses
7. Palindromic Substrings
8. Minimum Window Substring
9. Permutation in String
10. Zigzag Conversion

---

## Hard (Later)

1. Regular Expression Matching
2. Edit Distance
3. Text Justification

---

# Order to Study

Week 1:

* String basics
* Traversal
* Functions

Week 2:

* Frequency array
* Hashing

Week 3:

* Two pointer

Week 4:

* Sliding window

Week 5:

* Mixed questions

---

# Interview Tips

* First think:

  * Can I use two pointers?
  * Can I use frequency array?
  * Can I use hash map?
  * Can I use sliding window?

* Write brute force first.

* Then optimize.

* Practice daily:

  * 3 easy
  * 2 medium

Consistency beats speed.
