from config_handler import ConfigHandler
from data_generator import DataGenerator
from interactive_mode import InteractiveMode

class ArgsHandler:
    def __init__(self):
        self.config_handler = ConfigHandler()
        self.data_generator = DataGenerator()
        self.interactive_mode = InteractiveMode()

    def handle_arguments(self, args):
        if args.document:
            print_full_documentation()
            return
        elif args.clean_up:
            self.config_handler.clean_up_files(CONFIG_FILENAME, FLATTENED_KEYS_FILENAME, JSON_KEYS_FILENAME, GENERATED_DATA_FILE_NAME)
        elif args.load_configs:
            num_config_args = len([arg for arg in args.load_configs if arg.startswith('--config') or arg.startswith('--flattened_keys') or arg.startswith('--json_keys')])
            if num_config_args <= 3:
                config_file = flattened_keys_file = json_keys_file = None
                if '--config' in args.load_configs:
                    config_file = args.config
                if '--flattened_keys' in args.load_configs:
                    flattened_keys_file = args.flattened_keys
                if '--json_keys' in args.load_configs:
                    json_keys_file = args.json_keys
                self.config_handler.load_configs(config_file=config_file, flattened_keys_file=flattened_keys_file, json_keys_file=json_keys_file, file_format=args.file_format)
            else:
                # Handle the case of more than three arguments after --load_configs separately.
                pass
        elif args.generate_data:
            num_generate_args = len([arg for arg in args.generate_data if arg.startswith('--output_file') or arg.startswith('--output_format')])
            if num_generate_args <= 2:
                output_file = args.output_file if '--output_file' in args.generate_data else None
                file_format = args.output_format if '--output_format' in args.generate_data else 'json'
                self.data_generator.generate_data(output_file=output_file, file_format=file_format)
            else:
                # Handle the case of more than two arguments after --generate_data separately.
                pass
        else:
            self.interactive_mode.run()
