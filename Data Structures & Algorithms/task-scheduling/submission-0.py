'''
return min number of cycles to complete all tasks

[A,A,A,B,C] n = 3

[A:3, B:1, C:1]

max heap
[(3,A),(1,B),(1,C)]

pop off from heap
(3,A)
reduce task count and increase cycle count
(2,A) CC=1
add task and CC+n to queue
[(2,A,4)]
before adding to heap check if CC = queue[0][2] then add to heap
if task_count == 0 then don't add to queue
return CC
'''
import heapq
from collections import deque
class Solution:
    # runtime: O(n) where n is len of tasks
    # space: O(n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}
        max_heap = []
        cooldown_queue = deque()
        cycle_count = 0

        # task freq map
        for task in tasks:
            if task not in task_freq:
                task_freq[task] = 0
            task_freq[task] += 1

        # max heap
        for task, task_count in task_freq.items():
            heapq.heappush(max_heap, (-task_count, task)) # store in max heap

        # get most freq task from max_heap to process task
        while len(max_heap) > 0:
            task_count, task = heapq.heappop(max_heap)
            # process task
            task_count = task_count + 1 # reduced by 1 as neg value for max_heap
            cycle_count += 1
            # add task to cooldown queue if task count is not 0
            if task_count < 0:
                cooldown_queue.append((task_count, task, cycle_count + n))
            # add to max_heap from queue if cycle count == task cooldown
            if cooldown_queue and cycle_count == cooldown_queue[0][2]:
                q_task_count, q_task, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, (q_task_count, q_task))
            # add idle to heap and break if cooldown_queue is empty
            if len(max_heap) == 0 and cooldown_queue:
                heapq.heappush(max_heap, (-1, '#'))
        
        return cycle_count

# TODO: Handle idle case when
'''
["A","A","A","B","C"], n = 3
[A:3,B:1,C:1]
[]

Q=[]

CC=9
'''
        

        