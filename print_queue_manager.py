class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.time = 0

    def tick(self):
        self.time += 1
        for job in self.queue:
            job['waiting_time'] += 1
        self.apply_priority_aging()
        self.remove_expired_jobs()

    def apply_priority_aging(self):
        for job in self.queue:
            if job['waiting_time'] % 3 == 0 and job['waiting_time'] != 0:
                job['priority'] += 1

    def remove_expired_jobs(self):
        max_wait_time = 10
        self.queue = [job for job in self.queue if job['waiting_time'] <= max_wait_time]

    def enqueue_job(self, user_id, job_id, priority):
        job = {
            'user_id': user_id,
            'job_id': job_id,
            'priority': priority,
            'waiting_time': 0
        }
        self.queue.append(job)

    def show_status(self):
        sorted_queue = sorted(self.queue, key=lambda job: (-job['priority'], job['waiting_time']))
        for job in sorted_queue:
            print(f"User: {job['user_id']}, Job: {job['job_id']}, Priority: {job['priority']}, Waiting: {job['waiting_time']}")
