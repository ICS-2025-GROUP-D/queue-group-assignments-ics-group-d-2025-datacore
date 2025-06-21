# Define a job with metadata
class Job:
    def __init__(self, user_id, job_id, priority):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = priority  # Lower number = higher priority
        self.waiting_time = 0

    def __str__(self):
        return f"UserID: {self.user_id}, JobID: {self.job_id}, Priority: {self.priority}, Waiting Time: {self.waiting_time}"


# Shared class: each team member implements one function
class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.capacity = 10
        self.time = 0
        self.aging_threshold = 3
        self.expiry_time = 10

    # Module 1 – Core Queue Management
    def enqueue_job(self, user_id, job_id, priority):
        pass

    def dequeue_job(self):
        pass

    # Module 2 – Priority & Aging System
    def apply_priority_aging(self):
        pass

    # Module 3 – Job Expiry & Cleanup
    def remove_expired_jobs(self):
        pass

    # Module 4 – Concurrent Job Submission
    def handle_simultaneous_submissions(self, jobs):
        pass

    # Module 5 – Event Simulation (Time Management)
    def tick(self):
        pass

    # Module 6 – Visualization & Reporting
    def show_status(self):
        pass
