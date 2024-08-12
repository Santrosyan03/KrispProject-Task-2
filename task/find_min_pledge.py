############
#
# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#
############


def find_min_pledge(pledge_list):
    numbers = set()
    i = 1
    for pledge in pledge_list:
        if pledge not in numbers:
            numbers.add(pledge)
    while i in numbers:
        i += 1
    return i


if __name__ == '__main__':
    assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
    assert find_min_pledge([1, 2, 3]) == 4
    assert find_min_pledge([-1, -3]) == 1
