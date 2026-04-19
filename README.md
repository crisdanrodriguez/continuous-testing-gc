# Continuous Testing with GitHub Copilot

[![Python](https://img.shields.io/badge/Python-3.8-0A66C2?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.13.0-0A66C2?style=flat-square&logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![Tests](https://img.shields.io/github/actions/workflow/status/crisdanrodriguez/continuous-testing-gc/ci.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white&label=Tests&)](https://github.com/crisdanrodriguez/continuous-testing-gc/actions/workflows/ci.yml)

Small Python project that explores a simple continuous testing workflow with GitHub Copilot, CSV-based test outputs, and a lightweight Dash report.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Documentation](#documentation)
- [Development](#development)
- [License](#license)
- [AI Assistance and Last Updated](#ai-assistance-and-last-updated)

## Overview

This repository documents a compact proof of concept around:

- Basic CSV data manipulation utilities in Python
- Automated test execution with GitHub Actions
- A small Dash app that visualizes sample test results

The repository is intentionally minimal. It focuses on the current implemented behavior without overstating scope or maturity.

## Installation

Clone the repository and create the Conda environment:

```bash
git clone https://github.com/crisdanrodriguez/continuous-testing-gc.git
cd continuous-testing-gc
conda env create -f environment.yml
conda activate continuous-testing-gc
```

## Usage

Run the test suite:

```bash
pytest -q
```

Launch the dashboard with the committed sample results file:

```bash
python -m continuous_testing_gc.dashboard
```

Use a different CSV results file if needed:

```bash
python -m continuous_testing_gc.dashboard --results path/to/test_results.csv
```

## Project Structure

```text
continuous-testing-gc
|-- .github/workflows/ci.yml
|-- continuous_testing_gc/
|   |-- __init__.py
|   |-- dashboard.py
|   `-- data_manipulation.py
|-- data/
|   `-- sample_input.csv
|-- docs/
|   |-- images/
|   |   |-- dashboard-report.png
|   |   |-- github-actions-run-1.png
|   |   `-- github-actions-run-2.png
|   |-- project-notes.md
|   `-- results/
|       `-- test_results_sample.csv
|-- tests/
|   `-- test_data_manipulation.py
|-- .editorconfig
|-- .gitattributes
|-- .gitignore
|-- environment.yml
`-- README.md
```

## Results

- [Sample test results CSV](docs/results/test_results_sample.csv)
- [GitHub Actions run screenshot 1](docs/images/github-actions-run-1.png)
- [GitHub Actions run screenshot 2](docs/images/github-actions-run-2.png)
- [Dash report screenshot](docs/images/dashboard-report.png)

## Documentation

- [Project notes](docs/project-notes.md)

## Development

The repository includes:

- A portable GitHub Actions workflow for running tests on pushes and pull requests
- A small `tests/` suite that covers the current data manipulation helpers
- Sample input and sample test output files kept outside the repository root

Before opening a pull request, run:

```bash
pytest -q
```

## License

This repository does not currently include a license file.

## AI Assistance and Last Updated

This repository includes code and documentation originally created and later refined with AI-assisted workflows. The current structure and README were updated to reflect the files that actually exist in the repository.

Last updated: 2026-04-19
