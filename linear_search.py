def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not in the list

# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
target_element = 7

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Found {target_element} at index {result}.")
else:
    print(f"{target_element} not found in the list.")
