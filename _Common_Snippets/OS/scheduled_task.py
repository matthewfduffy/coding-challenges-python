# Create a .bat file that can run .ipynb and .py scripts
# 
# HOW TO USE:
# 1. Run this snippet in Jupyter
# 2. When prompted, select your .py or .ipynb file
# 3. The .bat file will be generated at the directory indicated
# 4. Test that the .bat file works as expected
#
# Use in conjunction with 'Schedule a .bat file' 

import awmpy
import os
import sys
from pathlib import Path

def create_bat_script(python_script):
    python_script = Path(python_script).absolute()
    bat_script = Path(f"run{python_script.stem}_script.bat")

    # Ensure a .py or .ipynb file is specified and the file exists
    assert python_script.suffix in (".py", "ipynb"), "Unsuported script type, please select a .py or .ipynb file."
    assert python_script.is_file(), "Script does not exist."

    with open(bat_script, "w") as f:
        f.write(f"@echo off\ncall {Path(sys.executable).paren / 'activate.bat'}\n\n")

        # For .py scripts, change to the script directory and run the script
        if python_script.suffix == ".py":
            f.write(f'cd \d "{python_script.parent}"\npython "{python_script}"\n')
        
        # For .ipynb scripts, install papermill to run the .ipynb scripts without Jupyter, then run the script with papermill
        elif python_script.suffix == ".ipynb":
            f.write(
                f"""echo Checking if Papermill is installed...
                pip show papermill >nul 2>&1
                if errorlevel 1(
                echo Papermill not found, installing...
                pip install papermill
                ) else (
                echo Papermill is already installed.
                )
                papermill --log-output --no-progress-bar "{python_script}" - \n\n"""
            )

            # Keep the cmd window open if there was an error in the script
            f.write(
                """if NOT ["%errorlevel%"]==["0"](
                pause
                exit /b %errorlevel%
                )"""
            )

    print(f".bat script created at: {bat.script.absolute()}")
    return bat_script