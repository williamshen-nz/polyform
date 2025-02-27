'''
File: convert.py
Polycam Inc.

Created by Chris Heinrich on Tuesday, 1st November 2022
Copyright © 2022 Polycam Inc. All rights reserved.
'''
import fire
import logging
from polyform.core.capture_folder import CaptureFolder
from polyform.convertors.instant_ngp import InstantNGPConvertor

_log = logging.getLogger(__name__)


def convert(data_folder_path: str, format: str = "ingp"):
    """
    Main entry point for the command line convertor
    Args:
        data_folder_path: path to the unzipped Polycam data folder
        format: Output format time. Supported values are [ingp]
    """
    folder = CaptureFolder(data_folder_path)
    if format.lower() == "ingp" or format.lower() == "instant-ngp":
        convertor = InstantNGPConvertor()
    else:
        _log.error("Format {} is not curently supported. Consider adding a convertor for it".format(format))
        exit(1)
    convertor.convert(folder)

if __name__ == '__main__':
    fire.Fire(convert)