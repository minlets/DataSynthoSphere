from setuptools import setup, find_packages

setup(
    name='DataSynthoSphere',
    version='1.0.0',
    description='DataSynthoSphere is an innovative and cutting-edge AI-powered Synthetic Data project that revolutionizes how organizations understand and interact with their customer data in the digital era. As businesses increasingly shift to online interactions and face stringent data privacy regulations, the need for privacy-preserving customer insights becomes more critical than ever.',
    author='Vidya Sagar Jalla',
    author_email='jallavidya.sagar@icloud.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'data_generator = App:App'
        ],
    },
    install_requires=[
        'openpyxl',
        'PyYAML',
        'click',
        'fuzzywuzzy',
        'config_handler'
    ],
)
