from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="rf-prediction-pipeline",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="RF prediction pipeline for pathogenicity assessment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rf-prediction-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "rf-predict=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.pkl", "*.csv", "*.fa", "*.fa.*"],
    },
) 