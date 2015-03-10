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

---
####Spare Matrix(稀疏矩陣)
 *  二維稀疏陣列,  太多格子裏面是空的  
 	　-->改用linkedlist (DS_textbook p.78): 可以省下記憶體空間

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
