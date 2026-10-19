file_name = "class-notes.txt"

sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

with open(file_name, "w") as file:
    file.writelines(sample_notes)
print("Sample file 'class-notes.txt' created.")



print("\nPART 1: Preview with read(n)")
n = int(input("How many characters do you want to preview? "))
with open(file_name, "r") as file:
    print(file.read(n))
print()

print("\nPART 2: readlines()")
with open(file_name, "r") as file:
    lines = file.readlines()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

print("\nPART 3: Loop line by line")
for i, line in enumerate(lines, start=1):
    print("Reading", i, "->", line.strip())

print("\nPART 4: Filter with a condition")
important_lines = []
for line in lines:
    if "IMPORTANT:" in line:
        important_lines.append(line)
print("Important notes:")
for line in important_lines:
    print(line.strip())

print("\nPART 5: Copy selected lines to a new file")
important_file_name = "important-notes.txt"
with open(important_file_name, "w") as file:
    file.writelines(important_lines)
print("Important notes copied to", important_file_name)

print("\nPART 6: Organized notes")
categories = ["IMPORTANT:", "TODO:", "NOTE:", "SKIP:"]
for category in categories:
    print(category)
    for line in lines:
        if line.startswith(category):
            print("  -", line[len(category):].strip())
