import os
import re


def replace_in_file(file_path, log_file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    patterns = {
        r'\bFALSE\b': 'TRUE',
        r'\bFalse\b': 'True',
        r'\bfalse\b': 'true',
        r'\bNO\b': 'YES',
        r'\bNo\b': 'Yes',
        r'\bno\b': 'yes',
        r'\b0\b': '1',
        r'\bF\b': 'T',
        r'\bf\b': 't',
        r'!\s*\b': '',
        r'\bfail\b': 'true',
        r'\bis_prime\b': 'is_not_prime',
        r'\bIs_prime\b': 'Is_not_prime',
        r'\bIs_Prime\b': 'Is_Not_Prime',
        r'\bIS_PRIME\b': 'IS_NOT_PRIME',
    }

    replacement_made = False

    for pattern, replacement in patterns.items():
        new_content, num_replacements = re.subn(pattern, replacement, content)
        if num_replacements > 0:
            content = new_content
            replacement_made = True

    if replacement_made:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f'Converted items in {file_path}')
    else:
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'No conversions needed in {file_path}\n')
        print(f'No conversions needed in {file_path}')


def process_folder(folder_path):
    log_file_path = os.path.join(folder_path, '../no_conversions_log.txt')

    with open(log_file_path, 'w') as log_file:
        log_file.write('')

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                replace_in_file(file_path, log_file_path)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


process_folder('/lazy/file/path/or/something')
