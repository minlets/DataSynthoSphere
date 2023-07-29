import os
import sys

import click

from ArgsHandler import ArgsHandler
from DocumentationPrinter import DocumentationPrinter

CONFIGS_DIR = "configs"

@click.command()
def main():
    if not os.path.exists(CONFIGS_DIR):
        os.makedirs(CONFIGS_DIR)

    config_handler = ConfigHandler()
    args = config_handler.parse_arguments()
    config_handler.configure_logging()

    args_handler = ArgsHandler()

    if not sys.argv[1:]:
        # If no arguments are provided, display the full documentation
        DocumentationPrinter.print_full_documentation()
    else:
        # Parse the command-line arguments and handle accordingly
        try:
            if args.document:
                DocumentationPrinter.print_full_documentation()
            elif args.generate_data:
                output_file = args.output_file if args.output_file else "configs/generated_data.json"
                file_format = args.file_format if args.file_format else "json"
                args_handler.handle_generate_data(output_file, file_format)
            elif args.load_configs:
                config_file = args.config if args.config else None
                flattened_keys_file = args.flattened_keys if args.flattened_keys else None
                json_keys_file = args.json_keys if args.json_keys else None
                file_format = args.file_format if args.file_format else "json"
                args_handler.handle_load_configs(config_file, flattened_keys_file, json_keys_file, file_format)
            elif args.clean_up:
                args_handler.handle_clean_up()
            else:
                # If invalid arguments are provided, display the full documentation
                DocumentationPrinter.print_full_documentation()
        except Exception as e:
            click.echo(f"Error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
