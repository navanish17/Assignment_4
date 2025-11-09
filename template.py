import os
from pathlib import Path
import logging 

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s')

title = 'Assignment_4'

list_of_files = [
    f"src/{title}/__init__.py",
    f"src/{title}/components/__init__.py",
    f"src/{title}/utils/__init__.py",
    f"src/{title}/utils/common.py",
    f"src/{title}/config/__init__.py",
    f"src/{title}/config/configuration.py",
    f"src/{title}/pipeline/__init__.py",
    f"src/{title}/entity/__init__.py",
    f"src/{title}/entity/config_entity.py",
    f"src/{title}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Data",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"creating folder {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        logging.info(f"{filename} already exists")