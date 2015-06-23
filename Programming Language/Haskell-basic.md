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
    test1 ('a':_)   = True  --第一個是'a'就是True
    test1 _         = False

	test2:: [Char] -> Bool
    test2 ['a',_,_] = True  --必須是長度為三的list而且第一個是'a'才是True
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



##Data Type
**Data type is a set of value**

 - Type Inference : Haskell 可以支持**類型推導**
 - restrictive Type:
   - `[Int] -> [Int]`
   - `[Char] -> [Char]`
 - general Type:
   - `[a] -> [a]`
 - Qualified Types:
   -  `Ord a => [a] -> [a]`  
   type a must be an instance of the ***Ord*** class  

- Type Declaration
 - `type String = [Char]` : String 是 [Char] 的同義詞
 - `type Pos = (Int, Int)` : Pos是一組數字

- Enumerated types  
   - `data Bool = False | True`  
     Bool is a new type, with two new values False and True.
   - `data Answer = Yes | No | Unknown`

  
   ```Haskell
   data Shape = Circle Float
                | Rect Float Float

   --We can define:

	square         :: Shape
    square          = Rect 1 1
    area           :: Shape → Float
    area (Circle r) = pi * r^2
    area (Rect x y) = x * y

   ```
- Parameterized types  
    `data Maybe a = Nothing | Just a`
- Recursive types  
   - `data List a = Nil | Cons a (List a)`  
    A List is either:  
    　　(1) Nil  
　　(2) Head node + another List

   - `data Nat = Zero | Succ Nat`
   - Binary Trees  

   ```
   data Tree = Leaf Int
               | Node Tree IntTree

   Ex.
   Node (Node (Leaf 1) 3 (Leaf 4))
    	   5
		  (Node (Leaf 6) 7 (Leaf 9))
   ```
---

##List Manipulation Functions
 - xs ++ ys 　　　(also known as append xs ys)


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
  -- O(n^2)
  reverse :: [a] -> [a]
  reverse [] = []
  reverse (x : xs) = reverse xs ++ [x]

  -- Tail recursion O(n)
  reverse :: [a] -> [a]
  reverse xs = tailRev xs []

  tailRev :: [a] -> [a] -> [a]
  tailRev [] ys 	= ys
  tailRev (x:xs) ys = tailRev xs (x:ys)
 ```
 - Zipping/Unzipping two lists
    - Zip: `Ex. zip [1, 2] [‘a’, ’b’] = [(1, ’a’),(2, ’b’)]`
 ```Haskell
  zip :: [a] -> [b] -> [(a, b)]
  zip [] ys = [] -- 沒得配對的，回傳空
  zip xs [] = [] -- 沒得配對的，回傳空
  zip (x:xs) (y:ys) = (x,y) : zip xs ys -- 有的配就先配一組，再recursive
 ```
    -Unzip:  `Ex. zip [(1, 'a'),(2, 'b')] = [1, 2] ['a', 'b'] `
 ```Haskell
  unzip :: [(a,b)] -> ([a], [b])
  unzip []		   = []
  --x 配 a, y 配 b, ps配剩下的(a, b)
  unzip ((x,y) : ps) = (x:xs, y:ys) -- 分解成兩個list, 先各unzip一個
                           where
                           (xs,ys) = unzip ps --recursive call 剩下的 ps
 ```

 - Mutual Recursion  
   Functions that reference to each other
   - Example: given a list, selecting **even or odd positions** from it.

    > evens::[a] -> [a]  
	> odds ::[a] -> [a]

	```Haskell
    evens :: [a] -> [a]
    evens [] 	  = []
    evens (x :xs) = x:odds xs
    odds :: [a] -> [a]
    odds []		  = []
    odds (_ : xs) = evens xs
    ```

    ```
    evens “abcde”
 		      = { apply evens}
    ’a’ : odds “bcde”
  		     = { apply odds}
    ’a’ : evens “cde”
   		    = { apply evens}
    ’a’ : ’c’ : odds “de”
    		   = { apply odds}
    ’a’ : ’c’ : evens “e”
    ...
    ```



##List Comprehension
**建構串列的簡潔方式**  
List comprehensions allow many functions on lists to be performed in a clear and precise manner

```Haskell
> [ x^2 | x<-[1..5] ]
[1,4,9,16,25]

--length function with wildcard and generator
length   :: [a] -> Int
length xs = sum [1 | _ <- xs]

--Multiple Generators
> [ (x, y) | x <- [1,2], y <- [8,9] ] -- x y寫的順序會影響產生出的Touple內的順序
[(1,8),(1,9),(2,8),(2,9)]

--產生List內元素所有組合
perms [] = [[]]
perms xs = [ x : ps| x  <- xs, --外迴圈 x一次取一個xs元素
					 ps <- perms ( xs \\ [x] ) ] --內迴圈 xs 扣掉 元素x

--Guard
> [x | x <- [1..10], even x] --The function even x is the guard function
[2,4,6,8,10]
```
Using List Comprehension with Guards to define Prime function:
```Haskell
factors  :: Int -> [Int]
factors n = [x| x <- [1..n], n `mod` x==0]

prime  :: Int -> Bool
prime n = length (factors n) == 2
```
#Tail recursion
- Tail recursion: **recursive call occurs last**
- The technique of accumulating parameters
- Is logically equivalent to a loop!

```Haskell
--recursion ver.
fac :: Int -> Int
fac n | n == 0  = 1
fac n | n > 0   = n * fac (n-1)

--(fac 5)
--5 * (fac 4)
--5 * 4 * (fac 3)
--...
--5 * 4 * 3 * 2 * 1 * 1
--120
```
```Haskell
--tail recursion ver.
fac n = tailfac n 1 
tailfac n acc | n == 0 = acc
              | n > 0  = tailfac (n-1) n * acc

--(fac 5)
--(tailfac 5 1)
--(tailfac 4 5)
--(tailfac 3 20)
--(tailfac 2 60)
--(tailfac 1 120)
--(tailfac 0 120)
--120

```

#Higher-Order Functions(HoF)
 - Functions take **functions as arguments**
 - Functional values and **Lambda Expressions**
 - Functions return **functions as results**

####List map function  
Given a function and a list (of appropriate types), applies the function to each element of the list. *(map可以把一個function套用在一個list中的所有元素)*

```Haskell
map :: (a -> b) -> [a] -> [b] --(a -> b) function as arguments
map f [] = []
map f (x : xs) = (f x) : map f xs
```

####partially evaluated (applied)
Haskell function argument 可以分期付款，所以也可以利用此來定義簡化版function.  
Ex. 遞增  
`plus :: Int -> Int -> Int`  
so  
`(plus 1) :: Int -> Int`


###Function values and Lambda Expressions
 - Function Values:  
 A function definition binds a name to its value, function 本身是有 value 的。function本身是可以不需要名子的
 - Lambda Expression  
 `\parameterPattern -> body`  
 Ex. `\x -> (x, x, x)`  
 Ex. `\x -> x * x` (square)  
 Ex. `\x -> (\y -> x + y)` same as `add x y = x + y`  
 Ex. `(^2)` = `\x = x^2`


###Fold(reduce)
`Ex. flodr (-) 0 [1,2,3,4,5] = (1-(2-(3-(4-(5-0))))) = 3`  
`Ex. foldl (–) 0 [1,2,3,4,5] = (((((0-1)-2)-3)-4)-5) = -15`

```Haskell
--Define:
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f z []       = z
foldr f z (x : xs) = f x (foldr f z xs)
```

###結構?
可拆解、組裝、易理解的

### Semantics
#### EXP1: 
利用Haskell實做一系列小語言
	- Binding  
	賦予變數一個意思(值、意義)
	- Environment  
	儲存Binding的對應
		- updEnv
		- findEnv
		  ```Haskell
		  findEnv:: String -> Env a -> Maybe a
		  // 不一定找得到對應，所以回傳 Maybe 型態 
		  ```
	- Error Checking


    ```






















































































    ```
