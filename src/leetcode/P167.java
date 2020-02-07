/**
 * Created by mike on 4/3/18.
 */
public class P167 {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = new int[2];
        int n = numbers.length;

        for (int i = 0; i < n; i++) {
            int t = target - numbers[i];
            if (i == 23)
            if (t == numbers[i]) {
                if (numbers[i] == numbers[i + 1]) {
                    ret[0] = i + 1;
                    ret[1] = i + 2;
                    break;
                }
                continue;
            }
            int l = 0, r = n - 1, mid = n;
            while (l <= r) {
                mid = (l + r) >> 1;
                if (t == numbers[mid]) break;
                if (t > numbers[mid])
                    l = mid + 1;
                else
                    r = mid - 1;
            }

            if (mid < n && t == numbers[mid]) {
                if (mid > i) {
                    ret[0] = i + 1;
                    ret[1] = mid + 1;
                }
                else {
                    ret[0] = mid + 1;
                    ret[1] = i + 1;
                }
                break;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        P167 p = new P167();
        p.twoSum(new int[]{12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997}, 542);
    }
}
