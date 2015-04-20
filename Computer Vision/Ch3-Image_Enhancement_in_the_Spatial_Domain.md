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
  
  ```C
  void HistogramEqualization(Mat& src)
  {
	int histogram_ori[255] = { 0 };
	int lookuptable[255] = { 0 };
	for (int i = 0; i < src.rows; i++)
		for (int j = 0; j < src.cols; j++)
			histogram_ori[src.at<uchar>(i, j) % 255]++; // get original histogram

	float totalPixel = src.rows*src.cols;
	float accumPr = 0;
	for (int i = 0; i < 255; i++)
	{
		accumPr += (float)histogram_ori[i] / totalPixel;
		lookuptable[i] = (int)(255.0*(accumPr) + 0.5);
	}

	for (int i = 0; i < src.rows; i++)
		for (int j = 0; j < src.cols; j++)
			src.at<uchar>(i,j) = lookuptable[src.at<uchar>(i, j)]; // set equalization histogram
  }
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
 * Lowpass Filters
  * Ideal Lowpass Filters  
 低頻就可以通過，其他就不能  
 有Ringing Effect，因為不連續性
 
  * Butterworth Lowpass Filters  
 還是有Ringing Effect，但比較不明顯
 
  * Gaussian Lowpass Filters  
  不會有負數，所以沒有Ringing Effect
 
 * Highpass Filters  
 `Highpass = 1- Lowpass`
  * Sharpening Filters
 

