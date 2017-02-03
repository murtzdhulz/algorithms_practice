__author__ = 'Murtaza'

# Print the pairs which add up to a given sum
def print_pairs(arr,sum):
    num_map={}
    for val in arr:
        target = sum-val
        if target in num_map:
            if num_map[target]>=1:
                print target,val
                num_map[target]-=1
        else:
            if val in num_map:
                num_map[val]+=1
            else:
                num_map[val]=1

print_pairs([11,1,7,-2,3,10,14,-6,10,18,8,-3],8)