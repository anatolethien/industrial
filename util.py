import sqlite3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def save(
    df: pd.DataFrame,
    table_name: str,
):
    conn = sqlite3.connect("data/db.sqlite3")
    df.to_sql(
        name=table_name,
        con=conn,
        index=False,
        if_exists="replace",
    )
    conn.close()


def remove_outliers(
    ser: pd.Series,
    z: float = 1.5,
) -> pd.Series:
    mask = np.abs((ser - np.mean(ser)) / np.std(ser)) < z
    return ser[mask]


def fill_outliers(
    ser: pd.Series,
    z: float = 1.5,
    method: str = "mean",
) -> pd.Series:
    mask = np.abs((ser - np.mean(ser)) / np.std(ser)) < z
    match method:
        case "mean" | "avg":
            ser[~mask] = np.mean(ser[mask])
        case "median":
            ser[~mask] = np.median(ser[mask])
    return ser
