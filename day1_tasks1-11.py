# DAY 1 – Logic, Binary, Lambda & Operator Precedence

# ===== TASK 1 – LOGIC OPERATORS =====
print("=" * 40)
print("TASK 1 – LOGIC OPERATORS")
print("=" * 40)
a = True
b = False
c = True
print("a AND b:", a and b)
print("b OR c:", b or c)
print("NOT a:", not a)
print("(a AND c) OR b:", (a and c) or b)

# ===== TASK 2 – LOGIC PRACTICE =====
print("\n" + "=" * 40)
print("TASK 2 – LOGIC PRACTICE")
print("=" * 40)
is_member = True
has_coupon = False
discount = is_member or has_coupon
print("Discount applies?", discount)

# ===== TASK 3 – BINARY OPERATORS =====
print("\n" + "=" * 40)
print("TASK 3 – BINARY OPERATORS")
print("=" * 40)
print("5 & 3 =", 5 & 3)
print("5 | 3 =", 5 | 3)
print("5 ^ 3 =", 5 ^ 3)
print("5 << 1 =", 5 << 1)
print("5 >> 1 =", 5 >> 1)

# ===== TASK 4 – BINARY CONVERSIONS =====
print("\n" + "=" * 40)
print("TASK 4 – BINARY CONVERSIONS")
print("=" * 40)
num = 10
binary_str = bin(num)
print(f"Binary of {num}: {binary_str}")
back_to_num = int(binary_str, 2)
print(f"Back to integer: {back_to_num}")

# ===== TASK 5 – LAMBDA OPERATORS =====
print("\n" + "=" * 40)
print("TASK 5 – LAMBDA OPERATORS")
print("=" * 40)
square = lambda x: x * x
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
print("Square of 5:", square(5))
print("Sum of 3 and 7:", add(3, 7))
print("Is 4 even?", is_even(4))
print("Is 5 even?", is_even(5))

# ===== TASK 6 – LAMBDA SORTING =====
print("\n" + "=" * 40)
print("TASK 6 – LAMBDA SORTING")
print("=" * 40)
people = [{"name": "Alice", "age": 25},
          {"name": "Bob", "age": 19},
          {"name": "Eve", "age": 30}]
sorted_by_age = sorted(people, key=lambda person: person["age"])
sorted_by_name = sorted(people, key=lambda person: person["name"])
print("Original:", people)
print("Sorted by age:", sorted_by_age)
print("Sorted by name:", sorted_by_name)

# ===== TASK 7 – OPERATOR PRECEDENCE =====
print("\n" + "=" * 40)
print("TASK 7 – OPERATOR PRECEDENCE")
print("=" * 40)
print("Step 1: 2 ** 2 =", 2 ** 2)
print("Step 2: 3 * 4 =", 3 * 4)
print("Step 3: 12 / 2 =", 12 / 2)
print("Step 4: 5 + 6.0 =", 5 + 6.0)
result = 5 + 3 * 2 ** 2 / 2
print(f"\nFinal result of 5 + 3 * 2 ** 2 / 2 = {result}")

# ===== TASK 8 – OPERATORS 1 =====
print("\n" + "=" * 40)
print("TASK 8 – OPERATORS 1")
print("=" * 40)
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# ===== TASK 9 – OPERATORS 2 =====
print("\n" + "=" * 40)
print("TASK 9 – OPERATORS 2")
print("=" * 40)
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(f"Weight: {weight} kg, Height: {height} m")
print(f"BMI: {bmi:.2f}")

# ===== TASK 10 – OPERATORS 3 =====
print("\n" + "=" * 40)
print("TASK 10 – OPERATORS 3")
print("=" * 40)
x = 5
print(f"Start: {x}")
print(f"After +10: {x + 10}")
print(f"After *3: {(x + 10) * 3}")
print(f"After -5: {((x + 10) * 3) - 5}")

# ===== TASK 11 – OPERATORS 4 =====
print("\n" + "=" * 40)
print("TASK 11 – OPERATORS 4")
print("=" * 40)
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swap: a = {a}, b = {b}")
