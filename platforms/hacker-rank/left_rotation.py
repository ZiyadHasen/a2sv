def rotateLeft(d, arr):
    n = len(arr)
    rotated_arr = [0] * n
    
    for i in range(n):
        # Calculate the new index for each element
        new_index = (i - d) % n
        rotated_arr[new_index] = arr[i]
        
    return rotated_arr