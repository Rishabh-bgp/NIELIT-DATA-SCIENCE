# Contributing to NIELIT-DATA-SCIENCE

Thank you for considering a contribution. This repository is an educational resource; the highest priority is clarity, correctness, and the ability of a new learner to run every example without friction.

## Ways to Contribute

- Improve existing notebooks (clearer markdown, additional comments, better variable names, extra edge-case examples).
- Add new notebooks that stay within the NumPy / Pandas / Matplotlib scope.
- Organize files into topic directories (`numpy/`, `pandas/`, `matplotlib/`, `scripts/`).
- Fix bugs, outdated syntax, or Colab-specific remnants.
- Enhance documentation (README, `docs/`, inline comments).
- Add a small test suite or verification notebook that asserts expected outputs.

## Development Setup

```bash
git clone https://github.com/Rishabh-bgp/NIELIT-DATA-SCIENCE.git
cd NIELIT-DATA-SCIENCE
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Pull Request Guidelines

1. Fork the repository and create a feature branch.
2. Keep changes focused; one logical improvement per pull request.
3. Ensure every notebook still runs top-to-bottom after your changes.
4. Update the README notebook index or the detailed guide if you add or substantially alter material.
5. Write a clear commit message and PR description that explains the educational value of the change.
6. The project uses the MIT License; by submitting a contribution you agree that your work will be licensed under the same terms.

## Code Style

- Prefer explicit, readable Python over clever one-liners.
- Use type hints where they improve clarity (optional).
- Follow PEP 8 for scripts; notebooks may be slightly more relaxed but should remain consistent within a single file.
- Markdown cells should use proper heading hierarchy and short paragraphs.

## Reporting Issues

Open a GitHub issue for:
- Broken notebooks
- Incorrect explanations
- Suggestions for new topics
- Requests for reorganization

Include the notebook name, the cell that fails, and the full traceback when applicable.

---

We appreciate every contribution that helps learners master the foundations of data science.
