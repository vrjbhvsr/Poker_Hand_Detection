import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Project name
project_name = "Poker_Hand_Detector"

# List of file paths to create
file_paths = [
    f"{project_name}/Components/data_ingestion.py",
    f"{project_name}/Components/data_validation.py",
    f"{project_name}/Components/card_recognition.py",
    f"{project_name}/Components/Hand_detector.py",
    f"{project_name}/Components/Displayer.py",
    f"{project_name}/Components/Model_pusher.py",
    f"{project_name}/Components/__init__.py",
    f"{project_name}/Notebooks/",
    f"{project_name}/Configuration/__init__.py",
    f"{project_name}/Configuration/s3_operation.py",
    f"{project_name}/constant/__init__.py",
     f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/__init__.py",
    f"template/index.html",
    f"template/results.html",
    "app.py",
    "Dockerfile",
    "setup.py",
    "requirements.txt",
    ".dockerignore",
]

# Create directories and files
for filepath in file_paths:
    filepath = Path(filepath)

    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory {file_dir} for file {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(file_name) == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Created empty file {file_name}")

    else:
        logging.info(f"File {file_name} already exists")