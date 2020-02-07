import java.util.Arrays;

/**
 * Created by mike on 2/6/18.
 */

public class P037 {
    class Cell implements Comparable<Cell> {
        int x, y, z;
        int c, v;

        Cell(int x, int y, int z, int c) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.c = c;
            this.v = -1;
        }

        @Override
        public int compareTo(Cell o) {
            return this.c - o.c;
        }
    }
    private int n = 9;

    private int m = 3;

    private boolean solved;

    private int[] bitmap;

    private int countOneOfBinary(int x) {
        int ret = 0;
        while (x > 0) {
            x = x & (x - 1);
            ret++;
        }

        return ret;
    }

    public void solveSudokuByDFS(Cell[] pendingCells, int pendingNumber, int currentCell, int[] r, int[] c, int[] g) {
        if (currentCell >= pendingNumber) {
            solved = true;
            return;
        }

        int x = pendingCells[currentCell].x;
        int y = pendingCells[currentCell].y;
        int z = pendingCells[currentCell].z;

        int possible = r[x] & c[y] & g[z];
        while (possible > 0) {
            int t = possible & (-possible);
            pendingCells[currentCell].v = bitmap[t];
            r[x] -= t;
            c[y] -= t;
            g[z] -= t;
            solveSudokuByDFS(pendingCells, pendingNumber, currentCell + 1, r, c, g);
            if (solved) return;
            r[x] += t;
            c[y] += t;
            g[z] += t;
            possible -= t;
        }
    }

    public void solveSudoku(char[][] board) {
        int[] r = new int[n];
        int[] c = new int[n];
        int[] g = new int[n];
        bitmap = new int[1 << n];

        for (int i = 0; i < 9; i++) {
            r[i] = (1 << 9) - 1;
            c[i] = (1 << 9) - 1;
            g[i] = (1 << 9) - 1;
            bitmap[1 << i] = i;
        }

        int p = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (board[i][j] != '.') {
                    board[i][j] = (char) (board[i][j] - '0' - 1 + '0');
                    int x = i, y = j;
                    int z = i / m * m + j / m;
                    int v = board[i][j] - '0';

                    r[x] -= 1 << v;
                    c[y] -= 1 << v;
                    g[z] -= 1 << v;
                }
                else
                    p++;

        Cell[] pendingCells = new Cell[p];
        int k = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (board[i][j] == '.') {
                    int x = i, y = j;
                    int z = i / m * m + j / m;
                    int count = countOneOfBinary(r[x] & c[y] & g[z]);

                    pendingCells[k++] = new Cell(x, y, z, count);
                }
        Arrays.sort(pendingCells);

        solved = false;
        solveSudokuByDFS(pendingCells, p, 0, r, c, g);

        for (int i = 0; i < p; i++) {
            int x = pendingCells[i].x, y = pendingCells[i].y;
            board[x][y] = (char) (pendingCells[i].v + '0');
        }

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = (char) (board[i][j] - '0' + 1 + '0');
    }

    public static void main(String[] args) {
        P037 p = new P037();
        char[][] board = new char[][]{{'.','.','9','7','4','8','.','.','.'},{'7','.','.','.','.','.','.','.','.'},{'.','2','.','1','.','9','.','.','.'},{'.','.','7','.','.','.','2','4','.'},{'.','6','4','.','1','.','5','9','.'},{'.','9','8','.','.','.','3','.','.'},{'.','.','.','8','.','3','.','2','.'},{'.','.','.','.','.','.','.','.','6'},{'.','.','.','2','7','5','9','.','.'}};
        p.solveSudoku(board);

        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) System.out.print(board[i][j]);
            System.out.println();
        }
    }
}
