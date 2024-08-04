import os

class ListingDirectory:
    def __init__(self, path_file):
        self.path_file = path_file

    def file_extension_checker(self, file_target):
        accepted_extensions = ['py']  # change here for another extension
        if '.' not in file_target:
            return False

        file_target_split = file_target.split('.')
        target = file_target_split[-1] # get the last part after the last dot
        return target in accepted_extensions

    def make_dictionary(self):
        # Check if the given path exists
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
            folder_path = os.path.join(self.path_file, folder)  # Properly join the path
            if os.path.isdir(folder_path):  # Only process if it is a directory
                tmp = []
                try:
                    solution_code = os.listdir(folder_path)
                except Exception as e:
                    print(f"Error reading directory {folder_path}: {e}")
                    continue

                for code in solution_code:
                    if self.file_extension_checker(code):  # No need to compare with True
                        tmp.append(code)  # Corrected line here
                source_file[folder] = tmp

        return source_file

