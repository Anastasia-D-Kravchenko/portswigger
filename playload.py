import string

# Capture the output
output = ""

# Iterate through lowercase alphabet and capture output
for char in string.ascii_lowercase:
    output += char + "\n"  # Add newline for each character

# Iterate through numbers 0 to 9 and capture output
for i in range(10):
    output += str(i) + "\n" # Add newline for each number

# Write the captured output to the file "output.txt"
with open("output.txt", "w") as file:
    file.write(output)

print("Output written to output.txt")
