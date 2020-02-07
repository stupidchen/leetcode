import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/11/18.
 */
public class P797 {
    private void getOneSolution(ArrayList<Integer> queue, ArrayList<Integer> last, int target, List<Integer> solution) {
        if (last.get(target) != -1) getOneSolution(queue, last, last.get(target), solution);
        solution.add(queue.get(target));
    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> ret = new LinkedList<>();
        if (n == 0) return ret;
        ArrayList<Integer> queue = new ArrayList<>();
        ArrayList<Integer> last = new ArrayList<>();
        ArrayList<Integer> visit = new ArrayList<>();
        queue.add(0);
        last.add(-1);
        visit.add(1);
        int h = 0, t = 1;
        while (h < t) {
            int cur = queue.get(h);
            if (cur == 1) {
                int a  =1;
            }
            if (cur == n - 1) {
                List<Integer> s = new LinkedList<>();
                getOneSolution(queue, last, h, s);
                ret.add(s);
            }
            int vis = visit.get(h);
            for (int i = 0; i < graph[cur].length; i++)
                if (((1 << graph[cur][i]) | vis) != vis) {
                    t++;
                    queue.add(graph[cur][i]);
                    last.add(h);
                    visit.add(vis + (1 << graph[cur][i]));
                }
            h++;
        }

        return ret;
    }
    public static void main(String[] args) {
        P797 p = new P797();
        p.allPathsSourceTarget(new int[][]{{5, 4, 1, 2, 3}, {2, 5}, {4, 5, 3}, {6, 5, 4}, {5, 6}, {6}, {}});
    }
}
