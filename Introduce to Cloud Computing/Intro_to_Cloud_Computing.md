 #Introduce to Cloud Computing

---

###Attribute to define cloud computing
 * Mutitenancy
 * Massive scalability
 * Elasticity:彈性雲(資源是有彈性的，可隨時改變分配的資源)
 * Pay per use 
 * Self-provisioning of resources
 * Talut tolerance:容錯率(Ex. Google App Engine)
 
###雲的服務分類
 * SPI分類
  * Software-as-a-service (SaaS)
  * Platform-as-a-service (PaaS)
  * Infrastructure-as-a-service (IaaS) 
 
 * 公、私有分類
 
| Public Cloud | Private Cloud | Hybrid Cloud|
| :----------: | :-----------: | :---------: |
| 比較便宜      |   比較貴       | ?? |
| 偏向公開		|   私有(對內)   |有對外有對內|
| 中小企業較常用 |	  大企業較常用  |以後會越來越多|

###VM Environment
Host OS -> multi Guest OS

###Big Data = 大數據?
 * Big != 大  
 Big 有範圍的概念，不只是只有資料量  
 * 數據 != 資料  
 數據通常代表這"numeric data"，而Data不只有numeric data, 還有text, picture... 


###Google File System
 * Files broken into chunks(4MB each)
 * each chunk have 3 copies distrbute at different disk
 * user only need to know FILE NAME, GFS will manage these file chunks


###Big Table

* (row, column, timestamp) -> cell content
* is column oriented & row oriented
* Distributed multi-level sparse map
* Scalable
* Self-managing

###Reference 
 * [Hadoop](http://hadoop.apache.org/)
 * [OpenStack](https://www.openstack.org/)
 * [Hyper-V](https://technet.microsoft.com/zh-tw/library/hh831531.aspx)

```
to be continue...








































	..
```