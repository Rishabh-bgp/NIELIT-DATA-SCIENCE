# Detailed Learning Guide — NIELIT Data Science Tutorials

This document expands on the high-level overview in the main README. It is intended for learners who want a clear mental model of how the notebooks fit together and what concepts each library contributes to a data-science workflow. All materials are now organized into library-specific directories for easier navigation.

## 1. Why These Three Libraries?

| Library | Directory | Primary Role | When You Reach for It |
|---------|-----------|--------------|-----------------------|
| **NumPy** | `numpy/` | Numerical computing foundation | Fast array math, linear algebra, random sampling, performance-critical loops |
| **Pandas** | `pandas/` | Tabular data manipulation | Loading CSVs, cleaning, filtering, grouping, joining, time-series |
| **Matplotlib** | `matplotlib/` | Visualization | Exploratory plots, publication figures, communicating results |

Together they form the classic “data science triangle” that almost every subsequent library (scikit-learn, seaborn, statsmodels, etc.) builds upon.

## 2. Recommended Learning Sequence

1. **`numpy/` (Tutorials 1 → 4)**  
   Start here. Understand why NumPy exists (speed) and master array creation, indexing, and broadcasting. Everything in Pandas is built on NumPy arrays under the hood.

2. **`pandas/` (Tutorials 1 → 4)**  
   Move to labeled, heterogeneous data. Practice selection, transformation, and aggregation. The standalone `pandas/pandas_manipulation_demo.py` is a good quick reference after Tutorial 3.

3. **`matplotlib/Matplotlib.ipynb`**  
   Once you can shape data, learn to display it. The notebook covers both the pyplot state-machine interface and the more explicit object-oriented style.

## 3. What to Expect Inside Each Notebook

### NumPy Series (`numpy/`)
- **Tutorial 1**: Empirical demonstration that vectorized NumPy is an order of magnitude faster than pure-Python list comprehensions for element-wise arithmetic. Includes a bar chart of the timing results.
- **Tutorial 2**: Constructors (`array`, `arange`, `linspace`, `zeros`, `ones`, `full`, `eye`) and basic arithmetic / universal functions.
- **Tutorial 3**: Integer, slice, and boolean indexing; fancy indexing; reshaping and transposing.
- **Tutorial 4**: Sorting utilities (`argsort`, `argmin`, `argmax`), linked-data sorting, and top-N / bottom-N selection patterns.

### Pandas Series (`pandas/`)
- **Tutorial 1**: Series vs DataFrame, construction from dicts/lists/arrays, index alignment.
- **Tutorial 2**: Inspection methods and basic missing-value strategies (`isna`, `dropna`, `fillna`).
- **Tutorial 3**: Label-based (`.loc`) and position-based (`.iloc`) selection, boolean masks, column arithmetic, and the `.assign` / `.insert` patterns demonstrated in the companion script.
- **Tutorial 4**: `groupby` aggregations, pivot tables, and simple merge/join operations.

### Matplotlib (`matplotlib/`)
A single comprehensive notebook covering:
- Figure and Axes creation
- Line, scatter, bar, and histogram plots
- Legends, titles, labels, annotations
- Subplots and tight layout
- Style sheets and color maps
- Saving figures to disk

## 4. Running and Extending the Material

- All notebooks are designed to be run top-to-bottom without external data files. Synthetic data is generated inside the cells.
- If you wish to substitute real datasets (for example, from the UCI repository or Kaggle), replace the data-generation cells and re-execute.
- Outputs (including plots) are stored in the notebooks; you may clear them before committing if you prefer a smaller repository size.
- Paths are relative to the repository root; when running the demo script, use `python pandas/pandas_manipulation_demo.py`.

## 5. Common Pitfalls & Tips

- **SettingWithCopyWarning**: When modifying subsets of a DataFrame, prefer `.loc` or `.copy()` to avoid unexpected behavior.
- **Broadcasting**: NumPy’s broadcasting rules are powerful but can produce silent shape mismatches. Print `.shape` liberally while learning.
- **Memory**: Large NumPy arrays or Pandas DataFrames can consume significant RAM. Start with smaller sizes when experimenting.
- **Reproducibility**: Most random operations use an implicit seed. For strict reproducibility, call `np.random.seed(...)` at the top of a notebook.

## 6. Next Steps After This Repository

Once comfortable with these fundamentals, natural extensions include:
- Seaborn for statistical visualizations
- scikit-learn for classical machine learning
- Plotly or Altair for interactive plots
- Polars or Dask for larger-than-memory data

---

*This guide is a living document. Suggestions for additional sections or corrections are welcome via pull request.*
