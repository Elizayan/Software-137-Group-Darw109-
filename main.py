global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers): # Pass 'my_set' as an argument to the function
    global global_variable
    local_variable = 5
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.discard(local_variable) #Used discard instead of remove for sets to safely remove elements.
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set.copy()) # Pass a copy of 'my_set' to avoid modifying the original
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable
modify_dict() # Remove the unnecessary argument (5)

def update_global():
    global global_variable
    global_variable += 10
for i in range(5):
    print(i)

if my_set is not None and 'key4' in my_dict and my_dict['key4'] == 10:  # Check if 'key4' exists before comparing its value
    print("Condition met!")

if 5 not in my_dict: #Checked if 5 is not in my_set to print the appropriate message.
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
