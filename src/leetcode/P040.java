import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 1/31/18.
 */
public class P040 {
    public void search(List<List<Integer>> solSet, Deque<Integer> curSol, int[] candidates, int[] sum, int point, int target) {
        if (target == 0) {
            List<Integer> sol = new LinkedList<>();
            for (Integer i: curSol) sol.add(i);
            solSet.add(sol);
            return;
        }
        if (point >= candidates.length || sum[point] < target) return;
        if (target - candidates[point] >= 0) {
            curSol.offer(candidates[point]);
            search(solSet, curSol, candidates, sum, point + 1, target - candidates[point]);
            curSol.pollLast();
        }
        int nextPoint = point + 1;
        while (nextPoint < candidates.length && candidates[nextPoint] == candidates[point]) nextPoint++;
        search(solSet, curSol, candidates, sum, nextPoint, target);
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        for (int i = 0; i < candidates.length >> 1; i++) {
            int tmp = candidates[i];
            candidates[i] = candidates[candidates.length - 1 - i];
            candidates[candidates.length - 1 - i] = tmp;
        }
        int[] sum = new int[candidates.length + 1];
        for (int i = candidates.length - 1; i >= 0; i--) sum[i] = sum[i + 1] + candidates[i];
        List<List<Integer>> solSet = new LinkedList<>();
        search(solSet, new LinkedList<>(), candidates, sum, 0, target);
        return solSet;
    }

    public static void main(String[] args) {
        P040 p = new P040();
        p.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8);
    }
}
