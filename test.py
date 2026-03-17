def get_longest_consecutive_from_min(numbers):
    if not numbers:
        return []
    sorted_uniques = sorted(list(set(numbers)))
    
    longest_seq = []
    current_val = sorted_uniques[0]
    
    for num in sorted_uniques:
        if num == current_val:
            longest_seq.append(num)
            current_val += 1
        else:
            break
            
    return longest_seq

print(get_longest_consecutive_from_min([1,2]))