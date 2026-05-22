#  programming_scripting-pands-mywork
This repository contains lab work and weekly task assignments completed as part of the  **Programming and Scripting** module.

The module introduces Python programming fundamentals including user input, file handling, functions, data visualisations, and working with external libraries.

## Repository Structure
```
programming_scripting-pands-mywork/
├── Labs/                         # Guided lab exercises
├── weekly-tasks/
|   ├── helloworld.py             # Weekly Task 1 - Hello World
|   ├── bank.py                   # Weekly Task 2 - Bank amount calculator
|   ├── accounts.py               # Weekly Task 3 - Amount number masking
|   ├── collatz.py                # Weekly Task 4 - Collatz sequence
|   ├── weekday.py                # Weekly Task 5 - Weekday checker
|   ├── squareroot.py             # Weekly Task 6 - Square root approximation (Newton's method)
|   ├── week07/
|   |   ├── es.py                 # Weekly Task 7 - Count letter 
|   |   └── test.txt              # text file for testing Weekly Task 7
|   ├── plottask.py               # Weekly Task 8 - Data visualisation
|   ├── plot.png                  # Output imaage for Weekly Task 8
└── .gitignore
```

## Weekly Tasks

### Weekly Task 1 - Hello World (`helloworld.py`)
Prints `Hello, World` to the terminal. Used to verify the Python environment was set up correctly at the start of the module.

### Weekly Task 2 - Bank (`bank.py`)
Prompts the user to enter two amounts in cents, adds them together as integers, then prompts the total formatted as euros and cent (e.g. `€2.45`). Uses integer arithmetic to avoid floating-point rounding errors.

### Weekly Task 3 - Accounts (`accounts.py`)
Reads in a bank account number of any length and masks all but the last 4 digits with `X` characters (e.g. `XXXXX7890`). Handles account numbers of 4 characters or fewer by displaying them in full.

### Weekly Task 4 -  Collatz (`collatz.py`)
Takes a positive integer from the user and applies the Collatz sequence: if the number is even , divide by 2; if odd, multiply by 3 and add 1. Repeats until the value reaches 1, printing each step along the way.

### Weekly Task 5 -  Weekday (`weekday.py`)
Uses Python's `datetime` module to check the current day of the week. Prints a message indicating whether today is a weekday (Monday - Friday) or a weekend (Saturday-Sunday). Requires no user input.

### Weekly Task 6 -  Square Root (`squareroot.py`)
Takes a positive floating-point number from the user and approximates its square root using Newton's method (without using built-in functions like `math.sqrt`). Iterates until the difference between estimates is less than 0.00001, then prints the roesults rounded to 1 decimal place. Includes a check to reject negative numbers.

### Weekly Task 7 - Count E's (`week07/es.py`)
Reads a `.txt` file supplied as a command-line argument and counts the total number of occurences of the letter `e` (both uppercase and lowercase). Includes error handling for: no arguement provided, file not found, and non-`.txt` files.

A sample test file (`test.txt`) is included in the repository containing a passage text, which can be used to text the program.

### Weekly Task 8 - Plot Task (`plottask.py`)
Uses `numpy` and `matplotlib` to display two plots on a single set of axes:
-  A histogram of 1000 values from a normal distribution (mean = 5, standard deviation = 2)
- A line plot of the function h(x) = x³ over the range 0 to 10

The plot includes a title, axis labels, legend, and grid. The output is also saved as `plot.png`

## Technologies used
| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `datetime` | Weekday detection (Weekly Task 5) |
| `sys` / `os` | Command-line arguements and file validation (Weekly Task 7) |
| `numpy` | Generating normal distribution data (Weekly Task 8) |
| `matplotlib` | Data visualisation and plot output (Task 8) |

## How to Run

### Prerequisites
- Python 3 installed
- Installed required libraries:

```bash
pip install matplotlib numpy
```

### Running individual tasks
Navigate to the `weekly-tasks/` folder and run any script:

```bash
python bank.py
python collatz.py
python weekday.py
python squareroot.py
```

**Weekly Task 7 requires a filename as a command-line argument:**
```bash
python week07/es.py test.txt
```

**Weekly Task will dislay a plot window and save a `plot.png` file:**
```bash
python plottask.py
```

## Labs
The Labs/ folder contains guided lab exercises, based on materials and code provided by lecturer.

## Author
Aiswaria Lajan

