################################
# Github Repo link: https://github.com/03230383/03230383_BIA101_B_CAP3
# Your Name: Tshering Wangmo
# Your Section : B
# Your Student ID Number: 03230383
################################
# REFERENCES
# https://machinesintheclouds.com/sliding-window-technique-in-python
# https://www.youtube.com/watch?v=BRrem1k3904
# SOLUTION
# Your Solution Score: 478095
################################


# Function to calculate the total sum of numbers
def calculate_total(input_file):
    total = 0
    with open(input_file, 'r') as file:
        for line in file:
            # Extract digits from the line
            digits = [char for char in line if char.isdigit()]

            # Ensure at least two digits are present
            if len(digits) >= 2:
                # Combine the first and last digits to form a number
                total += int(digits[0] + digits[-1])
    return total

# Main function
def main():
    # Specify the input file path
    input_file = "383.txt"

    # Calculate the total sum of numbers
    result = calculate_total(input_file)

    # Print the total sum
    print("Total sum of numbers:", result)

if __name__ == "__main__":
    main()
