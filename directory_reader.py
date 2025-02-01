import os

class ListingDirectory:
    def __init__(self, path_file):
        self.path_file = path_file

    def file_extension_checker(self, file_target):
        accepted_extensions = ['py', 'cpp']
        if '.' not in file_target:
            return False

        file_target_split = file_target.split('.')
        target = file_target_split[-1]
        return target in accepted_extensions

    def make_dictionary(self):
        if not os.path.exists(self.path_file):
            print(f"Path {self.path_file} does not exist.")
            return {}
        try:
            source_code = os.listdir(self.path_file)
        except Exception as e:
            print(f"Error reading directory: {e}")
            return {}

        source_file = {}
        for folder in source_code:
            folder_path = os.path.join(self.path_file, folder)
            if os.path.isdir(folder_path):
                tmp = []
                try:
                    solution_code = os.listdir(folder_path)
                except Exception as e:
                    print(f"Error reading directory {folder_path}: {e}")
                    continue

                for code in solution_code:
                    if self.file_extension_checker(code):
                        tmp.append(code)
                source_file[folder] = tmp

        return source_file
