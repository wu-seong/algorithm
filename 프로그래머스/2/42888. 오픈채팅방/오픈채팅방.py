def chat_room(record, nick_dict, result): # 명령어 모두 uid 딕셔너리로 처리
    command = record.split(" ")[0]
    if command == "Enter": 
        c,uid,nick = record.split(" ")
        result.append(nick_dict[uid] + '님이 들어왔습니다.')
    elif command == "Leave":
        c,uid = record.split(" ")
        result.append( nick_dict[uid] + '님이 나갔습니다.')
def find_last_nick(records, nick_dict):
    for record in records:
        split_record = record.split(" ")
        if len(split_record) == 3:
            c, uid, nick = split_record
            nick_dict[uid] = nick
def solution(records):
    # 입장 퇴장 시에는 로그남기기
    # 닉네임 변경 시에는 uuid: 변경된 닉네임으로 수정
    # 결과에는 uuid.현재닉네임
    result = []
    nick_dict = {}
    find_last_nick(records, nick_dict)
    for record in records:
        chat_room(record, nick_dict, result)
    #print(result)
    return result
    