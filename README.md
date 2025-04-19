# Partial Permutations

## Problem Description
A **partial permutation** is an arrangement of **k** distinct elements chosen from a set of **n** unique elements. The number of such arrangements is given by:

\[ P(n, k) = \frac{n!}{(n-k)!} \]

This formula counts how many ways you can arrange **k** elements from a total of **n**, where order matters.

### Input
Two positive integers:
- `n`: Total number of items (1 ≤ n ≤ 100)
- `k`: Number of items to arrange (1 ≤ k ≤ 10)

### Output
Return the number of partial permutations \( P(n, k) \) **modulo 1,000,000**.

---

## Example
**Input:**
```
21 7
```

**Output:**
```
51200
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Shouryanpatil/partial-permutations.git
cd partial-permutations
```

### 2. Run the script
```bash
python partial_permutations.py
```

---

## 📂 Files
- `partial_permutations.py` — Main script to compute partial permutations.
- `README.md` — Explanation of the problem and usage instructions.

---



## 📄 License
This project is licensed under the MIT License.

