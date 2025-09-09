# File Read & Write Challenge
try:
    # Open original file for reading
    with open("input.txt", "r") as f:
        content = f.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write to a new file
    with open("output.txt", "w") as f:
        f.write(modified_content)

    print("✅ File processed! Modified version saved as output.txt")

except FileNotFoundError:
    print("❌ input.txt not found. Please make sure the file exists.")

# Error Handling Lab
filename = input("Read challeng: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("✅ File content successfully read!")
        print(content)

except FileNotFoundError:
    print("❌ The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("❌ Permission denied. You don’t have access to this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
