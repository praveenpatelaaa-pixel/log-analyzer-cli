import sys
import re

# 1. file name lena (terminal se)
file_name = sys.argv[1]

# 2. error count
error_count = 0

# 3. error messages list
error_messages = []

# 4. file open karna
with open(file_name, "r") as file:
    for line in file:
        # agar line me [ERROR] hai
        if "[ERROR]" in line:
            error_count += 1

            # [ERROR] ke baad ka message nikalna
            message = re.search(r"\[ERROR\]\s+(.*)", line)
            if message:
                error_messages.append(message.group(1))

# 5. result print karna
print("Total Errors:", error_count)
print("Error Messages:")
for msg in error_messages:
    print("-", msg)