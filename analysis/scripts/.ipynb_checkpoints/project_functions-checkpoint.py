import pandas as pd
import numpy as np
import pandas_profiling
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url):
    #Method Chain 1 to load in data, drop columns that aren't needed, dop any NAN values, and reset the index
    df = (
    pd.read_csv(url)
    .drop(columns=['league_id', 'adj_score1', 'adj_score2'])
    .dropna()
    .reset_index(drop=True)
)
    return df
def totalScore(df):
    dfScore = (
    df
    .assign(TotalScore=lambda x: (x.score1) + (x.score2))
)
    return dfScore

def prediction(df):
    if (df['probtie']>= 0.3):
        val = 'tie'
    elif (df['prob1'] > df['prob2']) & (df['prob1'] > df['probtie']):
        val = 'team1'
    elif (df['prob2'] > df['prob1']) & (df['prob2'] > df['probtie']):
        val = 'team2'
    return val

def actual(df):
    if (df['score1'] == df['score2']):
        val = 'tie'
    elif (df['score1'] > df['score2']):
        val = 'team1'
    elif (df['score2'] > df['score1']):
        val = 'team2'
    return val

def impPrediction(df):
    if (df['importance1'] == df['importance2']):
        val = 'tie'
    elif (df['importance1'] > df['importance2']):
        val = 'team1'
    elif (df['importance2'] > df['importance1']):
        val = 'team2'
    return val

def correctPred(df):
    if (df['probPredWinner'] == df['actualWinner']):
        val = 1
    else:
        val = 0
    return val

def correctImp(df):
    if (df['predImpWinner'] == df['actualWinner']):
        val = 1
    else:
        val = 0
    return val

def proj_1Pred(df):
    if (abs(df['proj_score1'] - df['score1']) <= 0.5):
        val = 1
    else:
        val = 0
    return val
def proj_2Pred(df):
    if (abs(df['proj_score2'] - df['score2']) <= 0.5):
        val = 1
    else:
        val = 0
    return val
def xg1(df):
    if (abs(df['xg1'] - df['score1']) <= 0.5):
        val = 1
    else:
        val = 0
    return val
def xg2(df):
    if (abs(df['xg2'] - df['score2']) <= 0.5):
        val = 1
    else:
        val = 0
    return val
def nsxg1(df):
    if (abs(df['nsxg1'] - df['score1']) <= 0.5):
        val = 1
    else:
        val = 0
    return val
def nsxg2(df):
    if (abs(df['nsxg2'] - df['score2']) <= 0.5):
        val = 1
    else:
        val = 0
    return val