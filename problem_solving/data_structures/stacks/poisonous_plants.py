from typing import List


def poisonous_plants_naive(plants: List[int]) -> int:
    """
    Naive implementation of poisonous plants.
    """
    days = 0
    while True:
        start_length = len(plants)

        # store the plants that survived
        end_plants = []

        # initialize values
        previous_plant = None

        # debug
        # print("days:", days)
        # print("plants:", plants)

        for plant in plants:
            if previous_plant is not None:
                # compare pesticide level to plant to the left
                if plant <= previous_plant:
                    end_plants.append(plant)
            else:
                # handle case for first plant
                end_plants.append(plant)

            # update previous_plant
            previous_plant = plant

        # update end_length
        end_length = len(end_plants)
        del plants
        plants = end_plants

        if start_length == end_length:
            break
        else:
            # increment days
            days += 1

    return days


def poisonous_plants_naive_optimized(plants: List[int]) -> int:
    """
    Naive implementation of poisonous plants with in-place modification.
    """
    days = 0
    while True:
        start_length = len(plants)

        # store the indices of plants to delete
        plants_indices_to_delete = []

        # initialize value
        previous_plant = None

        for index, plant in enumerate(plants):
            # handle case for first plant
            if previous_plant is not None:
                # compare pesticide level to plant to the left
                if plant > previous_plant:
                    plants_indices_to_delete.append(index)

            # update previous_plant
            previous_plant = plant

        # delete indices in descending order to avoid indices shifting
        plants_indices_to_delete.sort(reverse=True)
        for index in plants_indices_to_delete:
            del plants[index]

        # update end_length
        end_length = len(plants)

        if start_length == end_length:
            break
        else:
            # increment days
            days += 1

    return days


def poisonous_plants_stack_based(plants: List[int]) -> int:
    """
    Stack-based implementation of poisonous plants.
    """
    # initialize values
    max_days = 0

    # an item in the stack will have the pesticide level and the days it survived
    # stack = [[pesticide_level, days_survived], ...]
    # example: stack = [[6, 0], [5, 0], ...]
    stack: List[List[int]] = []

    for plant in plants:
        # current plant's survival days
        days = 0

        # top plant on the stack has pesticide level greater than
        # or equal to the current plant
        while len(stack) > 0 and stack[-1][0] >= plant:
            #  killed plant is to the right
            killed_plant = stack.pop()
            killed_plant_days_survived = killed_plant[1]
            days = max(days, killed_plant_days_survived)

        # if there are surviving plants to the left
        if len(stack) > 0:
            # current plant will die one day after the more
            # poisonous plant to the left
            days += 1

        stack.append([plant, days])

        # maximum survival time of any plant
        max_days = max(max_days, days)

    return max_days


def test_poisonous_plants():
    """Test for poisonous_plants function."""
    # tests for naive implementation
    assert poisonous_plants_naive([6, 5, 8, 4, 7, 10, 9]) == 2
    assert poisonous_plants_naive([3, 6, 2, 7, 5]) == 2
    assert poisonous_plants_naive([4, 3, 7, 5, 6, 4, 2]) == 3

    # tests for naive implementation with in-place modification
    assert poisonous_plants_naive_optimized([6, 5, 8, 4, 7, 10, 9]) == 2
    assert poisonous_plants_naive_optimized([3, 6, 2, 7, 5]) == 2
    assert poisonous_plants_naive_optimized([4, 3, 7, 5, 6, 4, 2]) == 3

    # tests for stack-based approach
    assert poisonous_plants_stack_based([6, 5, 8, 4, 7, 10, 9]) == 2
    assert poisonous_plants_stack_based([3, 6, 2, 7, 5]) == 2
    assert poisonous_plants_stack_based([4, 3, 7, 5, 6, 4, 2]) == 3


test_poisonous_plants()
