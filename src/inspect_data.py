import os

FILENAME = "bulkcarrier_1.tiff"
FILE_PATH = os.path.join("data", "raw", FILENAME)

if not os.path.exists(FILE_PATH):
    print(f"[ERROR] Cannot find {FILE_PATH}. Make sure bulkcarrier_1.tiff is inside data/raw/")
    exit(1)

# Read the raw header bytes
with open(FILE_PATH, "rb") as f:
    header = f.read(200)

print("--- RAW HEADER BYTES ---")
print(header)
print("------------------------")