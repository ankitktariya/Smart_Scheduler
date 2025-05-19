from flask import Flask, render_template, request
from task import Task
from Scheduler import round_robin, sjf, priority_scheduling
from utils import log_execution
from gantt import draw_gantt_chart
import uuid
import os
import webbrowser
import threading

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

        # Save Gantt chart
        filename = f"{uuid.uuid4().hex}.png"
        chart_path = os.path.join("static", filename)
        draw_gantt_chart(schedule, output_file=chart_path)

        return render_template("result.html", schedule=schedule, chart_file=filename)

    return render_template("index.html")
if __name__ == "__main__":
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    # Thread me browser open karenge taki server block na ho
    threading.Timer(1, open_browser).start()
    
    app.run(debug=True)

