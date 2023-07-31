import os
import sys


from DocumentationPrinter import DocumentationPrinter as dp
from config_handler import ConfigHandler
from ArgsHandler import ArgsHandler

def main():
    config_handler = ConfigHandler()
    args_handler = ArgsHandler()
    config_handler.configure_logging()
    if not os.path.exists(config_handler.CONFIGS_DIR):
        os.makedirs(config_handler.CONFIGS_DIR)
    if not sys.argv[1:]:
        dp.print_full_documentation()
    else:
        args = args_handler.parse_arguments()
        args_handler.handle_arguments(args)
if __name__ == "__main__":
    main()
