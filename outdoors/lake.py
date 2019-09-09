def draw_lake(length, width):
    """
    Print a lake of given parameters(length and width)
    :param length: integer defining the length of a lake
    :param width: integer defining the width of a lake
    :return:
    """

    # Sanitizing parameters
    if length < 0:
        raise ValueError("Length is negative")
    if width < 0:
        raise ValueError("Length is negative")

    # Print the lake
    for _ in range(width):
        print('+', end='')
        for _ in range(length):
            print("~", end="")
        print('+')

    return
