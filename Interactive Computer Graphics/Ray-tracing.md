## Ray tracing

### For each pixel in film:

1. 從成像平面的像素射 ray
2. 尋找與場景中物件的交點
3. 產生**反射**、**折射**等新 ray，繼續追蹤這些新 ray(遞迴 2, 3 直到與光源相交)
4. 計算這個像素的顏色


