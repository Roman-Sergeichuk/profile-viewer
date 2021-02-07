import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='synchronizer')
    # parser.add_argument('url')
    # parser.add_argument(
    #     '-o',
    #     '--output',
    #     type=str,
    #     default='',
    #     help='set output directory'
    # )
    # parser.add_argument(
    #     '-l',
    #     '--level',
    #     type=str,
    #     default=None,
    #     choices=['debug', 'DEBUG', 'INFO', 'info', 'warning', 'WARNING',
    #              'ERROR', 'error', 'critical', 'CRITICAL', None, ''],
    #     help='level of logging'
    # )
    return parser