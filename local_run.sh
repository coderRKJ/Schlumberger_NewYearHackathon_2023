#! /bin/bash
echo "======================================================================"
echo "Welcome to the application. It will run the application in development mode."
echo "----------------------------------------------------------------------"
if [ -d "venv" ];
then
    echo "Enabling python 3.11 virtual env"
    # Activate virtual env
    . venv/bin/activate
else
    echo "No Virtual env detected. Please run setup.sh first"
    exit 1
fi

# run the application through uvicorn in debug mode
flask --debug run

# Deactivate virtual env 
deactivate
