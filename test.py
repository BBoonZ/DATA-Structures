def recursive_function(data, count=0):
    if count == 5:
        print("Reached maximum recursion depth.")
        return
    else:
        print(f"Recursive call {count + 1}: {data}")
        # Your recursive logic goes here

        # For example, let's make a recursive call with modified data
        new_data = data + 1
        recursive_function(new_data, count + 1)

# Example usage:
initial_data = 0
recursive_function(initial_data)