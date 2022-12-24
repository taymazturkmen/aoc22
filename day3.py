# Open the input file
with open('input.txt', 'r') as file:
    # Initialize the sum value
    sum_value = 0
    
    # Iterate over the lines in the file
    for line in file:
        # Divide the line into two halves
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        
        # Iterate over the characters in the first half
        for i, char in enumerate(first_half):
            # If the character is present in the second half and is equal to the character in the first half (case sensitive)
            if char in second_half and char == second_half[i]:
                # Calculate the value of the character
                if 'a' <= char <= 'z':
                    value = ord(char) - ord('a') + 1
                elif 'A' <= char <= 'Z':
                    value = ord(char) - ord('A') + 27
                # Add the value to the sum value
                sum_value += value
                
    # Print the sum value
    print(sum_value)
