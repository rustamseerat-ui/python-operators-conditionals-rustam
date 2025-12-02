# DAY 2 – Operators, Casting, Rounding, Conditionals

# ===== TASK 12 – OPERATORS 5 =====
print("=" * 40)
print("TASK 12 – OPERATORS 5")
print("=" * 40)
x = 15
y = 4
print(f"x // y = {x // y}")
print(f"x % y = {x % y}")
print(f"(x + y) * (x - y) = {(x + y) * (x - y)}")

# ===== TASK 13 – OPERATORS 6 =====
print("\n" + "=" * 40)
print("TASK 13 – OPERATORS 6")
print("=" * 40)
a, b, c = 10, 20, 30
average = (a + b + c) / 3
print(f"Numbers: {a}, {b}, {c}")
print(f"Average: {average}")

# ===== TASK 14 – OPERATORS 7 =====
print("\n" + "=" * 40)
print("TASK 14 – OPERATORS 7")
print("=" * 40)
price_a = 4.99
price_b = 7.49
tax_rate = 0.12
subtotal = price_a + price_b
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
print(f"Price A: ${price_a:.2f}")
print(f"Price B: ${price_b:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({tax_rate*100}%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")

# ===== TASK 15 – OPERATORS 8 =====
print("\n" + "=" * 40)
print("TASK 15 – OPERATORS 8")
print("=" * 40)
P = 1000
r = 0.05
t = 3
A = P * (1 + r) ** t
print(f"Principal: ${P}")
print(f"Annual rate: {r*100}%")
print(f"Time: {t} years")
print(f"Final amount: ${A:.2f}")

# ===== TASK 16 – CASTING =====
print("\n" + "=" * 40)
print("TASK 16 – CASTING")
print("=" * 40)
num_str = "123"
num_int = int(num_str)
print(f'"{num_str}" as integer: {num_int} (type: {type(num_int)})')
float_str = "45.9"
num_float = float(float_str)
print(f'"{float_str}" as float: {num_float} (type: {type(num_float)})')
number = 100
num_string = str(number)
print(f'{number} as string: "{num_string}" (type: {type(num_string)})')

# ===== TASK 17 – CASTING PRACTICE =====
print("\n" + "=" * 40)
print("TASK 17 – CASTING PRACTICE")
print("=" * 40)
age_str = "25"
age_int = int(age_str)
future_age = age_int + 5
print(f"Current age (as string): '{age_str}'")
print(f"Current age (as integer): {age_int}")
print(f"Age after 5 years: {future_age}")

# ===== TASK 18 – ROUNDING =====
print("\n" + "=" * 40)
print("TASK 18 – ROUNDING")
print("=" * 40)
num = 4.456
print(f"Original: {num}")
print(f"Nearest integer: {round(num)}")
print(f"1 decimal place: {round(num, 1)}")
print(f"2 decimal places: {round(num, 2)}")

# ===== TASK 19 – ROUNDING PRACTICE =====
print("\n" + "=" * 40)
print("TASK 19 – ROUNDING PRACTICE")
print("=" * 40)
numbers = [4.67, 5.12, 3.49]
rounded = [round(num, 1) for num in numbers]
print(f"Original: {numbers}")
print(f"Rounded (1 decimal): {rounded}")

# ===== TASK 20 – CONDITIONAL STATEMENTS BASIC =====
print("\n" + "=" * 40)
print("TASK 20 – CONDITIONAL STATEMENTS BASIC")
print("=" * 40)
score = 78
if score >= 60:
    print(f"Score: {score} - PASS")
else:
    print(f"Score: {score} - FAIL")

# ===== TASK 21 – CONDITIONAL CHAINS =====
print("\n" + "=" * 40)
print("TASK 21 – CONDITIONAL CHAINS")
print("=" * 40)
temp = 22
if temp < 0:
    category = "freezing"
elif temp <= 15:
    category = "cold"
elif temp <= 25:
    category = "warm"
else:
    category = "hot"
print(f"Temperature: {temp}°C - {category}")

# ===== TASK 22 – CONDITIONAL & OPERATORS =====
print("\n" + "=" * 40)
print("TASK 22 – CONDITIONAL & OPERATORS")
print("=" * 40)
age = 20
has_id = True
if age >= 18 and has_id:
    print(f"Age: {age}, Has ID: {has_id} - ENTRY ALLOWED")
else:
    print(f"Age: {age}, Has ID: {has_id} - ENTRY DENIED")

# ===== TASK 23 – NESTED CONDITIONALS =====
print("\n" + "=" * 40)
print("TASK 23 – NESTED CONDITIONALS")
print("=" * 40)
income = 45000
credit_score = 720
if income >= 30000:
    if credit_score >= 700:
        print(f"Income: ${income}, Credit: {credit_score} - LOAN APPROVED")
    else:
        print(f"Income: ${income}, Credit: {credit_score} - LOAN DENIED (bad credit)")
else:
    print(f"Income: ${income}, Credit: {credit_score} - LOAN DENIED (low income)")

# ===== TASK 24 – MINI PROJECT – CONDITIONALS =====
print("\n" + "=" * 40)
print("TASK 24 – MINI PROJECT – CONDITIONALS")
print("=" * 40)
correct_username = "admin"
correct_password = "secret123"

print("Test 1 - Correct credentials:")
input_username = "admin"
input_password = "secret123"
if input_username == correct_username and input_password == correct_password:
    print("Login SUCCESSFUL!")
else:
    print("Login FAILED - incorrect username or password")

print("\nTest 2 - Incorrect credentials:")
input_username = "user"
input_password = "wrong"
if input_username == correct_username and input_password == correct_password:
    print("Login SUCCESSFUL!")
else:
    print("Login FAILED - incorrect username or password")
