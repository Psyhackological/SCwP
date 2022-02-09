from math import floor


class Category:

    # CATEGORY CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    # RETURNS TRUE BECAUSE + AND + WILL ALWAYS BE +
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount
        return True

    # ALWAYS NEGATIVE AMOUNT
    def withdraw(self, amount, description=""):
        if amount > 0:
            amount *= -1

        # EXACTLY THE SAME AS DEPOSIT BUT WITH -
        if self.check_funds(amount):
            self.ledger.append({"amount": amount, "description": description})
            self.total += amount
            return True

        # IF INSUFFICIENT BALANCE
        else:
            return False

    # SIMPLE GETTER
    def get_balance(self):
        return self.total

    # METHOD THAT USES OTHER 3 METHODS
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        else:
            return False

    # ABS BECAUSE WITHDRAW IS NEGATIVE SO - IS ALWAYS LESS THAN +
    def check_funds(self, amount):
        if abs(amount) > self.total:
            return False

        else:
            return True

    # HOW TO PRINT THIS OBJECT
    def __str__(self):
        # HEADER
        mega_string = f"{self.name.center(30, '*')}\n"

        # BODY
        for ledge in self.ledger:
            description = ledge.get("description")
            amount = ledge.get("amount")
            amount = f"{amount : .2f}"
            mega_string += f"{description[:23]: <23}"
            mega_string += f"{amount : >7}\n"

        # FOOTER
        mega_string += f"Total:{self.total: .2f}"

        return mega_string

    def __repl__(self):
        # HEADER
        mega_string = f"{self.name.center(30, '*')}\n"

        # BODY
        for ledge in self.ledger:
            description = ledge.get("description")
            amount = ledge.get("amount")
            amount = f"{amount : .2f}"
            mega_string += f"{description[:23]: <23}"
            mega_string += f"{amount : >7}\n"

        # FOOTER
        mega_string += f"Total:{self.total: .2f}"

        return mega_string


def create_spend_chart(categories):

    # HEADER
    mega_string = "Percentage spent by category\n"

    # SCRAPE THE NEGATIVE DATA WITH TOTAL FROM EVERY CATEGORIES OBJECT
    spent_by_category = {}
    total_spent = 0

    # SINGLE OBJECT
    for category in categories:

        # SINGLE OBJECT NAME
        spent_by_category[category.name] = 0

        # SINGLE OBJECT LEDGER LIST WITH SINGLE DICTIONARY ENTRY
        for cat_ledge in category.ledger:

            # HELLO ARE YOU - ?
            if cat_ledge["amount"] < 0:

                # COOL LET ME ADD YOU TO SPENT DICT AND ALSO TO TOTAL_SPENT
                spent_by_category[category.name] += cat_ledge["amount"]
                total_spent += cat_ledge["amount"]

    # LET'S CREATE PERCENTAGES FLOORING THEM TO 10^1 PLACES (NOT 10^-1)
    spent_percentages = {}
    for category, spent in spent_by_category.items():
        # SPENT / TOTAL_SPENT = 0.PERCENTAGE
        # SO I MULTIPLY BY 100 TO MAKE %
        # THEN FLOOR THIS
        # DIVIDE BY 10 TO CUT THE N%10 AND THEN TO ADD ONE 0
        spent_percentages[category] = int(floor((spent / total_spent) * 100) / 10) * 10

    # NEEDED TO DETERMINE WHERE TO PUT BLANK LINES FROM ABOVE
    max_percentage = max(spent_percentages.values())

    # DETERMINES HOW MANY BLANK SPACES
    categories_num = len(categories)

    # FOR LOOP FROM 100 TO 0 (-1 BECAUSE 0 NEEDS TO BE INCLUDED)
    for row in range(100, -1, -10):
        # IF ROW IS HIGHER THAN MAX_PERCENTAGE THEN PRINT SPACES
        if row > max_percentage:
            mega_string += f"{row: >3}| {' ' * 3 * categories_num}\n"

        # ELSE THERE IS SOME o TO PRINT
        else:

            # STANDARD STUFF
            mega_string += f"{row: >3}| "

            # LOOP FROM PERCENTAGE VALUES
            for percent in spent_percentages.values():

                # IF PERCENT IS HIGHER THEN PRINT O AND 2 SPACES
                if row <= percent:
                    mega_string += "o  "

                # IF NOT PRINT 3 BLANK SPACES
                else:
                    mega_string += "   "

            # BREAK THE LINE
            mega_string += '\n'

    # DASHES ROW
    mega_string += f"    {'-' * (categories_num * 3 + 1)}\n"

    # DETERMINES HOW MANY ROWS ARE GOING TO BE UNDER THE DASHES
    max_str_length = max([len(string) for string in spent_percentages.keys()])

    # AND TO PRINT THEM OUT VERTICALLY WE NEED THEM (WOW)
    names = spent_percentages.keys()

    # FROM 0 TO MAX_STR_LENGTH
    for i in range(max_str_length):

        # LEFT PADDING
        mega_string += '     '

        for name in names:

            # IF COUNTER IS HIGHER THAT MEANS THE STR IS OUT OF CHARACTERS
            # ALSO LOOP WILL RUN LEN(NAMES) TIMES
            if len(name) <= i:
                mega_string += "   "

            # IF NOT PRINT THE CHARACTER WITH I INDEX
            else:
                mega_string += f"{name[i]}  "

        # BREAK THE LINE
        mega_string += '\n'

    # DELETE LAST \n
    mega_string = mega_string[:-1]

    return mega_string
