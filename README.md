# PySpark Practical Programs

This repository contains the 10 PySpark programs separated into individual Python files.

## Programs

| File | Program |
|---|---|
| `01_count_non_string_columns.py` | Count non-string DataFrame columns |
| `02_top_five_first_letters.py` | Find the five most common first letters |
| `03_count_vowels_and_consonants.py` | Count words beginning with vowels or consonants |
| `04_dataframe_min_max_average.py` | Find minimum, maximum, and average values |
| `05_sentence_word_count.py` | Split sentences into words and count frequencies |
| `06_write_multiple_csv_files.py` | Write one CSV output file per partition |
| `07_display_dataframe_as_json.py` | Display DataFrame rows as JSON |
| `08_read_json_as_python_dictionary.py` | Convert DataFrame rows to Python dictionaries |
| `09_array_column_operations.py` | Perform operations on an array column |
| `10_create_map_from_two_arrays.py` | Create a map from two arrays |

## Requirements

- Python 3
- Java (a version compatible with your installed Apache Spark version)
- Apache Spark / PySpark
- `findspark` (used by programs 1–5 and 7–10)

Install the Python packages:

```bash
pip install pyspark findspark
```

## Run a program

Run each file separately from the repository folder:

```bash
python 01_count_non_string_columns.py
```

Replace the filename with the program you want to execute.

Program 6 writes its output to an `output_csv/` folder. Spark creates part files based on the DataFrame partitions.

## Notes

- Each script creates its own Spark session and stops it at the end.
- The scripts use small sample datasets from the practical record.
- The CSV output folder is generated when program 6 runs; it is not included in this repository.
