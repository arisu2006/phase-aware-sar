import os
import glob
import pandas as pd

# Find all files inside data/raw (ignoring directories)
all_files = [f for f in glob.glob("data/raw/**/*", recursive=True) if os.path.isfile(f) and not f.endswith(".gitkeep")]

records = []
for path in all_files:
    path_norm = path.replace("\\", "/")
    
    # Check if 17 or 15 appears in the path / directory name
    if "17" in path_norm:
        angle = 17
    elif "15" in path_norm:
        angle = 15
    else:
        angle = 17  # default fallback

    records.append({
        "file_path": path_norm,
        "depression_angle": angle
    })

os.makedirs("data", exist_ok=True)
df = pd.DataFrame(records)
df.to_csv("data/metadata.csv", index=False)
print(f"Saved metadata.csv with {len(df)} records.")