def round_robin(tasks, time_quantum):
    schedule = []
    queue = tasks.copy()
    time = 0

    while queue:
        task = queue.pop(0)
        if task.burst_time > 0:
            start = time
            bt = min(time_quantum, task.burst_time)
            task.burst_time -= bt
            time += bt
            schedule.append((task.name, start, time))
            task.wait_time += start - task.wait_time
            if task.burst_time > 0:
                queue.append(task)
            else:
                task.status = "completed"  # ✅ Only if it really ran
    return schedule


def sjf(tasks):
    tasks = sorted(tasks, key=lambda x: x.burst_time)
    time = 0
    schedule = []
    for task in tasks:
        schedule.append((task.name, time, time + task.burst_time))
        time += task.burst_time
        task.status = "completed"
    return schedule


def priority_scheduling(tasks):
    time = 0
    schedule = []
    tasks = sorted(tasks, key=lambda x: (x.priority, x.wait_time))
    for task in tasks:
        # Aging logic: wait_time > 5 => priority boost
        if task.wait_time > 5:
            task.priority -= 1
        schedule.append((task.name, time, time + task.burst_time))
        time += task.burst_time
        task.status = "completed"
    return schedule
