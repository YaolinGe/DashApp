# paths.py

import os
import tempfile

temp_directory = tempfile.gettempdir()
subfolder = "CutFileParser"
datafolder_path = os.path.join(temp_directory, subfolder)
