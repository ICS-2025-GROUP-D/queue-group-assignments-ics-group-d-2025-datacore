from print_queue_manager import PrintQueueManager

def test_job_expiry():
    print("Running expiry test...")
    pq = PrintQueueManager(expiry_time=3)

    pq.enqueue_job("User1", "Job1", 1)
    pq.enqueue_job("User2", "Job2", 2)

    for _ in range(4):
        pq.tick()

    assert len(pq.queue) == 0, "Jobs should have expired but are still in queue"
    print("✅ Expiry logic passed.")

if __name__ == "__main__":
    test_job_expiry()
