### Heap(priority queue)
 * Structure  property: complete Binary Tree  
 (第一層到倒數第二層是滿的，最後一層由左而右是滿的)
 * Order property: for each node X, parents 一定小於或等於X
    * Instertion:(min-heap)  
          由於Heap是complete Binary Tree,所以insert的路徑已經決定了(最後一層由左而右第一個空位是目的地)
          1. 沿著路徑往上比對各節點
          2. 找到適當位置插入
          3. 其他點沿路徑往下擺
    * deletion:(min-heap)
          1. 把最後一層由左而右最後一個點先存到tmp
          2. 把root pop掉(因為是最小的)
          3. root的位置要有人遞補(候選人:root的孩子, tmp)
          4. 持續往下把空格遞補完(候選人一樣是父節點的孩子與tmp)

    * Delete_min: **precolate down O(logN)**
     * Insertion:  **precolate up   O(logN)**

 * Heap 可以用array寫(Complete Binary Tree)
    * Heap Sort 1 *(需要額外空間)*
          1. build up heap(min-heap)
          2. for(i=0; i<N; i++) DeleteMin;

    * Heap Sort 2
          1. build up heap(Max-heap)
          2. for(i=0; i<N; i++) DeleteMax;  
          //把Delete的點放到array的後面，省下開額外空間(善用Heap開的空間)

    * Building up Heap: 從最底層往上糾錯，一層層來
