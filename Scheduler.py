def round_robin(tasks, time_quantum):
    queue = tasks.copy()
    time = 0
    result = []
    while queue:
        task = queue.pop(0)
        if task.remaining_time > time_quantum:
            result.append((task.name, time, time + time_quantum))
            time += time_quantum
            task.remaining_time -= time_quantum
            queue.append(task)
        else:
            result.append((task.name, time, time + task.remaining_time))
            time += task.remaining_time
            task.remaining_time = 0
    return result

def sjf(tasks):
    tasks.sort(key=lambda t: t.burst_time)
    time = 0
    result = []
    for task in tasks:
        result.append((task.name, time, time + task.burst_time))
        time += task.burst_time
    return result

def priority_scheduling(tasks):
    time = 0
    result = []
    aging_rate = 1  # Define how much priority increases over time

    # Run the scheduling in a loop until all tasks are completed
    while tasks:
        # Sort tasks by priority, considering waiting time for aging
        tasks.sort(key=lambda t: (t.priority, t.arrival_time))

        # Pick the task with the highest priority (lowest priority value)
        current_task = tasks.pop(0)

        # Execute the task
        result.append((current_task.name, time, time + current_task.burst_time))
        time += current_task.burst_time

        # After executing the task, increase the waiting time for others
        for task in tasks:
            task.waiting_time += current_task.burst_time  # Increment waiting time of other tasks

            # Aging: Increase priority based on waiting time
            if task.waiting_time >= 5:  # You can modify this threshold
                task.priority = max(task.priority - aging_rate, 1)  # Decrease priority (increase priority rank)

    return result

