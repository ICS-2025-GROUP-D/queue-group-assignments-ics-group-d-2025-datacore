# FINAL SUBMISSION - updated by 192566

import threading

class PrintQueueManager:
    def __init__(self, capacity=10):
        self.queue = []
        self.capacity = capacity
        self.lock = threading.Lock()

    def enqueue_job(self, user_id, job_id, priority):
        with self.lock:
            if len(self.queue) < self.capacity:
                job = {
                    'user_id': user_id,
                    'job_id': job_id,
                    'priority': priority,
                    'waiting_time': 0
                }
                self.queue.append(job)
                print(f"Enqueued: {job}")
            else:
                print("Queue is full. Cannot add job.")

    def handle_simultaneous_submissions(self, jobs):
        """
        Accepts a list of job dictionaries with keys: user_id, job_id, priority
        Submits them concurrently using threads.
        """
        threads = []

        for job in jobs:
            t = threading.Thread(
                target=self.enqueue_job,
                args=(job['user_id'], job['job_id'], job['priority'])
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def show_status(self):
        """
        Prints current queue state.
        """
        print("\nQueue Status:")
        for i, job in enumerate(self.queue):
            print(f"{i + 1}: {job}")
