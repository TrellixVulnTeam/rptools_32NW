from argparse import ArgumentParser

default_comp = 'MNXC3'

def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument('input_sbml',
                        type=str,
                        help="input SBML file")
    parser.add_argument('output_sink',
                        type=str,
                        help="output sink file")
    parser.add_argument('--compartment_id',
                        type=str,
                        default=default_comp,
                        help=f'SBML compartment id from which to extract the chemical species (default: {default_comp})')
    parser.add_argument('--remove_dead_end',
                        action='store_true',
                        help='upon FVA evaluation, ignore chemical species that do not have any flux')
    return parser
