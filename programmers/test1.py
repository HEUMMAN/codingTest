def solution(id_list, report, k):
    report = set(report)
    reported = {}
    mail_list = {}
    for id in id_list:
        mail_list[id] = 0

    answer = []

    make_reported_cases(report, reported)

    reported = {key:value for key, value in reported.items() if value >= k}


    make_mails(mail_list, report, reported)


    for key, value in mail_list.items():
        answer.append(value)

    return answer



def make_mails(mail_list, report, reported):
    for r in report:
        if r.split(' ')[1] in reported:
            mail_list[r.split(' ')[0]] += 1




def make_reported_cases(report, reported):
    for r in report:
        if r.split(' ')[1] in reported:
            reported[r.split(' ')[1]] += 1
        else:
            reported[r.split(' ')[1]] = 1


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
# solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)