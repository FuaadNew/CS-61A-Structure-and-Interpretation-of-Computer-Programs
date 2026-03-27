# CS 61A Fall 2024 — Midterm 1 Solutions
@FuaadNew
## Q1: What Would Python Display? (8.0 pts)

```python
def mad(max):
    g = lambda: (print(1) or 2) or (print(3) or 4)
    print(max(5, 6))
    return g
print(mad(print)(), 7, print(8))
```

**Printed output:**

```
5 6
None
1
8
2 7 None
```

**(a)** Last line printed: **2 7 None**

**(b)** Whole lines that appear in printed output: **1, 5 6, 8, None**

**(c)** Order of first occurrence of 1, 6, 8: **6, 1, 8**

---

## Q2: Which One — Environment Diagram (8.0 pts)

```python
x, y, z = 1, 2, 3

def switch(x):
    z = 4
    if x == y:
        def which(one):
            return x + one
    else:
        def which(one):
            return x + one
        x = which(x)
    which(x)

def which(one):
    return x + one

switch(x+1)
x = 5
which(z)
```

| Blank | Answer |
|-------|--------|
| (a) | **4** |
| (b) | **func which(one) [parent=f1]** |
| (c) | **None** |
| (d) | **4** |
| (e) | **8** |
| (f) | **Global** |
| (g) | **3** |
| (h) | **15** |

---

## Q3: Final Digit (6.0 pts)

```python
def final_digit(n):
    """Sum the digits of n repeatedly to reach one digit."""
    while n >= 10:
        s = 0                        # (a)
        while n:                     # (b)
            n, s = n // 10, s + n % 10  # (c)
        n = s                        # (d)
    return n
```

| Blank | Answer |
|-------|--------|
| (a) | **0** |
| (b) | **while n** |
| (c) | **s + n % 10** |
| (d) | **n = s** |

---

## Q4: Close Enough (8.0 pts)

```python
def close(m, n):
    if m < n:
        m, n = n, m
    while m or n:
        if m % 10 == n % 10:              # (a)
            m, n = m // 10, n // 10        # (b)
        else:
            return m // 10 == n // 10 or m // 10 == n  # (c) or (d)
    return False                           # (e)
```

| Blank | Answer |
|-------|--------|
| (a) | **m % 10 == n % 10** |
| (b) | **m // 10, n // 10** |
| (c) | **m // 10 == n // 10** |
| (d) | **m // 10 == n** |
| (e) | **False** |

**Explanation:**
- (a)/(b): If last digits match, strip them from both numbers
- (c): After a mismatch, check if removing the last digit from both makes them equal → the digit was **changed**
- (d): Check if removing the last digit from m (the larger) makes it equal to n → a digit was **inserted/removed**
- (e): If we exhaust both numbers with no differences, m == n, and equal numbers are not "close"

---

## Q5: Shifty (10.0 pts)

### Part (a): shift (4.0 pts)

```python
def shift(k, f):
    return lambda x: f(x + k)         # (a.i)
```

**5a.i:** `lambda x: f(x + k)`

**5a.ii (alternate using compose):** `compose(f, lambda x: x + k)`

### Part (b): sum_range (6.0 pts)

```python
def sum_range(p, q, term):
    assert p <= q
    return summation(q - p + 1, shift(p - 1, term))
    #      (a)        (b)       (c)
```

| Blank | Answer |
|-------|--------|
| (a) | **summation** |
| (b) | **q - p + 1** |
| (c) | **shift(p - 1, term)** |

**Explanation:** `summation(n, term)` sums `term(1) + ... + term(n)`. We want `term(p) + ... + term(q)`, which is `q - p + 1` terms. `shift(p - 1, term)` maps `term(i)` → `term(i + p - 1)`, so `summation` calls `term(1+p-1) + ... + term(q-p+1+p-1)` = `term(p) + ... + term(q)`.

### Part (c): unshift (0.0 pts, A+ only)

```python
def unshift(shifted):
    return lambda g: shift(-shifted(lambda x: x)(0), g)
```




