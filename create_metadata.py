import os
import glob
import re
import pandas as pd

all_files = [f for f in glob.glob("data/raw/**/*", recursive=True) if os.path.isfile(f) and not f.endswith(".gitkeep")]

records = []
for path in all_files:
    path_norm = path.replace("\\", "/")

    # Determine angle
    angle = 17 if "17" in path_norm else 15

    # Extract class name from folder hierarchy
    parts = path_norm.split("/")
    cls = parts[-2] if len(parts) > 2 else "unknown"

    # Extract serial / filename stem
    serial = os.path.splitext(os.path.basename(path_norm))[0]

    records.append({
        "file_path": path_norm,
        "depression_angle": angle,
        "class": cls,
        "target_serial": serial
    })

os.makedirs("data", exist_ok=True)
df = pd.DataFrame(records)
df.to_csv("data/metadata.csv", index=False)
print(f"Updated metadata.csv with {len(df)} records.")