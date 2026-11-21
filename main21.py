def gcd(a, b):
    
    return a


def lcm(a, b):
    return 0  


def together_times(a, b, how_many):
    step = lcm(a, b)
    times = []
    return times


for a, b in [(12, 18), (10, 15), (7, 5), (20, 80)]:
    print(f"Every {a} and every {b} minutes: together again after {lcm(a, b)} minutes;"
          f" next 4 times: {together_times(a, b, 4)}")

print()
try:
    text = input("Type two bus gaps in minutes, like 12 18 (or press Enter to finish): ")
except EOFError:
    text = ""
parts = text.split()
if not parts:
    print("No gaps typed: demo only.")
elif len(parts) != 2 or not all(p.isdecimal() and len(p) <= 6 and int(p) > 0 for p in parts):
    print("Please type two whole numbers of minutes, each from 1 to 999999.")
else:
    a, b = int(parts[0]), int(parts[1])
    print(f"Every {a} and every {b} minutes: together again after {lcm(a, b)} minutes.")
print("Time: O(log min(a, b)) for gcd and lcm. Extra space: O(1).")
