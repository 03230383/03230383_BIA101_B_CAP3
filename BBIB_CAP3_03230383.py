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


def calculate_total(input_file):
    total = 0
    with open(input_file, 'r') as file:
        for line in file:
            digits = [char for char in line if char.isdigit()]
            if len(digits) >= 2:
                number = int(digits[0] + digits[-1])
                total += number
    return total

def main():
    input_file = "383.txt"  # Change this to match your index
    result = calculate_total(input_file)
    print("Total sum of numbers: ", result)

if __name__ == "__main__":
    main()
