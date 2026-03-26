
tasks = {}

numberOfTasks = input("Enter the number of tasks:  ")

for i in range(0, int(numberOfTasks)):
    taskName = input("Enter the name of the task:  ")
    numberOfDependencies = input("Enter the number of dependencies for " + taskName + ":  ")
    dependencies = []
    for j in range(0, int(numberOfDependencies)):
        dependency = input("Enter the name of dependency " + str(j+1) + ":  ")
        dependencies.append(dependency)
    tasks[taskName] = dependencies


print("\nTASK STRUCTURE:")
for task in tasks:
    print(task, "->", tasks[task])


print("\nINITIAL TASKS (no dependencies):")
foundInitialTask = False
for task in tasks:
    if len(tasks[task]) == 0:
        print(task)
        foundInitialTask = True

if foundInitialTask == False:
    print("None")


print("\nEXECUTION ORDER:")
completedTasks = set()
step = 1

while len(completedTasks) < len(tasks):
    taskExecuted = False

    for task in tasks:
        if task not in completedTasks:
            canExecute = True
            for dep in tasks[task]:
                if dep not in completedTasks:
                    canExecute = False

            if canExecute == True:
                print("Step", step, ":", task)
                completedTasks.add(task)
                step = step + 1
                taskExecuted = True

    if taskExecuted == False:
        if len(completedTasks) == 0:
            print("No task can be started.")
        print("ERROR: Circular dependency detected!")
        print("These tasks could not be completed:")
        for task in tasks:
            if task not in completedTasks:
                print(task)
        break


if len(completedTasks) == len(tasks):
    print("ALL TASKS COMPLETED SUCCESSFULLY")
