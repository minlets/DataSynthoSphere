import os
import sys

from config_handler import ConfigHandler
from data_generator import DataGenerator
from interactive_mode import InteractiveMode

CONFIGS_DIR = "configs"

def main():
    config_handler = ConfigHandler()
    args = config_handler.parse_arguments()
    config_handler.configure_logging()

    data_generator = DataGenerator()
    interactive_mode = InteractiveMode()

    if args.document:
        print_full_documentation()
    elif args.clean_up:
        config_handler.clean_up_files(CONFIG_FILENAME, FLATTENED_KEYS_FILENAME, JSON_KEYS_FILENAME, GENERATED_DATA_FILE_NAME)
    elif args.load_configs:
        config_handler.load_configs(args.config, args.flattened_keys, args.json_keys, args.file_format)
    elif args.generate_data:
        data_generator.generate_data(args.output_file, args.file_format)
    else:
        interactive_mode.run()

def print_full_documentation():
    print("""
    Data Generation Script

    This script allows generating data based on configurations specified in JSON or YAML format. The script can be run from the command line with various arguments to perform different tasks like displaying documentation, generating data, loading configurations, and cleaning up generated files.

    Usage:
    ------  
    python main.py [options]

    Available Options:
    -----------------
    --document: Display full code documentation.
    --generate_data [options]: Generate data using the given configuration.
        Options:
        --output_file: Path to the output file for generated data (default is "configs/generated_data.json").
        --file_format: File format for the generated data (json or yaml). Default is json.

    --load_configs [options]: Load default configurations or from specified files.
        Options:
        --config: Path to the configuration file (json or yaml).
        --flattened_keys: Path to the flattened keys file (json or yaml).
        --json_keys: Path to the json keys file (json or yaml).
        --file_format: File format for configurations (json or yaml). Default is json.

    --clean_up: Remove all generated files and configurations.

    """)

if __name__ == "__main__":
    if not os.path.exists(CONFIGS_DIR):
        os.makedirs(CONFIGS_DIR)
    
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    main()
