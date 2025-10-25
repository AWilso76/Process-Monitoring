# ⚙️System Process Monitoring Script


# Overview
This script monitors running system processes and flags any that exceed defined CPU or memory thresholds.  
It’s designed to demonstrate proactive system monitoring and troubleshooting.

# Features

- 🧠 Tracks all active system processes  
- 📈 Logs processes exceeding CPU/memory usage thresholds  
- ⏱️ Runs continuously at set intervals  
- ⚠️ Real-time alerts printed to console and saved to `process_monitor.log`  

# Tools & Technologies

- **Language:** Python 3.x  
- **Module:** `psutil`  
- **Environment:** Windows / Linux  

# Relevance to IT Support / Applications Analyst Role

This project highlights:
- Preventive monitoring for performance issues  
- Log creation for incident response and troubleshooting  
- Understanding of system resource management and automation scripting  

# Prerequisites

Install psutil

# Usage

1. Clone the repo

2. Run the script:

python process_monitor.py

3. Review alerts in the terminal or the generated log file.


# Example Log Output

[2025-10-25 15:22:44] ALERT: chrome.exe - CPU: 85% - Memory: 420 MB

[2025-10-25 15:24:01] ALERT: msedge.exe - CPU: 78% - Memory: 380 MB


# Future Enhancements

- Add email or Teams alert notifications

- Include configurable thresholds in config.json

- Integrate with enterprise monitoring tools (e.g., Splunk, Sentinel, SolarWinds)


# Screenshots

---
## Python Script
Using PyCharm created a script that monitors system processes and logs high CPU and memory usage.
At the bottom of this screenshot, you can see the logs generated, indicating high resource usage for "pycharm64.exe" with the (PID) process ID 26800.

<img width="1000" alt="image" src="https://i.imgur.com/9dWicBC.png">

---

## Task Manager
The same information regarding high CPU and memory usage regarding "pycharm64.exe" process log is reflected in Task Manager. Under the "Processes" header located in the left pane, under "Name", PyCharm Community Edition application is at 100% CPU usage and 93% memory usage same information displayed after running script. The (PID) process ID 26800 is in the last column.
<img width="1000" alt="image" src="https://i.imgur.com/Xz6shta.png">
