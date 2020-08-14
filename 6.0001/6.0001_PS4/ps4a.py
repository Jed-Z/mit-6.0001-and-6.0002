# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:  # 停止条件
        return [sequence]
    else:                   # 递归步骤
        permus = []         # 对sequence排列的结果
        for smaller in get_permutations(sequence[1:]):
            for i in range(len(smaller) + 1):
                permus.append(smaller[:i] + sequence[0] + smaller[i:])  #将首字母插入每个位置
        permus.sort()       # 字典序排序
        return permus


if __name__ == '__main__':
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example1 = '12'
    print('Input:', example1)
    print('Expected Output:', ['12', '21'])
    print('Actual Output:', get_permutations(example1))
    print('-' * 16)

    example2 = 'abc'
    print('Input:', example2)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example2))
    print('-' * 16)

    example3 = 'bust'
    print('Input:', example3)
    print('Expected Output:', ['bstu', 'bsut', 'btsu', 'btus', 'bust', 'buts', 'sbtu', 'sbut', 'stbu', 'stub',
                               'subt', 'sutb', 'tbsu', 'tbus', 'tsbu', 'tsub', 'tubs', 'tusb', 'ubst', 'ubts', 'usbt', 'ustb', 'utbs', 'utsb'])
    print('Actual Output:', get_permutations(example3))