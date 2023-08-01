from config_handler import ConfigHandler
from DataGenerator import DataGenerator
from interactive_mode import InteractiveMode
from DocumentationPrinter import DocumentationPrinter as dp
import click
from fuzzywuzzy import fuzz
import argparse
import sys

def suggest_closest_options(user_input, valid_options, threshold=70):
    closest_options = []
    for option in valid_options:
        similarity_score = fuzz.partial_ratio(user_input, option)
        if similarity_score >= threshold:
            closest_options.append(option)
    return closest_options

class ArgsHandler:
    def __init__(self):
        self.config_handler = ConfigHandler()
        self.DataGenerator = DataGenerator()
        self.interactive_mode = InteractiveMode()
    def parse_generate_data_args(self, generate_data_list):
        parser = argparse.ArgumentParser(description="Data Generation Script")
        parser.add_argument("--output_file", default=self.config_handler.GENERATED_DATA_FILE_NAME, help="Output filename for generated data (JSON)")
        parser.add_argument("--output_format", choices=["json", "yaml"], default=self.config_handler.OUTPUT_FORMAT, help="File format for generated data (json or yaml). Default is json.")
        return parser.parse_args(generate_data_list)
    def parse_load_configs_args(self, load_configs_list):
        parser = argparse.ArgumentParser(description="Data Generation Script")
        parser.add_argument("--input_format", default=self.config_handler.INPUT_FORMAT, help="Output filename for generated data (JSON)")
        parser.add_argument("--config", default=self.config_handler.CONFIG_FILENAME, help="Output filename for generated data (JSON)")
        parser.add_argument("--flattened_keys", default=self.config_handler.FLATTENED_KEYS_FILENAME, help="Output filename for generated data (JSON)")
        parser.add_argument("--json_keys", default=self.config_handler.JSON_KEYS_FILENAME, help="File format for generated data (json or yaml). Default is json.")
        return parser.parse_args(load_configs_list)
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Data Generation Script", epilog="Use --help with any argument to get more information.")
        parser.add_argument("--document", action="store_true", help="Display full code documentation.")
        parser.add_argument("--generate_data", nargs=argparse.REMAINDER, help="Generate data using the given configuration.")
        parser.add_argument("--load_configs", nargs=argparse.REMAINDER, help="Load default configurations or from specified files.")
        parser.add_argument("--config", default=self.config_handler.GENERATED_DATA_FILE_NAME, help="Path to the configuration file (json or yaml).")
        parser.add_argument("--flattened_keys", default=self.config_handler.GENERATED_DATA_FILE_NAME,help="Path to the flattened keys file (json or yaml).")
        parser.add_argument("--json_keys",default=self.config_handler.GENERATED_DATA_FILE_NAME, help="Path to the json keys file (json or yaml).")
        parser.add_argument("--clean_up", action="store_true", help="Remove all generated files and configurations.")
        parser.add_argument("--output_file", default=self.config_handler.GENERATED_DATA_FILE_NAME, help="Output filename for generated data (JSON)")
        parser.add_argument("--output_format", choices=["json", "yaml","csv"], default="json", help="File format for configurations (json or yaml). Default is json.")
        parser.add_argument("--input_format", choices=["json", "yaml"], default="json", help="File format for configurations (json or yaml). Default is json.")
        return parser.parse_args()
    def handle_arguments(self, args):
        try:
            if args.document:
                dp.print_full_documentation()
            elif args.generate_data:
                num_generate_args = len([arg for arg in args.generate_data if arg.startswith('--output_file') or arg.startswith('--output_format')])
                if num_generate_args <= 2:
                    generate_data_args = self.parse_generate_data_args(args.generate_data)
                    output_file = generate_data_args.output_file if '--output_file' in args.generate_data else args.output_file
                    output_format = generate_data_args.output_format if '--output_format' in args.generate_data else args.output_format
                    self.DataGenerator.generate_data(output_file=output_file, output_format=output_format)
                else :
                    dp.print_full_documentation(generate_data)   
            elif args.load_configs:
                num_config_args = len([arg for arg in args.load_configs if arg.startswith('--config') or arg.startswith('--flattened_keys') or arg.startswith('--json_keys')])
                if  num_config_args <= 3:
                    load_configs_args = self.parse_load_configs_args(args.load_configs)
                    config_file = load_configs_args.config if '--config' in args.load_configs else args.config
                    flattened_keys_file = load_configs_args.flattened_keys if '--flattened_keys' in args.load_configs else args.flattened_keys
                    json_keys_file = load_configs_args.json_keys if '--json_keys' in args.load_configs else args.json_keys
                    input_format = load_configs_args.input_format if '--input_format' in args.load_configs else args.input_format
                    self.config_handler.load_configs(config_file=config_file, flattened_keys_file=flattened_keys_file, json_keys_file=json_keys_file, input_format=args.input_format)
                else :
                    dp.print_full_documentation(load_configs) 
            elif args.clean_up:
                self.config_handler.clean_up_files(self.config_handler.CONFIG_FILENAME, self.config_handler.FLATTENED_KEYS_FILENAME, self.config_handler.JSON_KEYS_FILENAME, self.config_handler.GENERATED_DATA_FILE_NAME)
            else:
                valid_options = ["--document", "--generate_data", "--load_configs", "--config", "--flattened_keys", "--json_keys", "--clean_up", "--output_file", "--input_format","--output_format"]
                suggested_options = suggest_closest_options(sys.argv[1], valid_options)
                click.echo(f"Invalid option! Did you mean one of these: {', '.join(suggested_options)}")
                dp.print_full_documentation()
        except Exception as e:
            dp.print_full_documentation()
            click.echo(f"Error: {str(e)}")
            sys.exit(1)
