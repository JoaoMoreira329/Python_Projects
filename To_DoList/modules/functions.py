FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:  # the with block makes sure that when done the file will be closed
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
