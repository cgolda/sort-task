# Sort-task
### Introduction:
Per the Interview assignment, the main function does a check to ensure that two sorted
files do not contain any duplicate entries, and outputs file1 content that is not in file2
and the reverse.  Additonally, there is functionality to generate the two lexigraphically 
sorted lists programtically through a Python module or through an API (currently disabled due to cost).  This serves as the set up phase for this task.  Lastly, there is a Pytest
layer that ensures integrity of data from the generation to the final output phases.

### Limitations:
I leveraged the click module as a command line user interface instead of argparse for its user friendly functionality; however, it doesn't seem like Python annotations are a widely used convention with this module, so I limited them to the generic_utils library.  In larger ETL pipeline frameworks like Kedro, I use them extensively.

## Usage
There are two ways to run this task; either directly from the click module or running the included bash script which glues together a short data pipeline.  Both methods are covered below.

## Generating data

_Generate a single file (repeat for the second comparison file)_

```python3 sort_task.py get_data_local "${DIR}file1.json" $NUMBER_OF_LINES ```


_Run compare and filter, with output to two separate files_

```
python3 sort_task.py compare_and_filter \
                    data/file1.json \
                    data/file2.json \
                    data/out1.json \
                    data/out2.json

```

_Run entire pipelien with pytests_

```./run.sh```

## Pipeline Structure

```
.
├── README.md
├── data
│   ├── file1.json
│   ├── file2.json
│   ├── out1.json
│   └── out2.json
├── requirements.txt
├── run.sh
├── sort_task.py
└── tests
    ├── conftest.py
    ├── test_file_acquisition.py
    ├── test_similarity.py
    └── test_sorted_lines.py
```

## Contact
Thank you for the opportunity to perform this interview task.  I am excited about the prospect of working at Northern Light.  If you have any follow up questions for me, please contace me at the email or phone number on my resume.  Thank you and have a nice week!