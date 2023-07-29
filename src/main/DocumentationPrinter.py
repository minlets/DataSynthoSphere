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
            click.echo("DataSynthoSphere CLI Documentation")
            # Print the rest of the documentation

        elif generate_data:
            click.echo("Usage: python src/main/main.py --generate_data [options]")
            # Print help for --generate_data option
        elif load_configs:
            click.echo("Usage: python src/main/main.py --load_configs [options]")
            # Print help for --load_configs option
        elif clean_up:
            click.echo("Usage: python src/main/main.py --clean_up")
            # Print help for --clean_up option
        else:
            click.echo("Invalid option! Please use one of the following options:")
            click.echo("  python src/main/main.py --document")
            click.echo("  python src/main/main.py --generate_data [options]")
            click.echo("  python src/main/main.py --load_configs [options]")
            click.echo("  python src/main/main.py --clean_up")
