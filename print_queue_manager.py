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
        print("\nQueue Status:")
        for i, job in enumerate(self.queue):
            print(f"{i + 1}: {job}")

# Example usage:
if __name__ == "__main__":
    pq_manager = PrintQueueManager(capacity=5)

    # Simultaneous job submissions
    jobs_to_submit = [
        {'user_id': 'U1', 'job_id': 'J101', 'priority': 2},
        {'user_id': 'U2', 'job_id': 'J102', 'priority': 3},
        {'user_id': 'U3', 'job_id': 'J103', 'priority': 1}
    ]

    pq_manager.handle_simultaneous_submissions(jobs_to_submit)
    pq_manager.show_status()
