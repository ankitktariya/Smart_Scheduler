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
    aging_rate = 1 
    while tasks:
       
        tasks.sort(key=lambda t: (t.priority, t.arrival_time))

       
        current_task = tasks.pop(0)

 
        result.append((current_task.name, time, time + current_task.burst_time))
        time += current_task.burst_time

      
        for task in tasks:
            task.waiting_time += current_task.burst_time 

            
            if task.waiting_time >= 5: 
                task.priority = max(task.priority - aging_rate, 1)  

    return result

