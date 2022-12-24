# initialize score to 0
score = 0

# open the file 'input.txt' for reading
with open('input.txt', 'r') as f:
    # read each line in the file
    for line in f:
        # split the line into two characters
        first, second = line.strip().split()
        # add points based on the second character
        if second == 'X':
            score += 1
        elif second == 'Y':
            score += 2
        elif second == 'Z':
            score += 3
        # check for wins or draws
        if second == 'X' and first == 'C':
            score += 6
        elif second == 'Y' and first == 'A':
            score += 6
        elif second == 'Z' and first == 'B':
            score += 6
        elif second == 'X' and first == 'A':
            score += 3
        elif second == 'Y' and first == 'B':
            score += 3
        elif second == 'Z' and first == 'C':
            score += 3

# print out the score for the second player
print(score)
