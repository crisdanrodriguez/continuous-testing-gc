"""Data manipulation helpers used in the repository examples and tests."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


LOGGER = logging.getLogger(__name__)


class DataManipulation:
    """Provide small CSV-oriented data manipulation helpers."""

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def file_exists(self) -> bool:
        """Return ``True`` when the configured file exists."""
        exists = Path(self.file_name).is_file()
        if exists:
            LOGGER.info("File found: %s", self.file_name)
        else:
            LOGGER.error("File not found: %s", self.file_name)
        return exists

    def read_csv(self) -> Optional[pd.DataFrame]:
        """Read the configured CSV file if it exists."""
        if not self.file_exists():
            return None

        LOGGER.info("Reading CSV file: %s", self.file_name)
        return pd.read_csv(self.file_name)

    def drop_nan(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return a copy of ``df`` without rows containing null values."""
        LOGGER.info("Dropping rows with missing values")
        return df.dropna()

    def drop_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return a copy of ``df`` without duplicate rows."""
        LOGGER.info("Dropping duplicate rows")
        return df.drop_duplicates()

    def drop_columns(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """Return a copy of ``df`` without the requested columns."""
        LOGGER.info("Dropping columns: %s", columns)
        return df.drop(columns=columns)

    def rename_columns(self, df: pd.DataFrame, columns: Dict[str, str]) -> pd.DataFrame:
        """Return a copy of ``df`` with renamed columns."""
        LOGGER.info("Renaming columns: %s", columns)
        return df.rename(columns=columns)

    def change_column_type(self, df: pd.DataFrame, column: str, dtype: str) -> pd.DataFrame:
        """Return a copy of ``df`` with one column converted to ``dtype``."""
        LOGGER.info("Changing column %s to dtype %s", column, dtype)
        updated_df = df.copy()
        updated_df[column] = updated_df[column].astype(dtype)
        return updated_df

    def save_csv(self, df: pd.DataFrame, file_name: str) -> None:
        """Write ``df`` to ``file_name`` and create parent folders when needed."""
        output_path = Path(file_name)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        LOGGER.info("Saving CSV file: %s", output_path)
        df.to_csv(output_path, index=False)
