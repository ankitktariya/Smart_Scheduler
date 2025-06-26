#  Smart Task Scheduler

A web-based simulation tool to demonstrate core **Operating System Scheduling Algorithms** like **Round Robin**, **Shortest Job First**, and **Priority Scheduling**, along with advanced features like **Deadlock Detection**, **Zombie Process Identification**, and **Starvation Detection**.

---

##  Features

-  Round Robin Scheduling with Time Quantum
-  Shortest Job First (SJF) Scheduling
-  Priority-based Scheduling
-  Deadlock Detection (resource wait graph)
-  Zombie & Starving Process Detection
-  Gantt Chart Visualization
-  Flask-based Web UI (HTML + CSS + Jinja)

---

##  Objective

To simulate how operating systems schedule tasks, detect potential deadlocks or zombie processes, and visually display execution timelines to improve practical understanding of CPU scheduling algorithms.

---

##  Tech Stack

- **Python 3**
- **Flask**
- **Matplotlib**
- **HTML/CSS**
- **Jinja2**
- **UUID, OS module**

---

##  Project Structure
Smart_Scheduler/
├── main.py
├── task.py
├── Scheduler.py
├── utils.py
├── gantt.py
├── deadlock.py
├── static/
│ └── style.css
├── templates/
│ ├── index.html
│ └── result.html
└── execution_log.txt



