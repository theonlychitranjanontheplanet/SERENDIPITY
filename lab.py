vector = [1, 2, 3, 4]  # Example list


vector_str = ','.join(map(str, vector)) #converts to 1,2,3,4
# Split the string by commas to get a list of substrings


number_list_str = vector_str.split(',')
# Convert each string in the list to an integer
back_to_list = [int(num) for num in number_list_str]

