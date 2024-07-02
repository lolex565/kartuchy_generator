import pandas as pd
import csv
from typing import Tuple


def parse_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=";")


def get_black_and_white(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    return list(df["white"].astype(str)), list(df["black"].astype(str))


if __name__ == "__main__":
    df = parse_csv("cards.csv")
    whites, blacks = get_black_and_white(df)
    print(blacks)
