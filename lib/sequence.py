def remove_duplicates(sequence):
    seen = set()  # Create an empty set to keep track of seen items
    result = []   # Create an empty list to store the result
    
    for item in sequence:
        if item not in seen:
            result.append(item)  # Add item to result list if not seen before
            seen.add(item)  # Add item to the set of seen items
    
    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
