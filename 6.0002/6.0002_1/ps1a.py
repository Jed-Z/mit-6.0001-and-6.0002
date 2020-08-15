###########################
# 6.0002 Problem Set 1a: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_weights = {}
    with open(filename) as file:
        for line in file:
            line_list = line.strip().split(',')  # 以逗号分隔
            cow_weights[line_list[0]] = int(line_list[1])  # 字符串:整数键值对
    return cow_weights


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted = sorted(cows.items(), key=lambda x:x[1], reverse=True)
    transports = []
    while cows_sorted and cows_sorted[-1][1] < limit:
        current_weight = 0      # 当次运输的重量
        current_transport = []  # 档次运输的奶牛名字
        for cow in cows_sorted.copy():  # 从大到小遍历
            if current_weight + cow[1] <= limit:
                current_transport.append(cow[0])
                current_weight += cow[1]
                cows_sorted.remove(cow)  # 从剩余奶牛列表中移除
        transports.append(current_transport)  # 添加一次运输
    return transports


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # 首先删除那些重量超过限制的奶牛
    cows_filtered = {k:v for k,v in cows.items() if v <= limit}

    transports = []
    for partition in get_partitions(cows_filtered):
        flag = True  # 当前分片是否有效
        for transport in partition:
            if sum(map(cows_filtered.get, transport)) > limit:
                flag = False
                break
        if flag:
            if len(partition) < len(transports) or len(transports) == 0:
                transports = partition
    return transports
        

# Problem 4
def compare_cow_transport_algorithms(filename):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows(filename)

    start = time.perf_counter()  # 开始：处理器时间
    greedy_result = greedy_cow_transport(cows)
    end = time.perf_counter()  # 结束：处理器时间
    print('--- Greedy algorithm ---')
    print('Result:', end=' ')
    print(greedy_result)
    print('Time cost:', end=' ')
    print('{:.4f} ms'.format((end-start)*1000))

    start = time.perf_counter()  # 开始：处理器时间
    brute_result = brute_force_cow_transport(cows)
    end = time.perf_counter()  # 结束处理器时间
    print('--- Brute force algorithm ---')
    print('Result:', end=' ')
    print(brute_result)
    print('Time cost:', end=' ')
    print('{:.4f} ms'.format((end-start)*1000))


if __name__ == '__main__':
    compare_cow_transport_algorithms('ps1_cow_data.txt')
    print()
    compare_cow_transport_algorithms('ps1_cow_data_2.txt')
    print()
    compare_cow_transport_algorithms('ps1_cow_data_3.txt')