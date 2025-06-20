class PrintQueueManager:
    def __init__(self, capacity=10):
        self.queue = []
        self.capacity = capacity
        self.current_time = 0

    def enqueue_job(self, user_id, job_id, priority):
        pass  # Module 1

    def dequeue_job(self):
        pass  # Module 1

    def apply_priority_aging(self):
        pass  # Module 2

    def remove_expired_jobs(self):
        pass  # Module 3

    def handle_simultaneous_submissions(self, jobs):

        pass  # Module 4

    def tick(self):
         pass     # Module 5

    def show_status(self):
        pass  # Module 6
