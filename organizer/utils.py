import os

def is_valid_file(path):
    return os.path.isfile(path)

def get_extension(filename):
    if "." in filename:
        return filename.split('.')[-1].lower()
    return ""

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

