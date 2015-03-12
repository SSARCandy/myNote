# Computer Vision
 
  * System Characterization
  * [Convolution](http://pages.jh.edu/~signals/convolve/)  
  傅立葉轉換 *O(n^2)* --> 快速傅立葉轉換(FFT)  *O(n  logn)*
  * Smoothing
    
     
     --------   			[1, 1, 1]
     |   .  |   ---> 1/9	[1, 1, 1]  
     |(x, y)|   			[1, 1, 1]
     -------- 
    
  * Weber's Law  
  Just Noticeable Difference (JND)
  
  
# Digital Image Fundamentals
 * [Optical Illusions](http://www.michaelbach.de/ot/)
 * Simultaneous Contrast
 * Sampling & Quantization  
 數位轉類比必經之路
 * Representing Digital Images: **2-D matrix**
 * Spatial Resolution: (*縮圖*)
   * Subsample : 降解析度(縮圖) 
   * Resample  : 提高解析度(低解析還原高解析，可以用內插等方式補齊丟失的資訊)
 * Gray-level Resolution:
   * 16-bits, 8-bits, 4-bits, 2-bits
 * Zooming and Shrinking
   * Nearest neighbor interpolation
   * Pixel replication (a special case of nearest neighbor interpolation)
   * Bilinear interpolation

    
# Distance Measure
      
      P1 =(x1,x2,...,xn)
      P2 =(y1,y2,...,yn)
      
      General Equation :  Ld = (sum |xi - yi|^d )^1/d

 * Euclidean distance
  ```
  d(P1,P2) =  sqrt( sum(xi - yi)^2 )
  ex.
     [sqrt(2), 1, sqrt(2)]
     [  1,     0,    1   ]
     [sqrt(2), 1, sqrt(2)]
  ```
 * D4 distance (city-block distance)
 ```
  d(P1,P2) = sum abs(xi - yi)
  ex.
     [2, 1, 2]
     [1, 0, 1]
     [2, 1, 2]
 ```
 * D8 distance (chessboard distance)
 ```
  d(P1,P2) = max abs(xi - yi)
  ex.
     [1, 1, 1]
     [1, 0, 1]
     [1, 1, 1]
 ```
    
  
    
    
    
    
  ```
	to be continue...




























  .










  ```
