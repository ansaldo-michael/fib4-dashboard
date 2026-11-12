# Decisions Log

## Goal
Build a deployed FIB-4 calculator as the first piece of a cardiometabolic health dashboard, as a portfolio project for a clinical AI / implementation career pivot.

## Decision 1: Follow the equation's constraints
FIB-4 = (age x AST) / (platelets x sqrt(ALT))
Units: age in years, AST and ALT in U/L, platelets in 10^9/L.

- Hard rules (code rejects the input): age, AST, ALT, and platelets must all be greater than 0.
- Clinical limits (code warns, still calculates): the score is less reliable under age 35 or over 65. Age-specific cutoffs are added in a later step.

Why: the formula needs valid inputs to be mathematically correct, and clinical limits come from published guidelines (AASLD, McPherson 2017).

## Build order
1. FIB-4 function + tests (done)
2. Input validation
3. Web interface
4. Deployment
5. PREVENT and an AI explanation layer

## Decision 2: Evaluate LLM output before executing
Every piece of LLM-generated code or guidance is reviewed and understood before I run it, and checked against sources and tests.

## Decision 3: Hard limits and warnings
Hard limits reject the input. Warnings still calculate the score but flag the result.

Hard limits:
- All four inputs: a real, finite number greater than 0
- AST: at most 10,000 U/L
- ALT: at most 10,000 U/L
- Platelets: at most 1000 x10^9/L
- Age: 18 to 120 years

Warnings:
- AST or ALT above 300 U/L (likely acute injury, where FIB-4 is unreliable)
- Age under 35 or over 65 (FIB-4 is less reliable outside 35 to 65)

Why: hard limits catch impossible or mistyped values only. Normal ranges are not used as limits, because FIB-4 is meant for patients whose values are often abnormal.
Sources (US): ACG 2017 abnormal liver chemistries guideline, AASLD NAFLD guidance, NHLBI, StatPearls.

## Decision 4: Age-specific risk cutoffs
Risk category depends on age:

- Age under 65: Low below 1.3, Indeterminate 1.3 to 2.67, High above 2.67
- Age 65 or older: Low below 2.0, Indeterminate 2.0 to 2.67, High above 2.67

Boundaries:
- Age exactly 65 uses the older-adult table. Sources disagree on "65 or older" vs "over 65", so I chose to include 65.
- A score exactly at a cutoff (1.3, 2.0, 2.67) is Indeterminate. Low means strictly below the lower cutoff, High means strictly above 2.67.
- Age under 35 gets a reliability warning only. No separate cutoffs are defined for it.

Source (US): AASLD clinical guidance on noninvasive assessment of MASLD.

Sources for Decision 4 (age 65+ thresholds):
- AGA: Clinical Care Pathway for Risk Stratification and Management of Patients With MASLD. Gastroenterology, March 2026. DOI 10.1053/j.gastro.2026.02.023 (DOI as provided; existence of the pathway confirmed, DOI not independently verified).
- AASLD: Rinella ME et al. AASLD Practice Guidance on the clinical assessment and management of NAFLD. Hepatology 2023;77(5):1797-1835. DOI 10.1097/HEP.0000000000000323. Age-65 thresholds also stated on AASLD's clinical-pearl page on noninvasive MASLD assessment.
- ADA: Comprehensive Medical Evaluation and Assessment of Comorbidities: Standards of Care in Diabetes-2026. Diabetes Care 2026;49(Suppl 1):S61-S88. (Covers FIB-4 triage; age-specific cutoff text not independently confirmed.)

## Decision 5: Product direction
Many free FIB-4 calculators already exist. This project differentiates by becoming a cardiometabolic dashboard that interfaces with an EHR, pulls a patient's lab values, and gives providers an at-a-glance view of cardiometabolic health. The FIB-4 calculator is the first slice.

Design implications (planned, not yet built):
- Keep the calculation logic separate from the interface so a web page or an EHR connection can call the same functions.
- Real EHR data is messier than typed-in data (missing labs, old results, different units), so validation and warnings matter more. Possible future warnings: no value on file, or lab result is old.
- EHR data would come through the FHIR standard, with labs identified by LOINC codes. Development and testing use synthetic patients only, never real patient data.

## Decision 6: Classify the exact score, display 3 decimals
Risk category is determined from the exact (unrounded) FIB-4 score, so the criteria are applied as published: Low is strictly below the lower cutoff (1.3, or 2.0 at age 65+), High is strictly above 2.67.

Why: the published criteria are defined on the score itself, and none of the guidance reviewed specifies rounding before classification. Rounding first would change the patient's score before applying the criteria.

Display: the interface will show the score to 3 decimals so the number and the label never appear to disagree (for example, 2.674 shows as High, not "2.67 = High").
