"""
Solution to SCU ACM's week 3 challenge "zig-zag"
Author: Julian Callin
"""


def zig_zag(input_string):
    """
    Trivial solution for printing a string in zig-zag form read line by line
    Zig-zag always has height of 3. See function below for description
    """
    input_li = list(input_string)

    top_row = ""
    mid_row = ""
    bottom_row = ""

    while(input_li):
        # Repeat this append pattern in order to form the correct zig-zag
        try:
            top_row += input_li.pop(0)
            mid_row += input_li.pop(0)
            bottom_row += input_li.pop(0)
            mid_row += input_li.pop(0)
        except IndexError:
            break

    print(top_row + mid_row + bottom_row)


def zig_zag2(input_string, height):
    """
    Print an input string in "zig-zag" form read line by line. The zig-zag
    pattern has a height defined by integer @height

    Example usage:  zig_zag2("PAYPAL", 4)

    zig-zagged: Row 1    P
                Row 2    A   L
                Row 3    Y A
                Row 4    P

    Output:         "PALYAP"

    Output is the zig-zagged form read line-by-line
    """

    # Track which row we want to append to next
    row_counter = 0

    # Rename height to num_rows for clarity
    num_rows = height

    # Operations on the input string make more sense as operations on a list of
    # characters
    input_li = list(input_string)

    # Make an array of strings, one for each row defining the height of the
    # zig-zag
    row_array = ["" for i in range(num_rows)]

    # Add a letter at the first row, fill the middle rows, then add a letter to
    # the last row. Repeat.
    # This prevents the first and last rows from getting letters added twice

    while(input_li):
        try:
            # Add a letter to the first row
            row_array[0] += input_li.pop(0)
            row_counter += 1

            # Add one letter to each row going down
            while(row_counter < num_rows - 1):
                row_array[row_counter] += input_li.pop(0)
                row_counter += 1

            # Add a letter to the last row
            row_array[row_counter] += input_li.pop(0)
            row_counter -= 1

            # Add one letter to each row going up
            while(row_counter > 0):
                    row_array[row_counter] += input_li.pop(0)
                    row_counter -= 1

        except IndexError:
            break

    # Concatenate all rows to produce the zig-zag string read by rows
    final_str = reduce(lambda x, y: x+y, row_array)
    print(final_str)

if __name__ == '__main__':
    zig_zag("PAYPALISHIRING")
    zig_zag2("PAYPALISHIRING", 4)
    zig_zag2("PAYPALIS", 4)
