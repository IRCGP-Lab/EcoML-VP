# EcoML-VP

A machine learning pipeline that uses Random Forest to predict pathogenicity levels (High-virulence (HV), Latent-virulence (LV), Avirulent) from genomic data using BLAST and abricate analysis.

## Installation

```bash
# Clone the repository
git clone https://github.com/IRCGP-Lab/EcoML-VP.git
cd EcoML-VP

# Create a new conda environment (recommended)
conda create -n ecoml-vp python=3.9
conda activate ecoml-vp

# Install all dependencies
bash install.sh
```

## Usage

### Command Line Interface

```bash
# Basic usage
ecoml-vp input.fasta

# Or using python directly
python main.py input.fasta
```

### Example

```bash
# Predict pathogenicity for a sample
ecoml-vp testfiles/CMCEC0923.fasta
# Output: High-virulence (HV), Latent-virulence (LV), or Avirulent
```

## Input Format

The pipeline expects a FASTA file containing genomic sequences for analysis.

## Output

The pipeline outputs one of three pathogenicity levels:
- **High-virulence (HV)**: High pathogenicity predicted
- **Latent-virulence (LV)**: Latent pathogenicity predicted  
- **Avirulent**: Low pathogenicity predicted

## Dependencies

- Python >= 3.7
- pandas
- scikit-learn
- BLAST+ (blastn)
- abricate

## Files

- `main.py`: Main pipeline script
- `final_RF.pkl`: Trained Random Forest model
- `train_df.csv` : Data used for training
- `test_df.csv`: Reference dataframe for feature columns
- `ecoli/e.coli_pathotype.fa`: BLAST database
- `abricate_reproducible/`: Abricate tools and databases

## Citation

If you use this pipeline in your research, please cite:

```
[Paper citation]
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
