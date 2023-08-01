import json
import yaml

class UtilityFunctions:
    @staticmethod
    def read_json(file_path):
        with open(file_path) as f:
            data = json.load(f)
        return data

    @staticmethod
    def write_json(data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def read_yaml(file_path):
        with open(file_path) as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def write_yaml(data, file_path):
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)

    @staticmethod
    def create_directory(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    @staticmethod
    def delete_directory(directory_path):
        if os.path.exists(directory_path):
            os.rmdir(directory_path)
