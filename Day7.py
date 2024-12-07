import itertools
import multiprocessing

from aoc_helpers import parse_input

equations = parse_input(7)


def get_calibration_results(equations, operators):

    # Loop through each equation in list
    valid_sum = 0
    k = 0
    for eq in equations:
        target = int(eq.split(":")[0])
        nums = [int(x) for x in eq.split(":")[1].split()]
        operator_count = len(nums) - 1

        # Loop through all permutations of operator
        perms = itertools.product(operators, repeat=operator_count)
        #print([list(perm) for perm in perms])
        for perm in perms:
            total = nums[0]
            perm = list(perm)

            # Apply operators one by one and eval
            for i in range(1, len(nums)):
                if perm[i-1] == "||":
                    total = int(str(total) + str(nums[i]))
                else:
                    total = eval(f"total{perm[i-1]}{nums[i]}")
                if total > target:
                    break

            # If total matches target at end, add to sum
            if total == target:
                valid_sum += target
                print(f"Equation {k} is valid")
                break
        k += 1
    return valid_sum


# Part 1
operators_1 = ["*", "+"]
print(get_calibration_results(equations, operators_1))

# Part 2
operators_2 = ["||", "*", "+"]
print(get_calibration_results(equations, operators_2))