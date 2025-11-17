# sagittal_average

A small Python package to compute sagittal averages from brain coronal-plane CSV files.

## Installation

Install in editable mode:

```bash
pip install -e .
```

Be careful, it should be installed in the project root directory.

## Usage
### Python API

```python
from sagittal_average import compute_sagittal_average
compute_sagittal_average("brain_sample.csv", "brain_average.csv")
```

### Command Line Interface

```bash
sagittal_average brain_sample.csv brain_average.csv
```

## Contributing
Pull requests are welcome. This package was developed as part of UCL COMP0233 Coursework.

