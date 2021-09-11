import math

def solution(fees, records):
    dic = {}

    for record in records:
        hour = record.split(':')[0]
        record = record.split(':')[1]
        minute = record.split(' ')[0]
        car = record.split(' ')[1]
        in_out = record.split(' ')[2]


        if car not in dic:
            time_sum = 0
            dic[car] = hour, minute, time_sum, in_out
        else:
            if in_out == 'OUT':
                h, m, t = dic[car][0], dic[car][1], dic[car][2]
                h = int(hour) - int(h)
                m = int(minute) - int(m)
                t = int(h)*60 + int(m) + t
                dic[car] = hour, minute, t, 'OUT'
                print(dic[car])

            elif in_out == 'IN':
                dic[car] = hour, minute, dic[car][2], 'IN'

        if record == records[-1].split(':')[1]:
            for key, value in dic.items():
                if value[3] == 'IN':
                    h, m, t = dic[key][0], dic[key][1], dic[key][2]
                    h = 23 - int(h)
                    m = 59 - int(m)
                    t = int(h)*60 + int(m) + t
                    dic[key] = '23', '59', t, 'OUT'
                    print(key)

    for key, value in dic.items():
        if value[2] <= fees[0]:
            dic[key] = fees[1]
        else:
            minus_fee = value[2] - fees[0]
            time = minus_fee / fees[2]
            time = math.ceil(time)
            result = time * fees[3]
            dic[key] = result + fees[1]
    dic = sorted(dic.items())
    answer = []
    for i in range(len(dic)):
        answer.append(dic[i][1])
    print(dic)
    print(answer)



    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
