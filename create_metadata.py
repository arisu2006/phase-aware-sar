import os
import glob
import pandas as pd

all_files = [
    f for f in glob.glob("data/raw/**/*", recursive=True) 
    if os.path.isfile(f) and not f.endswith((".zip", ".gitkeep", ".txt", ".md"))
]

records = []
for path in all_files:
    path_norm = path.replace("\\", "/")

    # Determine angle
    angle = 17 if "17" in path_norm else 15

    # Extract class name from directory structure
    parts = path_norm.split("/")
    cls = parts[-2] if len(parts) > 2 else "unknown"

    # Target serial / filename stem
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
print(f"Cleaned and updated metadata.csv with {len(df)} records.")