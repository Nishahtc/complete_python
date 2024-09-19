
def counter_function():
    
    count = 0

    
    def increment_count():
        nonlocal count  
        count += 1   
        print(f"Count: {count}")  

    # Call increment_count multiple times
    increment_count()  # First call
    increment_count()  # Second call
    increment_count()  # Third call

# Call the outer function to execute the code
counter_function()