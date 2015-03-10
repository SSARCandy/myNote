###**stack**
  可用於Postfix Conversion  

```
a+b*c+(d*e+f)*g
operand ( a . b . c ...... )
token ( + . - . * .  / .... )
```

**Algorithm**

```C
while ( input token != EOF ){
    if( token == operand )    " 1 "
        output token
    else if ( token == closing parenthesis ){   " 2 "
        while ( top != opening parenthesis ){
            pop & output
                pop /* discard opening parenthesis */
        }
    }
    else{
        while priority(top) >= priority(token )   " 3 "
            pop & output
    }
    push token
}
```

 **ex1.** 　a+b*c 　  => 　abc*+

  Steps| token   |   stack  |   output
  :---: | :------: | :--------: | :-----------:
  1|  a     |            |   a
  2|  +     |     +      |
  3|  b     |     +      |   ab
  4|  *     |    + *    |
  5|  c     |    + *   |     abc
  6|        |         |      abc*+  



**ex2.**　	a + b * c + ( d * e + f ) * g  　 =>  　a b c * +   d e * f + g *   +

 Steps| token    |       stack    |       output         |   operation
  :---: | :--------: | :--------------: | :--------------------: | :-----------:
 1    |  a       |                |       a              |    " 1 "
 2    |  +       |        +       |       a              |    " 3 "
 3    |  b       |        +       |       ab             |    " 1 "
 4    |  *       |        + *     |       ab             |    " 3 "
 5    |  c       |        + *     |       abc            |    " 1 "
 6    |  +       |        +       |       abc*+          |    " 3 "
 7    |  (       |        + (     |       abc*+          |    " 3 "
 8    |  d       |        + (     |       abc*+d         |    " 1 "
 9    |  *       |        + ( *   |       abc*+d         |    " 3 "
 10   |  e       |        + ( *   |       abc*+de        |    " 1 "
 11   |  +       |        + ( +   |       abc*+de*       |    " 3 "
 12   |  f       |        + ( +   |       abc*+de*f      |    " 1 "
 13   |  )       |        +       |       abc*+de*f+     |    " 2 "
 14   |  *       |        + *     |       abc*+de*f+     |    " 3 "
 15   |  g       |        + *     |       abc*+de*f+g    |    " 1 "
 16   |          |                |       abc*+de*f+g*+  |    " 3 "


---
**Function Calls**  
recursive is using STACK to store all function call  
OS mantaining programs is using STACK

####**Queue**
 * First In First Out (FIFO)
 * operation
   * Enqueue at rear (end)
   * Dequeue at front (start)

 * Application of Queue
    * Job scheduling in operating system
    * file server
    * Printer server


### Priority Queue
 * Job scheduling (printer job , CPU job)
   * First-In-First-Out(Queue)
   * Shortest
