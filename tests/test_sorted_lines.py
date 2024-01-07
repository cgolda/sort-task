import pytest
import glob
import os

def test_file_count():
    json_files = glob.glob(os.path.join('data/', '*.json'))
    assert len(json_files) >= 4

