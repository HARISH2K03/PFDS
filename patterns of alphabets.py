def print_pattern():
    n = 9  # length of the longest line
    for i in range(n, 0, -2):
        # Generate spaces
        spaces = " " * ((n - i) // 2)
        # Generate the string from 'a' to the corresponding length
        chars = " ".join(chr(96 + j) for j in range(1, i // 2 + 1))
        # Combine spaces and characters and print
        print(spaces + chars)

print_pattern()