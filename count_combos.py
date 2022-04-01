ncolors_by_variation = [
    [1],  # base
    [0] * 8,  # arms
    [0, 2, 3, 3, 5, 4, 5, 7],  # backdrop
    [0] * 8,  # eyes
    [0, 2, 3, 0, 1, 1, 2, 2],  # hats
    [1] * 7 + [3],  # heads
    [0, 1, 1, 2, 2],  # inshirts
    [0, 7, 6, 6, 3, 4, 2, 7],  # landscapes
    [0] * 4 + [1] + [0] * 3,  # mouths
    [0, 2, 2, 1, 1],  # neckwear
    [0, 2, 2, 3]  # outshirts
]

STEPS_PER_COLOR_BIT = 8

n_color_choices = STEPS_PER_COLOR_BIT ** 3

noptions_by_variation = []
for ncolors in ncolors_by_variation:
    noptions_by_variation.append(sum(n_color_choices ** n for n in ncolors))

total = 1
for noptions in noptions_by_variation:
    total *= noptions

print(total)
