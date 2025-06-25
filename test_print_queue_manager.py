import unittest
from print_queue_manager import PrintQueueManager

class TestPrintQueueManager(unittest.TestCase):
    def test_enqueue_and_tick(self):
        pq = PrintQueueManager()
        pq.enqueue_job("U1", "J101", 1)
        pq.enqueue_job("U2", "J102", 2)

        pq.tick()
        pq.tick()
        pq.tick()

        status = pq.show_status()
        self.assertEqual(len(status), 2)
        self.assertEqual(status[0]['user_id'], "U2")
        self.assertEqual(status[0]['priority'], 3)  # aged at 3 ticks

    def test_expiry(self):
        pq = PrintQueueManager()
        pq.enqueue_job("U1", "J101", 1)

        for _ in range(11):
            pq.tick()

        status = pq.show_status()
        self.assertEqual(len(status), 0)  # job expired after 10 ticks

if __name__ == '__main__':
    unittest.main()
