# SagittalBrain
[![](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

A small Python package to compute sagittal averages from brain coronal-plane CSV files.
## Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
You can install this package via:
```bash
$ git clone https://github.com/scottsux/sagittal_average.git
```

Then navigate to the project directory and install using pip:
```bash
$ cd sagittal_average
$ pip install -e .
```

Be careful, it should be installed in the project root directory.

## Usage
### Python API

```python
import sagittal_average

sagittal_average.run_averages("brain_sample.csv", "brain_average.csv")
```

### Command Line Interface

```bash
$ sagittal_average brain_sample.csv

$ sagittal_average brain_sample.csv brain_average.csv
```

### Input
The input CSV file should contain coronal-plane brain data with the following structure:
- Each row represents a coronal slice of the brain.
- Each column represents a different measurement point across the width of the brain.

Example input:
```bash
0,1,2
3,4,5
6,7,8
```

### Output
The output CSV file will contain the sagittal average of the input data, computed by averaging corresponding columns across all rows. 

Example output for the above input:
```bash
3.0,4.0,5.0
```

## Contributing
Pull requests are welcome. This package was developed as part of UCL COMP0233 Coursework.

