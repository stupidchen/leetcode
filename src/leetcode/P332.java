import java.util.*;

public class P332 {
    private Random random = new Random();
    private int compare(String[][] tickets, int x, int y) {
        int t = tickets[x][0].compareTo(tickets[y][0]);
        if (t != 0) return t;
        t = tickets[x][1].compareTo(tickets[y][1]);
        return t;
    }
    private void sort(String[][] tickets, int[] order, int x, int y) {
        int l = x, r = y, mid;
        mid = order[random.nextInt(y - x + 1) + x];
        while (l <= r) {
            while ((l <= r) && (compare(tickets, order[l], mid) < 0)) l++;
            while ((l <= r) && (compare(tickets, order[r], mid) > 0)) r--;
            if (l <= r) {
                if (order[l] != order[r]){
                    order[l] = order[l] ^ order[r];
                    order[r] = order[l] ^ order[r];
                    order[l] = order[l] ^ order[r];
                }
                l++;
                r--;
            }
        }
        if (l < y) sort(tickets, order, l, y);
        if (x < r) sort(tickets, order, x, r);
    }
    public int findIndex(String[][] tickets, int[] order, int n, String place) {
        int l = 0, r = n, mid = 0;
        while (l <= r) {
            mid = (l + r) >> 1;
            int t = tickets[order[mid]][0].compareTo(place);
            if (t == 0) break;
            if (t < 0) l = mid + 1;
            else r = mid - 1;
        }
        while ((mid > 0) && (tickets[order[mid - 1]][0].compareTo(place)) == 0) mid--;
        return mid;
    }
    public List<String> findItinerary(String[][] tickets) {
        int n = tickets.length;
        List<String> result = new ArrayList<String>();
        if (n != 0) {
            int[] order = new int[n];
            boolean[] visit = new boolean[n];
            for (int i = 0; i < n; i++) {
                order[i] = i;
                visit[i] = false;
            }
            sort(tickets, order, 0, n - 1);

            String lastVisited = "JFK";
            result.add(lastVisited);
            for (int i = 0; i < n; i++) {
                int t = findIndex(tickets, order, n - 1, lastVisited);
                while (visit[t]) t++;
                visit[t] = true;
                lastVisited = tickets[order[t]][1];
                result.add(lastVisited);
            }
        }
        return result;
    }
}