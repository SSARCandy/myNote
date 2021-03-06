##Plant Asserts, Natural Resources, and Intangible Assert
### Non-current Assert
 * Tangible Asserts 有形
    1. Property, Plant, and Equipment  
    (Fixed Assert; Plant Assert; Plant Equipment)
    2. Natural Resources
    3. Long-term Investments
* Intangible Asserts 無形


### Plant Asserts

需用在營業生產用途:使用年限一年以上

* Cost Determination  
  購入資產，使其投入生產行列所支出之合理、必要支出，為其購入成本。 
  
* Land 
  - **Land Improvements**(土地改良物)  
  有一定年限，附著於土地上之物品  
  ex.灑水器、停車場
  - **Buildings**  
  ex.仲介費、建築費.....
  - **Machinery & Equipment**  
  以淨發票價(扣除現金折扣，無論是否有)衡量，保費為一般花費(其效益於當年即消耗完畢)
  - **Sales Tax**:營業費
* Group Purchase (補)
  ```C
    Purchase Price : $25,000,000
    Fair Value     : Land	   $15,000,000
             		 Building  $ 5,000,000
    
     Land	    $ 18,750,000
     Building   $  6,250,000
    	 Cash 			     $ 25,000,000
    
                FV    % of Total Value  Cost Assigned
            ----------------------------------------------------
    Land      15,000,000      75%       18,750,000
    Building   5,000,000      25%        6,250,000
            ----------------------------------------------------
              20,000,000     100%       25,000,000
    ```
* Noncash Acquisitions (補): 以換入/換出的公允價值衡量
* Donated Asserts (補): 以捐贈物的公允價值衡量
* Depreciation 
  - Depreciation methods
    ```C
    Example
    機器成本  $ 60,000
    殘值      $  5,000
    使用年限  5 年 (生產單位數 $ 20,000)
    ```
    1. Straight-Line method   
    公式 = `(Cost - Residual Value) / Useful Life`  
    ```C
    (60,000 - 5,000) / 5 = 11,000
    ```  
    
    2. Units-of-Activity method (Units-of-Production method)  
    ```C
    ex. 當年生產 6,000u
    (6,000 - 5,000) / 20,000 x 6,000 = 16,500
    ```

    3. Sum-of-the-Years-Digits method (SYD 年數合計法)  
    **屬於加速折舊法 (Accelerated Depreciation method)**  
    公式 = `(Cost - Residual Value) x (剩餘使用年限 / SYD)`
    
    ```C
    SYD = 5+4+3+2+1 = 15

    Year 1    (60,000 - 5,000) x 5/15 = 18,333
    Year 2    (60,000 - 5,000) x 4/15 = 14,667
    Year 3    (60,000 - 5,000) x 3/15 = 11,000
    Year 4    (60,000 - 5,000) x 2/15 =  7,333
    Year 5    (60,000 - 5,000) x 1/15 =  3,667
    ```

    4. Double-Declining-Balance method (DDB 倍數餘額遞減法)  
    **屬於加速折舊法 (Accelerated Depreciation method)**  
    公式 = `Beginning Book Value  x  (S-L Rate x2)`

    ```C
              Beginning Value           Depreciation
    Year 1              60,000          60,000 x 2/5 = 24,000
    Year 2    (60,000 - 24,000)         36,000 x 2/5 = 14,400
    Year 3    (36,000 - 14,400)         21,600 x 2/5 =  8,640
    Year 4    (21,600 -  8,640)         12,900 x 2/5 =  5,184
    Year 5    (12,900 -  5,184)          7,776 x 2/5 =  3,110
                                                        ^^^^^
                               但只提2,776 (7,776 - 殘值5,000)
    ```

  - Partial-Year Depreciation
    ```C
    Example
    機器成本  $ 25,000
    殘值      $  5,000
    使用年限 4 年 (總產量 10,000 u)
    資產於 10/1 購入
    ```    

    1. Straight-Line
        ```C
        Year 1  (25,000 - 5,000) / 4 x 3/12 = 1,250
        Year 2  (25,000 - 5,000) / 4        = 5,000
        Year 3  (25,000 - 5,000) / 4        = 5,000
        Year 4  (25,000 - 5,000) / 4        = 5,000
        Year 5  (25,000 - 5,000) / 4 x 9/12 = 3,750 
        ```                              
    
    2. Units-of-Activity
        ```C
        第一年產量 2,000 u
        Year 1  (25,000 - 5,000) / 10,000 x 2,000 = 4,000
        ```

    3. SYD (Sum-of-the-Years-Digits)
        ```C
        示意圖:
                 3個月        9個月
            ---|-------|-----------------|-------|-------->
              10/1   12/31             10/1    12/31
    
        SYD = 1+2+3+4 = 10
    
        1. 先以一年周期做折舊表 (12-month Period)
          1st     (25,000 - 5,000) x 4/10 = 8,000
          2nd     (25,000 - 5,000) x 3/10 = 6,000
          3rd     (25,000 - 5,000) x 2/10 = 4,000
          4th     (25,000 - 5,000) x 1/10 = 2,000
       
        2. 再轉做成正確的折舊表
          Year 1                 8,000 x 3/12 = 2,000
          Year 2  8,000 x 9/12 + 6,000 x 3/12 = 7,500
          Year 3  6,000 x 9/12 + 4,000 x 3/12 = 5,500
          Year 4  4,000 x 9/12 + 2,000 x 3/12 = 3,500
          Year 5  2,000 x 9/12                = 1,500
        ```

    4. DDB (Double-Declining-Balance)
        ```C
        Year 1    25,000 x 1/2 x 3/12  =  3,125
        Year 2    21,875 x 1/2         = 10,938
        Year 3    10,937 x 1/2         =  5,469
        Year 4     5,468 x 1/2         =  2,734
                                         ^^^^^^^
                                         但只提 468 (5,468 - 殘值 5,000)
        ```

  - Changes in Estimates
  	```C
    Example
    機器成本   $ 60,000
    殘值       $  5,000
    使用年限 5 年 (生產單位數 20,000 u)
    使用兩年後，估計可再使用 6 年，殘值 $3,000
    ```
    1. Straight-Line
        ```C
        //用了兩年後剩餘的價值 = 22,000
        (60,000 - 5,000)/5 x 2        = 22,000

        //重新估計每年的折舊費用
        ((60,000 - 22,000) - 3,000)/6 = 5,833
        ```

    2. Units-of-Activity
        ```C
        第一、二年已生產 7,000 u
        第三年修正，預計可以再生產 25,000 u ，殘值 3,000
        假定第三年產量 4,500 u

                (60,000 - 5,000)/20,000 x 7,000            = 19,250
        第三年  ((60,000 - 19,250) - 3,000)/25,000 x 4,500 = 6,795
        ```

    3. SYD (Sum-of-the-Years-Digits)
        ```C
        //頭兩年的折舊總額
        (60,000 - 5,000) x (5+4)/15 = 33,000
        //重新估算時的剩餘價值
        60,000 - 33,000 = 27,000

        新SYD = 1+2+3+4+5+6 = 21
        Year 3   (27,000 - 3,000) x 6/21 = 6,857
        Year 4   (27,000 - 3,000) x 5/21 = 5,714
        Year 5   (27,000 - 3,000) x 4/21 = 4,571
        Year 6   (27,000 - 3,000) x 3/21 = 3,429
        Year 7   (27,000 - 3,000) x 2/21 = 2,286
        Year 8   (27,000 - 3,000) x 1/21 = 1,143
        ```

    4. DDB (Double-Declining-Balance)
        ```C
        Year 1    60,000 x 2/5 = 24,000
        Year 2    36,000 x 2/5 = 14,400
        //重估時的剩餘價值 = 21,6000
          60,000 - (24,000 + 14,400) = 21,600
        Year 3    21,600 x 2/6 =  7,200
        Year 4    14,400 x 2/6 =  4,800
        Year 5     9,600 x 2/6 =  3,200
        Year 6     6,400 x 2/6 =  2,133
        Year 7     4,267 x 2/6 =  1,422
                                  ^^^^^
                                  但只提 1,267 (4,267 - 殘值 3,000) 
        ```

  - Component Depreciation (組成折舊)
  `BE 9-7`

* Subsequent Expenditures or Plant Asserts
  - Capital Expenditures
    - Additions (增加)
    - Improvements (改良)
    - Extraordinary Repairs (大修)(延長年限)
  - Revenue Expenditures
    - Maintenance & Repairs Expenditures 

  ```C
  機器成本     $ 4,000
  已使用 2 年，使用年限 10 年
  無殘值
  第三年初大修 $  700
  可再用 13 年

  01/01/03  Accumulated Depreciation   $700
                                Cash        $700

  12/31/03  Depreciation Expenditures  $300
                              Acc Dep       $300

  4,000/10 x 2 = 800     //頭兩年累計折舊
  800 - 700 = 100        //第三年初因大修故機器成本增加 $700
  (4,000 - 100)/13 = 300 // 剩餘價值除剩餘使用年限 = 大修之後的線性折舊
  ```

* Disposals
  - Sales  
  [Gain] **Sales Price > Book Value**  
  [Loss] **Sales Price < Book Value**
  ```
  Dep Exp     $xxx
      Acc Dep      $xxx
  ```

  ```
  Cash                              $xxx
  Accumulated Depreciation          $xxx
  Loss on Disposal of Plant Asserts $xxx
      Equipment                           $xxx
  ```
  or  
  ```
  Cash                              $xxx
  Accumulated Depreciation          $xxx
      Gain on Disposal of Plant Asserts   $xxx
      Equipment                           $xxx
  ```

  ```C
  Example
    01/01/00  Machine Cost   $ 20,000
    10 Years, Residual Value $  1,000
    07/01/03  Sold for       $ 12,000
    Using S-L  
  --
  07/01/03  Dep Exp                950
                Acc Dep - Machinery       950
  // (20,000 - 1,000)/10 = 1,900   每年的折舊費用
  // 1,900 x 6/12 = 950

  07/01/03  Cash                    12,000 // 賣出所得
            Acc Dep - Machinery      6,650 // 1,900 x 3.5
            Loss on Disposal of PA   1,350 // Book Value - sold value
                Machinery                   20,000
  ```

* Retirement
  1. Fully Depreciated (Cost = A/D)
    
    ```
     A/D          $xxx
        Equipment     $xxx
    ```
  2. Not Fully Depreciated  
  Salvaged Materials recorded out the lower of Scrap Value or Book Value
    - Scrap Value >= Book Value  
    
      ```
       Salvaged Material (=BV)  $xxx
       A/D - Equipment          $xxx
          Equipment                   $xxx
      ```
    - Scrap Value <  Book Value  
    
      ```
       Salvaged Material (=SV)  $xxx
       A/D - Equipment          $xxx
          Equipment                   $xxx
      ```

* Exchanges
  1. Having Commercial Substance 商業實質的交換交易  
    - New Assert recorded at FV(old) + Cash Paid 
    - New Assert recorded at FV(old) - Cash Received

    ```C
                              Office Equipment Exchange for Machine
                                      (1)                 (2)
    Cost of Office Equipment        10,000              10,000
    A/D of Office Equipment          2,500               6,500
    FV of Office Equipment           4,000               4,000
    Cash Paid                        3,000               3,000
    FV of Machine                    7,000               7,000
    
    (1)
    Machine                     7,000
    Acc Dep - Office Equipment  2,500
    Loss on Disposal of PA      3,500
        Office Equipment              10,000
        Cash                           3,000

    (2)
    Machine                     7,000
    Acc Dep - Office Equipment  6,500
        Gain on Disposal of PA           500
        Office Equipment              10,000
        Cash                           3,000
    ```

  2. Having no Commercial Substance   
    - New Assert recorded at BV(old) + Cash Paid 
    - New Assert recorded at BV(old) - Cash Received

    ```C
                              Old Machine Exchange for new Machine
                                      (3)                 (4)
    Cost of old Machine              7,000               7,000
    A/D of old Machine               4,000               2,000
    FV of old Machine                3,800               2,800
    Cash Paid                          200                 200
    FV of new Machine                4,000               3,000
    
    (3)
    Machinery (New)             3,200 // (7,000 - 4,000) + 200 = 3,200
    Acc Dep - Machinery         4,000
        Machinery                      7,000
        Cash                             200

    (4)
    Machinery (New)             5,200 // (7,000 - 2,000) + 200 = 5,200
    Acc Dep - Machinery         2,000
        Machinery                      7,000
        Cash                             200
    ```
    
* Revaluation of Plant Assert
    ```C
    Equipment:
        Cost    10,000
        A/D      1,500
        FV       9,000

    (1) Acc Dep - Equipment    1,500
    (3)    Revaluation surplus         500
    (2)    Equipment                 1,000 //(10,000 - 9,000)
    ```


### Natural Resources 地耗資源


   * Depletion 折耗
    
    ```
    Depletion Exp       $xxx
        Acc Depletion        $xxx
    ```

    ```C
    Example

    Acquisition Cost (含土地)       $ 20,000,000
    Exploration Cost                $  5,000,000
    Development Cost                $  4,000,000
    Land                            $  1,000,000
        # of u to be extracted                   2,800,000 u
        # of u extracted durning the Period         10,000 u // 4,000 u sold
    Mining labor Cost               $    700,000
    Depreciation on Machine         $     50,000
    ```

    ```C
    Ore Deposits    19,000,000
    Land             1,000,000
        Cash                  20,000,000

    Ore Deposits     9,000,000
        Cash                   9,000,000

    Depletion Exp      100,000
        Acc Depletion            100,000
    // (19,000,000 + 9,000,000)/2,800,000 x 10,000 = 100,000

    Wages Exp (Mining) 700,000
        Wages payable            700,000

    Dep Exp(Mining)     50,000
        Acc Dep - Mining Eq       50,000

    **Closing Entry**
    CGS (40%)           340,000
    Inventory(60%)      510,000
        Depletion Exp           100,000
        Wages Exp(Mining)       700,000
        Dep Exp(Mining)          50,000
    ```

### Intangible Assert
   - Liimted Life Intangible Asserts: **Amortization 攤銷**

    ```
        Amortization Exp-Patents    $xxx
            Patents                      $xxx
    ```
      - Patents 專利權
      - Copyright 著作權
      - Franchises 特許權

        ```
            (1) Franchises  xx          (2) Franchises Exp  xx
                    Cash        xx              Cash            xx

                Amortization Exp  xx
                    Franchises        xx
        ```
        
    - Indefinite Life Intangible Assert: **無年限設定，不需攤銷**
        - Trademark 商標
        - Goodwill  商譽

### Research and Development Costs
   1. Research Exp
    2. Development Exp
    3. Development Cost
        - 達成資產的技術可行性沒有問題
        - 公司有意願
        - 公司有能力使用或處分
        - 資產可賣出
        - 經費可區分為兩部分

### Impairment of Asserts  資產減損 (補)
   - Recoverable Amount = `Max( NetFV(FV less cost to sell), Value in use )`
    - Book value > Recoverable Amount  -->  **Impairment Loss**

        ```
        Example
        05年1/1 購入機器，成本 1,000,000 使用年限5年，殘值 200,000 ，S-L
        05年底，機器公允價值 730,000 使用價值 765,179
        07年底，可回收金額 520,000
        09年底，以 210,000 售出
        ```

        ```C
        05/01/01 Machinery      1,000,000
                    Cash                  1,000,000

        05/12/31 Dep Exp          160,000
                    Acc Dep                 160,000
                // (1,000,000 - 200,000)/5 = 160,000

        05/12/31 Impairment Loss   74,821
                    Acc Impairment           74,821
                // 1,000,000 - 160,000 = 840,000
                // 840,000 - 765,179 = 74,821

        06/12/31 Dep Exp          141,295
                    Cash                    141,295
                // (765,179 - 200,000)/4 = 141,295

        07/12/31 Dep Exp          141,295
                    Acc Dep                 141,295
        // BV = 1,000,000 - (160,000 + 141,295 * 2) - 74,821 = 482,589
        // BV (if Impairment loss not recognized) = 1,000,000 - (160,000 * 3) = 520,000

        07/12/31 Acc Impairment    37,411
                    Gain on Residual-
                    of Assert Impairment     37,411
        // 520,000 - 482,589 = 37,411

        08/12/31 Dep Exp          160,000
                    Acc Dep                 160,000
        // (520,000 - 200,000)/2 = 160,000

        09/12/31 Cash             210,000 // Sold Price
                 Acc Dep          762,590 // Accumulated Dep
                 Acc Impairment    37,410 // 74,821 - 37,411
                    Gain on Disposal-
                    of Plant Assert         10,000
                    Machinery            1,000,000 // Ori Price
        ```

### Assert Turnover Ratio  資產周轉率
公式 = `Net Sales/Avg Total Asserts`  
`E 9-16`
