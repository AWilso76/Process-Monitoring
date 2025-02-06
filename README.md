# Process-Monitoring
Created a python script which monitors system processes and logs high CPU and memory usage.

# Overview

This script monitors system processes and logs high CPU and memory usage. 
It's useful for system administrators to detect resource-heavy processes and optimize system performance.

# Features
1. Monitors all running processes.
2. Logs processes exceeding CPU or memory thresholds.
3. Displays real-time alerts in the console.
4. Saves logs to process_monitor.log for review.

---

# Python Script
Using PyCharm created a script that monitors system processes and logs high CPU and memory usage.
At the bottom of this screenshot, you can see the logs generated, indicating high resource usage for "pycharm64.exe" with the (PID) process ID 26800.

<img width="1000" alt="image" src="https://i.imgur.com/9dWicBC.png">

---

# Task Manager
The same information regarding high CPU and memory usage regarding "pycharm64.exe" process log is reflected in Task Manager. Under the "Processes" header located in the left pane, under "Name", PyCharm Community Edition application is at 100% CPU usage and 93% memory usage same information displayed after running script. The (PID) process ID 26800 is in the last column.
<img width="1000" alt="image" src="https://i.imgur.com/Xz6shta.png">
