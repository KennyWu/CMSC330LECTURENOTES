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

   terminal_re = re.compile(r"^[-+*/()]")
 31     number_re = re.compile(r"^-?\d+")
 30     wspace_re = re.compile(r"\s+")
 29     pos = 0
 28     strlen = len(instr
 27     while (pos < strlen):
 26         match = re.match(numbar_re, instr[pos:])
 25         if match:
 24             toklst.append(match.group(1))
 23             pos += len(match.group(1))
 22         else:
 21             match = re.match(terminal_re, instr[pos:])
 20             if match:
 19                 toklst.append(match.group(1))
 18                 pos += 1
 17             else:
 16                 match = re.match(wspace_re, instr[pos:])
 15                 if match:
 14                     toklst.append(match.group(0))
 13                     pos += 1
 12                 else:
 11                     raise SyntaxError("invalid chracter detected")
 10         return toklst
  9
  8 Now parsers
  7 #take toklist -> tree
  6 #edge cases: 1 + 2 -
  5             1 - 2 * 4 order of operations is adhered to
  4 def parse(toklist):
  3
  2 def parse_E(toklst):
  1     mparse = parse_M(toklst)
150     #remaining tokens after M is parsed, should be [], [+,...] or [-,....]
  1
  2 def parse_M(toklst):
  3

