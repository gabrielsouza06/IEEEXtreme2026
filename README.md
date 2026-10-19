cat << 'EOF' > README.md
# 🚀 IEEEXtreme 20.0 — Competitive Programming Repository

Repository dedicated to training, library algorithms, and problem solutions for **IEEEXtreme 20.0** (October 2026).

## 📌 Repository Structure
IEEEXtreme2026/
├── lib/
│   └── snippets.py       # Core CP library (Fast I/O, DSU, Dijkstra, Sieve)
├── cs_academy/
│   └── anagrams.py       # CS Academy - Anagrams solution
└── README.md             # Project documentation


## 🛠️ Environment & Setup

* **Primary Runtime:** PyPy3 (Python 3.11 / PyPy 7.9) via JIT Compilation
* **Secondary Runtime:** CPython 3.13 (for `numpy` / `scipy` tasks)
* **Backup Language:** C++20 / C++23 (for strict time limit edge cases)
* **Platform Constraints:** Max 100 KB workspace capacity on CS Academy

## 📦 Key Components (`lib/snippets.py`)

* **Fast I/O:** Token-based batch input processing using `sys.stdin.read().split()`
* **Graph Algorithms:** Optimized Dijkstra with `heapq`
* **Data Structures:** Disjoint Set Union (DSU) with Path Compression & Rank Optimization
* **Math Utilities:** Sieve of Eratosthenes prime generator

## 🎯 Solved Problems

| Platform | Problem | Solution File | Approach | Time Complexity |
| :--- | :--- | :--- | :--- | :--- |
| CS Academy | Anagrams | `cs_academy/anagrams.py` | Counter & Word Sorting | $O(N \cdot L \log L)$ |

## ✒️ Author

Maintained by **Gabriel Souza Vieira** (`gabrielsouza06`) for IEEEXtreme 20.0 preparation.
EOF

# 2. Registrar no Git
git add README.md
git commit -m "docs: add README.md documentation"

# 3. Enviar para o GitHub
git push origin main
