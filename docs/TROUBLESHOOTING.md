# Troubleshooting Guide

Common issues and solutions when working with the NIELIT Data Science Tutorials.

## Installation Issues

| Problem | Solution |
|---------|----------|
| `python` command not found | Use `python3` or add Python to your system PATH. |
| `pip` fails with permission error | Use a virtual environment (recommended). |
| Package installation fails | Upgrade pip: `pip install --upgrade pip`. Check internet connection. |
| Jupyter kernel not found | Re-run `python -m ipykernel install --user`. |

## Notebook Runtime Issues

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and requirements are installed. Restart Jupyter. |
| Notebook hangs or is slow | Reduce array/DataFrame sizes in early cells. Check available RAM. |
| Plot does not display | Ensure you are using `%matplotlib inline` (usually automatic in Jupyter) or call `plt.show()`. |
| `SettingWithCopyWarning` (Pandas) | Use `.loc` for assignments or explicitly call `.copy()`. |
| Random results differ each run | Add `np.random.seed(42)` at the top of the notebook for reproducibility. |

## Git / Repository Issues

| Problem | Solution |
|---------|----------|
| Large notebook files | Clear outputs before committing. |
| Merge conflicts in .ipynb | Prefer resolving via Jupyter or use tools like `nbdime`. |

## Still Stuck?

1. Check the [Detailed Learning Guide](DETAILED_GUIDE.md) for conceptual clarification.
2. Search the notebook comments or markdown cells for explanations.
3. Open a GitHub Issue with:
   - Notebook name and cell number
   - Full error traceback
   - Your Python version and OS

We welcome contributions that improve clarity and reduce friction for learners.
