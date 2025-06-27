from flask import Flask, render_template, request
from task import Task
from Scheduler import round_robin, sjf, priority_scheduling
from utils import log_execution
from gantt import draw_gantt_chart
from deadlock import detect_deadlock
import uuid
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tasks = []
        names = request.form.getlist("name")
        burst_times = request.form.getlist("burst_time")
        priorities = request.form.getlist("priority")
        algorithm = request.form["algorithm"]
        tq = request.form.get("time_quantum", type=int)

        # Create Task objects
        for name, bt, pr in zip(names, burst_times, priorities):
            tasks.append(Task(name, int(bt), int(pr)))

        # Scheduling
        if algorithm == "rr":
            schedule = round_robin(tasks, tq)
        elif algorithm == "sjf":
            schedule = sjf(tasks)
        elif algorithm == "priority":
            schedule = priority_scheduling(tasks)
        else:
            return "Invalid Algorithm!"

        # Deadlock detection
        allocation = {t.name: f"R{i}" for i, t in enumerate(tasks)}
        requested = {t.name: f"R{(i + 1) % len(tasks)}" for i, t in enumerate(tasks)}
        deadlocked = detect_deadlock(allocation, requested)

        # Zombie & starvation detection
        for task in tasks:
            if task.burst_time == 0 and task.status != "completed":
                task.status = "zombie"
            if task.wait_time > 10:
                task.status = "starving"

        filename = f"{uuid.uuid4().hex}.png"
        chart_path = os.path.join("static", filename)
        draw_gantt_chart(schedule, output_file=chart_path)
        log_execution(schedule, "execution_log.txt")

        return render_template("result.html", schedule=schedule, chart_file=filename, tasks=tasks, deadlocked=deadlocked)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    