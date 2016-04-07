import java.util.ArrayList;
import java.util.List;
import java.lang.String;

public class P228{
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<String>();
        if (nums.length != 0) {
            int i, ll = nums[0];
            for (i = 1; i < nums.length; i++) {
                if (nums[i] - nums[i - 1] != 1) {
                    if (nums[i - 1] == ll) {
                        result.add(String.valueOf(ll));
                    } else {
                        result.add(String.valueOf(ll) + "->" + String.valueOf(nums[i - 1]));
                    }
                    ll = nums[i];
                }
            }
            if (nums[i - 1] == ll) {
                result.add(String.valueOf(ll));
            }
            else{
                result.add(String.valueOf(ll) + "->" + String.valueOf(nums[i - 1]));
            }
        }
        return result;
    }
}