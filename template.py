import os
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctim)s]: %(message)s:')

list_of_files = [
    "src/_init_.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path (filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info (f"creating diractory; {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info (f"creating empty file {filepath}")

    else:
        logging.info (f"{filename} is already exist")