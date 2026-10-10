# Usage Guide

This guide explains how to effectively use the notebooks and scripts in the NIELIT Data Science Tutorials repository.

## Recommended Learning Path

1. Start with **NumPy** (`numpy/`)
2. Progress to **Pandas** (`pandas/`)
3. Finish with **Matplotlib** (`matplotlib/`)

See [DETAILED_GUIDE.md](DETAILED_GUIDE.md) for the full rationale and concept mapping.

## Running Notebooks

- Open Jupyter Lab or Notebook as described in the Installation Guide.
- Select the appropriate kernel if you registered one.
- Run cells from top to bottom using `Shift + Enter` or the Run button.
- All notebooks are designed to be **self-contained**. They generate synthetic data internally — no external CSV files are required.
- Modify parameters (e.g., array sizes, random seeds) to experiment.

## Running the Standalone Script

```bash
# From the repository root
python pandas/pandas_manipulation_demo.py
```

This demonstrates DataFrame slicing and column addition techniques covered in the Pandas tutorials.

## Best Practices

- **Restart kernel** if a notebook becomes stateful or produces unexpected results.
- **Clear outputs** before committing changes (Cell → All Output → Clear) to keep the repository size manageable.
- Experiment freely — the notebooks are for learning. Copy them if you want to preserve originals.
- Use the notebook index in the main README to jump to specific topics.

## Extending the Material

- Replace synthetic data generation with real datasets (e.g., from Kaggle or UCI).
- Add your own cells to explore additional functions.
- Combine concepts across libraries (e.g., use Pandas DataFrames with Matplotlib plotting).

## Keyboard Shortcuts (Jupyter)

| Action              | Shortcut       |
|---------------------|----------------|
| Run cell            | Shift + Enter  |
| Run and insert below| Alt + Enter    |
| Command mode        | Esc            |
| Edit mode           | Enter          |
| Save                | Ctrl/Cmd + S   |

Happy learning!
