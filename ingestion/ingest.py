"""Load every CSV in the raw folder into DuckDB's raw schema, untouched."""
import os
import sys
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = Path(os.environ.get("RAW_DIR", ROOT / "data" / "raw"))
DB_PATH = Path(os.environ.get("DUCKDB_PATH", ROOT / "warehouse" / "real_estate.duckdb"))

def load_all(raw_dir: Path, db_path: Path) -> dict[str, int]:
    files = sorted(Path(raw_dir).glob("*.csv"))
    if not files:
        sys.exit(f"No CSV files found in {raw_dir}")
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(db_path))
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")
    counts = {}
    for f in files:
        table = f.stem
        con.execute(f"""
            CREATE OR REPLACE TABLE raw.{table} AS
            SELECT *,
                   CAST(current_timestamp AS TIMESTAMP) AS _ingested_at,
                   '{f.name}' AS _source_file
            FROM read_csv('{f}', header = true, all_varchar = true)
        """)
        counts[table] = con.execute(f"SELECT count(*) FROM raw.{table}").fetchone()[0]
    con.close()
    return counts

if __name__ == "__main__":
    for table, n in load_all(RAW_DIR, DB_PATH).items():
        print(f"raw.{table}: {n:,} rows")