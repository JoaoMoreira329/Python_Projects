prompt = "Type add, show or exit: "
todos = []

while True:
    action = input(prompt)
    action = action.strip()

    if 'add' in action:
        todo = action[4:]

        with open('todos.txt', 'r') as file:  # the with block makes sure that when done the file will be closed
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in action:
        number = int(action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        print("Here are the tasks: ", todos)
        newTask = input("New task: ")
        todos[number] = newTask + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(action[9:])
        todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in action:
        break

    else:
        print("Command not available")