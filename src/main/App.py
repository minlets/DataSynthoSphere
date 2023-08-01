import os
import sys


from DocumentationPrinter import DocumentationPrinter as dp
from ConfigHandler import ConfigHandler
from ArgsHandler import ArgsHandler

def main():
    ch = ConfigHandler()
    ah = ArgsHandler()
    ch.configure_logging()
    if not os.path.exists(ch.CONFIGS_DIR):
        os.makedirs(ch.CONFIGS_DIR)
    if not sys.argv[1:]:
        dp.print_full_documentation()
    else:
        args = ah.parse_arguments()
        ah.handle_arguments(args)
if __name__ == "__main__":
    main()
