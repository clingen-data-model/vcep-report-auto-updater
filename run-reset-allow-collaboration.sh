#!/bin/bash

# activate the virtual environment
source venv/3.12/bin/activate

# run the script to reset the ClinVar reports to allow collaboration
python src/ResetClinVarReportsToAllowCollaboration.py
