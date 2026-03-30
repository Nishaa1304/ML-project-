import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
Project_name="MLproject"
list_of_file=[
   
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__int__.py",
    f"src/{Project_name}/components/data_ingestion.py",
    f"src/{Project_name}/components/data_transformation.py",
    f"src/{Project_name}/components/model_trainer.py",
    f"src/{Project_name}/components/model_monitoring.py",
    f"src/{Project_name}/pipelines/__init__.py",
    f"src/{Project_name}/pipelines/training_pipeline.py",
    f"src/{Project_name}/pipelines/prediction_pipeline.py",
    f"src/{Project_name}/pipelines/exception.py",
    f"src/{Project_name}/pipelines/logger.py",
    f"src/{Project_name}/pipelines/utils.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "" :
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
        if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                    pass
            logging.info(f"creating empty file:{filepath}")

        else:
             logging.info(f"{filename} already exists")
        
