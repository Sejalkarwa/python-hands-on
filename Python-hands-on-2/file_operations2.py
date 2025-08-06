import os

# -------------------------------
# Step 1: Check/Create data_input folder
# -------------------------------
input_folder = "data_input"
output_folder = "data_output"

if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print(f"Folder '{input_folder}' created. Please add .txt files inside it and rerun the script.")
    exit()

# Create data_output if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# -------------------------------
# Step 2: Read all .txt files from data_input
# -------------------------------
txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

if not txt_files:
    print("No .txt files found in data_input folder. Please add some files and rerun.")
    exit()

# Prepare summary data
summary_data = []

# -------------------------------
# Step 3: Process each file
# -------------------------------
for file_name in txt_files:
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)

    line_count = 0
    word_count = 0
    modified_lines = []

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip().startswith("#"):  # Ignore comment lines
            continue

        # Count lines and words
        line_count += 1
        word_count += len(line.split())

        # Replace 'temp' with 'permanent'
        modified_line = line.replace("temp", "permanent")
        modified_lines.append(modified_line)

    # Write modified content to data_output
    with open(output_path, "w") as f:
        f.writelines(modified_lines)

    # Add to summary
    summary_data.append(f"{file_name}\tLines: {line_count}\tWords: {word_count}")

# -------------------------------
# Step 4: Create summary.txt in data_output
# -------------------------------
summary_path = os.path.join(output_folder, "summary.txt")
with open(summary_path, "w") as f:
    f.write("Filename\tLines\tWords\n")
    for entry in summary_data:
        f.write(entry + "\n")

print(f"Processing complete! Modified files and summary.txt saved in '{output_folder}' folder.")
