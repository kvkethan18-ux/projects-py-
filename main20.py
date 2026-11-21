def binary_to_decimal(bits):
    """Return (value, steps), or (None, 0) if bits is empty or has a digit other than 0 or 1."""
    bits = bits.strip()
    if bits == "":
        return None, 0
    value = 0
    steps = 0
    for digit in bits:
        return value, steps

for bits in ["1101", "010", "1000", "11111111", "1012", ""]:
    value, steps = binary_to_decimal(bits)
    if value is None:
        print(f"  '{bits}' is not a binary number (use only 0 and 1)")
    else:
        print(f"{bits:>12} -> {value:<4} steps = {steps}")
print()
print("Time: O(L) for L binary digits (one step per digit). Extra space: O(1).")
