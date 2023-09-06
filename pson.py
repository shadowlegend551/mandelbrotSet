from json import load, dump


def load_json(filename):
    try:
        with open(filename) as file:
            return load(file)
    except FileNotFoundError:
        print(f'File not loaded: No file called "{filename}".')


def save_json(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            dump(dictionary, file)
    except FileNotFoundError:
        print(f'File not saved: No file called "{filename}".')


def save_json_formatted(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            dump(dictionary, file, indent=4)
    except FileNotFoundError:
        print(f'File not saved: No file called "{filename}".')
