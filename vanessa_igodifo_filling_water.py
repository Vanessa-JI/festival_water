def bottle_fill_time(queue, num_taps):

    # input validation using assertions
    # asserting that the queue of people is input as a list of positive integers
    assert isinstance(queue, list) and all(isinstance(val, int) and val > 0 for val in queue), \
        "Water bottle sizes must be positive integers."

    # asserting that the taps parameter is a positive integer greater than 1
    assert isinstance(num_taps, int) and num_taps > 1, \
        "Must specify an integer value of at least 1 tap."

    # in the case that there are no water bottles to fill, return 0 seconds
    if not queue:
        return 0

    # in the case that we have enough taps to fill each water bottle at the same time, return
    if len(queue) <= num_taps:
        highest_capacity = max(queue)
        return highest_capacity / 100

    # in the case that we don't have enough taps to fill all bottles at the same time
    # define a times array that states how long each tap has been filling a bottle for
    times = [0] * num_taps
    for i in range(len(queue)):
        # add the time it takes to fill the current water bottle to the times array
        times[0] += queue[i] / 100
        # sort the taps in ascending order so we'll always be filling the most recently free tap at a time
        times.sort()

    # return the time it takes to fill the tap that takes the longest to fill
    return max(times)


def bottle_fill_time_with_walk(queue, num_taps, walk_time):

    # input validation using assertions
    # asserting that the queue of people is input as a list of positive integers
    assert isinstance(queue, list) and all(isinstance(val, int) and val > 0 for val in queue), \
        "Water bottle sizes must be positive integers."

    # asserting that the taps parameter is a positive integer greater than 1
    assert isinstance(num_taps, int) and num_taps > 1, \
        "Must specify an integer value of at least 1 tap."

    # asserting that the walk time is a positive integer
    assert isinstance(walk_time, int) and walk_time >= 0, \
        "The time to walk from the queue to the tap must be a positive integer."

    # in the case that there are no water bottles to fill, return 0 seconds
    if not queue:
        return 0

    # in the case that we have enough taps to fill each water bottle at the same time, return
    if len(queue) <= num_taps:
        highest_capacity = max(queue)
        return walk_time + highest_capacity / 100

    # in the case that we don't have enough taps to fill all bottles at the same time
    # define a times array that states how long each tap has been filling a bottle for
    times = [0] * num_taps
    for i in range(len(queue)):
        # add the time it takes to fill the current water bottle to the times array
        times[0] += queue[i] / 100
        # sort the taps in ascending order so we'll always be filling the most recently free tap at a time
        times.sort()

    # return the time it takes to fill the tap that takes the longest to fill
    return max(times) + (walk_time * len(queue))  # considering the first person must also walk to the tap


def bottle_fill_time_with_walk_and_flow_rates(queue, num_taps, walk_time, tap_flow_rates):

    # input validation using assertions
    # asserting that the queue of people is input as a list of positive integers
    assert isinstance(queue, list) and all(isinstance(val, int) and val > 0 for val in queue), \
        "Water bottle sizes must be positive integers."

    # asserting that the taps parameter is a positive integer greater than 1
    assert isinstance(num_taps, int) and num_taps > 1, \
        "Must specify an integer value of at least 1 tap."

    # asserting that the walk time is a positive integer
    assert isinstance(walk_time, int) and walk_time >= 0, \
        "The time to walk from the queue to the tap must be a positive integer."

    # asserting that there is a corresponding flow rate specified for each tap, where flow rates are positive integers
    assert isinstance(tap_flow_rates, list) and all(isinstance(item, int) and item > 0 for item in tap_flow_rates), \
        "Each tap must have a defined flow rate of integer type with a value greater than 0."

    # asserting a flow rate has been defined for each tap
    assert len(tap_flow_rates) == num_taps, \
        "Each tap must have a defined flow rate."

    # in the case that there are no people in the queue with water bottles to fill, return 0 seconds
    if not queue:
        return 0

    # in the case that we have enough taps to fill each water bottle at the same time, return the time it takes to fill
    # the largest capacity water bottle + the time it takes to walk to the tap
    if len(queue) <= num_taps:
        highest_capacity = max(queue)
        idx = queue.index(highest_capacity)
        return walk_time + highest_capacity / idx

    # in the case that we don't have enough taps to fill all bottles at the same time
    # define a times array that states how long each tap has been filling a bottle for
    times = [0] * num_taps
    for i in range(len(queue)):
        # add the time it takes to fill the current water bottle to the times array
        times[0] += queue[i] / tap_flow_rates[0]
        # sort the taps in ascending order so we'll always be filling the most recently free tap at any time
        # we also sort the flow rates according to the sorted order of the taps
        tap_flow_rates = [val for (_, val) in sorted(zip(times, tap_flow_rates), key=lambda x: x[0])]
        times.sort()

    # return the time it takes to fill the tap that takes the longest to fill
    return max(times) + (walk_time * len(queue))  # considering the first person also walks to the tap


print(bottle_fill_time([400, 750, 500, 1000], 2))
print(bottle_fill_time_with_walk([400, 750, 500, 1000], 2, 2))
print(bottle_fill_time_with_walk_and_flow_rates([400, 750, 500, 1000], 2, 2, [100, 50]))


