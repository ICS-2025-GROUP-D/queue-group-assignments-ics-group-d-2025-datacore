import unittest
from print_queue_manager import Job, PriorityManager, JobQueues

class TestPriorityManager(unittest.TestCase):

    def test_priority_conversion(self):
        job = Job("U1", "J1", "High")
        self.assertEqual(job.priority, 1)
        job2 = Job("U2", "J2", "Medium")
        self.assertEqual(job2.priority, 2)
        job3 = Job("U3", "J3", "Low")
        self.assertEqual(job3.priority, 3)

    def test_enqueue_and_dequeue(self):
        queue = JobQueues(2)
        job1 = Job("U1", "J1", "Medium")
        job2 = Job("U2", "J2", "Low")

        queue.enqueue(job1)
        queue.enqueue(job2)

        self.assertEqual(len(queue.queues), 2)

        removed = queue.dequeue()
        self.assertEqual(removed.job_id, "J1")  # Medium priority is higher than Low

    def test_priority_aging(self):
        queue = JobQueues(1)
        job = Job("U1", "J1", "Low")  # Priority 3
        queue.enqueue(job)

        for _ in range(5):
            queue.applying_age(threshold=2)

        # Priority should now be boosted from 3 to 1
        self.assertEqual(job.priority, 1)

if __name__ == '_main_':
    unittest.main()