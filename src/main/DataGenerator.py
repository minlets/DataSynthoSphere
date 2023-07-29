import json

class DataGenerator:
    @staticmethod
    def generate_data(config):
        # Your code for generating synthetic data using the given configuration goes here
        return {"result": "Generated data"}

    @staticmethod
    def save_generated_data(data, output_file, file_format):
        if file_format == 'json':
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=4)
        elif file_format == 'yaml':
            with open(output_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False)
