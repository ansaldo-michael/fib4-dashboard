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
