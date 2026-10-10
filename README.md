# NIELIT Data Science Tutorials

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![NumPy](https://img.shields.io/badge/NumPy-Tutorials-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Tutorials-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)

A curated collection of hands-on Jupyter notebooks and scripts covering the foundational libraries of the Python data science ecosystem: **NumPy**, **Pandas**, and **Matplotlib**. These materials were developed in the context of the NIELIT (National Institute of Electronics and Information Technology) Data Science curriculum and are intended for learners who want practical, runnable examples rather than abstract theory.

Each notebook is self-contained, executable, and focused on core concepts with benchmarks, visualizations, and real-world-style manipulations.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [What You Will Learn](#what-you-will-learn)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Notebook Index](#notebook-index)
- [Scripts](#scripts)
- [How to Contribute](#how-to-contribute)
- [License](#license)
- [Author](#author)

---

## Repository Structure

```
NIELIT-DATA-SCIENCE/
├── LICENSE
├── README.md                  # This file
├── requirements.txt            # Python dependencies
├── .gitignore
├── NumPy_Tutorial_1.ipynb      # Speed comparison & fundamentals
├── NumPy_Tutorial_2.ipynb
├── NumPy_Tutorial_3.ipynb
├── NumPy_Tutorial_4.ipynb
├── Pandas_Tutorial_1.ipynb
├── Pandas_Tutorial_2.ipynb
├── Pandas_Tutorial_3.ipynb
├── Pandas_Tutorial_4.ipynb
├── Matplotlib.ipynb            # Comprehensive plotting guide
└── pandas_manipulation_demo.py # Standalone Pandas slicing & column operations demo
```

All notebooks currently live at the repository root for immediate accessibility. Future reorganization into topic-specific directories is welcome via pull request.

---

## What You Will Learn

- **NumPy**: Array creation, vectorized operations, broadcasting, performance advantages over pure Python, indexing, and mathematical operations.
- **Pandas**: Series and DataFrame construction, indexing (`.loc` / `.iloc`), data selection, missing-value handling, grouping, reshaping, and practical data wrangling patterns.
- **Matplotlib**: Figure/axis management, line/bar/scatter plots, customization, subplots, and publication-quality visualization techniques.
- **Integrated workflow**: How the three libraries complement each other in a typical data-science pipeline.

---

## Prerequisites

- Python 3.10 or newer
- Basic familiarity with Python syntax
- (Recommended) A virtual environment manager (`venv`, `conda`, or `uv`)

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Rishabh-bgp/NIELIT-DATA-SCIENCE.git
cd NIELIT-DATA-SCIENCE

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
# or
jupyter lab
```

Open any `*_Tutorial_*.ipynb` or `Matplotlib.ipynb` and run the cells sequentially. Most notebooks were originally authored in Google Colab; they have been cleaned of Colab-specific paths and are fully local-runnable.

---

## Notebook Index

| Notebook | Focus | Key Topics |
|----------|-------|------------|
| `NumPy_Tutorial_1.ipynb` | Performance & basics | List vs array speed benchmark, visualization of timing results |
| `NumPy_Tutorial_2.ipynb` | Array creation & ops | `np.array`, `arange`, `linspace`, arithmetic, broadcasting |
| `NumPy_Tutorial_3.ipynb` | Indexing & slicing | Advanced indexing, boolean masks, reshaping |
| `NumPy_Tutorial_4.ipynb` | Linear algebra & utilities | Matrix operations, random generation, statistical functions |
| `Pandas_Tutorial_1.ipynb` | Series & DataFrame intro | Creation, basic attributes, simple selection |
| `Pandas_Tutorial_2.ipynb` | Data inspection & cleaning | `head`/`tail`/`info`/`describe`, handling missing data |
| `Pandas_Tutorial_3.ipynb` | Selection & transformation | `.loc`, `.iloc`, boolean indexing, `apply`, column operations |
| `Pandas_Tutorial_4.ipynb` | Aggregation & reshaping | `groupby`, pivot, merge/join patterns |
| `Matplotlib.ipynb` | Visualization | Line, bar, scatter, histogram, subplots, styling, annotations |

> **Note**: Exact cell-level content may vary slightly; open the notebook for the authoritative sequence of examples.

---

## Scripts

- **`pandas_manipulation_demo.py`**  
  A self-contained Python script demonstrating:
  - DataFrame construction and index setting
  - Column and row slicing (`.loc` / `.iloc`)
  - Adding columns via direct assignment, `.assign()`, `.insert()`, and conditional logic with `np.select`
  
  Run it directly:
  ```bash
  python pandas_manipulation_demo.py
  ```

---

## How to Contribute

Contributions are welcome. Suggested improvements include:

1. Reorganizing notebooks into `numpy/`, `pandas/`, and `matplotlib/` directories.
2. Adding explanatory markdown cells or companion `.md` notes for each tutorial.
3. Including sample datasets where notebooks currently generate synthetic data.
4. Writing unit tests or verification scripts for key examples.
5. Translating comments or adding multilingual versions.

Please open an issue or submit a pull request. All contributions should maintain the educational, runnable character of the existing material.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Er. Rishabh Aryan

---

## Author

**Er. Rishabh Aryan**  
Indian Institute of Information Technology, Bhagalpur  
GitHub: [Rishabh-bgp](https://github.com/Rishabh-bgp)  
Focus areas: interpretable machine learning, advanced data-mining pipelines, and predictive engineering analytics.

---

*Built as a practical companion to the NIELIT Data Science syllabus. Feel free to fork, adapt, and extend.*
