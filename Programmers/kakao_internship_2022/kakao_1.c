#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char *solution(const char* survey[], size_t survey_len, int choices[], size_t choices_len) {
    char alpha[4] = {'R', 'C', 'J', 'A'};
    char* answer = (char*)malloc(5 * sizeof(char));
    int result[4] = {0};

    for (int i = 0; i < survey_len; i++){
	for (int j = 0; j < 4; j++){
	    if (survey[i][0] == alpha[j]) {
		result[j] += 4 - choices[i];
		break;
	    }
	    if (survey[i][1] == alpha[j]) {
		result[j] += choices[i] - 4;
		break;
	    }
	}
    }

    answer[0] = (result[0] >= 0) ? 'R' : 'T';
    answer[1] = (result[1] >= 0) ? 'C' : 'F';
    answer[2] = (result[2] >= 0) ? 'J' : 'M';
    answer[3] = (result[3] >= 0) ? 'A' : 'N';
    answer[4] = '\0';
    return answer;
}
