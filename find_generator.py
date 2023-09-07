def find_generator(group):
    generators = []
    mod = len(group) + 1
    for element in group:
        is_gengerator = True
        if pow(element, len(group), mod) != 1:
            is_gengerator = False
            break
        for power in range(1, len(group)):
            if pow(element, power, mod) == 1:
                is_gengerator = False
                break
        if is_gengerator:
            generators.append(element)
    return generators


print(find_generator((1, 2, 3, 4, 5, 6)))
