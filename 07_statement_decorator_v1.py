# Constants
deco_top_bottom = "*"
deco_sides = "~"
start_statement = "Hello Wirld"

# Main Routine goes here
# Sets up decoration for sides of statement and top / bottom
single_statement = f"{deco_sides} {start_statement} {deco_sides}"

top_bottom = deco_top_bottom * len(single_statement)

big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

# Prints single and three line statements
print(single_statement)
print()
print(big_statement)