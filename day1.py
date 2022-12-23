# Open the input file in read mode
with open('input.txt', 'r') as file:
    # Initialize a variable to store the maximum sum
    max_sum = 0

    # Initialize a variable to store the current sum
    current_sum = 0

    # Iterate over the lines in the file
    for line in file:
        # If the line is a number, add it to the current sum
        if line.strip().isdigit():
            current_sum += int(line.strip())
        # If the line is blank, update the maximum sum and reset the current sum
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0

    # Update the maximum sum one last time after reading the entire file
    max_sum = max(max_sum, current_sum)

    # Print the maximum sum
    print(max_sum)
