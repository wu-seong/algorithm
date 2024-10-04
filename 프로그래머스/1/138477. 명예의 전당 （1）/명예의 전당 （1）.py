def solution(k, scores):
    # k크기의 배열 전까지는 계속 push하면서 가장작은 값을 추가
    result = []
    board = []
    for i in range(min(k,len(scores))):
        board.append(scores[i])
        result.append(min(board))
    board.sort(reverse=True)
    # k부터는 최솟값보다 작으면 pass 크거나 같으면 추가 후 정렬
    for i in range(k,len(scores)):
        #print(board)
        min_value = min(board)
        if scores[i] <= min_value:
            result.append(min_value)
            continue
        else:
            board.remove(min_value)
            board.append(scores[i])
            result.append(min(board))
    return (result)