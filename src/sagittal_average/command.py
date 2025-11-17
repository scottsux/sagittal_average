from argparse import ArgumentParser
from .sagittal_brain import run_averages


def main():
    parser = ArgumentParser(
        description="Calculates the average for each sagittal-horizontal plane."
    )
    parser.add_argument(
        "file_input",
        nargs="?",
        default="brain_sample.csv",
        help="Input CSV file with brain data. Defaults to brain_sample.csv",
    )
    parser.add_argument(
        "-o",
        "--file_output",
        default="brain_average.csv",
        help="Output CSV file. Defaults to brain_average.csv",
    )
    args = parser.parse_args()

    run_averages(args.file_input, args.file_output)
