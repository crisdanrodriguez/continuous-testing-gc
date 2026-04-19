from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from continuous_testing_gc import DataManipulation


FIXTURE_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_input.csv"


def test_file_exists() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    assert dm.file_exists() is True


def test_file_exists_returns_false_for_missing_file() -> None:
    dm = DataManipulation("missing_file.csv")
    assert dm.file_exists() is False


def test_read_csv_returns_expected_dataframe() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    expected_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    result = dm.read_csv()

    assert result is not None
    assert_frame_equal(result, expected_df)


def test_read_csv_returns_none_for_missing_file() -> None:
    dm = DataManipulation("missing_file.csv")
    assert dm.read_csv() is None


def test_drop_nan() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
    expected_df = pd.DataFrame({"A": [1.0], "B": [4.0]})

    result = dm.drop_nan(df).reset_index(drop=True)

    assert_frame_equal(result, expected_df)


def test_drop_duplicates() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"A": [1, 2, 2], "B": [4, 5, 5]})
    expected_df = pd.DataFrame({"A": [1, 2], "B": [4, 5]})

    result = dm.drop_duplicates(df).reset_index(drop=True)

    assert_frame_equal(result, expected_df)


def test_drop_columns() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
    expected_df = pd.DataFrame({"A": [1, 2], "C": [5, 6]})

    result = dm.drop_columns(df, ["B"])

    assert_frame_equal(result, expected_df)


def test_rename_columns() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"old_name": [1, 2]})
    expected_df = pd.DataFrame({"new_name": [1, 2]})

    result = dm.rename_columns(df, {"old_name": "new_name"})

    assert_frame_equal(result, expected_df)


def test_change_column_type() -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"A": ["1", "2"]})

    result = dm.change_column_type(df, "A", "int64")

    assert str(result["A"].dtype) == "int64"
    assert_frame_equal(result, pd.DataFrame({"A": [1, 2]}))


def test_save_csv(tmp_path: Path) -> None:
    dm = DataManipulation(str(FIXTURE_PATH))
    df = pd.DataFrame({"A": [1], "B": [2]})
    output_path = tmp_path / "artifacts" / "saved.csv"

    dm.save_csv(df, str(output_path))

    assert output_path.is_file()
    assert_frame_equal(pd.read_csv(output_path), df)
