class Task:
    def __init__(self, name, burst_time, priority):
        self.name = name
        self.burst_time = burst_time
        self.original_bt = burst_time
        self.priority = priority
        self.wait_time = 0
        self.status = "waiting"
