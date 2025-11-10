#!/bin/bash

# Build script for conda package

set -e

echo "Building conda package..."

# Check if conda-build is installed
if ! command -v conda-build &> /dev/null; then
    echo "Installing conda-build..."
    conda install -y conda-build
fi

# Build the package
conda-build . --output-folder ./build

echo "Package built successfully!"
echo "To install locally: conda install --use-local rf-prediction-pipeline"
echo "To upload to conda-forge: anaconda upload ./build/*/rf-prediction-pipeline-*.tar.bz2" 