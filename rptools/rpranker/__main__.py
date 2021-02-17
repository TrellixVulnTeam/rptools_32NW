from rptools.rpranker import (
    rank,
)
from rptools.rpranker.Args import add_arguments
from rptools import build_args_parser
from rptools.rplibs import rpSBML
from os import (
    path as os_path,
    mkdir
)
from shutil import copy
from typing import (
    List,
    Dict,
    Tuple
)


def entry_point():
  
    parser = build_args_parser(
        prog = 'rpranker',
        description = 'Rank pathways accoring to their global score',
        m_add_args = add_arguments
    )
    args = parser.parse_args()

    from rptools.__main__ import init
    logger = init(parser, args)

    ranked_pathways = rank(
        pathways = args.pathways,
        logger = logger
    )

    # Write into a file the list of top ranked pathways
    if args.outfile != '':
        store_into_file(
            ranked_pathways[:args.top],
            args.outfile
        )
        logger.info(
            '\nTop {top} pathways ranking is available in file {file}.'.format(
                top = args.top,
                file = args.outfile
            )
        )

    # Copy top ranked rpsbml files into a folder
    if args.outdir != '':
        copy_into_folder(
            ranked_pathways[:args.top],
            args.outdir
        )
        logger.info(
            '\nTop {top} pathways are available in folder {folder}.'.format(
                top = args.top,
                folder = args.outdir
            )
        )

    if not args.silent:
        if args.log.lower() in ['critical', 'error', 'warning']:
            print(ranked_pathways)
        else:
            logger.info('\nRanked Pathways')
            logger.info('   |-' + '\n   |-'.join('{}: {}'.format(*k) for k in enumerate(ranked_pathways)))


def store_into_file(
    pathways: List[ Tuple[float, str] ],
    outfile: str
) -> None:
    with open(outfile, 'w') as fp:
        for item in pathways:
            fp.write(
                '{score} {filename}\n'.format(
                    score  = item[0],
                    filename = item[1]
                )
            )


def copy_into_folder(
    pathways: List[ Tuple[float, str] ],
    outdir: str
) -> None:
    if not os_path.exists(outdir):
        mkdir(outdir)
    for item in pathways:
        copy(item[1], outdir)


if __name__ == '__main__':
    entry_point()
