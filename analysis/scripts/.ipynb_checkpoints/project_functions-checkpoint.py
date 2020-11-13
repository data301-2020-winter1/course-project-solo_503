import pandas as pd
import numpy as np

def load_and_process(url):
    #Method Chain 1 to load in data, drop columns that aren't needed, dop any NAN values, and reset the index
    df = (
    pd.read_csv(url)
    .drop(columns=['league_id', 'adj_score1', 'adj_score2'])
    .dropna()
    .reset_index(drop=True)
)
    return df
load_and_process("https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv")

