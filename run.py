# -*- coding: utf-8 -*-

"""
Author: Szymon Miks
05.01.2019
Recruitment task for company: ADGROUP
"""

import argparse
from application.ParcelsParser import ParcelsParser


def arg_parser():
    description = """Application for decoding 
    county code, commune code, commune type, district number, parcel number
    based on cadastral parcel identifiers.
    Important! Column names in the file are required
    """

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--filename", help="path to the file with data", default="cadastral_parcels.tsv")
    parser.add_argument("--column", help="name of the column in file where data are located",
                        default="cadastral_parcel_identifier")

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit()

    return args


if __name__ == "__main__":
    args = arg_parser()
    parser = ParcelsParser(args.filename, args.column)

    parser.get_identifiers_data()
    parser.extract_data()

    print(parser)
    parser.beautify_print()
