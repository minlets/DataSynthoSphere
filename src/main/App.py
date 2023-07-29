import os
import sys
import click
from fuzzywuzzy import fuzz
from ArgsHandler import ArgsHandler
from DocumentationPrinter import DocumentationPrinter

CONFIGS_DIR = "configs"

def suggest_closest_options(user_input, valid_options, threshold=70):
    closest_options = []
    for option in valid_options:
        similarity_score = fuzz.partial_ratio(user_input, option)
        if similarity_score >= threshold:
            closest_options.append(option)
    return closest_options

@click.command()
def main():
    if not os.path.exists(CONFIGS_DIR):
        os.makedirs(CONFIGS_DIR)

    args_handler = ArgsHandler()
    args = args_handler.parse_arguments()
    args_handler.configure_logging()

    if not sys.argv[1:]:
        DocumentationPrinter.print_full_documentation()
    else:
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
                valid_options = ["--document", "--generate_data", "--load_configs", "--config", "--flattened_keys", "--json_keys", "--clean_up", "--output_file", "--file_format"]
                suggested_options = suggest_closest_options(sys.argv[1], valid_options)
                click.echo(f"Invalid option! Did you mean one of these: {', '.join(suggested_options)}")
                DocumentationPrinter.print_full_documentation()
        except Exception as e:
            click.echo(f"Error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
