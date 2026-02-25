# Break and continue statement in For Loops

# Break statement is used to exit/terminate the loop completely
# when a certain condition is met

print("=" * 50)
print("Example 1: Break Statement")
print("=" * 50)

for i in range(12):
    print("5 x", i, "=", 5 * i)
    if (i == 8):
        print("The iteration breaks at i = 8")
        break
    # The break statement exits from the loop when condition becomes true

print("\n" + "=" * 50)
print("Example 2: Break in Search")
print("=" * 50)

# Finding a number in a list
numbers = [10, 20, 30, 40, 50, 60, 70]
search_for = 40

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}! Stopping search.")
        break
    print(f"Checking {num}...")

# ====================
# 2. CONTINUE STATEMENT
# ====================
# Continue statement skips the current iteration and moves to the next one
# The loop does NOT terminate, it just skips the rest of the code for that iteration

print("\n" + "=" * 50)
print("Example 3: Continue Statement")
print("=" * 50)

for w in range(12):
    if (w == 5):
        print(f"Skipping w = {w}")
        continue
    # It skips the current iteration and continues with the next one
    print("5 x", w, "=", 5 * w)

print("\n" + "=" * 50)
print("Example 4: Continue with Even/Odd")
print("=" * 50)

# Print only odd numbers
for num in range(1, 11):
    if num % 2 == 0:  # If even number
        continue  # Skip even numbers
    print(f"{num} is odd")

# ====================
# 3. COMBINING BREAK AND CONTINUE
# ====================

print("\n" + "=" * 50)
print("Example 5: Break + Continue Together")
print("=" * 50)

# Print odd numbers but stop at 15
for num in range(1, 21):
    if num > 15:
        print(f"Stopping at {num}")
        break
    if num % 2 == 0:
        continue
    print(f"{num} is odd")

# ====================
# 4. NESTED LOOPS WITH BREAK
# ====================

print("\n" + "=" * 50)
print("Example 6: Break in Nested Loop")
print("=" * 50)

for i in range(1, 4):
    print(f"\nOuter loop: i = {i}")
    for j in range(1, 6):
        if j == 4:
            print(f"  Breaking inner loop at j = {j}")
            break
        print(f"  Inner loop: j = {j}")

# ====================
# KEY POINTS
# ====================
print("\n" + "=" * 50)
print("Summary:")
print("=" * 50)
print("✓ BREAK: Exits the loop completely")
print("✓ CONTINUE: Skips current iteration, moves to next")
print("✓ FOR loop: Used when we know the number of iterations")
print("✓ WHILE loop: Used when we don't know the number of iterations")
print("=" * 50)

