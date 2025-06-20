def tick(self):
    self.time += 1

    for job in self.queue:
        job["waiting_time"] += 1

    for job in self.queue:
        if job["waiting_time"] % self.aging_threshold == 0:
            job["priority"] += 1  # or -= 1 if lower number = higher priority

    self.queue = [
        job for job in self.queue if job["waiting_time"] <= self.expiry_time
    ]
