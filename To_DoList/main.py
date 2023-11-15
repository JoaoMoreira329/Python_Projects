prompt = "Type add, show or exit: "
todos = []

while True:
    action = input(prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter todo: ")

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of task: "))
            number = number - 1
            newTask = input("New task: ")
            todos[number] = newTask
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break


