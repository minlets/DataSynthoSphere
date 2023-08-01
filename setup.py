from setuptools import setup, find_packages

setup(
    name='DataSynthoSphere',
    version='1.0.0',
    description='DataSynthoSphere is an innovative and cutting-edge AI-powered Synthetic Data project that revolutionizes how organizations understand and interact with their customer data in the digital era. As businesses increasingly shift to online interactions and face stringent data privacy regulations, the need for privacy-preserving customer insights becomes more critical than ever.',
    author='Vidya Sagar Jalla',
    author_email='jallavidya.sagar@icloud.com',
    packages=find_packages('src/main'),
    package_dir={'': 'src/main'},
    entry_points={
        'console_scripts': [
            'DataSynthoSphere = App:App'
        ],
    },
    install_requires=[
        'openpyxl==3.2.0b1',
        'PyYAML==6.0',
        'click==7.0',
        'fuzzywuzzy==0.18.0',
        'config_handler==0.1.0',
        'python-Levenshtein==0.21.1'
    ],
    python_requires='>=3.10.8',
    setup_requires=[
        'pip==23.2.1'
    ]
)
