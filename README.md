# FIB-4 Calculator

> **DISCLAIMER: This is a portfolio and educational project. It is NOT a medical device and is NOT intended for diagnosis, treatment, or clinical decision-making. Do not use it to guide patient care. Do not enter real patient information.**

## What this is
The first piece of a planned cardiometabolic health dashboard. It calculates the FIB-4 index from age, AST, ALT, and platelet count:

FIB-4 = (age x AST) / (platelets x sqrt(ALT))

Units: age in years, AST and ALT in U/L, platelets in x10^9/L.

It also validates inputs, classifies the score as Low, Indeterminate, or High using age-adjusted cutoffs, and shows warnings where FIB-4 is less reliable.

## Status
In development. The calculation logic, input validation, a Flask web interface, and automated tests are in place. Deployment and further features are planned.

## Run it locally
pip install flask
python3 -m flask --app app run --port 5001
Then open http://127.0.0.1:5001

## Run the tests
pip install pytest
python3 -m pytest

## Design decisions
See DECISIONS.md for the reasoning behind the input limits, cutoffs, warnings, and interface.

## Built with
Python and Flask. Built with assistance from Claude (AI); clinical and design decisions, and source review, are mine.
