data = [4, 4, 8, 2, 7, 8]

def sort_numbers(data):
    result = []  # Store sorted numbers
    while data:  
        current_value = data[0]  # Assume first element is smallest
        for pointer2 in range(1, len(data)):  
            if data[pointer2] < current_value:  
                current_value = data[pointer2]  # Update smallest value
        data.remove(current_value)  # Remove smallest
        result.append(current_value)  # Add to result
    print(result)  # Output sorted list

sort_numbers(data)
