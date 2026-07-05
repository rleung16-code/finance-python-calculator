# Finance Python Calculator

A beginner-friendly Python project that connects finance knowledge with programming.

This project was built as part of my transition from Finance to Computer Science / AI. It demonstrates Python fundamentals, financial formulas, clean project structure, unit testing, Git, and GitHub documentation.

## Features

1. Compound interest calculator
2. Monthly loan payment calculator
3. Return on investment calculator
4. Savings goal calculator
5. CSV export for calculation results

After each calculation, the program saves the result to a local CSV file:

    results.csv

The CSV file is ignored by Git because it is generated locally when the program runs.

## Why this project matters

This project connects my finance background with software development. It shows that I can:

- Build a working Python command-line program
- Use functions to organize financial calculations
- Handle user input
- Write unit tests
- Save calculation results to a CSV file
- Use Git and GitHub for version control
- Document a project clearly for a public portfolio

## How to run

Clone or download the repository, then run:

    python main.py

You will see a menu:

    Finance Python Calculator
    1. Compound interest
    2. Monthly loan payment
    3. Return on investment
    4. Savings goal
    5. Exit

Choose an option and enter the requested values.

## CSV output

When a calculation is completed, the result is saved to:

    results.csv

Example CSV format:

    timestamp,calculation_type,input_summary,result
    2026-07-05T18:01:49,Return on investment,"initial=1000.0, final=1500.0",50.00%

The results.csv file is listed in .gitignore, so it is not uploaded to GitHub.

## Run tests

To run the unit tests:

    python -m unittest discover -s tests -p test_*.py -v

Expected result:

    Ran 4 tests

    OK

## Project structure

    finance-python-calculator/
    ├── main.py
    ├── calculators.py
    ├── csv_exporter.py
    ├── README.md
    ├── .gitignore
    └── tests/
        └── test_calculators.py

## Files

- main.py — command-line menu and user interaction
- calculators.py — financial calculation functions
- csv_exporter.py — saves calculation results to CSV
- tests/test_calculators.py — unit tests for core calculator functions
- .gitignore — excludes cache files, local environment files, and generated CSV output

## Current status

Completed:

- Basic finance calculator
- Four financial calculation functions
- Unit tests
- CSV result export
- GitHub repository setup
- Public portfolio documentation

## Next improvements

Possible future upgrades:

- Add better currency formatting
- Add charts for savings and investment growth
- Add input validation improvements
- Add a simple web version
- Add a small AI assistant feature later