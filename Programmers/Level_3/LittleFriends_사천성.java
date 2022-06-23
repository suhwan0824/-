import java.util.*;

class LittleFriends_사천성 {

    static ArrayList<node>[] arrayLists = new ArrayList[26];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static char[][] map;

    public String solution(int m, int n, String[] board) {
        HashSet<Character> hashSet = new HashSet<>();
        String answer = "";
        map = new char[m][n];
        int count = 0;

        for (int i = 0; i < 26; i++) {
            arrayLists[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            String[] str = board[i].split("");
            for (int j = 0; j < n; j++) {
                char c = str[j].charAt(0);
                map[i][j] = c;
                if ('A' <= c && c <= 'Z') {
                    arrayLists[c - 'A'].add(new node(i, j, 0, 0));
                    count++;
                    hashSet.add(c);
                }
            }
        }

        count /= 2;
        while (count-- >= 0) {
            for (int i = 0; i < 26; i++) {
                if (arrayLists[i].size() > 0) {
                    if (bfs(m, n, i)) {
                        answer += (char) (i + 65);
                        break;
                    }
                }
            }
        }

        if (hashSet.size() != answer.length()) answer = "IMPOSSIBLE";
        return answer;
    }

    public static boolean bfs(int m, int n, int idx) {
        Queue<node> queue = new LinkedList<>();
        int first_x = arrayLists[idx].get(0).x;
        int first_y = arrayLists[idx].get(0).x;
        queue.add(new node(first_x, first_y, 0, 0));
        queue.add(new node(first_x, first_y, 1, 0));
        queue.add(new node(first_x, first_y, 2, 0));
        queue.add(new node(first_x, first_y, 3, 0));

        while (!queue.isEmpty()) {
            node cur = queue.poll();
            if (cur.count > 1) continue;

            if (cur.x == arrayLists[idx].get(1).x && cur.y == arrayLists[idx].get(1).y) {
                map[arrayLists[idx].get(0).x][arrayLists[idx].get(0).y]
                        = map[arrayLists[idx].get(1).x][arrayLists[idx].get(1).y]
                        = '.';
                arrayLists[idx].remove(1);
                arrayLists[idx].remove(0);
                return true;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (map[nx][ny] == '*') continue;
                if (map[nx][ny] == '.' || map[nx][ny] == map[arrayLists[idx].get(0).x][arrayLists[idx].get(0).y]) {
                    if (cur.dir == i) queue.add(new node(nx, ny, i, cur.count));
                    else queue.add(new node(nx, ny, i, cur.count + 1));
                }
            }
        }
        return false;
    }

    static class node{
        int x, y, dir, count;

        public node(int x, int y, int dir, int count) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.count = count;
        }
    }
}