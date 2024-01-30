"""
This module cleans up the temporary folder used for storing uploaded files.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
import os
from controller.paths import datafolder_path


def clean_up():
    for file in os.listdir(datafolder_path):
        file_path = os.path.join(datafolder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
