import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Assessly"


list_of_files = [


    ".github/workflows/.gitkeep",
    "frontend/public/index.html",
    "frontend/src/components/Button.js",
    "frontend/src/pages/LoginPage.js",
    "frontend/src/pages/DomainPage.js",
    "frontend/src/pages/DashboardPage.js",
    "frontend/src/pages/UploadPage.js",
    "frontend/src/pages/DifficultyPage.js",
    "frontend/src/routes/AppRouter.js",
    "frontend/src/services/api.js",
    "frontend/src/App.js",
    "frontend/src/index.js",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "backend/app/main.py",
    "backend/app/routes/auth.py",
    "backend/app/routes/domain.py",
    "backend/app/routes/interview.py",
    "backend/app/services/resume_parser.py",
    "backend/app/services/question_generator.py",
    "backend/app/models/user.py",
    "backend/app/utils/token.py",
    "backend/app/database.py",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")