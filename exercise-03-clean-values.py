## Exercise 3: Clean Values

raw_values = [100, None, 250, "invalid", 300, None, 450]

# --- Solution 1: Using a loop, continue, and isinstance() ---
valid_integers_loop = []

for val in raw_values:
    # Skip if the value is not an integer (this automatically filters out None and strings)
    # Note: In Python, bool is a subclass of int, but our list doesn't have booleans. 
    # isinstance(val, int) is standard here.
    if not isinstance(val, int):
        continue
    valid_integers_loop.append(val)

print("Cleaned list using a loop:", valid_integers_loop)


# --- Solution 2: Using a list comprehension ---
for val in raw_values:
    if isinstance(val, int):
        valid_integers_comp = val

print("Cleaned list using list comprehension:", valid_integers_comp)