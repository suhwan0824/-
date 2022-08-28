def solution(survey, choices):
    answer = ''
    alpha = ['R', 'C', 'J', 'A']
    result = [0, 0, 0, 0]
    
    for i in range(len(survey)):
        for j in range(4):
            if survey[i][0] == alpha[j]:
                result[j] += 4 - choices[i]
            if survey[i][1] == alpha[j]:
                result[j] += choices[i] - 4
    answer += 'R' if result[0] >= 0 else 'T'
    answer += 'C' if result[1] >= 0 else 'F'
    answer += 'J' if result[2] >= 0 else 'M'
    answer += 'A' if result[3] >= 0 else 'N'
    return answer
