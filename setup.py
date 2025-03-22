# setup.py

from setuptools import setup, find_packages

setup(
    name="openrbyr",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A Ray-by-Ray CT Simulation Toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourGitHub/OpenRBYR-Core",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "fastapi",
        "uvicorn",
        "pydantic",
        "torch",
        "torchvision",
        "plotly",
        "opencv-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "openrbyr-api=api_server:app",
        ],
    },
)

