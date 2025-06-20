from print_queue_manager import PrintQueueManager


pq = PrintQueueManager()


pq.enqueue_job("User1", "J001", 2)
pq.enqueue_job("User2", "J002", 3)
pq.enqueue_job("User3", "J003", 1)


pq.show_status()

pq.dequeue_job()


pq.show_status()
