# NIELIT Data Science Tutorials

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![NumPy](https://img.shields.io/badge/NumPy-Tutorials-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Tutorials-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)

A curated collection of hands-on Jupyter notebooks and scripts covering the foundational libraries of the Python data science ecosystem: **NumPy**, **Pandas**, and **Matplotlib**. These materials were developed in the context of the NIELIT (National Institute of Electronics and Information Technology) Data Science curriculum and are intended for learners who want practical, runnable examples rather than abstract theory.

Each notebook is self-contained, executable, and focused on core concepts with benchmarks, visualizations, and real-world-style manipulations.

## Documentation

| Document | Description |
|----------|-------------|
| [Detailed Learning Guide](docs/DETAILED_GUIDE.md) | Recommended sequence, library roles, pitfalls, and next steps |
| [Installation Guide](docs/INSTALLATION.md) | Step-by-step setup instructions |
| [Usage Guide](docs/USAGE.md) | How to run notebooks and the demo script effectively |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common issues and solutions |
| [Contributing](CONTRIBUTING.md) | Guidelines for contributions |
| [Code of Conduct](CODE_OF_CONDUCT.md) | Community standards |
| [Changelog](CHANGELOG.md) | Project history |
| [Security](SECURITY.md) | Vulnerability reporting |

Per-library overviews: [numpy/](numpy/README.md) · [pandas/](pandas/README.md) · [matplotlib/](matplotlib/README.md)

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
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── SECURITY.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── DETAILED_GUIDE.md
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   └── TROUBLESHOOTING.md
├── numpy/
│   ├── README.md
│   ├── NumPy_Tutorial_1.ipynb
│   ├── NumPy_Tutorial_2.ipynb
│   ├── NumPy_Tutorial_3.ipynb
│   └── NumPy_Tutorial_4.ipynb
├── pandas/
│   ├── README.md
│   ├── Pandas_Tutorial_1.ipynb
│   ├── Pandas_Tutorial_2.ipynb
│   ├── Pandas_Tutorial_3.ipynb
│   ├── Pandas_Tutorial_4.ipynb
│   └── pandas_manipulation_demo.py
└── matplotlib/
    ├── README.md
    └── Matplotlib.ipynb
```

---

## What You Will Learn

- **NumPy** (`numpy/`): Array creation, vectorized operations, broadcasting, performance advantages over pure Python, indexing, and mathematical operations.
- **Pandas** (`pandas/`): Series and DataFrame construction, indexing (`.loc` / `.iloc`), data selection, missing-value handling, grouping, reshaping, and practical data wrangling patterns.
- **Matplotlib** (`matplotlib/`): Figure/axis management, line/bar/scatter plots, customization, subplots, and publication-quality visualization techniques.
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

For detailed instructions, see the [Installation Guide](docs/INSTALLATION.md) and [Usage Guide](docs/USAGE.md).

Navigate into `numpy/`, `pandas/`, or `matplotlib/` and open the notebooks. Run cells sequentially. Most notebooks were originally authored in Google Colab; they have been cleaned of Colab-specific paths and are fully local-runnable.

---

## Notebook Index

### NumPy (`numpy/`)
| Notebook | Focus | Key Topics |
|----------|-------|------------|
| `NumPy_Tutorial_1.ipynb` | Performance & basics | List vs array speed benchmark, visualization of timing results |
| `NumPy_Tutorial_2.ipynb` | Array creation & ops | `np.array`, `arange`, `linspace`, arithmetic, broadcasting |
| `NumPy_Tutorial_3.ipynb` | Indexing & slicing | Advanced indexing, boolean masks, reshaping |
| `NumPy_Tutorial_4.ipynb` | Sorting & utilities | `argsort`, `argmin`/`argmax`, linked sorting, top-N selection |

### Pandas (`pandas/`)
| Notebook | Focus | Key Topics |
|----------|-------|------------|
| `Pandas_Tutorial_1.ipynb` | Series & DataFrame intro | Creation, basic attributes, simple selection |
| `Pandas_Tutorial_2.ipynb` | Data inspection & cleaning | `head`/`tail`/`info`/`describe`, handling missing data |
| `Pandas_Tutorial_3.ipynb` | Selection & transformation | `.loc`, `.iloc`, boolean indexing, `apply`, column operations |
| `Pandas_Tutorial_4.ipynb` | Aggregation & reshaping | `groupby`, pivot, merge/join patterns |

### Matplotlib (`matplotlib/`)
| Notebook | Focus | Key Topics |
|----------|-------|------------|
| `Matplotlib.ipynb` | Visualization | Line, bar, scatter, histogram, subplots, styling, annotations |

> **Note**: Exact cell-level content may vary slightly; open the notebook for the authoritative sequence of examples. The [Detailed Learning Guide](docs/DETAILED_GUIDE.md) provides additional context for each tutorial.

---

## Scripts

- **`pandas/pandas_manipulation_demo.py`**  
  A self-contained Python script demonstrating:
  - DataFrame construction and index setting
  - Column and row slicing (`.loc` / `.iloc`)
  - Adding columns via direct assignment, `.assign()`, `.insert()`, and conditional logic with `np.select`
  
  Run it directly:
  ```bash
  python pandas/pandas_manipulation_demo.py
  ```

---

## How to Contribute

Contributions are welcome. Suggested improvements include:

1. Adding explanatory markdown cells or companion `.md` notes for each tutorial.
2. Including sample datasets where notebooks currently generate synthetic data.
3. Writing unit tests or verification scripts for key examples.
4. Translating comments or adding multilingual versions.
5. Further refining the folder structure or adding cross-library examples.

Please open an issue or submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines. All contributions should maintain the educational, runnable character of the existing material. Please also read our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Er. Rishabh Aryan

---

## Author

**Er. Rishabh Aryan**  
M.Tech (Artificial Intelligence and Data Science)  
Department of Computer Science and Engineering  
Indian Institute of Information Technology, Bhagalpur (Bihar)  

**E-mail:** [rishabh.250201011@iiitbh.ac.in](mailto:rishabh.250201011@iiitbh.ac.in)  
**ORCID:** [0009-0004-7595-9440](https://orcid.org/0009-0004-7595-9440)  
**GitHub:** [Rishabh-bgp](https://github.com/Rishabh-bgp)  

Focus areas: interpretable machine learning, advanced data-mining pipelines, and predictive engineering analytics.

---

*Built as a practical companion to the NIELIT Data Science syllabus. Feel free to fork, adapt, and extend.*
