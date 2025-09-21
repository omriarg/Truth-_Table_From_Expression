# Logic Truth Table Generator (Python)

A **standalone Python tool** to generate truth tables for logical expressions.  


The repository contains only two files:
- `TruthTableMain.py` – entry point of the program  
- `Evaluator.py` – evaluates logical expressions and generates the table  

---

## 🚀 How to Run

1. Run the program:
   ```bash
    python TruthTableMain.py
   ```
2. Enter your logical expression according to the notation guide below.  
   The program will output the truth table in the console.

---

## 🧭 Notation Guide

- **Variables:**  
  Use letters such as `A`, `B`, `C`.

- **Operators:**  
  - **NOT:** `!` or `~` (e.g., `!A`, `~A`)  
  - **AND:** `&` or `*` (e.g., `A&B`, `A*B`)  
  - **OR:** `|` or `+` (e.g., `A|B`, `A+B`)  

- **Expressions:**  
  Combine variables and operators with parentheses for grouping.  
  Examples:  
  - `A+(!BC)`  
  - `!(A&B)|C`  
  - `(A+B)*(!C)`

> Preferred convention: use `!A` instead of `A'`, and `!(expr)` for negation.

---

## 📖 Example

Input:
```
(A&B)+!C
```

Output:
```
A B C | (A&B)+!C
0 0 0 | 1
0 0 1 | 0
0 1 0 | 1
0 1 1 | 0
1 0 0 | 1
1 0 1 | 0
1 1 0 | 1
1 1 1 | 1
```

---

## 🎯 Purpose

This project was built for **educational purposes**:
- Practice with **algorithmic design** and **expression parsing**  
- Understanding **Boolean logic**  
- Applying **data structures** for truth table generation  
