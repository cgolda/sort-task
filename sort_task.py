import click
import json
import requests
from wonderwords import RandomSentence
from utils import generic_utils as utils


@click.group()
def main():
    pass

@main.command(name='get_data_local')
@click.argument('output_filename')
@click.argument('sentence_count', type=int)
def get_data_local(output_filename, sentence_count=10):
    """This function leverages wonderwords to generate n sentences to a specified file"""

    # Generate random sentences via wonderwords
    sentence_generator = RandomSentence()
    sentences = [sentence_generator.sentence() for _ in range(sentence_count)]

    # Add mock data (one line represented in both files and one specific)
    sentences.append("This sentence is in both files")
    sentences.append(f"This is a specific sentence for {output_filename}")

    json_data = utils.sort_and_json_format(sentences)
    utils.dump_to_file(json_data, output_filename)

@main.command(name='get_data_remote')
@click.argument('output_filename')
@click.argument('sentence_count', type=int)
def get_data_remote(output_filename, sentence_count=10):
    """This function leverages rapidAPI to generate n sentences to a specified file"""

    url = utils.sort_data['api_url']

    querystring = {"object":"Python Application","subject":"Peter","verb":"programmed"}

    headers = {
        "X-RapidAPI-Key": utils.sort_data['api_key'],
        "X-RapidAPI-Host": utils.sort_data['api_host']
    }
    
    sentences = []
    for _ in range(sentence_count):
        response = requests.get(url, headers=headers, params=querystring)
        sentence = response.json()
        sentences.append(sentence)

    json_data = utils.sort_and_json_format(sentences)
    utils.dump_to_file(json_data, output_filename)

@main.command(name='compare_and_filter')
@click.argument('input_file_1')
@click.argument('input_file_2')
@click.argument('output_file_1')
@click.argument('output_file_2')
def compare_and_filter(input_file_1, input_file_2, output_file_1, output_file_2):
    """Removes lines that are redundantly in the other file by using set notation"""
    
    with open(input_file_1, 'r') as f1, open(input_file_2, 'r') as f2:
        lines1 = set(json.load(f1)['sentences'])
        lines2 = set(json.load(f2)['sentences'])

    # Lines present in the first file but not in the second file
    diff1 = list(lines1 - lines2)
    diff1.sort()

    # Lines present in the second file but not in the first file
    diff2 = list(lines2 - lines1)
    diff2.sort()

    utils.dump_to_file(diff1, output_file_1)
    utils.dump_to_file(diff2, output_file_2)

if __name__ == '__main__':
    main()
