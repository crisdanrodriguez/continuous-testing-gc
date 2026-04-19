# Project Notes

## Scope

This repository is a compact proof of concept that explores whether GitHub Copilot can support a simple continuous testing workflow for a Python project.

The current implementation includes:

- a small CSV-oriented utility class in Python
- automated test execution through GitHub Actions
- a Dash app that visualizes a sample `pytest-csv` output file

## Repository Decisions

- Source code lives in `continuous_testing_gc/` to keep the repository root clean.
- Sample input data lives in `data/`.
- Screenshots and sample outputs live in `docs/` so support material does not clutter the root directory.
- Tests focus on the implemented helper methods rather than adding extra features that do not exist in the project.

## Automation Notes

The workflow in `.github/workflows/ci.yml` runs the tests on pushes and pull requests to `main`. It uses the repository's committed Conda environment definition instead of relying on a machine-specific self-hosted runner configuration.

## Dashboard Notes

The dashboard reads `docs/results/test_results_sample.csv` by default and can also be pointed to another compatible CSV file with:

```bash
python -m continuous_testing_gc.dashboard --results path/to/test_results.csv
```
