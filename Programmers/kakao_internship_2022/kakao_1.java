class Solution{
    
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        char[] str = {'R', 'C', 'J', 'A'};
        int[] result = {0, 0, 0, 0};

        for (int i = 0; i < survey.length; i++) {
            char[] tmp = survey[i].toCharArray();
            for (int j = 0; j < 4; j++) {
                if (tmp[0] == str[j]) {
                    result[j] += 4 - choices[i];
                    break;
                }
                if (tmp[1] == str[j]) {
                    result[j] += choices[i] - 4;
                }
            }
        }

        answer += (result[0] >= 0) ? 'R' : 'T';
        answer += (result[1] >= 0) ? 'C' : 'F';
        answer += (result[2] >= 0) ? 'J' : 'M';
        answer += (result[3] >= 0) ? 'A' : 'N';
        return answer;
    }
}


