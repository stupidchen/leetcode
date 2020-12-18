bool increasingTriplet(int* nums, int numsSize) {
    int min1 = -0xfffffff, min2 = -0xfffffff, min3 = -0xfffffff;
    int i;

    for (i = 0; i < numsSize; i++){
        int t = *(nums + i);
        if (t > min2 && min2 != -0xfffffff){
            if (t < min3 || min3 == -0xfffffff){
                min3 = t;
                return true;
            }
        }
        if (t > min1 && min1 != -0xfffffff){
            if (t < min2 || min2 == -0xfffffff) min2 = t;
        }
        if (t < min1 || min1 == -0xfffffff) min1 = t;
    }

    return false;
}