# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Heap:
    def __init__(self, data):
        self.heap = data
        self.size = len(data)
    
    def __left_child(self, i):
        if 2*(i+1) - 1 >= len(self.heap):
            return i
        else:
            return 2*(i+1) - 1

    def __right_child(self, i):
        if 2*(i+1) >= len(self.heap):
            return i
        else:
            return 2*(i+1)

    def __shift_down(self, i):
        min_idx = i
        l = self.__left_child(i)
        r = self.__right_child(i)
        if (self.heap[l][0] < self.heap[min_idx][0]) or (self.heap[l][0] == self.heap[min_idx][0] and self.heap[l][1] < self.heap[min_idx][1]):
            min_idx = l
        if (self.heap[r][0] < self.heap[min_idx][0]) or (self.heap[r][0] == self.heap[min_idx][0] and self.heap[r][1] < self.heap[min_idx][1]):
            min_idx = r

        if i != min_idx:
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            self.__shift_down(min_idx)
    
    def build_heap(self):
        self.__shift_down(0)
        
    def extract_min(self):
        return self.heap[0]

    def insert(self, insert_val):
        self.heap[0][0] = insert_val

def efficient_parallel(n_workers, jobs):
    tmp, result = [], []
    # make a heap
    for i in range(n_workers):
        tmp.append([0, i])
    heap = Heap(tmp)
    del tmp

    for i in range(len(jobs)):
        latest_time, latest_thread = heap.extract_min()
        heap.insert(latest_time + jobs[i])
        heap.build_heap()

        result.append(AssignedJob(latest_thread, latest_time))
    return result

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    # n_workers, n_jobs = 10, 100
    jobs = list(map(int, input().split()))
    # tmp = '124860658 388437511 753484620 349021732 311346104 235543106 665655446 28787989 706718118 409836312 217716719 757274700 609723717 880970735 972393187 246159983 318988174 209495228 854708169 945600937 773832664 587887000 531713892 734781348 603087775 148283412 195634719 968633747 697254794 304163856 554172907 197744495 261204530 641309055 773073192 463418708 59676768 16042361 210106931 901997880 220470855 647104348 163515452 27308711 836338869 505101921 397086591 126041010 704685424 48832532 944295743 840261083 407178084 723373230 242749954 62738878 445028313 734727516 370425459 607137327 541789278 281002380 548695538 651178045 638430458 981678371 648753077 417312222 446493640 201544143 293197772 298610124 31821879 46071794 509690783 183827382 867731980 524516363 376504571 748818121 36366377 404131214 128632009 535716196 470711551 19833703 516847878 422344417 453049973 58419678 175133498 967886806 49897195 188342011 272087192 798530288 210486166 836411405 909200386 561566778'
    # jobs = [int(j) for j in tmp.split(' ')]
    assert len(jobs) == n_jobs

    assigned_jobs = efficient_parallel(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
