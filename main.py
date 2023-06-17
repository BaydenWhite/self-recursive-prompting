def recursive_function(value, recursion_count=0, recursion_limit=10):
    # Base case: recursion limit reached
    if recursion_count >= recursion_limit:
        print("Recursion limit reached!")
        return

    # Print the current recursion count and value
    print(f"Recursion {recursion_count}: {value}")

    # Recursive call
    # Modify the value for the next recursion (example: increment by 1)
    new_value = value + 1
    recursive_function(new_value, recursion_count + 1, recursion_limit)


# Example usage
recursive_function(0)  # Start with value 0 and recursion limit of 10
