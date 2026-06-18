# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

# Fix the code by:
# 1. Making middle an optional parameter
# 2. Add if statement to properly format display of full name
#    with and without the middle name
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()