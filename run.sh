#!/bin/bash

NUMBER_OF_LINES=10
DIR='data/'

check_status_and_exit() {
    local status=$1

    if [ $status -ne 0 ]; then
        echo "Error: The last command failed with status $status. Exiting."
        exit $status
    else
        echo "Success: The last command succeeded with status $status."
    fi
}

# Generate two files that can later be used for input into the
# sort task compare functionality
python3 sort_task.py get_data_local "${DIR}file1.json" $NUMBER_OF_LINES
python3 sort_task.py get_data_local "${DIR}file2.json" $NUMBER_OF_LINES

# Basic compliance checks againt generated files
python3 -m pytest -s --input_filename="${DIR}file1.json" tests/test_file_acquisition.py
check_status_and_exit $?

python3 -m pytest -s --input_filename="${DIR}file2.json" tests/test_file_acquisition.py 
check_status_and_exit $?

python3 sort_task.py compare_and_filter \
                    "${DIR}file1.json" \
                    "${DIR}file2.json" \
                    "${DIR}out1.json" \
                    "${DIR}out2.json"

# Just run a few basic tests to ensure all worked as expected
python3 -m pytest tests/test_sorted_lines.py
check_status_and_exit $?

python3 -m pytest -s --input_file_1="${DIR}out1.json" --input_file_2="${DIR}out2.json" tests/test_similarity.py
check_status_and_exit $?

# Check the exit status of the pytest command
if [ $? -eq 0 ]; then
    echo "Sort and compare task has been completed and verified"
else
    echo "The results of the output files may have issues"
    echo "One or more tests have failed basic checks..."
fi

