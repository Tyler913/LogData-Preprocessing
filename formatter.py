def change_space(file_path):
    with open(file_path, 'r') as file:
        context = file.read()
    changed_context = context.replace("  ", " ")
    
    with open(file_path, 'w') as new_file:
        new_file.write(changed_context)

change_space("/Users/tyler/Desktop/Development/smart/haveATry.txt")