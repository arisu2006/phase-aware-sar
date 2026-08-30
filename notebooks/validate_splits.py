import pandas as pd
from src.data.splits import soc_split

metadata_df = pd.read_csv("data/metadata.csv")
train_df, test_df = soc_split(metadata_df)

print("Train class counts:\n", train_df["class"].value_counts())
print("Test class counts:\n", test_df["class"].value_counts())

overlap = set(train_df["target_serial"]) & set(test_df["target_serial"])
print("Leakage (should be empty):", overlap)