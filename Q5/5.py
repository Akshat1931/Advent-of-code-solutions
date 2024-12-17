

from collections import defaultdict
from pathlib import Path



def get_data() -> tuple[list[tuple[int, ...]], list[list[int]]]:

    rules: list[tuple[int, ...]] = []
    updates: list[list[int]] = []

    first_section = True

    with Path("Q5\input.txt").open() as file:
        for line in file:
            line = line.strip()
            if not line:
                first_section = False
                continue

            if first_section:
                rules.append(tuple(map(int, line.split("|"))))
            else:
                updates.append(list(map(int, line.split(","))))

    return rules, updates


def preprocess_rules() -> defaultdict[int, set[int]]:
    """Convert rules into a defaultdict for faster lookups."""
    rule_dict = defaultdict(set)
    for x, y in rules:
        rule_dict[x].add(y)
    return rule_dict


def reorder_bad_update(update: list[int]) -> list[int]:
    """Reorder an update based on the global RULE_DICT."""
    while True:
        swapped = False
        for page, dependencies in rule_dict.items():
            if page in update:
                for dependent in dependencies:
                    if dependent in update:
                        i1 = update.index(page)
                        i2 = update.index(dependent)
                        if i1 > i2:
 
                            update[i1], update[i2] = update[i2], update[i1]
                            swapped = True
        if not swapped:
            break
    return update


def day5() -> tuple[int, int]:
  
    valid_count = 0
    fixed_count = 0

    for update in updates:
        valid = True
        for page in update:

            if page in rule_dict:
                for after_page in rule_dict[page]:
                    if after_page in update:

                        if update.index(page) > update.index(after_page):
                            valid = False
                            break
            if not valid:
                break

        if valid:

            valid_count += update[len(update) // 2]
        else:

            fixed_update = reorder_bad_update(update)
            fixed_count += fixed_update[len(fixed_update) // 2]

    return valid_count, fixed_count


rules, updates = get_data()
rule_dict = preprocess_rules()
valid_count, fixed_count = day5()

print(f"Valid updates total: {valid_count}")  
print(f"Fixed update total: {fixed_count}")  