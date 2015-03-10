
# Sort Algorithms

###**Bucket Sort**
    e.g.(6, 4, 8, 3, 6, 1, 3, 6)
    類似次數分配表
    -----------------------------------------
    | 1 | 0 | 2 | 1 | 0 | 3 | 0 | 1 | 0 | 0 |
    -----------------------------------------
      1   2   3   4   5   6   7   8   9   10

    Given N integers in the range 1 to M --> O(M+N)
    disadvantage: if M = N^P, 需要開的陣列就太大了

###**Radix Sort I**
    Given (64, 8, 216, 512, 27, 729 0, 1, 343, 125)
    先根據個位數做Bucket Sort, 再根據十位數, 再根據百位數(不可百-->十-->個)
    (**依據有幾個籃子判斷要mod多少。EX. 7 個籃子，就 mod 7 後放相對應籃子**)
    做的回合　 M = log(M)
    放幾次數字 N = log(M)*N
    收籃子幾次   = 10*log(M)

    Sum = log(M)(N+10)

    用linkedlist來達成減少記憶體空間：
    -----------------------------------------
    | 1 | 0 | 2 | 1 | 0 | 3 | 0 | 1 | 0 | 0 |
    -----------------------------------------
      1   2   3   4   5   6   7   8   9   10

    Given N integers in the range 1 to M --> O(M+N)
    disadvantage: if M = N^P, 需要開的陣列就太大了

###**Radix Sort II**
    Given (64, 8, 216, 512, 27, 729 0, 1, 343, 125)
    先根據個位數做Bucket Sort, 再根據十位數, 再根據百位數(不可百-->十-->個)

    做的回合M = log(M)       |
    放幾次數字N = log(M)*N   |--> Sum = log(M)(N+10)
    收籃子幾次 = 10*log(M)   |

    *用linkedlist來達成減少記憶體空間：
                        ----
                        |  |  
                        ----
                         ^
                         |
                        ---- ----
                        |  | |  |  
                        ---- ----
                         ^    ^
                         |    |
                        -----------------------------------------
    存linkedlist的頭--> |    |   |   |   |   |   |   |   |   |   |
                        -----------------------------------------
                          1   2   3   4   5   6   7   8   9   10



### Instertion Sort
        0   1   2  ... ...  P  ... ... ... N-1    每回合中
      -----------------------------------------   將 index P 的值插入到sorted的正確位置
      |   |   |   |   |   |   |   |   |   |   |   **index P就是 sorted & unsorted 的交界處
      -----------------------------------------
      |-------sorted------||-----unsorted-----|

### Selection Sort
        0   1   2  ... ...  P  ... ... ... N-1    每回合中
      -----------------------------------------   將 unsorted 中最小值(min) 換到 index P 的位置
      |   |   |   |   |   |   |   |min|   |   |   **index P就是 sorted & unsorted 的交界處
      -----------------------------------------
      |-------sorted------||-----unsorted-----|

### Merge Sort
    11   8   14   7   6   8   23   4
     \  /     \  /     \  /    \  /
     8,11     7,14     6,8     4,23
       \       /        \       /
       7,8,11,14         4,6,8,23
           \                /
           4,6,7,8,8,11,14,23

### Quick Sort
    每回合中：
        1. 選 pivot, 把資料分成 >pivot & <pivot 兩種
        2. 持續將切分的資料再選 pivot 切分
        3. merge

    -要選出好的標兵(中位數) = 通常都是拿一筆資料 頭、中、尾 選中間的
    -Divide and Conquer, needs extra spaces for stack(recursive)


## Sorting
method 	|	average |	worst 		|	stability   |	extra space
----------- | ------------ | ------------- | ------------- | ---------------------
Bucket 	|	O(n) 	|	O(m) 		|	stable 		|	O(m)
Radix 	|	O(nlogpK) |	O(nlogpK)~O(n)|  stable 	|		O(nxp)
Instertion |	O(n^2) 	|	O(n^2) 		|	stable 		|	O(1)
Selection |	O(n^2)	|	O(n^2) 		|	unstable 	|	O(1)
Bubble 	|	O(n^2)	|	O(n^2)        |  stable 	|		O(1)
Merge 	|	O(nlogn) |	O(nlogn)      |  stable 	|		O(n)
Quick 	|	O(nlogn) |	O(n^2) 		|	unstable 	|	O(logn)~O(n)
Heap 	|	O(nlogn) |	O(nlogn) 	|	unstable 	|	O(1)


* 同分時的順序不改變為stable
* Sorting(Comparison base Algorithm) 最快就是 O(nlogn)

## Sorting Large Structures `p.312`
大型資料排序要做太多交換動作 ---> (用一個陣列當key值) ---> Indirect sorting

---
