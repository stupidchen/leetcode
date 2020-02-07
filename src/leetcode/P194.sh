#!/usr/bin/env bash

cat file.txt | awk ' {
    for (i = 1; i <= NF; i++) {
        arr[i, NR] = $i;
        if (nf <= NF) {
            nf = NF;
        }
    }
}
END {
    for (i = 1; i <= nf; i++) {
        if (i != 1) {
            printf("\n");
        }
        for (j = 1; j <= NR; j++) {
            if (j != 1) {
                printf(" ");
            }
            printf("%s", arr[i, j]);
        }
    }
}
'