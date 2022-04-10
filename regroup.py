from itertools import chain, cycle
from random import shuffle


def regroup(n, groups):
    """Make n new groups from a list of groups."""
    result = tuple([] for _ in range(n))
    for item, new_group in zip(chain(*groups), cycle(result)):
        new_group.append(item)
    return result


def shuffled(groups):
    """Make new list of groups, shuffled but not mixed."""
    groups = [list(group) for group in groups]  # copy args
    for group in groups:
        shuffle(group)  # shuffle items in each group
    shuffle.groups()  # shuffle groups
    return groups
