# FIB-4 Calculator

> **DISCLAIMER: This is a portfolio and educational project. It is NOT a medical device and is NOT intended for diagnosis, treatment, or clinical decision-making. Do not use it to guide patient care. Do not enter real patient information.**

## What this is
The first piece of a planned cardiometabolic health dashboard. It calculates the FIB-4 index from age, AST, ALT, and platelet count:

FIB-4 = (age x AST) / (platelets x sqrt(ALT))

Units: age in years, AST and ALT in U/L, platelets in x10^9/L.

## Status
In development. Input validation and tests are in place. A web interface, deployment, and further features are planned.

## Design decisions
See DECISIONS.md for the reasoning behind the input limits and warnings.

## Run the tests
python3.15 -m pytest
