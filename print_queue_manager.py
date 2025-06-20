class PrintQueueManager:
    def __init__(self, expiry_time=10):
        self.queue = []
        self.expiry_time = expiry_time
        self.current_time = 0

    def enqueue_job(self, user_id, job_id, priority):
        job = {
            'user_id': user_id,
            'job_id': job_id,
            'priority': priority,
            'waiting_time': 0,
            'arrival_time': self.current_time
        }
        self.queue.append(job)

    def tick(self):
        self.current_time += 1
        for job in self.queue:
            job['waiting_time'] += 1
        self.remove_expired_jobs()

    def remove_expired_jobs(self):
        expired_jobs = [job for job in self.queue if job['waiting_time'] >= self.expiry_time]
        self.queue = [job for job in self.queue if job['waiting_time'] < self.expiry_time]

        for job in expired_jobs:
            print(f"[EXPIRED] Job {job['job_id']} from user {job['user_id']} expired after {job['waiting_time']} ticks.")

    def show_status(self):
        print(f"\n[STATUS @ tick {self.current_time}]")
        if not self.queue:
            print("Queue is empty.")
        else:
            for job in self.queue:
                print(f"JobID: {job['job_id']}, UserID: {job['user_id']}, Priority: {job['priority']}, Waiting: {job['waiting_time']} ticks")
        print()
