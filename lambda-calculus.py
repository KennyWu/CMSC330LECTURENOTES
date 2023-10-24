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
