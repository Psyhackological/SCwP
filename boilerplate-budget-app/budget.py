from math import floor


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount
        self.check_funds(amount)

    def withdraw(self, amount, description=""):
        if amount > 0:
            amount *= -1

        if (self.total + amount) > 0:
            self.ledger.append({"amount": amount, "description": description})
            self.total += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.total >= amount:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.total:
            return False

        else:
            return True

    def __str__(self):
        mega_string = f"{self.name.center(30, '*')}\n"

        for ledge in self.ledger:
            description = ledge.get("description")
            amount = ledge.get("amount")
            amount = f"{amount : .2f}"
            mega_string += f"{description[:23]: <23}"
            mega_string += f"{amount : >7}\n"

        mega_string += f"Total:{self.total: .2f}"

        return mega_string


def create_spend_chart(categories):
    mega_string = "Percentage spent by category\n"
    spent_by_category = {}

    total_spent = 0
    for category in categories:
        spent_by_category[category.name] = 0
        for ledger in category.ledger:
            if ledger["amount"] < 0:
                spent_by_category[category.name] += ledger["amount"]
                total_spent += ledger["amount"]

    spent_percentages = {}
    for category, spent in spent_by_category.items():
        spent_percentages[category] = int(floor((spent / total_spent) * 100) / 10) * 10

    max_percentage = max(spent_percentages.values())

    categories_num = len(categories)
    for row in range(100, -1, -10):
        if row > max_percentage:
            mega_string += f"{row: >3}| "
            mega_string += ' ' * 3 * categories_num
            mega_string += '\n'

        else:
            mega_string += f"{row: >3}| "
            for name, percent in spent_percentages.items():
                if row <= percent:
                    mega_string += "o  "
                else:
                    mega_string += "   "
            mega_string += '\n'

    mega_string += "    "
    mega_string += '-' * (categories_num * 3 + 1)
    mega_string += '\n'

    max_str_length = max([len(string) for string in spent_percentages.keys()])

    names = spent_percentages.keys()
    for i in range(max_str_length):
        mega_string += '     '
        for name in names:
            if len(name) <= i:
                mega_string += "   "
            else:
                mega_string += f"{name[i]}  "
        mega_string += '\n'
    mega_string = mega_string[:-1]
    return mega_string
