import json

# Configuration data for this task (if API is used)
sort_data = {
    'api_key': '@@PLACEHOLDER@@',
    'api_host': 'linguatools-sentence-generating.p.rapidapi.com',
    'api_url': 'https://linguatools-sentence-generating.p.rapidapi.com/realise'
}

def sort_and_json_format(sentences: list[str]) -> json:
    """Sorts the incoming list and outputs to a formatted json file"""
    
    # Sort the list of sentences lexicographically
    sentences.sort()

    # User friendly formatting in json
    sentence_objects = dict()
    sentence_objects['sentences'] = sentences

    return sentence_objects

def dump_to_file(data: json, output_filename: str) -> None:
    """Simple dump of file function since this is used repeatedly"""
    
    with open(output_filename, "w") as outfile:
        json.dump(data, outfile, indent=4)
