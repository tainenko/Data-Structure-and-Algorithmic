# python3
import heapq


class Worker:
    def __init__(self, id, free_Time=0):
        self.id = id
        self.free_Time = free_Time

    def __lt__(self, other):
        if self.free_Time == other.free_Time:
            return self.id < other.id
        return self.free_Time < other.free_Time

    def __gt__(self, other):
        if self.free_Time == other.free_Time:
            return self.id > other.id
        return self.free_Time > other.free_Time

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def adv_assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.worker = [Worker(i) for i in range(self.num_workers)]

        for i in range(len(self.jobs)):
            freeThread = heapq.heappop(self.worker)
            self.assigned_workers[i] = freeThread.id
            self.start_times[i] = freeThread.free_Time
            freeThread.free_Time += self.jobs[i]
            heapq.heappush(self.worker, freeThread)




    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        #self.assign_jobs()
        self.adv_assign_jobs()
        self.write_response()
if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

