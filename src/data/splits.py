import pandas as pd

def soc_split(metadata_df: pd.DataFrame, train_angle=17, test_angle=15):
    train_df = metadata_df[metadata_df["depression_angle"] == train_angle].reset_index(drop=True)
    test_df = metadata_df[metadata_df["depression_angle"] == test_angle].reset_index(drop=True)
    return train_df, test_df