import pandas as pd

def standardize(series):
    """Standardize a pandas series"""
    return (series - series.mean()) / series.std()