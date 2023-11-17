#from functions import get_todos, write_todos
from modules import functions

prompt = "Type add, show or exit: "
todos = []

while True:
    action = input(prompt)
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]

        todos = functions.get_todos('todos.txt')

        todos.append(todo + '\n')

        functions.write_todos('todos.txt', todos)

    elif action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number = number - 1

            todos = functions.get_todos('todos.txt')

            print("Here are the tasks: ", todos)
            newTask = input("New task: ")
            todos[number] = newTask + '\n'

            functions.write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('complete'):
        try:
            todos = functions.get_todos('todos.txt')

            number = int(action[9:])
            todos.pop(number - 1)

            functions.write_todos('todos.txt', todos)
        except IndexError:
            print("There is no item with the inputted number")

    elif action.startswith('exit'):
        break

    else:
        print("Command not available")

