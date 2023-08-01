import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='DataSynthoSphere',
    version='1.0.0',
    author='Vidya Sagar Jalla',
    author_email='jallavidya.sagar@icloud.com',
    description='DataSynthoSphere is an innovative and cutting-edge AI-powered Synthetic Data project that revolutionizes how organizations understand and interact with their customer data in the digital era. As businesses increasingly shift to online interactions and face stringent data privacy regulations, the need for privacy-preserving customer insights becomes more critical than ever.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/minlets/DataSynthoSphere',
    packages=setuptools.find_packages('src/main'),
    package_dir={'': 'src/main'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='DataSynthoSphere synthetic data AI customer-insights privacy-preserving',
    python_requires='>=3.6, <4',
    install_requires=[
        'openpyxl>=3.2.0b1',
        'PyYAML>=6.0',
        'click>=7.0',
        'fuzzywuzzy>=0.18.0',
        'config_handler>=0.1.0',
        'python-Levenshtein>=0.21.1'
    ],
    entry_points={
        'console_scripts': [
            'DataSynthoSphere=App:App'
        ],
    },
    project_urls={
        'Bug Tracker': 'https://github.com/minlets/DataSynthoSphere/issues',
        'Documentation': 'https://github.com/minlets/DataSynthoSphere/wiki',
        'Source Code': 'https://github.com/minlets/DataSynthoSphere',
    },
)
