int firstMissingPositive(int *nums, int numsSize) {
    int i, t1, t2, t;

    i = 0;
    while (i < numsSize) {
        t1 = *(nums + i);
        if (t1 == i + 1 || t1 <= 0 || t1 > numsSize) {
            i++;
        }
        else {
            t2 = *(nums + t1 - 1);
            if (t1 != t2) {
                t = *(nums + i);
                *(nums + i) = *(nums + t1 - 1);
                *(nums + t1 - 1) = t;
            }
            else i++;
        }
    }

    i = 0;
    while ((*(nums + i) == i + 1) && i < numsSize) i++;

    return i + 1;
}
