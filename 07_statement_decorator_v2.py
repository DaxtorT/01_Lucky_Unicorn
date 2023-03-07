# Functions go heer
def statement_deco(deco_sides, deco_top_bottom, start_statement, three_line):
    # Sets up decoration for sides of statement and top / bottom
    sides = deco_sides * 3
    single_statement = f"{sides} {start_statement} {sides}"

    top_bottom = deco_top_bottom * len(single_statement)
    big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

    # Outputs either single or triple line statement
    if three_line == 1:
        return single_statement

    elif three_line ==3:
        return big_statement

# Main Routine goes here
statement_one = statement_deco("-", "*", "Hello World", 3)
print(statement_one)
print()

statement_two = statement_deco("=", ".", "Blah Blah Blah", 1)
print(statement_two)
