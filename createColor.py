import random
import json
def generate_unique_color_combinations(filename, seed):
    random.seed(seed)  
    combinations = {}
    used_colors = set()
    while len(combinations) < 256:
        color = random.randint(0, 16777215)  
        if color not in used_colors:
            used_colors.add(color)
            key = format(len(combinations), '08b')  
            value = format(color, '06X') 
            combinations[key] = value
    with open(filename, 'w') as file:
        json.dump(combinations, file, indent=4)
generate_unique_color_combinations('color_codesA.json', seed=15674586451568765456)
