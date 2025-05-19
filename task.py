class Task:
    def __init__(self, name, burst_time, priority=0, arrival_time=0):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.waiting_time = 0  # Add waiting time to track
