###**Tree**
 * Tree triversal  
    * 以ROOT為角度定義pre, in, post order
      * Pre-order( Root --> Left Subtree --> Right Subtree )  
        應用：系統目錄(Windows, Unix...)

      * In-order( Left Subtree --> Root --> Right Subtree )
      * Post-order( Left Subtree --> Right Subtree --> Root )  
        應用：系統目錄大小(累加)

 * Expression Tree
    * leaves: 	 **operands**
    * other nodes: **operators**

```C
// Construct an Expression Tree ( form postfix to expression tree )
    while(input token != EOF){
          if(token == operand)
              push a tree with the token;
          else{
              pop two trees X, Y;
              construct a tree Z rooted with the token connected to X, Y;
              push Z;
          }
    }
```
 * Binary Tree
    * Def: Degrees is 2
      * Using Struct (*left, *right, data) implementation of Binary Tree
     * Using Array implementation of Binary Tree
    * Binary Search Tree
        * is a Binary Tree
        * for every node X:
            * value of all keys in left subtree are smaller than key in X
            * value of all keys in right subtree are larger than key in X

    ```C
    Position Find(ElementType X, SearchTree T){
                  if(T == NULL)
                      return NULL;
                  if(X < T->Element)
                      return Find(X, T->Left);
                  else if(X > T->Element)
                      return Find(X, T->Right)
                  else
                      return T;
    }
    ```

     *  Delete node in Binary Search Tree
     * Different input produce different Binary Search Tree  
    ex. come in order  ----> degenerates to linked list

     * Given a Binary Search Tree with ndepth Different
       * Insert: 	Best O(1), Worst O(n)
       * Retrieve:  Best O(1), Worst O(n)

 *  AVL Tree
  **An balanced Binary Search Tree:**
     * 深度差不超過正負1  
      不平衡狀況：LL,  LR, 	RL,	RR
       * STEP1: 找出critical NODE  , 就是深度差超過正負1的NODE(挑離ROOT最遠的)
       * STEP2: 判斷Critical NODE 與新增NODE的的關係(LL LR RR RL)
       * STEP3: 進行相對應的調整

     * 旋轉時間複雜度是O(1)  
  LR 可以利用先做 RR 再做 LL 達到相同效果, 所以稱之為 Double Rotate
     * Complexity:

Operation | Complexity
-------- | ---------
Search | O(logN)  
Instertion |	O(logN)  
Rotation | O(1)  
Deletion | O(logN)




 * B-Tree
  * B-Trees of order M
      * every node have M ways
      * Root is either a leaf or has between **2 & M children**
      * All nonleaf nodes have between **上界(M/2) & M children**
      * All leaves are at the same depth
      * Overflow: Split(分居) --> nonleaf node change(標兵要反應事實)

    **EX. Instert `19` into a `2-3 Tree`**

```
        BEFORE                         AFTER

        22 : - 			   		      16 : 22
        /     \ 					 /   |   \
      11:16  41:58   			   11:- 18:- 41:58
     /  |  \                       / \  /  \
    1   11 16                    1  11 16 18
    8   12 17                    8  12 17 19
            18
```

---
