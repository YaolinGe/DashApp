import subprocess
import os
script_path = os.path.join(".", "src", "app.py")


# You can also handle exceptions to catch errors
try:
    result = subprocess.run(["python", script_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while executing script: {e}")
