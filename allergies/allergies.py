class Allergies(object):

    allergens_dict = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        # for key, value in allergens_dict.items():

    @property
    def lst(self):
        pass

# So if Tom is allergic to peanuts and chocolate, he gets a score of 34.
#
# Now, given just that score of 34, your program should be able to say:
#
# Whether Tom is allergic to any one of those allergens listed above.
# All the allergens Tom is allergic to.
# Note: a given score may include allergens not listed above (i.e. allergens
# that score 256, 512, 1024, etc.). Your program should ignore those components
# of the score. For example, if the allergy score is 257, your program should only
# report the eggs (1) allergy.
