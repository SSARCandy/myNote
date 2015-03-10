#Pattern Matching 
 - Const pattern:**`1, 3.5, 'a', []`**
 - Structured pattern with var:**`(x:xs)`**
 - Var pattern:**` x, xs, ...`**
 - Wildcard pattern: **`_`**

##List Pattern

```Haskell
      [3, 5, 7]
    = 3:[5, 7]
    = 3:(5:[7])
    = 3:(5:(7:[]))
```

##Compute length of a list

```Haskell
length [] = 0
length (_:xs) = 1 + length xs 
```

##Pattern Matching Examples
 - Difference between 

  	```Haskell
    test1:: [Char] -> Bool
    test1 (’a’:_)   = True  --第一個是'a'就是True
    test1 _         = False

	test2:: [Char] -> Bool
    test2 [’a’,_,_] = True  --必須是長度為三的list而且第一個是'a'才是True
    test2 _         = False
  	```

 - Tuple Patterns  
 A tuple of patterns is itself a pattern which matches any tuple of the **same arity** whose components match the corresponding patterns *in order*
 
	```Haskell
  fst:: (Int, Char) -> Int
  fst   (x, _) = x
  
  snd:: (Int, Char) -> Char
  snd   (_, y) = y
 	```
    
    - Selection using Pattern Matching   
    `Ex. (x1, x2, x3) = (100, 'A', "Math")`
    
    
##Polymorphic Functions & Types  
**Polymorphic function** does not care about the element typeof its list parameter  
  類似物件導向的**多型** , For example:  `length ::[a] -> Int`  
  //*Here **a** is a type variablethat can be instantiated to any types*
    
    
    
##Type 
 - Type Inference : Haskell 可以支持**類型推導**
 - restrictive Type:
   - `[Int] -> [Int]`
   - `[Char] -> [Char]`
 - general Type:
   - `[a] -> [a]`
 - Qualified Types:
   -  `Ord a => [a] -> [a]`  
   type a must be an instance of the ***Ord*** class  
    
    
##List Manipulation Functions
 - xs ++ ys 　　　(also known asappend xs ys)
 
 ```Haskell
	 (++) :: [a] -> [a] -> [a]
	 [] ++ ys       = ys
	 (x : xs) ++ ys = x : (xs ++ ys)
 ```
 
 ```
[1,2,3] ++ [4,5,6]
				= { apply ++}
1: ([2,3] ++ [4,5,6])
				= { apply ++}
1: (2: ([3] ++ [4,5,6]))
…
1: (2: (3: [4,5,6])))
				= { list notation }
[1,2,3,4,5,6] 
 ```
 - reverse function
 
 ```Haskell
  reverse :: [a] -> [a]
  reverse [] = []
  reverse (x : xs) = reverse xs ++ [x]

 ```























    
    ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ```