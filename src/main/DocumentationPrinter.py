import click

class DocumentationPrinter:
    @staticmethod
    @click.command()
    @click.option('--document', is_flag=True, help='Display full code documentation.')
    @click.option('--generate_data', is_flag=True, help='Generate synthetic data using the given configuration.')
    @click.option('--load_configs', is_flag=True, help='Load default configurations or configurations from specified files.')
    @click.option('--clean_up', is_flag=True, help='Remove all generated files and configurations.')
    def print_full_documentation(document, generate_data, load_configs, clean_up):
        if document:
            click.echo("""
DataSynthoSphere CLI Documentation

DataSynthoSphere is an AI-powered Synthetic Data project designed to provide privacy-preserving customer insights while ensuring compliance with data privacy regulations. This CLI application allows you to generate synthetic data and analyze it securely.

Getting Started:
----------------
To use DataSynthoSphere, follow these steps:

1. Clone the repository:
   git clone https://github.com/minlets/DataSynthoSphere
   cd DataSynthoSphere

2. Set up the application:
   python setup.py

3. Run the DataSynthoSphere CLI application:
   python src/main/main.py [options]

Available Options:
------------------
The DataSynthoSphere CLI supports the following options:

1. --document: Display the full code documentation.

2. --generate_data: Generate synthetic data using the given configuration.
   - --output_file: Specify the path to the output file for generated synthetic data (default: "configs/generated_data.json").
   - --file_format: Choose the file format for the generated data (json or yaml). Default is json.

3. --load_configs: Load default configurations or configurations from specified files.
   - --config: Path to the configuration file (json or yaml).
   - --flattened_keys: Path to the flattened keys file (json or yaml).
   - --json_keys: Path to the json keys file (json or yaml).
   - --file_format: File format for configurations (json or yaml). Default is json.

4. --clean_up: Remove all generated files and configurations.

Example Usages:
---------------
1. Display full documentation:
   python src/main/main.py --document

2. Generate synthetic data with custom output file and format:
   python src/main/main.py --generate_data --output_file path/to/output_file.json --file_format yaml

3. Load configurations from custom files:
   python src/main/main.py --load_configs --config path/to/config.json --flattened_keys path/to/flattened_keys.json --json_keys path/to/json_keys.yaml --file_format json

4. Clean up generated files and configurations:
   python src/main/main.py --clean_up

Contribution Guidelines:
------------------------
We welcome contributions to improve DataSynthoSphere. If you have bug fixes, new features, or improvements, please submit a pull request following our contribution guidelines.

License:
--------
Private

Acknowledgments:
----------------
We appreciate the contributions from the open-source community to the DataSynthoSphere project.
""")
        elif generate_data:
            # Display help for generating synthetic data
            click.echo("""
Usage: python src/main/main.py --generate_data [options]

Generate synthetic data using the given configuration.

Options:
  --output_file PATH      Specify the path to the output file for generated synthetic data (default: "configs/generated_data.json").
  --file_format TEXT     Choose the file format for the generated data (json or yaml). Default is json.
""")
        elif load_configs:
            # Display help for loading configurations
            click.echo("""
Usage: python src/main/main.py --load_configs [options]

Load default configurations or configurations from specified files.

Options:
  --config PATH             Path to the configuration file (json or yaml).
  --flattened_keys PATH     Path to the flattened keys file (json or yaml).
  --json_keys PATH          Path to the json keys file (json or yaml).
  --file_format TEXT        File format for configurations (json or yaml). Default is json.
""")
        elif clean_up:
            # Display help for cleaning up
            click.echo("""
Usage: python src/main/main.py --clean_up

Remove all generated files and configurations.
""")
        else:
            click.echo("Invalid option! Please use one of the following options:")
            click.echo("  python src/main/main.py --document")
            click.echo("  python src/main/main.py --generate_data [options]")
            click.echo("  python src/main/main.py --load_configs [options]")
            click.echo("  python src/main/main.py --clean_up")

