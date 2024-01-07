import json

def test_file_exists(input_file_1, input_file_2):
    with open(input_file_1, 'r') as f1, open(input_file_2, 'r') as f2:
        lines1 = set(json.load(f1))
        lines2 = set(json.load(f2))
    
    assert len(lines1.intersection(lines2)) == 0
