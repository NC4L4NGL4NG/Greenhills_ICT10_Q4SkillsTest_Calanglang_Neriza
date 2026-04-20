import matplotlib.pyplot as plt
import numpy as np
from pyscript import display, document

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absence_counts = np.array([0, 0, 0, 0, 0])

def generate_graph():
    plt.clf() 
    fig, ax = plt.subplots(figsize=(7, 5))
    
    ax.plot(days, absence_counts, marker='o', color='blue')
    
    ax.set_title("Weekly Attendance")
    ax.set_xlabel("Day")
    ax.set_ylabel("Absences")
    ax.grid(True)
    ax.set_ylim(0, 10) 

    document.getElementById("graph-output").innerHTML = "" 
    display(fig, target="graph-output")

def update_data(event):
    day = document.getElementById("day-select").value
    val = document.getElementById("absence-input").value
    
    if not val:
        val = 0
    
    for i in range(len(days)):
        if days[i] == day:
            absence_counts[i] = int(val)
    
    generate_graph()

generate_graph()