let g x = x + 1 in g -> the scope of g exists ONLY in (let g = x + 1 in (g)) - self contained

let x = 4 in let y = 5 in x + y
	     ------------------ scope of x
	     		  ----- scope of y
let var = e1 in e2
		-- is the scope of the var

let x = 4 in let x = 5 in x + y;; error unbound var y

let x = 4 in let x = 5 in x => 10 -- the inner x shadows over the first one
equivalents to 
let x = 4 in 
   let x = 5 in 
	x + x

x = 4
{ x = 5
  x + x
}
x in python, this x = 5, as opposed to ocaml, where this is now 4

let x = 4 in let y = let x = 4 in x in x

let x = 4 in let y = let x = 3 in x in x
              -------------------------- scope of y
			----------scope of x = 3
				    ---- scope of x = 4

f = lambda x: lambda y: x + y
g = f(4)
in this case 
g = lambda y: 4 + y
g = {lambda y: x + y, [x = 4]} # this is the idea of a closure
DEFINTION: Process of partially calling functions is called CURRYING

In ocaml we cannot update a closure once it has been created
let a = fun a -> fun b -> a + b
let f a b = a + b
let g = f 4    (* here closure is created*)
g 3		(* the closure is called and evaluated*) 

let x = 4
let f a = x + a (* x + a, x = 4 *)
let x = 3;; (this overshadows the x = 4 binding)
f 2 => 6 returns 6

MAP AND FOLD in OCAML

MAP: let rec map f lst = 
	match lst with 
	  [] -> []
	 |h::t -> (f h)::(map f t)

type: (a -> b) -> a list -> b list

map ( fun x -> int_fo_float x) [1.0;2.0]

map (int_to_float) [1.0;2.0]

Because map's input function has type a -> b functions that don't follow this cannot be sent into map 
map (fun a b -> a + b) [1;2;3;4] wouldn't work

FOLD: let rec fold f a lst = match lst with 
 	[] -> a
	|h::t -> fold f (f a h) t

(a -> b -> a) -> a -> b list -> a

Ocaml should have a garbage collector

let f a x = let _ = print_int x in a (*is a side effect as prints out number inside function*)
f 2 3 - prints 3, returns 2

let rec foldr f lst a =
    match lst with 
    [] -> a 
    |h::t -> (f h (foldr f t a ))

('a -> 'b -> 'b) -> 'a list -> 'b -> 'b

(*Notice the difference to types between regular fold and fold right*)
(*Notice the arguments are swapped*) 
(*Swapped params for foldl and foldr
swapped params for f that is used in foldr and foldl 
order of work is different:
    foldl: do work then recurse 
    foldr: recurse then do work*)

(*Tail call optimization*): can optimize function if the last thing done is recurse

let rec fold f a lst = 
    match lst with 
    [] -> a
    |h::t -> fold f (f a h) t

fold (+) 0 [1;2]
---------stack frame-----
f = (+)
a = 0
lst = [1;2]
return addr 
return fold f 1 [2]
------stack frame
f = (+)
a = 1
lst = [2]
return addr
return fold 1 3 []
------stack frame------
f = (+)
a = 3
lst = []
return 3
(*top is tail call optimization*)
Tail call optimization - (*won't need new stack frames, replaces its own stack frame because it doesnt need previous stack frame so no need to create new ones, 
Less likes to run out of space*) 

foldr stack frame
foldr (+) [1;2] 0
---------stack frame------
f = (+)
lst = [1;2]
a = 0
return (+) 0 (foldr (+) [2] 0)
----------stack frame--------
f = (+)
lst = [2]
a = 0
return (+) 2 (fold


(*essentially foldr is not as optimal as it needs to add more stack frames on top of eachother as it won't overwrite the current stack frame*)
(*essentially foldr is called first but the function f hasnt so the previous tack information needs to be saved*)

(*fibonacci*)
let rec fib n =
    if n <= 1 then 1
    else fib(n-1) + fib(n-2)

recurse 
recurse 
add 
(*not tail optimized*)

let rec fib n a b =
    if n <= 1 tghen b
    else fib (n-1) b (a+b)
(*Is tail optimized*) doesnt require previous returning function as no information from calling function is needed 

---------unit----------
 - type that doesnt return anything 
(*You get it when you call print*)
expressed as ()
- used to sometimes express a side effect
- result of functions that don't need to return anything
---------tree---------------- 
type tree = Node of int * tree * tree| Leaf
let onetwothree = Node(1, Node(2, Leaf, Leaf), Node (3, Leaf, Leaf))
let rec addone t = match t with
    Leaf -> Leaf
    |Node(v, left, right) when left = Leaf -> Node(v+1, addone left, addone right) (*Only when left = Leaf do we do the action*)
    |Node(v, left, right) -> Node(v, addone left, addone right)
--------generic options----------
type 'a gtree = Node of ('a * gtree * gtree)|Leaf
type 'a l = B of 'a |Nil
(*generic 'a*)
This ' option allows generics
type 'a option = Some of 'a|None
-Use generics to wrap a return value around something
