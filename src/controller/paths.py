import os
import tempfile

temp_directory = tempfile.gettempdir()
subfolder = "CutFileParser"  # cannot be other name, as it is hardcoded in the C# code
datafolder_path = os.path.join(temp_directory, subfolder)
os.makedirs(datafolder_path, exist_ok=True)

working_directory = os.getcwd()
logfolder_path = os.path.join(working_directory, "logs")
os.makedirs(logfolder_path, exist_ok=True)
log_path = os.path.join(logfolder_path, "DashApp.log")
# if os.path.exists(log_path):
#     os.remove(log_path)
