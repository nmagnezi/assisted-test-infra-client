import argparse
import logging


def configure_logger(debug_mode):
    logging.basicConfig(
        level=logging.DEBUG if debug_mode is True else logging.INFO,
        format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
    )


def process_args():
    parser = argparse.ArgumentParser(
        description='POC test-infra-client'
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        required=False,
        help='List tests'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        required=False,
        default=False,
        help='Enable Debug mode.',
    )
    return parser.parse_args()
