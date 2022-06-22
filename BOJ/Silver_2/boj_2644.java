package com.hello.core;


import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class boj_2644 {
    static int n, m;
    static int a, b;
    static int[] visited;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = sc.nextInt();
        b = sc.nextInt();
        m = sc.nextInt();

        map = new int[n + 1][n + 1];
        visited = new int[n + 1];

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            map[x][y] = 1;
            map[y][x] = 1;
        }
        bfs(a, b);

        if (visited[b] == 0) {
            System.out.println(-1);
        } else {
            System.out.println(visited[b]);
        }

    }

    public static void bfs(int start, int end) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);

        while (!q.isEmpty()) {
            int vertex = q.poll();

            if (vertex == end)
                break;
            for (int i = 1; i <= n; i++) {
                if (map[vertex][i] == 1 && visited[i] == 0) {
                    visited[i] = visited[vertex] + 1;
                    q.add(i);
                }
            }
        }
    }
}