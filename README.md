# DataSynthoSphere

DataSynthoSphere is an innovative and cutting-edge AI-powered Synthetic Data project that revolutionizes how organizations understand and interact with their customer data in the digital era. As businesses increasingly shift to online interactions and face stringent data privacy regulations, the need for privacy-preserving customer insights becomes more critical than ever.

## Key Features and Benefits

- **Privacy-Preserving Insights:** DataSynthoSphere empowers businesses to extract accurate and actionable customer insights without compromising individual privacy. The synthetic data ensures that original customers are no longer re-identifiable, providing a secure environment for data analysis.

- **QA Reporting:** Each generated synthetic dataset comes with a comprehensive Quality Assurance (QA) report. This report analyzes the synthetic characters' authenticity, ensuring they are genuinely fictional and devoid of any re-identification risks.

- **Confident Data Sharing:** With DataSynthoSphere, organizations can confidently share data assets internally and with trusted partners. The project serves as the foundation for digital transformation initiatives, enabling stakeholders to gain clear insights into the impact and benefits of data-driven strategies.

- **Customizable Insights:** DataSynthoSphere offers customization options, allowing businesses to tailor synthetic data generation to specific use cases and customer segments. The flexibility of the platform makes it adaptable to diverse industries and data requirements.

- **Seamless Integration:** The DataSynthoSphere platform seamlessly integrates into existing data ecosystems, ensuring a smooth and efficient data generation process. It provides an intuitive interface for easy data management and insights extraction.

## Getting Started:
----------------
To use DataSynthoSphere, follow these steps:

1. Clone the repository:
   git clone https://github.com/minlets/DataSynthoSphere
   cd DataSynthoSphere

2. Set up the application:
   python setup.py

3. Run the DataSynthoSphere CLI application:
   python src/main/main.py [options]

## Available Options:
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

## Example Usages:
---------------
1. Display full documentation:
   ```bash
   python src/main/main.py --document
   ```bash

2. Generate synthetic data with custom output file and format:
   ```bash
   python src/main/main.py --generate_data --output_file path/to/output_file.json --file_format yaml
   ```bash

3. Load configurations from custom files:
   ```bash
   python src/main/main.py --load_configs --config path/to/config.json --flattened_keys path/to/flattened_keys.json --json_keys path/to/json_keys.yaml --file_format json
   ```bash

5. Clean up generated files and configurations:
   ```bash
   python src/main/main.py --clean_up
   ```bash

## Contribution Guidelines

We welcome contributions from the community to enhance and improve DataSynthoSphere. If you have any bug fixes, new features, or improvements, please submit a pull request following our contribution guidelines.

## License
Private

## Acknowledgments

We would like to express our gratitude to the open-source community and contributors for their valuable contributions to the project.
