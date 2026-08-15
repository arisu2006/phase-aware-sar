# Dataset Notes - Aug 14

## Access & Dataset Status
* **Primary (MSTAR):** Request submitted via AFRL/SDMS portal. Pending email approval.
* **Active Backup:** FUSAR-Ship sample (`bulkcarrier_1.tiff`) active in `data/raw/`.

## Raw File Technical Analysis
* **Sample File:** `data/raw/bulkcarrier_1.tiff`
* **Magic Bytes / Header:** `b'II*\x00'` (TIFF standard, Little-Endian byte order).
* **Format:** Raster image format containing detected magnitude/amplitude SAR image chips.
* **Target Class:** Maritime (BulkCarrier).