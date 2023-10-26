"Turing Machine" - Machine which can solve any problem
    - Things like balanced parenthesis can be solved
    - The halting problem cannot be solved

"Turing Machine" - need an infinite ticker tape
    - Has a pointer that can read and write
    - Finite states with directions
    - "Turing complete" Language can simulate a turing machine

"Lambda Calc" - is also 'turing complete'
    - "λ" - calculus
    - e -> x, x is a variable
        |λx.e function def
        |e e application
    - "a b c" e -> e e -> a e
                -> a e e -> a b e
                         -> a b c
    - "λx.x" e -> λx.e -> λx.x
    - "λx.a" e -> λx.e -> λx.a
    - "λx.a b" e -> λx.e -> λx.ee -> λx.ae -> λx.ab
    - Grammer is ambigious
    - λ-calc is left associative (1+2)-3
        - When give expression like ((e e) e) the left two things are done first
    - (λx.x) a - λx(in).x(output) a(argument)
    - (λx(param).e(body)) a (argument)
    - "bound variables" - variables that are referring to the parameter variable
        - (λ.x.y) a => y
        - "y" is a free variable, "x" is a bound variable
    - "free variable" - variables that arent bound
        - In the above example y and a are free variables
    - (λx.λy.xy) a - a is a free variable
    - "alpha equivalence" - when functions are alpha equivalent - all bound variables can change but they still remain the same
        - (λx.x) a - alpha equiv (λb.b) a
        - not alpha equiv to (λy.y) b
        - We can chage bound variables, not free ones
    - (λx.(λx.x)) - fun x -> fun x -> x
    - (λx.(λy.y)) - fun x -> fun y -> y
    (λx.(λy.yyx)y)x - fun x -> fun y -> x+y
        --------- body of the x function
           --- body of the y function
    - We can use () to prematurely end the scope of expressions
    - "Beta normal form" - a λ calc expression that cannot be reduced any further
    - "B - reduction" - apply an argument to a function
    - (λx.xy) (λa.aa) - we can apply a function as an argument
        - Reduce -> ((λa.aa)y)  
    - To "overwrite" default behavior ("left associative") 
        - add ()
        - λx.xyx
        - (λx.(xy))x
    - (λx.xy)a alpha equivalent to (λb.by)a 
        - (λx.λx.x)
        - (λy.λx.y) a -> (λx.x) a -> a doesnt work
            - (fun x -> fun y -> x) x a -> (fun y -> x) a -> we return x 
            - (fun y -> fun x -> fun y) x a -> (fun x -> x) a -> we incorrectly bound because there is both a dependent and independent x
            - There is a scoping issue here  
        - ((λy.λx.y)x) a  - > (λx.x) a -> x is not bound when before it was free - doesnt work
            - "bound variables cannot become unbound" and "unbound cannot become bound"
            - The alpha equivalent - ((λb.λc.b)x)a -> (λc.x)a - is valid 
            - (λc.x) -> fun c -> 3 
            - (λc.x)a -> (fun c -> 3) a
        - "There are times when you need to alpha convert" - so the semantics will be made as intended and there wont be incorrect bounds
    - "call by name (lazy)" - evaluate only when needed
    - "call by value (eager)" - evaluate the argument first
    - (fun x -> print_int 3)(print_int 4) 
        - 43 : eager
        - 3: lazy - we dont evaluate the argument at all unless we need to 
    - Why care - runtime, figure out how we want to reduce, changes how looping works 
    - (λx.xx)(λx.xx) - > (λx.xx)(λx.xx)
    - (λx.y)((λx.xx)(λx.xx))
        - "lazy" - y
        - "eager" - (λx.y)((λx.xx)(λx.xx)
    - We can encode data 
        - We can for example (λx.λy.x) = true 
        - (λx.λy.y) = false
    - if a the b else c 
    - if true then false else true
        - lambda a,b,c
        - ((λx.λy.x)(λx.λy.y))(λx.λy.x) 
        - (λy.(λx.λy.y))(λx.λy.x) - the y outer doesnt have scope over y inner (λy.(λx.λy.y))
        - (λx.λy.y) = false
        - if false then true else false => false
        - 

