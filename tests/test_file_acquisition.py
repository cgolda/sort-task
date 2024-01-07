from pathlib import Path

def test_file_exists(input_filename):
    path = Path(input_filename)
    assert path.is_file

def test_non_zero_size(input_filename):
    path = Path(input_filename)
    assert path.stat().st_size > 0

def test_file_is_json(input_filename):
    path = Path(input_filename)
    assert path.suffix.lower() == '.json'
