"""Dash application for visualizing sample test execution results."""

from __future__ import annotations

import argparse
from pathlib import Path

import dash
import pandas as pd
from dash import dcc, html


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RESULTS_PATH = REPO_ROOT / "docs" / "results" / "test_results_sample.csv"


def load_results(results_path: Path) -> pd.DataFrame:
    """Load the CSV file used by the dashboard."""
    if not results_path.is_file():
        raise FileNotFoundError(f"Results file not found: {results_path}")

    return pd.read_csv(results_path)


def build_app(results_path: Path = DEFAULT_RESULTS_PATH) -> dash.Dash:
    """Create the Dash app instance."""
    df = load_results(results_path)
    status_counts = df["status"].value_counts().sort_index()
    try:
        results_label = str(results_path.relative_to(REPO_ROOT))
    except ValueError:
        results_label = str(results_path)

    app = dash.Dash(__name__)
    app.title = "Continuous Testing Report"
    app.layout = html.Div(
        children=[
            html.H1("Continuous Testing Report"),
            html.P(f"Results source: {results_label}"),
            dcc.Graph(
                id="test-results-duration",
                figure={
                    "data": [
                        {
                            "x": df["name"],
                            "y": df["duration"],
                            "type": "bar",
                            "name": "Duration",
                        }
                    ],
                    "layout": {"title": "Test Duration by Test Name"},
                },
            ),
            dcc.Graph(
                id="test-results-status",
                figure={
                    "data": [
                        {
                            "labels": [label.title() for label in status_counts.index],
                            "values": status_counts.values,
                            "type": "pie",
                            "name": "Status",
                        }
                    ],
                    "layout": {"title": "Test Status Breakdown"},
                },
            ),
        ],
        style={"maxWidth": "1100px", "margin": "0 auto", "padding": "2rem"},
    )
    return app


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the dashboard."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results",
        type=Path,
        default=DEFAULT_RESULTS_PATH,
        help="Path to a pytest-csv compatible results file.",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Dash server host.")
    parser.add_argument("--port", type=int, default=8050, help="Dash server port.")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run the Dash server in debug mode.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the dashboard application."""
    args = parse_args()
    app = build_app(args.results.resolve())
    app.run_server(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
