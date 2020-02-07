/**
 * Created by mike on 3/4/18.
 */
public class P794 {
    public boolean validTicTacToe(String[] board) {
        int n = board.length;
        if (n != 3) return false;
        for (int i = 0; i < n; i++)
            if (board[i].length() != 3) return false;

        int numX = 0, numO = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if (board[i].charAt(j) == 'X') {
                    numX++;
                }
                else {
                    if (board[i].charAt(j) == 'O') {
                        numO++;
                    }
                    else {
                        if (board[i].charAt(j) != ' ') return false;
                    }
                }
            }

        if (numO > numX || numX - numO > 1) return false;

        int winX = 0, winO = 0;
        char t;
        for (int i = 0; i < n; i++) {
            t = board[i].charAt(0);
            boolean win = true;
            for (int j = 1; j < n; j++)
                if (board[i].charAt(j) != t) {
                    win = false;
                    break;
                }
            if (win) {
                if (t == 'X')
                    winX++;
                if (t == 'O')
                    winO++;
            }

            win = true;
            t = board[0].charAt(i);
            for (int j = 1; j < n; j++)
                if (board[j].charAt(i) != t) {
                    win = false;
                    break;
                }
            if (win) {
                if (t == 'X')
                    winX++;
                if (t == 'O')
                    winO++;
            }
        }
        t = board[0].charAt(0);
        if (t == board[1].charAt(1) && t == board[2].charAt(2)) {
            if (t == 'X')
                winX++;
            if (t == 'O')
                winO++;
        }
        t = board[0].charAt(2);
        if (t == board[1].charAt(1) && t == board[2].charAt(0)) {
            if (t == 'X')
                winX++;
            if (t == 'O')
                winO++;
        }

        if (winX + winO > 1) return false;
        if (winX != 0 && numO == numX) return false;
        if (winO != 0 && numX > numO) return false;
        return true;
    }

    public static void main(String[] args) {
        P794 p = new P794();
        boolean r = p.validTicTacToe(new String[]{"   ", "   ", "   "});
    }
}
