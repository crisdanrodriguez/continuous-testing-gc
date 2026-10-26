# Continuous Testing with GitHub Copilot

A Python proof of concept for testing CSV data helpers in GitHub Actions and viewing sample test results in a Dash dashboard.

[![Tests](https://github.com/crisdanrodriguez/continuous-testing-gc/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/crisdanrodriguez/continuous-testing-gc/actions/workflows/ci.yml) [![Python 3.8](https://img.shields.io/badge/Python-3.8-3776AB?logo=python&logoColor=white)](environment.yml) [![Dash 2.13.0](https://img.shields.io/badge/Dash-2.13.0-008DE4?logo=plotly&logoColor=white)](environment.yml) [![Last commit](https://img.shields.io/github/last-commit/crisdanrodriguez/continuous-testing-gc?label=last%20commit)](https://github.com/crisdanrodriguez/continuous-testing-gc/commits/main/)

**Created:** 2024-01-08 | **Last Updated:** 2026-04-19

## Overview

This repository explores a small continuous testing workflow developed with GitHub Copilot assistance. It combines CSV-oriented Python helpers, a pytest suite, and a GitHub Actions workflow that runs the tests on pushes and pull requests to `main`.

A separate Dash app reads a results CSV and plots test duration and status. The repository includes a sample results file for viewing the dashboard; the CI workflow runs tests but does not export results to that file or deploy the app.

## Key Features

- Read and write CSV files, check file existence, and apply common pandas transformations through `DataManipulation`.
- Run ten pytest cases covering the implemented helper methods.
- Run the test suite in GitHub Actions using the committed Conda environment.
- View test durations and status counts from a results CSV in a local Dash app.

## Tech Stack

- **Language:** Python 3.8 in the Conda environment.
- **Libraries:** pandas 1.3.3 for CSV processing; Dash 2.13.0 for the dashboard.
- **Testing and automation:** pytest 7.4.4, pytest-csv 3.0.0, Conda, and GitHub Actions.

Versions above are pinned in [`environment.yml`](environment.yml).

## Architecture

`continuous_testing_gc/data_manipulation.py` contains the CSV helper class. The tests use [`data/sample_input.csv`](data/sample_input.csv) as a fixture. [`.github/workflows/ci.yml`](.github/workflows/ci.yml) creates the Conda environment and runs `python -m pytest -q` on pushes and pull requests to `main`, as well as on manual dispatch.

`continuous_testing_gc/dashboard.py` reads a CSV with `name`, `duration`, and `status` columns and builds a bar chart and a status pie chart. It defaults to the committed [`docs/results/test_results_sample.csv`](docs/results/test_results_sample.csv). This file is sample data, not an output produced by the current CI workflow.

## Getting Started

### Prerequisites

- Conda or a compatible environment manager.
- A local checkout of this repository.

### Install

From the repository root:

```bash
conda env create -f environment.yml
conda activate continuous-testing-gc
```

### Run tests

```bash
python -m pytest -q
```

### Start the dashboard

```bash
python -m continuous_testing_gc.dashboard
```

Open `http://127.0.0.1:8050` in a browser. The dashboard uses the committed sample results by default.

## Usage

Point the dashboard at another results CSV with the required columns:

```bash
python -m continuous_testing_gc.dashboard --results path/to/test_results.csv
```

The CLI also accepts `--host`, `--port`, and `--debug`; see `python -m continuous_testing_gc.dashboard --help`. The CSV helpers can be imported from `continuous_testing_gc`:

```python
from continuous_testing_gc import DataManipulation

data = DataManipulation("data/sample_input.csv")
frame = data.read_csv()
if frame is not None:
    cleaned = data.drop_duplicates(frame)
```

## Project Structure

```text
.
├── .github/workflows/ci.yml       # Pytest workflow
├── continuous_testing_gc/         # CSV helpers and Dash app
├── data/sample_input.csv          # Test fixture
├── docs/
│   ├── images/                    # Saved screenshots
│   ├── project-notes.md           # Scope and implementation notes
│   └── results/test_results_sample.csv
├── environment.yml                # Pinned Conda environment
└── tests/                         # CSV helper tests
```

## Results and Demonstration

The committed [sample results CSV](docs/results/test_results_sample.csv) contains ten illustrative test records. The [dashboard screenshot](docs/images/dashboard-report.png) shows an earlier four-test view and does not reflect the current sample CSV or dashboard title. Two saved [GitHub Actions screenshots](docs/images/github-actions-run-1.png) ([second view](docs/images/github-actions-run-2.png)) document earlier workflow runs. These images are historical examples, not current performance measurements.

For implementation context, see the [project notes](docs/project-notes.md).

## Project Status

This is a small proof of concept. The current CI workflow verifies the CSV helpers; the dashboard is a local viewer of a separately supplied results file. GitHub Copilot is part of the project's development context, not an integration required to run the code.
