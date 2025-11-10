# RF Prediction Pipeline

A machine learning pipeline that uses Random Forest to predict pathogenicity levels (HIGH, INTERMEDIATE, LOW) from genomic data using BLAST and abricate analysis.

## Installation

### Using conda (recommended)

```bash
# Create a new conda environment
conda create -n rf-prediction python=3.9
conda activate rf-prediction

# Install the package
conda install -c conda-forge -c bioconda rf-prediction-pipeline
```

### Using pip

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install BLAST and abricate
conda install -c bioconda blast abricate
```

### Manual installation

```bash
# Clone the repository
git clone https://github.com/yourusername/rf-prediction-pipeline.git
cd rf-prediction-pipeline

# Run the installer
bash install.sh
```

## Usage

### Command Line Interface

```bash
# Basic usage
rf-predict input.fasta

# Or using python directly
python main.py input.fasta
```

### Example

```bash
# Predict pathogenicity for a sample
rf-predict testfiles/MFDS2008729.fasta
# Output: HIGH, INTERMEDIATE, or LOW
```

## Input Format

The pipeline expects a FASTA file containing genomic sequences for analysis.

## Output

The pipeline outputs one of three pathogenicity levels:
- **HIGH**: High pathogenicity predicted
- **INTERMEDIATE**: Intermediate pathogenicity predicted  
- **LOW**: Low pathogenicity predicted

## Dependencies

- Python >= 3.7
- pandas
- scikit-learn
- BLAST+ (blastn)
- abricate

## Files

- `main.py`: Main pipeline script
- `final_RF.pkl`: Trained Random Forest model
- `test_df.csv`: Reference dataframe for feature columns
- `ecoli/e.coli_pathotype.fa`: BLAST database
- `abricate_reproducible/`: Abricate tools and databases

## Citation

If you use this pipeline in your research, please cite:

```
[Your paper citation here]
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
