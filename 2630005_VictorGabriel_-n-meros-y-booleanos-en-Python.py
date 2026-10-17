# =============================================================================
# COVER PAGE
# =============================================================================
# Name:      VICTOR GABRIEL HERNANDEZ LUGO
# Student ID: 263005
# Group:     ______ (write your group here)
# Topic:     Numeric types (int, float) and booleans in Python
# GitHub:    https://github.com/v1592/2630005_VictorGabriel_strings.py
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================
# In Python, int stores whole numbers (age, hours, items) and float stores
# numbers with decimals (temperature, salary, BMI). They differ in precision:
# an int is exact, while a float is an approximation, so results are usually
# rounded with round() before showing them. A boolean (bool) can only be True
# or False and is produced by comparisons (<, >, <=, >=, ==, !=) and combined
# with and, or, not. Validating ranges and avoiding division by zero is vital,
# because wrong or impossible data produces wrong results or crashes.
# This document contains 6 problems: temperature converter, overtime payment,
# discount eligibility, statistics of three integers, loan eligibility and
# BMI. Each one documents its inputs, outputs, validations and 3 test cases
# (normal, border, error), and uses int, float and bool to make decisions.

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES
# =============================================================================
# - Use the right type: int for counters, float for values with decimals.
# - Avoid repeating complex expressions: store intermediate results.
# - Validate data before operating (hours and salaries cannot be negative).
# - Use descriptive variable names and clear messages for the user.
# - Document what a boolean means (what True and False represent) in each
#   problem.

import math

# Constants (UPPER_SNAKE_CASE)
ERROR_MESSAGE = "Error: invalid input"
HIGH_TEMPERATURE_LIMIT = 30.0
REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_TOTAL_LIMIT = 1000.0
DISCOUNT_FACTOR = 0.9
MIN_LOAN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0


# -----------------------------------------------------------------------------
# Helper functions (shared by all problems)
# -----------------------------------------------------------------------------
def parse_float(value):
    """Convert value to a finite float, or return None if it is not possible."""
    try:
        number = float(str(value).strip())
    except ValueError:
        return None
    if not math.isfinite(number):  # rejects nan and inf
        return None
    return number


def parse_int(value):
    """Convert value to int, or return None. '3.5' is NOT a valid integer."""
    try:
        return int(str(value).strip())
    except ValueError:
        return None


def bool_text(flag):
    """Show a bool as 'true' or 'false' (lowercase)."""
    return str(flag).lower()


# =============================================================================
# Problem 1: Temperature converter and range flag
# =============================================================================
# Description: Converts a temperature from Celsius to Fahrenheit and Kelvin.
#   It also builds the boolean is_high_temperature: True when temp_c >= 30.0.
#
# Inputs:
# - temp_c (float): temperature in degrees Celsius.
#
# Outputs:
# - "Fahrenheit: <temp_f>", "Kelvin: <temp_k>", "High temperature: true|false"
#
# Validations:
# - temp_c must be convertible to float.
# - temp_k cannot be below 0.0 (physically impossible).
#
# Boolean meaning: is_high_temperature True = 30.0 C or more.
#
# Test cases:
# 1) Normal: 35 -> Fahrenheit: 95.00, Kelvin: 308.15, High temperature: true
# 2) Border: 30.0 -> High temperature: true (limit included);
#            -273.15 -> Kelvin: 0.00 (lowest valid value)
# 3) Error:  "abc" or -300 (Kelvin would be negative) -> Error: invalid input

def convert_temperature(temp_c_text):
    """Return (temp_f, temp_k, is_high_temperature) or None if invalid."""
    temp_c = parse_float(temp_c_text)
    if temp_c is None:
        return None
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        return None
    is_high_temperature = temp_c >= HIGH_TEMPERATURE_LIMIT
    return temp_f, temp_k, is_high_temperature


def run_problem_1(temp_c_text):
    print(f"Input: {temp_c_text}")
    result = convert_temperature(temp_c_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    temp_f, temp_k, is_high_temperature = result
    print(f"Fahrenheit: {temp_f:.2f}")
    print(f"Kelvin: {temp_k:.2f}")
    print(f"High temperature: {bool_text(is_high_temperature)}")


# =============================================================================
# Problem 2: Work hours and overtime payment
# =============================================================================
# Description: Computes the weekly pay. Up to 40 hours are paid at
#   hourly_rate; extra hours (> 40) are paid at 150% of the rate.
#
# Inputs:
# - hours_worked (float), hourly_rate (float).
#
# Outputs:
# - "Regular pay: ...", "Overtime pay: ...", "Total pay: ...",
#   "Has overtime: true|false"
#
# Validations:
# - hours_worked >= 0 and hourly_rate > 0.
#
# Boolean meaning: has_overtime True = worked more than 40 hours.
#
# Test cases:
# 1) Normal: 45 hours, rate 100 -> Regular 4000.00, Overtime 750.00,
#            Total 4750.00, Has overtime: true
# 2) Border: 40 hours, rate 100 -> Overtime 0.00, Has overtime: false
# 3) Error:  -5 hours, rate 100 / 40 hours, rate 0 -> Error: invalid input

def calculate_pay(hours_text, rate_text):
    """Return (regular_pay, overtime_pay, total_pay, has_overtime) or None."""
    hours_worked = parse_float(hours_text)
    hourly_rate = parse_float(rate_text)
    if hours_worked is None or hourly_rate is None:
        return None
    if hours_worked < 0 or hourly_rate <= 0:
        return None
    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT
    return regular_pay, overtime_pay, total_pay, has_overtime


def run_problem_2(hours_text, rate_text):
    print(f"Input: hours={hours_text}, rate={rate_text}")
    result = calculate_pay(hours_text, rate_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    regular_pay, overtime_pay, total_pay, has_overtime = result
    print(f"Regular pay: {regular_pay:.2f}")
    print(f"Overtime pay: {overtime_pay:.2f}")
    print(f"Total pay: {total_pay:.2f}")
    print(f"Has overtime: {bool_text(has_overtime)}")


# =============================================================================
# Problem 3: Discount eligibility with booleans
# =============================================================================
# Description: A customer gets a 10% discount if is_student OR is_senior OR
#   purchase_total >= 1000.0. Shows eligibility and the final total.
#
# Inputs:
# - purchase_total (float), is_student_text ("YES"/"NO"),
#   is_senior_text ("YES"/"NO").
#
# Outputs:
# - "Discount eligible: true|false", "Final total: <final_total>"
#
# Validations:
# - purchase_total >= 0.0.
# - Texts are normalized with strip() and upper(); anything other than
#   "YES" or "NO" is an error.
#
# Boolean meaning: discount_eligible True = the 10% discount is applied.
#
# Test cases:
# 1) Normal: 500, "yes", "no" -> Discount eligible: true, Final total: 450.00
# 2) Border: 1000, "NO", "NO" -> true (limit included), Final total: 900.00;
#            999.99, "NO", "NO" -> false, Final total: 999.99
# 3) Error:  500, "maybe", "no" / -10, "yes", "no" -> Error: invalid input

def yes_no_to_bool(text):
    """Return True for 'YES', False for 'NO', None for anything else."""
    normalized_text = str(text).strip().upper()
    if normalized_text == "YES":
        return True
    if normalized_text == "NO":
        return False
    return None


def calculate_discount(total_text, student_text, senior_text):
    """Return (discount_eligible, final_total) or None if invalid."""
    purchase_total = parse_float(total_text)
    is_student = yes_no_to_bool(student_text)
    is_senior = yes_no_to_bool(senior_text)
    if purchase_total is None or purchase_total < 0.0:
        return None
    if is_student is None or is_senior is None:
        return None
    discount_eligible = (is_student or is_senior
                         or purchase_total >= DISCOUNT_TOTAL_LIMIT)
    if discount_eligible:
        final_total = purchase_total * DISCOUNT_FACTOR
    else:
        final_total = purchase_total
    return discount_eligible, final_total


def run_problem_3(total_text, student_text, senior_text):
    print(f'Input: total={total_text}, student="{student_text}", '
          f'senior="{senior_text}"')
    result = calculate_discount(total_text, student_text, senior_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    discount_eligible, final_total = result
    print(f"Discount eligible: {bool_text(discount_eligible)}")
    print(f"Final total: {final_total:.2f}")


# =============================================================================
# Problem 4: Basic statistics of three integers
# =============================================================================
# Description: Reads three integers and calculates the sum, the average
#   (float), the maximum, the minimum and whether all three are even.
#
# Inputs:
# - n1, n2, n3 (int). Negative numbers are allowed.
#
# Outputs:
# - "Sum: ...", "Average: ...", "Max: ...", "Min: ...",
#   "All even: true|false"
#
# Validations:
# - The three values must be convertible to int ("3.5" is not an int).
#
# Boolean meaning: all_even True = n1, n2 and n3 are all divisible by 2.
#
# Test cases:
# 1) Normal: 4, 7, 10 -> Sum 21, Average 7.00, Max 10, Min 4, All even: false
# 2) Border: -2, -4, -6 (all negative and even) -> Sum -12, Average -4.00,
#            Max -2, Min -6, All even: true; 0, 0, 0 -> All even: true
# 3) Error:  "abc", 2, 3 / 2.5, 2, 3 -> Error: invalid input

def calculate_three_stats(n1_text, n2_text, n3_text):
    """Return a dict with the statistics or None if invalid."""
    n1 = parse_int(n1_text)
    n2 = parse_int(n2_text)
    n3 = parse_int(n3_text)
    if n1 is None or n2 is None or n3 is None:
        return None
    sum_value = n1 + n2 + n3
    return {
        "sum": sum_value,
        "average": sum_value / 3,
        "max": max(n1, n2, n3),
        "min": min(n1, n2, n3),
        "all_even": (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0),
    }


def run_problem_4(n1_text, n2_text, n3_text):
    print(f"Input: {n1_text}, {n2_text}, {n3_text}")
    stats = calculate_three_stats(n1_text, n2_text, n3_text)
    if stats is None:
        print(ERROR_MESSAGE)
        return
    print(f"Sum: {stats['sum']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Max: {stats['max']}")
    print(f"Min: {stats['min']}")
    print(f"All even: {bool_text(stats['all_even'])}")


# =============================================================================
# Problem 5: Loan eligibility (income and debt ratio)
# =============================================================================
# Description: Decides if a person is eligible for a loan using
#   debt_ratio = monthly_debt / monthly_income. Eligible is True when:
#   monthly_income >= 8000.0 AND debt_ratio <= 0.4 AND credit_score >= 650.
#
# Inputs:
# - monthly_income (float), monthly_debt (float), credit_score (int).
#
# Outputs:
# - "Debt ratio: <debt_ratio>", "Eligible: true|false"
#
# Validations:
# - monthly_income > 0.0 (avoids division by zero).
# - monthly_debt >= 0.0 and credit_score >= 0.
#
# Boolean meaning: eligible True = the three conditions are all met.
#
# Test cases:
# 1) Normal: 20000, 5000, 700 -> Debt ratio 0.25, Eligible: true
# 2) Border: 8000, 3200, 650 (every limit exactly) -> Debt ratio 0.40,
#            Eligible: true; 8000, 5000, 700 -> Debt ratio 0.62, false
# 3) Error:  income 0 (division by zero) / debt -100 -> Error: invalid input

def check_loan(income_text, debt_text, score_text):
    """Return (debt_ratio, eligible) or None if invalid."""
    monthly_income = parse_float(income_text)
    monthly_debt = parse_float(debt_text)
    credit_score = parse_int(score_text)
    if monthly_income is None or monthly_debt is None or credit_score is None:
        return None
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        return None
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_LOAN_INCOME
                and debt_ratio <= MAX_DEBT_RATIO
                and credit_score >= MIN_CREDIT_SCORE)
    return debt_ratio, eligible


def run_problem_5(income_text, debt_text, score_text):
    print(f"Input: income={income_text}, debt={debt_text}, "
          f"score={score_text}")
    result = check_loan(income_text, debt_text, score_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    debt_ratio, eligible = result
    print(f"Debt ratio: {debt_ratio:.2f}")
    print(f"Eligible: {bool_text(eligible)}")


# =============================================================================
# Problem 6: Body Mass Index (BMI) and category flag
# =============================================================================
# Description: Calculates bmi = weight_kg / (height_m * height_m) and creates
#   booleans for the category: underweight (bmi < 18.5), normal
#   (18.5 <= bmi < 25.0) and overweight (bmi >= 25.0).
#
# Inputs:
# - weight_kg (float), height_m (float).
#
# Outputs:
# - "BMI: <rounded to 2 decimals>", "Underweight: ...", "Normal: ...",
#   "Overweight: ..."
#
# Validations:
# - weight_kg > 0.0 and height_m > 0.0.
#
# Boolean meaning: exactly one of the three flags is true for any valid BMI.
# The comparisons use the unrounded BMI, and round() is only for display.
#
# Test cases:
# 1) Normal: 70 kg, 1.75 m -> BMI 22.86, Normal: true
# 2) Border: 74 kg, 2.0 m -> BMI 18.50, Normal: true (lower limit included);
#            100 kg, 2.0 m -> BMI 25.00, Overweight: true
# 3) Error:  0 kg, 1.75 m / 70 kg, 0 m -> Error: invalid input

def calculate_bmi(weight_text, height_text):
    """Return (bmi, is_underweight, is_normal, is_overweight) or None."""
    weight_kg = parse_float(weight_text)
    height_m = parse_float(height_text)
    if weight_kg is None or height_m is None:
        return None
    if weight_kg <= 0.0 or height_m <= 0.0:
        return None
    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT
    return bmi, is_underweight, is_normal, is_overweight


def run_problem_6(weight_text, height_text):
    print(f"Input: weight={weight_text}, height={height_text}")
    result = calculate_bmi(weight_text, height_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    bmi, is_underweight, is_normal, is_overweight = result
    print(f"BMI: {round(bmi, 2):.2f}")
    print(f"Underweight: {bool_text(is_underweight)}")
    print(f"Normal: {bool_text(is_normal)}")
    print(f"Overweight: {bool_text(is_overweight)}")


# =============================================================================
# TEST RUNNER
# =============================================================================
def print_title(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    print_title("Problem 1: Temperature converter")
    run_problem_1("35")          # normal
    run_problem_1("30.0")        # border (limit)
    run_problem_1("-273.15")     # border (absolute zero)
    run_problem_1("abc")         # error (not a number)
    run_problem_1("-300")        # error (Kelvin below zero)

    print_title("Problem 2: Overtime payment")
    run_problem_2("45", "100")   # normal
    run_problem_2("40", "100")   # border (no overtime)
    run_problem_2("-5", "100")   # error (negative hours)
    run_problem_2("40", "0")     # error (rate must be > 0)

    print_title("Problem 3: Discount eligibility")
    run_problem_3("500", "yes", "no")      # normal
    run_problem_3("1000", "NO", "NO")      # border (exactly 1000)
    run_problem_3("999.99", "NO", "NO")    # border (just below)
    run_problem_3("500", "maybe", "no")    # error (invalid text)
    run_problem_3("-10", "yes", "no")      # error (negative total)

    print_title("Problem 4: Statistics of three integers")
    run_problem_4("4", "7", "10")          # normal
    run_problem_4("-2", "-4", "-6")        # border (negatives, all even)
    run_problem_4("0", "0", "0")           # border (zeros)
    run_problem_4("abc", "2", "3")         # error (not a number)
    run_problem_4("2.5", "2", "3")         # error (not an integer)

    print_title("Problem 5: Loan eligibility")
    run_problem_5("20000", "5000", "700")  # normal
    run_problem_5("8000", "3200", "650")   # border (every limit exactly)
    run_problem_5("8000", "5000", "700")   # not eligible (ratio too high)
    run_problem_5("0", "500", "700")       # error (division by zero)
    run_problem_5("9000", "-100", "700")   # error (negative debt)

    print_title("Problem 6: Body Mass Index (BMI)")
    run_problem_6("70", "1.75")            # normal
    run_problem_6("74", "2.0")             # border (BMI = 18.5)
    run_problem_6("100", "2.0")            # border (BMI = 25.0)
    run_problem_6("0", "1.75")             # error (weight must be > 0)
    run_problem_6("70", "0")               # error (height must be > 0)


if __name__ == "__main__":
    main()


# =============================================================================
# CONCLUSIONS
# =============================================================================
# Integers and floats work together in real calculations: for example, hours
# (float) multiplied by a rate (float) and compared with limits, or averages
# (float) computed from integers. Comparisons produce booleans, and those
# booleans let a program decide what to do with if statements. Validating
# ranges and avoiding divisions by zero (such as monthly_income = 0 in the
# loan problem) prevents crashes and impossible results. I learned that
# conditions combined with and, or and not must be designed carefully, and
# that limits like >= and <= matter in the border cases. These patterns are
# repeated in payroll, discounts, loans and health calculations.

# =============================================================================
# REFERENCES
# =============================================================================
# References:
# 1) Python documentation - Built-in Types: Numeric Types - int, float, complex
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type - bool
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python documentation - Built-in Functions: round(), min(), max()
#    https://docs.python.org/3/library/functions.html
# 4) Python Tutorial - An Informal Introduction to Python (numbers)
#    https://docs.python.org/3/tutorial/introduction.html#numbers
# 5) Python documentation - Floating-Point Arithmetic: Issues and Limitations
#    https://docs.python.org/3/tutorial/floatingpoint.html
# 6) PEP 8 - Style Guide for Python Code (naming conventions)
#    https://peps.python.org/pep-0008/