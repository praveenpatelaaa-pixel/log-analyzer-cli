import sys
import re

# 1. taking a file name to terminal
file_name = sys.argv[1]

# 2. to count error
error_count = 0

# 3. list a error message
error_messages = []

# 4. opening a file
with open(file_name, "r") as file:
    for line in file:
        # if error in a line
        if "[ERROR]" in line:
            error_count += 1

            # [ERROR] taking out the message after error
            message = re.search(r"\[ERROR\]\s+(.*)", line)
            if message:
                error_messages.append(message.group(1))

# 5. printing theresult
print("Total Errors:", error_count)
print("Error Messages:")
for msg in error_messages:

    print("-", msg)

