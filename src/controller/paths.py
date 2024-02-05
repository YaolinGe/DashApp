import os
import tempfile

temp_directory = tempfile.gettempdir()
subfolder = "CutFileParser"  # cannot be other name, as it is hardcoded in the C# code
datafolder_path = os.path.join(temp_directory, subfolder)

os.makedirs(datafolder_path, exist_ok=True)
