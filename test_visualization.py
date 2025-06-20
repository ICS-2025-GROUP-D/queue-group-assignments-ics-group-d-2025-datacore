from tkinter import Tk
from types import SimpleNamespace
from print_queue_manager import PrintQueueManager

def test_visualization_with_dummy_data():
    manager = PrintQueueManager()

    # Create dummy job data using SimpleNamespace (acts like a simple object)
    dummy_jobs = [
        SimpleNamespace(user_id="U001", job_id="J101", priority=5, waiting_time=2),
        SimpleNamespace(user_id="U002", job_id="J102", priority=3, waiting_time=4),
        SimpleNamespace(user_id="U003", job_id="J103", priority=7, waiting_time=1),
    ]

    # Add dummy jobs to the manager's queue
    manager.queue = dummy_jobs

    # Display the GUI (will block until closed)
    manager.show_status_gui()

if __name__ == "__main__":
    test_visualization_with_dummy_data()
