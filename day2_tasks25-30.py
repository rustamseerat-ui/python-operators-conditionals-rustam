# DAY 2 – BIG PRACTICAL SECTION

# ===== TASK 25 – COMBINED OPERATORS =====
print("=" * 40)
print("TASK 25 – COMBINED OPERATORS")
print("=" * 40)
num1 = 10
num2 = 3
print(f"Numbers: {num1} and {num2}")
print("=" * 30)
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"\nEven/Odd check:")
print(f"{num1} is {'even' if num1 % 2 == 0 else 'odd'}")
print(f"{num2} is {'even' if num2 % 2 == 0 else 'odd'}")

# ===== TASK 26 – BINARY + LAMBDA =====
print("\n" + "=" * 40)
print("TASK 26 – BINARY + LAMBDA")
print("=" * 40)
numbers = [3, 5, 12, 7]
doubled = list(map(lambda x: x * 2, numbers))
print("Original:", numbers)
print("Doubled :", doubled)
print("\nBinary representations:")
for num in numbers:
    print(f"{num:2} -> binary: {bin(num)}")

# ===== TASK 27 – STRING + LOGIC + CASTING =====
print("\n" + "=" * 40)
print("TASK 27 – STRING + LOGIC + CASTING")
print("=" * 40)
birth_year_str = "2000"
current_year = 2025
birth_year = int(birth_year_str)
age = current_year - birth_year
category = "minor" if age < 18 else "adult"
print(f"Birth year (string): '{birth_year_str}'")
print(f"Birth year (int): {birth_year}")
print(f"Current year: {current_year}")
print(f"Age: {age}")
print(f"Classification: {category}")

# ===== TASK 28 – OPERATOR PRECEDENCE =====
print("\n" + "=" * 40)
print("TASK 28 – OPERATOR PRECEDENCE")
print("=" * 40)
print("Step-by-step calculation:")
print("1. Inside first parentheses: 10 + 3 * 5")
print("   Multiplication first: 3 * 5 =", 3 * 5)
print("   Then addition: 10 + 15 =", 10 + 15)
first_part = 10 + 3 * 5
print("   Result:", first_part)

print("\n2. Inside second parentheses: 4 % 3 + 1")
print("   Modulo first: 4 % 3 =", 4 % 3)
print("   Then addition: 1 + 1 =", 1 + 1)
second_part = 4 % 3 + 1
print("   Result:", second_part)

print("\n3. Exponentiation: (25) ** 2 =", first_part ** 2)

print("\n4. Division: 625 / 2 =", first_part ** 2 / second_part)

result = (10 + 3 * 5) ** 2 / (4 % 3 + 1)
print(f"\nFinal result: (10 + 3 * 5) ** 2 / (4 % 3 + 1) = {result}")

# ===== TASK 29 – CONDITIONAL CALCULATOR =====
print("\n" + "=" * 40)
print("TASK 29 – CONDITIONAL CALCULATOR")
print("=" * 40)
test_cases = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 5, "/"),
    (10, 0, "/"),
]

for num1, num2, operator in test_cases:
    print(f"\nCalculator: {num1} {operator} {num2}")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"
    
    print(f"Result: {result}")

# ===== TASK 30 – MINI PROGRAM =====
print("\n" + "=" * 40)
print("TASK 30 – MINI PROGRAM")
print("=" * 40)
# Student Grade Analyzer
student_name = "Alice"
scores = [85.5, 92.0, 78.5, 88.0]

# Arithmetic: Calculate average
average_score = sum(scores) / len(scores)

# Rounding
rounded_avg = round(average_score, 1)

# Lambda: Convert score to letter grade
grade_converter = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# Logical operators: Check conditions
has_passing_grade = rounded_avg >= 60
has_honors = rounded_avg >= 85

# Conditional output
status = "PASS" if has_passing_grade else "FAIL"
honors_status = "with Honors" if has_honors else ""

# Formatted summary
print("=" * 40)
print("STUDENT GRADE ANALYSIS")
print("=" * 40)
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Average Score: {average_score:.2f} → rounded: {rounded_avg}")
print(f"Letter Grade: {grade_converter(rounded_avg)}")
print(f"Status: {status} {honors_status}")
print("=" * 40)

print("\n" + "=" * 40)
print("ALL 30 TASKS COMPLETED SUCCESSFULLY! 🎉")
print("=" * 40)
