from collections import deque
def solution(bridge_length, limit, truck_weights):
    # 초당 시뮬
    # queue에 다리의 길이나 무게가 수용가능하면 queue에 다리 탈출 시간을 넣는다.
    # 만약 수용가능하지 않으면 deque하면서 다음 탈출 시간으로 갱신
    truck_weights = deque(truck_weights)
    queue = deque()
    current_weight = 0
    time = 0
    while truck_weights:
        #print(time, queue, current_weight)
        weight = truck_weights.popleft()
        while queue: # queue가 비거나 수용가능할 때 까지 deque하고 타임 갱신
            end_time, w = queue[0]
            if len(queue) < bridge_length and (current_weight + weight) <= limit:
                break
            else:
                time = end_time
                current_weight -= w
                queue.popleft()
        time += 1
        queue.append((time + bridge_length-1, weight))
        current_weight += weight
        if queue[0][0] < time: # 시간이 1초 지남에 따라 pop
            current_weight -= queue[0][1]
            queue.popleft()
            
    #print(time, queue)
    return queue[-1][0] + 1
        
        