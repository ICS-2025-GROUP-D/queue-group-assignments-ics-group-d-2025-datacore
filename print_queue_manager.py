class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.time = 0

    def enqueue_job(self, user_id, job_id, priority):
        job = {
            "user_id": user_id,
            "job_id": job_id,
            "priority": priority,
            "waiting_time": 0
        }
        self.queue.append(job)

    def tick(self):
        self.time += 1

        for job in self.queue:
            job["waiting_time"] += 1

        for job in self.queue:
            if job["waiting_time"] % 3 == 0:
                job["priority"] += 1

        self.queue = [
            job for job in self.queue if job["waiting_time"] <= 10
        ]

    def show_status(self):
        sorted_jobs = sorted(
            self.queue,
            key=lambda job: (-job["priority"], job["waiting_time"])
        )
        return sorted_jobs
