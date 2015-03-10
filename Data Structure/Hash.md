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
 *  rehashing 時機：**滿50%** 或 **有人無法Insert**
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
