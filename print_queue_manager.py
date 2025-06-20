class Job:
    def __init__(self, user_id, job_id, priority):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = self.priority_level(priority)
        self.waiting_time = 0

    def priority_level(self, label):
        levels = {"High": 1, "Medium": 2, "Low": 3}
        return levels.get(label, 3)

    def __str__(self):
        return f"UserID: {self.user_id}, JobID: {self.job_id}, Priority: {self.priority}, Waiting Time: {self.waiting_time}"


class PriorityManager:
    def update_priority(self, job, boost=1):
        old_priority = job.priority
        job.priority = max(1, job.priority - boost)  # Boost priority (lower value = higher)
        print(f"Priority Boosted: Job {job.job_id} {old_priority} → {job.priority}")


class JobQueues:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queues = []

    def enqueue(self, job):
        if len(self.queues) < self.capacity:
            self.queues.append(job)
            print(f"Enqueued: {job}")
        else:
            print("Queue is Full!")

    def dequeue(self):
        if not self.queues:
            print("Queue is empty")
            return None

        self.queues.sort(key=lambda x: x.priority)
        removed = self.queues.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def applying_age(self, threshold=5):
        pm = PriorityManager()
        for job in self.queues:
            job.waiting_time += 1
            if job.waiting_time >= threshold:
                print(f"Job {job.job_id} exceeded waiting time threshold.")
                pm.update_priority(job)

    def display(self):
        print("\nCurrent Queue:")
        if not self.queues:
            print("Queue is empty.")
        else:
            for job in sorted(self.queues, key=lambda x: x.priority):
                print(job)


if __name__ == "__main__":
    queues = JobQueues(capacity=3)

    # Create jobs
    jobs = [
        Job("user01", "job101", "High"),
        Job("user02", "job102", "Low"),
        Job("user03", "job103", "Medium")
    ]

    # Enqueue jobs
    for job in jobs:
        queues.enqueue(job)

    queues.display()

    # Simulate waiting
    print("\n-- Applying Aging --")
    for i in range(3):  # Simulate 3 time steps
        queues.applying_age(threshold=3)

    queues.display()

    # Dequeue one and enqueue a new one to maintain capacity
    print("\n-- Dequeue and Enqueue --")
    queues.dequeue()
    queues.enqueue(Job("user04", "job104", "Low"))

    queues.display()
