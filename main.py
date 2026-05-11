import matplotlib.pyplot as plt
import numpy as np
from pyscript import display, document

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absence_counts = np.array([0, 0, 0, 0, 0])

def generate_graph():
    plt.clf() 
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(days, absence_counts, marker='o', color='black')
    
    ax.set_title("Weekly Attendance")
    ax.set_xlabel("Day")
    ax.set_ylabel("Absences")
    ax.grid(True)

    # --- THE FIX IS HERE ---
    current_max = np.max(absence_counts)
    if current_max < 10:
        ax.set_ylim(0, 1000) # Keep it at 10 if numbers are small
    else:
        ax.set_ylim(0, current_max + 5) # If Sir goes over 10, expand the paper!
    # -----------------------

    document.getElementById("graph-output").innerHTML = "" 
    display(fig, target="graph-output")
