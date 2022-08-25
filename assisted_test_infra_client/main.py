import logging
import sys

import yaml_parser
from common import constants
from common import helpers


LOG = logging.getLogger(__name__)


def main(args):
    LOG.debug(f"Args: {args}")
    yaml_parser.download_yaml(f'{constants.TEST_FILE_URL}/{constants.TEST_FILE_NAME}')
    yaml_parser.read_yaml(constants.TEST_FILE_NAME)


if __name__ == '__main__':
    cmd_line_args = helpers.process_args()
    helpers.configure_logger(cmd_line_args.debug)
    sys.exit(main(cmd_line_args))
