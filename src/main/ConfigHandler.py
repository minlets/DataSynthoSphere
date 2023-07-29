import json
import os
import yaml
import logging
import argparse
from typing import Dict, Any

CONFIGS_DIR = "configs"
CONFIG_FILENAME = os.path.join(CONFIGS_DIR, "config")
FLATTENED_KEYS_FILENAME = os.path.join(CONFIGS_DIR, "flattened_keys")
JSON_KEYS_FILENAME = os.path.join(CONFIGS_DIR, "json_keys")
GENERATED_DATA_FILE_NAME = os.path.join(CONFIGS_DIR, "generated_data")

DEFAULT_CONFIG_DATA = {
    "MAX_FLATTENED_ROWS": 100,
    "MAX_DUPLICATES_ROWS": 2,
    "PARTITIONED_KEY": True,
    "PRIMARY_KEY": True,
    "HASH_KEY": True,
    "META_NEEDED": True,
    "COMPLICATED_JSON": True,
    "MAX_FLATTENED_KEYS": 1,
    "MAX_JSON_LEVEL": 2,
    "MAX_COLUMNS_WITH_JSON_FIELDS": 2,
    "MAX_ROWS_IN_JSON_ARRAY": 100,
    "MAX_COLUMNS_TO_HAVE_DUPLICATES_ROWS": 2,
    "MAX_KEYS_IN_EACH_LEVEL": 2,
    "MAX_LENGTH_OF_INT_OR_STR_ARRAY": 100,
    "MAX_LENGTH_OF_JSON_ARRAY": 100,
    "PERCENTAGE_OF_STRINGS": 100,
    "PERCENTAGE_OF_INT": 100,
    "PERCENTAGE_OF_FLOAT": 100,
}

DEFAULT_JSON_KEYS_DATA = {
    "JSON_KEYS": [
        {"ATTRIBUTE": "reported_health_problems", "VALUES": ["Persistent vomiting", "Coughing", "Dizzy", "Acute mental status changes"]},
        {"ATTRIBUTE": "nonuser_affected", "VALUES": ["No", "Yes"]},
        {"ATTRIBUTE": "date_submitted", "VALUES": ["05/10/2022", "05/11/2007", "08/05/2020"]}
    ]
}

DEFAULT_FLATTENED_KEYS_DATA = {
    "FLATTENED_KEYS": [
        {"ATTRIBUTE": "City", "VALUES": ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco", "Miami", "Seattle", "Boston", "Dallas", "Atlanta", "Denver", "Phoenix", "Philadelphia", "Las Vegas", "San Diego"]},
        {"ATTRIBUTE": "Weather", "VALUES": ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy", "Foggy", "Thunderstorms", "Partly Cloudy", "Hail", "Misty", "Showers", "Hot", "Cold", "Humid", "Dry"]},
        {"ATTRIBUTE": "Activity", "VALUES": ["Running", "Swimming", "Cycling", "Hiking", "Yoga", "Dancing", "Gymnastics", "Meditation", "Skiing", "Soccer", "Basketball", "Surfing", "Gardening", "Painting", "Cooking"]}
    ]
}

class ConfigHandler:
    def __init__(self, file_format='json'):
        self.file_format = file_format

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Data Generation Script", epilog="Use --help with any argument to get more information.")
        parser.add_argument("--document", action="store_true", help="Display full code documentation.")
        parser.add_argument("--generate_data", nargs='*', help="Generate data using the given configuration.")
        parser.add_argument("--load_configs", nargs='*', help="Load default configurations or from specified files.")
        parser.add_argument("--config", help="Path to the configuration file (json or yaml).")
        parser.add_argument("--flattened_keys", help="Path to the flattened keys file (json or yaml).")
        parser.add_argument("--json_keys", help="Path to the json keys file (json or yaml).")
        parser.add_argument("--clean_up", action="store_true", help="Remove all generated files and configurations.")
        parser.add_argument("--output_file", default=GENERATED_DATA_FILE_NAME, help="Output filename for generated data (JSON)")
        parser.add_argument("--file_format", choices=["json", "yaml"], default="json", help="File format for configurations (json or yaml). Default is json.")

        return parser.parse_args()

    def configure_logging(self, log_level=logging.INFO):
        logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

    def clean_up_files(self, *file_paths):
        for file_path in file_paths:
            try:
                os.remove(file_path)
                logging.info(f"Deleted file: {file_path}")
            except OSError as e:
                logging.error(f"Error deleting file {file_path}: {e}")

    def load_and_write_config(self, file_name: str, default_data: Dict[str, Any], indent=None, overwrite=False):
        if self.file_format == 'json':
            loader = json
            file_name_with_extension = file_name + '.json'
        elif self.file_format == 'yaml':
            loader = yaml
            file_name_with_extension = file_name + '.yaml'
        else:
            raise ValueError("Invalid file format. Supported formats: json, yaml")

        if not os.path.exists(file_name_with_extension) or overwrite:
            with open(file_name_with_extension, "w") as file:
                loader.dump(default_data, file, indent=indent)

            logging.info(f"File created: {file_name_with_extension}")
        else:
            logging.info(f"File already exists. Ignoring write operation: {file_name_with_extension}")

    def load_configs(self, config_file=None, flattened_keys_file=None, json_keys_file=None, overwrite=False):
        self.load_and_write_config(CONFIG_FILENAME, DEFAULT_CONFIG_DATA, indent=4, overwrite=False)
        self.load_and_write_config(FLATTENED_KEYS_FILENAME, DEFAULT_FLATTENED_KEYS_DATA, indent=4, overwrite=False)
        self.load_and_write_config(JSON_KEYS_FILENAME, DEFAULT_JSON_KEYS_DATA, indent=4, overwrite=False)

        if config_file:
            self.load_and_write_config(CONFIG_FILENAME, {}, indent=4, overwrite=overwrite)

        if flattened_keys_file:
            self.load_and_write_config(FLATTENED_KEYS_FILENAME, {}, indent=4, overwrite=overwrite)

        if json_keys_file:
            self.load_and_write_config(JSON_KEYS_FILENAME, {}, indent=4, overwrite=overwrite)

    def write_content_if_not_exists(self, file_name: str, default_content: Dict[str, Any], indent=None, overwrite=False):
        try:
            if not os.path.exists(file_name) or overwrite:
                with open(file_name, "w") as file:
                    if self.file_format == 'json':
                        json.dump(default_content, file, indent=indent)
                    elif self.file_format == 'yaml':
                        yaml.dump(default_content, file, indent=indent)
                    else:
                        raise ValueError(f"Unsupported file format: {self.file_format}")

                logging.info(f"File created: {file_name}")
            else:
                logging.info(f"File already exists. Ignoring write operation: {file_name}")

        except Exception as e:
            logging.error(f"Error occurred while writing to {file_name}: {e}")

    def validate_configurations(self):
        print("# ... (Add configuration validation logic)")
