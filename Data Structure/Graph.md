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
