int getPosition(int *nums, int numsSize, int target, int method) { //Get the most left/right position of the target, method = 0 is left, otherwise is right
    int l, r, mid, midp;
    int result = -1;

    l = 0; r = numsSize - 1;
    while (l <= r) {
        midp = (l + r) >> 1;
        mid = *(nums + midp);
        if (mid > target) {
            r = midp - 1;
            continue;
        }
        if (mid < target) {
            l = midp + 1;
            continue;
        }

        result = midp;
        if (method) {
            l = midp + 1;
        } 
        else {
            r = midp - 1;
        }
    }

    return result;
}

int *searchRange(int *nums, int numsSize, int target, int *returnSize) {
    int *result = (int *)malloc(sizeof(int) * 2);
    int l, r;

    l = getPosition(nums, numsSize, target, 0);
    r = getPosition(nums, numsSize, target, 1);

    *result = l;
    *(result + 1) = r;
    *returnSize = 2;

    return result;
}
