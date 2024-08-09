# README: CELL 02

Welcome to the Python exercises repository! This README provides details about the exercises and files included in this directory. These exercises are designed to help you practice basic Python concepts such as input handling, conditionals, and arithmetic operations.

## Table of Contents

1. [Exercise Descriptions](#exercise-descriptions)
   - [Exercise iszero.py](#exercise-iszeropy)
   - [Exercise isneg.py](#exercise-isnegpy)
   - [Exercise password.py](#exercise-passwordpy)
   - [Exercise mult.py](#exercise-multpy)
2. [How to Run the Exercises](#how-to-run-the-exercises)
3. [Additional Information](#additional-information)

## Exercise Descriptions

### Exercise iszero.py

**Description:**
This exercise checks if a given number is zero or not and prints an appropriate message. It also handles non-numeric inputs.

**File:** `iszero.py`


**Expected Output:**
- If the input number is `0`: `This number is equal to zero.`
- If the input number is non-zero: `This number is different from zero.`
- If the input is not a number: `Oops! Número inválido. Tente novamente...`


### Exercise isneg.py

**Description:**
This exercise determines whether a given number is positive, negative, or zero and prints the result. It also handles non-numeric inputs.

**File:** `isneg.py`


**Expected Output:**
- If the input number is `0`: `This number is both positive and negative.`
- If the input number is negative: `This number is negative.`
- If the input number is positive: `This number is positive.`
- If the input is not a number: `Oops! Número inválido. Tente novamente...`

**Explanation:**
- The script uses conditional statements to classify the number as positive, negative, or zero and handles invalid inputs.

### Exercise password.py

**Description:**
This exercise checks if the input password matches a predefined password and prints a corresponding message.

**File:** `password.py`

**Expected Output:**
- If the input matches the password: `ACCESS GRANTED.`
- If the input does not match the password: `ACCESS DENIED.`

### Exercise mult.py

**Description:**
This exercise performs multiplication on two user-provided numbers and prints the result along with a message about the result's sign.

**File:** `mult.py`

**Expected Output:**
- Displays the result of the multiplication along with a message about the result's sign:
  - `The result is positive and negative.` if the result is `0`
  - `The result is positive.` if the result is greater than `0`
  - `The result is negative.` if the result is less than `0`


## How to Run the Exercises

1. **Download the Files:**
   - Clone the repository or download the files from this directory.

2. **Save the Files:**
   - Ensure each file (`iszero.py`, `isneg.py`, `password.py`, and `mult.py`) is saved in a directory on your local machine.

3. **Open a Terminal or Command Prompt:**
   - Navigate to the directory where the files are saved.

4. **Run the Code:**
   - Execute each file using the Python interpreter with the following commands:
     ```bash
     chmod +x iszero.py
     ./iszero.py
     ```
     ```bash
     chmod +x isneg.py
     ./isneg.py     
     ```
     ```bash
     chmod +x password.py
     ./password.py
     ```
     ```bash
     chmod +x mult.py
     ./mult.py
     ```

5. **View the Output:**
   - The output will be displayed in your terminal or command prompt.

## Additional Information

- **Python Version:** These exercises are compatible with Python 3.x.
- **Learning Objectives:** These exercises help in understanding input handling, conditional statements, string comparison, and basic arithmetic operations.
