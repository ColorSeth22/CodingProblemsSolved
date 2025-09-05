def tower_builder(n_floors):
    baseLength = n_floors + n_floors - 1
    tower = []
    print(baseLength)
    i = 1
    while i <= n_floors:
        stars = '*' * ((i * 2) - 1)
        floor = ' ' * int((baseLength - len(stars)) / 2)
        floor += stars
        floor += ' ' * int((baseLength - len(stars)) / 2)
        tower.append(floor)
        i += 1
    return (tower)

tower_builder(3)