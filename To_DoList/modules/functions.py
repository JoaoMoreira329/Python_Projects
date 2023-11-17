def get_todos(filepath):
    with open(filepath, 'r') as file_local:  # the with block makes sure that when done the file will be closed
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
