def arithmetic_arranger(problems, display_outcome=False):
    # PRIORITIZED ERROR CHECKING
    if len(problems) > 5:
        return "Error: Too many problems."

    # DATA ORGANIZATION OF ROWS
    first_row = []
    second_row = []
    signs = []
    lines = []

    if display_outcome:
        outcomes = []

    # SCRAPPING THE DATA
    for problem in problems:
        # SIGN AND ERROR CHECKING
        if "-" in problem:
            first, second = problem.split(" - ")
            sign = "-"
        elif "+" in problem:
            first, second = problem.split(" + ")
            sign = "+"
        else:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # APPENDING TO APPROPRIATE COLLECTIONS
        first_row.append(first)
        second_row.append(second)
        signs.append(sign)

        line = (max(len(first), len(second)) + 2) * "-"
        lines.append(line)

        if display_outcome:
            if sign == "+":
                outcome = int(first) + int(second)
            else:
                outcome = int(first) - int(second)
            outcomes.append(outcome)

    # NEEDED VARIABLES TO CALCULATE AND APPEND FINAL STRING
    widths = [len(line) for line in lines]
    mega_string = ""

    # FORMATTING THE DATA
    for first, width in zip(first_row, widths):
        # F-STRING ALIGNS TO THE RIGHT BY WIDTH - LEN(FIRST)
        mega_string += f"{first : >{width}}    "
    mega_string = mega_string[:-4]
    mega_string += "\n"

    for second, sign, width in zip(second_row, signs, widths):
        # F-STRING ALIGNS TO THE RIGHT BY WIDTH - LEN(SECOND) - 1
        mega_string += f"{sign}{second: >{width-1}}    "
    mega_string = mega_string[:-4]
    mega_string += "\n"

    for line in lines:
        mega_string += f"{line}    "
    mega_string = mega_string[:-4]

    if display_outcome:
        mega_string += "\n"
        for outcome, width in zip(outcomes, widths):
            # F-STRING ALIGNS TO THE RIGHT BY WIDTH - LEN(OUTCOME)
            mega_string += f"{outcome : >{width}}    "
        mega_string = mega_string[:-4]

    return mega_string
