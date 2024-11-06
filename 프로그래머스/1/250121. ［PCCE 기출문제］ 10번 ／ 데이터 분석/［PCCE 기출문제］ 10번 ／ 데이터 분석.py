def solution(datas, ext, val_ext, sort_by):
    '''
    ext의 key값을 인덱스로 변형시키기
    해당 인덱스로 접근하여 val_ext보다 작은 것만 필터링 하기
    sort_by의 key값을 인덱스로 변형시켜 정렬하기
    '''
    key_to_index = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    filtered_data = []
    for data in datas:
        index = key_to_index[ext]
        if data[index] <= val_ext:
            filtered_data.append(data)
    sort_index = key_to_index[sort_by]
    filtered_data.sort(key = lambda x: x[sort_index])
    
    return filtered_data
    
    