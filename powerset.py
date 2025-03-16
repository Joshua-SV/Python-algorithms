# creates a power set list from a list input this is O(2^N)

def power_set(input_set):
    if  len(input_set) == 0:
        return [[]]

    power_lst = [[]]
    for item in input_set:
        new_subsets = []
        for lst in power_lst:
            new_subset = lst + [item]  # Create a new list instead of modifying `lst`
            new_subsets.append(new_subset)
        power_lst.extend(new_subsets)
    
    return power_lst  # Return the correctly built power set
        
        