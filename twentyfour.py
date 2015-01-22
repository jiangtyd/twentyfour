import itertools

# exponentiation causes out of bounds :(
func_strs = ['+', '-', '*', '/']
funcs = [lambda x,y: 1.0*x+y, lambda x,y: 1.0*x-y, lambda x,y: 1.0*x*y, lambda x,y: 1.0*x/y]

def solve(nums, result):
    solns = []
    for perm in itertools.permutations(nums):
        solns.extend(solutions_ordered(perm, result))
    return solns

def single_reduce(l, f):
    return [f(l[0], l[1])] + list(l[2:]) if len(l) > 1 else l

# string with the operations for a solution with nums in this order, or None otherwise
def solutions_ordered(nums, result):
    # all but first number
    solns = _solutions_ordered(nums, result)
    parens = "(" * (len(nums)-1)
    return [parens + str(nums[0]) + s for s in solns]

# take care of all but the first number
def _solutions_ordered(nums, result):
    ret = []
    if len(nums) == 1:
        if nums[0] == result:
            ret = ['']
    elif len(nums) > 1:
        for i in xrange(len(funcs)):
            solns = _solutions_ordered(single_reduce(nums, funcs[i]), result)
            if len(solns) > 0:
                ret.extend([func_strs[i] + str(nums[1]) + ")" + s for s in solns])
    return ret

