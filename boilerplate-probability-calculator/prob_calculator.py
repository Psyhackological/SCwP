# THE DIFFERENCE BETWEEN SHALLOW AND DEEP COPY
# SHALLOW COPY - COPIES ALL THE CONTENTS BUT INNER CONTENTS IS POINTING TO ITS COPIER
# DEEP COPY - COPIES ALL THE CONTENTS AND INNER CONTENTS WITHOUT POINTING TO ITS COPIER
# BECAUSE I DO NOT USE OBJECTS WITHIN THE OBJECTS IT IS THE SAME
from copy import copy
import random


class Hat:
    # WAY TO HAVE KEY VALUE WITH ARGUMENT PASSING
    def __init__(self, **kwargs):
        # CONVERTING DICT TO LIST BY KEYS X THEIR VALUES
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

        # COPY OF CONTENTS LIST
        self.start_list = copy(self.contents)

    def draw(self, to_draw):
        # IF TOO MUCH OR EQUAL RETURN AND DON'T RUN THE REST
        if to_draw >= len(self.contents):
            return self.contents

        # WE MAKE SURE THAT WE HAVE START LIST
        self.contents = copy(self.start_list)

        # APPEND ONE BY ONE RANDOM_COLOR TO DRAWN AND REMOVE FROM CONTENTS
        drawn = []
        for _ in range(to_draw):
            random_color = random.choice(self.contents)
            self.contents.remove(random_color)
            drawn.append(random_color)

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # IT IS EASIER TO DETERMINE HOW MANY IS BAD THAN GOOD (EFFICIENCY)
    bad = 0
    for _ in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)

        # IF DRAWN HASN'T ENOUGH OF EXPECTED BALLS THEN BREAK AND CHECK THE NEXT DRAW
        for k, v in expected_balls.items():
            if not (v <= drawn.count(k)):
                bad += 1
                break

    # NUM_EXPERIMENTS - BAD = GOOD
    return (num_experiments - bad) / num_experiments
