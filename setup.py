# setup.py
from setuptools import setup, find_packages

setup(
    name='openrbyr-core',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-image',
        'pydicom',
        'nibabel'
    ],
    entry_points={
        'console_scripts': [
            'phantom-viewer=cli.phantom_cli:main'
        ],
    },
    author='Your Name',
    description='Core simulation engine for Ray-by-Ray CT (OpenRBYR)',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

