import psutil
import time
import logging

# Configure logging
logging.basicConfig(filename="process_monitor.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def monitor_processes():
    """Monitors system processes and logs high CPU/memory usage."""
    threshold_cpu = 20.0  # Set CPU usage threshold (percentage)
    threshold_memory = 200 * 1024 * 1024  # Set memory usage threshold (200MB)

    print(f"Monitoring processes... (CPU > {threshold_cpu}%, Memory > 200MB)")

    while True:
        for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                pid = process.info['pid']
                name = process.info['name']
                cpu_usage = process.info['cpu_percent']
                memory_usage = process.info['memory_info'].rss  # Resident Set Size (RAM usage)

                # Log processes exceeding thresholds
                if cpu_usage > threshold_cpu or memory_usage > threshold_memory:
                    log_message = f"High resource usage: {name} (PID {pid}) - CPU: {cpu_usage:.2f}%, Memory: {memory_usage / (1024 * 1024):.2f}MB"
                    logging.warning(log_message)
                    print(log_message)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        time.sleep(5)  # Check every 5 seconds


if __name__ == "__main__":
    monitor_processes()
