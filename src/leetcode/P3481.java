import java.util.*;

/**
 * Created by mike on 1/30/18.
 */
public class Solution {
    public void search(List<List<Integer>> solSet, Deque<Integer> curSol, int[] candidates, int point, int target) {
        if (target == 0) {
            List<Integer> sol = new LinkedList<>();
            for (Integer i: curSol) sol.add(i);
            solSet.add(sol);
            return;
        }
        if (point >= candidates.length) return;
        int limit = target / candidates[point];
        for (int i = 0; i < limit; i++) {
            curSol.offer(candidates[point]);
        }
        target = target % candidates[point];
        for (int i = limit; i > 0; i--) {
            search(solSet, curSol, candidates, point + 1, target);
            curSol.pollLast();
            target += candidates[point];
        }
        search(solSet, curSol, candidates, point + 1, target);
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        for (int i = 0; i < candidates.length >> 1; i++) {
            int tmp = candidates[i];
            candidates[i] = candidates[candidates.length - 1 - i];
            candidates[candidates.length - 1 - i] = tmp;
        }
        List<List<Integer>> solSet = new LinkedList<>();
        search(solSet, new LinkedList<>(), candidates, 0, target);
        return solSet;
    }
}
