# encoding: utf-8
'''
logger.py

Created by Ale Sanchez on 2018-07-23

Copyright (c) 2018. All rights reserved.
'''

import logging


def init_logger(logfile):
    log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

def get_logger():
    return logging.getLogger()