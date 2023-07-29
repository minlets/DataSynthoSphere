import os
import sys


CONFIGS_DIR = "configs"


def main():
    if not os.path.exists(CONFIGS_DIR):
        os.makedirs(CONFIGS_DIR)

    config_handler = ConfigHandler()
    args = config_handler.parse_arguments()
    config_handler.configure_logging()

    args_handler = ArgsHandler()
    args_handler.handle_arguments(args)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    main()
