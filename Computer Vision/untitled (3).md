##Image Enhancement in the Spatial Domain

####影像強化
 
 * 空間域:影像平面
 * 頻率域
 
####Size of Neighborhood
 
 * point processing
 * larger neighborhood(**kernel size**)
 
 
###Gray-level Transformation
 
 * thresholding
 * stretching(曲線調整)
 * Image negatives: s =L-1-r --> 負片
 * Log transformation: s =clog(1+r) 
 * Power-law transformation: s=cr^gama
 * Bit-plane Slicing  
 8-bit就切成八片,分別呈現各個bit
 
 
 ###Histogram Processing
 
  * Histogram Equalization  
  
  ```
  //用這公式可以讓任何PDF變uniform (理想上)
  // 1. 不過由於影像值非連續(Discrete)的，所以還是有差
  // 2. 輸出(s)是整數而非連續
  s = T(r) = (L-1) Integral{0~r}(Pr (w)dw)  
  
  ds/dr = (L-1)(d/dr)[Integral{0~r}(Pr (w)dw)]
          = (L-1) x Pr(r)

  dr/ds = (1/(L-1)Pr(r))
    
    --> Ps(s) = Pr(r) |(dr/ds)| = Pr(r)( 1 / (L-1)Pr(r) )
     		 = 1/(L-1)
  ```  
  ```
  ex.
   s0 = T(r0) = 7 x 0.19             = 1.33 --> s0=1
   s1 = T(r1) = 7 x (0.19+0.25)      = 3.08 --> s1=3
   s2 = T(r2) = 7 x (0.19+0.25+0.21) = 4.35 --> s2=4
   ...                                          s4=6.23
                                                 s5=6.68
                                                 s6=6.86
                                                 s7=7
   
  ```
  
  * Histogram Matching  
   Histogram Equalization is a case of  Histogram Matching  
   
   ```
                                          T2
   Source --------->   Histogram    ----------------> Destination
      Img     T1      Equalization   <----------------     Img
                                       inverse T2

   Source  -------------------> Destination
             inverse T2( T1(r) )

   ```
   
   
 ###Smoothing Spatial Filters
 * Box filter  
 
 ```
    1      [1,1,1]
 ---  x  [1,1,1]
    9      [1,1,1]
 ```
 
 * Weighted average 
 ```
    1       [1,2,1]
 ----  x  [2,4,2]
    16      [1,2,1]
 ```

  