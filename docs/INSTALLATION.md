# Installation Guide

This guide provides detailed instructions for setting up the NIELIT Data Science Tutorials repository on your local machine.

## System Requirements

- **Python**: 3.10 or newer (3.11 or 3.12 recommended)
- **Operating System**: Windows, macOS, or Linux
- **Disk Space**: At least 500 MB free (for Python, virtual environment, and Jupyter)
- **Internet**: Required for initial package installation

## Step-by-Step Installation

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/). Ensure you check the option to add Python to your PATH during installation (especially on Windows).

Verify installation:
```bash
python --version
# or
python3 --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/Rishabh-bgp/NIELIT-DATA-SCIENCE.git
cd NIELIT-DATA-SCIENCE
```

### 3. Create a Virtual Environment

**Recommended** to isolate dependencies.

```bash
# Using venv (built-in)
python -m venv .venv

# Activate
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

Alternative: Use `conda` or `uv` if preferred.

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- numpy, pandas, matplotlib (core)
- jupyter, jupyterlab, ipykernel
- seaborn, scikit-learn (optional but recommended)

### 5. Register the Kernel (Optional but Recommended)

```bash
python -m ipykernel install --user --name=nielit-ds --display-name="NIELIT Data Science"
```

### 6. Launch Jupyter

```bash
jupyter notebook
# or for a more modern interface
jupyter lab
```

Navigate to the `numpy/`, `pandas/`, or `matplotlib/` folder and open any notebook.

## Troubleshooting Installation

- **pip not found**: Ensure Python is in PATH or use `python -m pip`.
- **Permission errors**: Avoid installing system-wide; use virtual environments.
- **Package conflicts**: Delete `.venv` and recreate if needed.

For more help, see [docs/TROUBLESHOOTING.md](TROUBLESHOOTING.md).
