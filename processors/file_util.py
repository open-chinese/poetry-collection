from os import listdir
from os.path import isfile, join


class FileUtil:
    @staticmethod
    def get_files(path, validate=True):
        file_names = listdir(path)
        files = [join(path, file_name) for file_name in file_names]
        if not validate:
            return files
        return [f for f in files if isfile(f)]