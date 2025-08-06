import os

# Folder where .txt files should be added
input_folder = "data_input"

# Sample file content
sample_content_1 = """# This is a comment
This is a temp file.
It contains some temp values.
# Ignore this comment line
Here is another line with temp."""

sample_content_2 = """# Another comment
temp data should be replaced.
This line is normal.
# Comment again
temp appears here too."""

# File paths
file1_path = os.path.join(input_folder, "file1.txt")
file2_path = os.path.join(input_folder, "file2.txt")

# Write content to files
with open(file1_path, "w") as f:
    f.write(sample_content_1)

with open(file2_path, "w") as f:
    f.write(sample_content_2)

print("Sample .txt files created successfully in 'data_input' folder.")
