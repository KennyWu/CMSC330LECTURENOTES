Syntax: What does something look like?
Semantics: what does something mean?
"grammer": subset of syntax; structure of sentence
    "Ex": the green truck
        We have a determiner (the, singular), adj (green), noun(truck)
"Regular Expression" - cant be used for verifying grammer, but rather if all the symbols are valid 
    If we were to list out the possible words and their combinations it really wouldnt be that feasible 


"Context Free Grammer" - next step up from regular expression - they actually have memory in it 
    Ex: Say we have R -> empty
                        |episilon
                        |RR
                        |R|R
                        |R* 
    "R": Is the "Non terminal": symbol that stands or is a placeholder of other symbols
    "Terminals": base symbols/symbols found in the alphabet "a", "b", "" 
    "production rules": rules that declare what terminals/order of terminals that nonterminals can be
    
    "Nonterminals": R
    "Terminals": Empty, episolon, *, |
    "Productions rules": 5 of them 
                        R -> ____
                            _____
    How does production rules define define ordering? 
        -*a is valid
        -|ab is invalid - "definitely invalid because we cant derive it"  
        -a|b is valid
    "Derivation": ways to prove/derive a string from a CFG
        R->R*->a* 
        R->R|R->a|R->a|b
        We prove that "a|b" and "a*" are derived 
        "ex": a*|bc
            R->R|R->R*|R->a*|R->a*|RR->a*|bR->a*|bc
    
    "Leftmost derivation": When you expand or define leftmost nonterminal during a derivation 
    "Rightmost derivation": When you expand or define the rightmost non termianl during a derivation
    "ex": E _> E + E | n, n in Z
        1 + 2 + 3
        Wartch the goddamn vid im too lazy
    Languages can be ambigious
    There can be multiple versions of leftmost derivation maybe we define the nonterminal on the leftside
        - But in the other version we would expand the leftmost instead
        - However ambigiuty is not optimal and in CFG context occurs if two valid leftmost derivations 
        exist for any particular strings 
        "Ex": +                      +
             / \                    / \
            1  +                   +  3 
              / \                 / \   
             2  3                1   2

    "Ex": E-> M + E | M
          M-> N * M | N
          N-> 1|2|3
          "nonterminals" : EMN
          "terminals": +, *, 1,2,3
          We define different layers to out CFG - allows us to have order to operations, less ambiguity
    We can define with CFG balanced Parenthesis
    "Ex":  E -> E + E | E* E|n|(E)
    We dont have to define recursively in a linear format
    it could also be in a nonlinear format
    -CFG are like a superset of regular expressions in terms of the strings they accept
    
    a^nb^nc^x n, x \in naturals >= 1
    - Describes all a and bs to be the same amount and c to be >= to one
    - Cannot track equal lengths of a's' and b's' with regular ex[ression so we have to use CFG
    - We thus use CFG to describe this constraint
    - S -> AC
      A -> aAb|empty
      c -> cC|c
We should be able to determine if a grammer is ambigious or not
An ambigious grammer - when there is two ways to define a leftmost or two rightmost
    -Not rightmost and leftmost
Given CFG check if something is gramatically correct
CFG is just a new way to describe a set of strings - just more powerful due to memeory 
    -pushdown automata


there are a variety of different parsers that exist
  Left leaning and right leaning parsers
  Look-a-head  parsers
  backtracking parsers
  recursive descent parsers
  bottom-up parsers

  in this course: LL(1) -> Left leaning, lookahead by 1 parser (via recursive descent)
  LL(1) parsers have some restrictions: cannot parse ambiguous grammars
  ambiguous grammars can be converted to nonambiguous grammars if you are restrained to LL1 parser

         
evaluating: the process of deriving meaning from a grammatically correct sentence

  allowed
  1 + 2
  3 * 6
  true && false

  disallowed
  true + 4.0 

lexing: string -> token list

parsing: token list -> parse tree or Absract syntax tree
    - Focus building an recursive tree
evaluator: tree -> value|code
  interpreter: value
    1 + 2 -> 3
  compiler: code
    1 + 2 -> mov 1 abx;
             mov 2 aby;
             add abx aby;

"Abstract Syntax Tree" - abstracts away the specific operator (+) as op, represents 2,3 as just n and n
        OP 
       /  \ 
      n    n 


'''≈
CFG
E -> M + E|M - E|M
M -> N * M|N / M|N
N -> n|(E)

1 + 2
1+2
1 / 3 * 5
1 * (2 - 4)
12+13
  -> [12], "+13"

terminals: n,+,-,/,*,(,)
'''

from functools import reduce
import re
# string -> token list
def lex(instr):
  toklst = []
  number_re = re.compile(r"^(-?\d+)")
  terminal_re = re.compile(r"^[()\-+/*]")
  wspace_re = re.compile(r"^(\s+)")
  pos = 0
  strlen = len(instr)
  while pos < strlen:
    match = re.match(number_re,instr[pos:])
    if match:
      toklst.append(match.group(1))
      pos += len(match.group(1))
    else:
      match = re.match(terminal_re,instr[pos:])
      if match:
        toklst.append(match.group(0))
        pos += 1
      else:
        match = re.match(wspace_re,instr[pos:])
        if match:
          pos += len(match.group(1))
        else:
          raise SyntaxError("Invalid character")
  return toklst

'''≈
  1 CFG
  2 E -> M + E|M - E|M
  3 M -> N * M|N / M|N
  4 N -> n|(E)
  5 
  6 1 + 2
  7 1+2
  8 1 / 3 * 5
  9 1 * (2 - 4)
 10 12+13
 11   -> [12], "+13"
 12 
 13 terminals: n,+,-,/,*,(,)
 14 '''
 15 


class Node:
    def __init__(self, t, value, left=None, right=None):
        self.type=t
        self.left=left
        self.right=right
        self.value=value

# token list -> tree
def parser(toklst):

def parse_e(toklist):
    #first need a M, then need a plus, lastly we need an E
    mtree, remain = parse_m(toklist)
    #Flag maybe something not right here
    if r


def parse_m(toklist):

def parse_n(toklist):


# tree -> value
def eval(tree): 
