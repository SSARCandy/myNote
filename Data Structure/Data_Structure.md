#Data Structure
---

###System Life Cycle
#### 　需求 --> 分析 --> Coding, Debug --> 維護
 * 了解需求
 * 系統分析
 * 設計
 * coding & refinement
 * 確認、測試功能

###演算法：
 * input
 * output
 * definiteness  (夠明確)
 * finiteness    (執行能截止)
 * effectiveness (要有效果)

```C
Instertion Sort(A[]){
		for(P=0; P<N; P++){
			insert A[p] in to A[0]~A[P-1] 中正確位置
		}
}
```
```C
Selection Sort(A[] {
		for(P=0; P<N; P++){
			找到A[]中最小的，並insert in to A[i]
		}
}
```
```C
Binary Search(){
        while(還有值能找){
            middle = (left + right)/2;
            if(serch_num < list[middle])
                right = middle -1;
            else if(serch_num == list[middle])
                return middle;
            else
                left = middle + 1;
        }
}
```
###**問題：找出第k大的值(未排序的資料)**
 * 解一：排序(由大而小)完後取出array[k-1]的值
 * 解二：每次找最大值，然後踢掉本值，重複k次就能得到
 * 解三：將array的值當作另一個array2的index，最後找array2中第k筆非零的值的index
 * 解四：先讀k筆資料進array並sort，之後再一一讀入其他值，比第k筆資料大者就插入至array，最後第k筆就是答案


####performance Evaluation
 * Perfomance analysis:    **Machine independent**
 * Perfomance measurement: **Machine dependent**

####Perfomance Analysis
 * Complexity theory
	* space complexity: **記憶體空間**

    ```
		S(P) = c + Sp(I)
		c: fixed space
		Sp(I): depends on characteristics of instance I (根據輸入資料決定)
		characteristics: number, size, values of I/O associated
	```
	* time complexity:  **電腦執行時間**

    ```
		T(P) = c + Tp(I)
		c:compile time
		Tp(I):program execution time, depends on characteristics of instance I
		characteristics: number, size, values of I/O associated
	```
	* Worst case, Best case, Average case 

	```
   	 EX：7 sorted data , Binary sort

		  3,  2,  3,  1,  3,  2,  3 	(每個位置的狀況要找幾次)

		  Average case = (1 + 2*2 + 3*4)/17 (假設每筆被搜尋機率相等,且不會搜尋沒有的資料)
	```
    
	* Big O notation(成長速度)
	
	```C
			//找出上下界(最小上界與最大下界)
			Rules example:
				for(i=0; i<n; i++){
					x++;
					y++;
					z++;
				}
				/**** 3n *****/
				
				for(i=0; i<n; i++){
					a[i] = 0;
					for(j=0; j<n; j++)
			 			for(k=0; k<n; k++)
							x++;
				}
				/***** n^3 + n  *****/
	```
####Perfomance measurement
 * timing event *< time.h>*
	* clock function : system clock
	* time function
 * Generating test data: sutiable for large number random test data

---


###**C只有call by value !!**
   想要在C中達到call by reference 的話要傳記憶體位置(就是加&)   
   Free 一個Linked-list的node需要一個一個free(node),不會因為free頭就free到一整串

##Sorting Algorithms
####**Bucket Sort**
	e.g.(6, 4, 8, 3, 6, 1, 3, 6)
	類似次數分配表
	-----------------------------------------
	| 1 | 0 | 2 | 1 | 0 | 3 | 0 | 1 | 0 | 0 |
	-----------------------------------------
	  1   2   3   4   5   6   7   8   9   10

	Given N integers in the range 1 to M --> O(M+N)
	disadvantage: if M = N^P, 需要開的陣列就太大了

####**Radix Sort I**
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

####**Radix Sort II**
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

---
####Spare Matrix(稀疏矩陣)
 *  二維稀疏陣列,  太多格子裏面是空的  
 	　-->改用linkedlist (DS_textbook p.78): 可以省下記憶體空間

---
###**stack**
  可用於Postfix Conversion  

```
a+b*c+(d*e+f)*g 
operand ( a . b . c ...... )
token ( + . - . * .  / .... )
```

**Algorithm**

```C
while ( input token != EOF ){
	if( token == operand )    " 1 "
		output token 
	else if ( token == closing parenthesis ){   " 2 "
		while ( top != opening parenthesis ){
			pop & output 
				pop /* discard opening parenthesis */
		}
	}
	else{
		while priority(top) >= priority(token )   " 3 " 
			pop & output
	}
	push token
} 
```

 **ex1.** 　a+b*c 　  => 　abc*+

  Steps| token   |   stack  |   output
  :---: | :------: | :--------: | :-----------:
  1|  a     |            |   a      
  2|  +     |     +      |         
  3|  b     |     +      |   ab     
  4|  *     |    + *    |           
  5|  c     |    + *   |     abc    
  6|        |         |      abc*+  
  


**ex2.**　	a + b * c + ( d * e + f ) * g  　 =>  　a b c * +   d e * f + g *   +

 Steps| token    |       stack    |       output         |   operation 
  :---: | :--------: | :--------------: | :--------------------: | :-----------: 
 1    |  a       |                |       a              |    " 1 "       
 2    |  +       |        +       |       a              |    " 3 "    
 3    |  b       |        +       |       ab             |    " 1 "    
 4    |  *       |        + *     |       ab             |    " 3 "    
 5    |  c       |        + *     |       abc            |    " 1 "    
 6    |  +       |        +       |       abc*+          |    " 3 "    
 7    |  (       |        + (     |       abc*+          |    " 3 "    
 8    |  d       |        + (     |       abc*+d         |    " 1 "    
 9    |  *       |        + ( *   |       abc*+d         |    " 3 "    
 10   |  e       |        + ( *   |       abc*+de        |    " 1 "    
 11   |  +       |        + ( +   |       abc*+de*       |    " 3 "    
 12   |  f       |        + ( +   |       abc*+de*f      |    " 1 "    
 13   |  )       |        +       |       abc*+de*f+     |    " 2 "    
 14   |  *       |        + *     |       abc*+de*f+     |    " 3 "      
 15   |  g       |        + *     |       abc*+de*f+g    |    " 1 "    
 16   |          |                |       abc*+de*f+g*+  |    " 3 "    


---
**Function Calls**  
　　recursive is using STACK to store all function call  
　　OS mantaining programs is using STACK

####**Queue**
 * First In First Out (FIFO)
 * operation 
   * Enqueue at rear (end)
   * Dequeue at front (start)

 * Application of Queue
	* Job scheduling in operating system
	* file server
	* Printer server
---

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

### Priority Queue 
 * Job scheduling (printer job , CPU job)
   * First-In-First-Out(Queue)
   * Shortest 


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

###  Hashing  
* have a Hash table (array)
* have a Hashing function: H(K) = K % TS  (table size)
* Instertion, Deletion, find is O(1)
* **Hashing 沒有排序**

	ex. H(K) = K % 10
	
		Insert 89 18 11 62, 要搜尋時再利用Hash function得出要找的array index
         `-----------------------------------------
          |   | 11| 62|   |   |   |   |   | 18| 89|
         `-----------------------------------------
      	  0   1   2   3   4   5   6   7   8   9  

* Collision : two keys hash in same index
* Overflow  : Collision and the cell is full  
**為了解決上述兩問題**
	* Static hashing
		* perfect hashing without collision:  
        **事先知道資料,可以找出hashing function 讓他無collision**
		* hashing with collision
		  * seprate chaining:  
          每個array都是一個linked list的頭
		  * open addressing: 
		  
```
          //遇到collision時, 用F(i)這個新函式跟H(K)相加再mod後找到新的cell 
          //[Hi(k) = (h(k) + F(i)) % TS]
			  **F(i)的i是collision的次數
			  **Deletion --> lazy deletion(不真的刪掉只弄個記號)
			  liner probing:     F(i) = i
			  quadratic probing: F(i) = i^2
			  double hashing:    F(i) = i*( TS2-(K % TS2) ) TS2 is a prime smaller than TS
```
          * rehashing:  
          弄個更大的array來重新hash(新TS通常是原TS的兩倍大的第一個質數)
           * rehashing time complexity is O(N)
		   * rehashing 時機：**滿50%** 或 **有人無法Insert**
	* Dynamic hashing
	   * Hashing function is change dynamically
	   * Extendible hashing: for searching of large amount of data  
       擴充Array. `EX.  00 01 10 11  --->  000 001 010 011 100 101 110 111`
	   * Linear hashing

**A GOOD HASH FUNCTION**

* Simple to compute
* Minimize the number of collision  
	dependent upon all the characters in the identifiers  
    　　--> uniform hash function(每個格子被取到的機率相等)

	TS(Table Size) for numbers:
		bad choice of TS: 二的次方
		good choice of TS: prime 	

	TS(Table Size) for strings:
		h(K) = sum( ASCII(Ki) ) % TS
		h(K) = sum( ASCII(Ki)*27^i ) % TS 考慮到字母位置
		
---
## GRAPH 
    G = (V, E)  
    	V: a set of vertices  
    	E: a aset of edges

 * Directed graph (Digraph): 邊有方向性
 * Undirected graph: 邊沒有方向性
 * Adjacent: w is a adjacent to v if (v, w) 屬於 E

** Tree 有上下階層關係， Graph 則沒有 **

### PATH

Noun|Define
--:|:--
Loop| an edge (v, v) from vertex to itself(指向自己的邊)
                   Simple_path| a path where all vertices are distinct expect the first and last  (除了起點終點可以一樣之外，其他都不一樣)
    Cycle_in_a_directied_graph| a path such that W1=Wn
                 Acyclic_graph| no any cycle in the graph
                     Connected|	每點都有連通到其他點(間接或直接)
                Complete_graph|	任兩點之間都有邊
             Strongy_connected|	directied graph 中每點都可以走到其他點(間接或直接)
              Weakly_connected|	directied graph 中若不考慮方向(可以逆向), 每點都可以走到其他點(間接或直接)


### Graph 的表示 
* Adjacency Martix Representation: 用於較密集的GRAPH比較好, O(|v^2|)
	* Undirected graph的Adjacency Martix Representation會是對稱於對角線的

* Adjacency List Representation: 用linked list來節省空間, O(|V|+|E|)

### Traversal of Graph 
* 指定一個起點後再遍歷
* EXAMPLE: spider(爬蟲器),藉由hyperlink來找遍網站
 * Depth First Search(DFS):先深後廣  
	先一直往下走,沒辦法再往下就先往回一個再往下 (用recursive實作)
						  
						
 * Breadth First Search(BFS):先廣後深, 走完就變得像Tree (用queue實作)
>            A            
>			/|\     從A開始：		
>		   B E C 	DFS: A B D F E C G
>		  /\ | |     BFS: A B E C D F G
>		 D F_| G

		```C
		BFS(Graph G){
			Queue Q(size = number of vertices);
			enqueue(Start vertex, Q);
			while(!IsEmpty(Q)){
				tmp = dequeue(Q);
				for(所有與 tmp adjacent 點 W){
					if(!Visited[W]){
						Visited[W] = true;
						enqueue(W, Q);
					}
				}
			}
		}
		```

### Topological Sorting 
ordering of vertices in a DAG(Directed Acyclic Graph) such that if there is a path from Vi to Vj,
then Vj appears after Vi in the ordering

```
	 1 → 2 	ANS: 1,2,5,4,3,7,6
   ↙ ↘  ↙ ↘          
  3 ←  4 ←  5      紀錄每個點的Indegree, 拿掉Indegree = 0的點, 然後相鄰的點的Indegree都減1
   ↘ ↙  ↘ ↙       然後再找新的Indegree = 0的點(如果同時有兩個以上Indegree=0的就隨便選一個)
     6 ← 7         Time-complexity: O(|V|^2) 
                       --> 利用queue記錄下一回合Indegree會是0的點, 可以改善成O(|E|+|V|)
```


### Shortest-Path 
	Unweighted Shortest Paths (BFS)					 			O(|V|+|E|)
	Shortest Paths in Acyclic Graph (Topological sort)		  	O(|E|+|V|)
	Weighted Shortest Paths in cyclic graph without negative edges  O(|E|log|V|)
	Weighted Shortest Paths in cyclic graph with negative edges     O(|E|*|V|)


        1:1 → 2:2    	-Unweighted Shortest Paths
       ↗  ↘  ↙  ↘    	用 BFS, 先廣後深
     3:0 ← 4:2 ← 5:3     
       ↘  ↙  ↘  ↙  
        6:1 ← 7:3   
        

### Weighted Shortest Paths - 沒cyclic###
1. 按照Topological order來做 --> 找出下一個要到的節點
2. 比較邊的權重			  --> 決定到下一個節點的路徑

### Weighted Shortest Paths - 有cyclic###
* Dijkstra's Algorithm  (greedy algorithm)
  * unsorted table: O(|E|+|V|^2)
  * priority queue: O(|E|log|V| + |V|log|V|)	
  * 幾個點就做幾回,一回合中
	 1. 選出主角(選已知最短距離最小的點)
	 2. 更新adjacent點的最短距離
	 
	
```C
		Dijkstras (Table T){
			vertex V, W;
			while (1) {
				V = smallest_known_distance_vertex();
				if(V == NULL)
					break;
				else{
					T[V].known = true;
					for(each W adjacent to V){
						if(T[V].dis + Cvw < T[W].dis){
							T[W].dis = T[V].dis + Cvw;
							T[W].path = V;
						}
					}
				}
			}
		}
```
	
### All-Pairs Shortest Paths ###
* D(k,i,j) 從i to j的路中經過的點編號最大是k
* D(k,i,j) = D(k-1,i,j) 　　　　　 不經過k  
　　　	or D(k-1,i,k)+D(k-1,k,j) 經過k

```C
All-Pairs_Shortest_Paths(2D-array D, 2D_array Path, int N){
	D 初始成原始的 adjacency matrix;
	for(k=0; k<N; k++)
		for(i=0; i<N; i++)
			for(j=0; j<N; j++)
				if(D[i][k] + D[k][j] < D[i][j]){
					D[i][j] = D[i][k] + D[k][j];
					Path[i][j] = k;
				}
}
```
### Minimum Spanning Tree ###
* 任兩點中都有間接可通的路
* 一個Graph 有很多Spanning Tree
* edges 總和最小的稱之為 **Minimum Spanning Tree**
* 幾個點就做幾回,	重複連結已經選上所有的點中cost最小的點

	- Kruskal's Algorithm 
			每回合中，選一條 edge (過程中會造成forest)
			* 這條 edge 需是 smallest cost edge in unselected edges
			* 這條 edge 不可以造成 cycle
	- Prim's Algorithm
			每回合中，選一條 edge 加進tree中(過程中只會有一個tree)
			* 這條 edge 需是 smallest cost edge in unselected edges(而且是與tree相連的)
			* 這條 edge 不可以造成 cycle
		

### Critical Path ###
* Earliest completion time: longest path  
	先改成 Weighted path 表示法，然後用 Topological order 算
* Lastest completion time:  
	往回算(Slack time) 
	
### Sort Algorithm ###	
	# Instertion Sort
	  	  0   1   2  ... ...  P  ... ... ... N-1    每回合中
	  	-----------------------------------------   將 index P 的值插入到sorted的正確位置
	  	|   |   |   |   |   |   |   |   |   |   |   **index P就是 sorted & unsorted 的交界處
	  	-----------------------------------------
		  |-------sorted------||-----unsorted-----|

	# Selection Sort
	  	  0   1   2  ... ...  P  ... ... ... N-1    每回合中
	  	-----------------------------------------   將 unsorted 中最小值(min) 換到 index P 的位置
	  	|   |   |   |   |   |   |   |min|   |   |   **index P就是 sorted & unsorted 的交界處
	  	-----------------------------------------
	  	|-------sorted------||-----unsorted-----|

	# Merge Sort
		11   8   14   7   6   8   23   4
		 \  /     \  /     \  /    \  /
		 8,11     7,14     6,8     4,23
		   \       /        \       / 
		   7,8,11,14         4,6,8,23
		       \                /
			   4,6,7,8,8,11,14,23

	# Quick Sort
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
	
### Algorithm Design Techniques  `p.447`
 * Algorithm type:
	* Greedy Algorithm：
		* 短視近利，每次都找local optimum, 最後得到 global optimum
		* Job Scheduling
		* Run Length Coding
		* Huffman Coding(較常出現的字元用較短編碼)
			* unique prefix property(編碼不可以是別的編碼的字首)

	* Divide and Conquer
	* Dynamic Programming
	* Randomized Algorithm
	* Backtracking Algorithm
	* Branch and Bound
	* ...

