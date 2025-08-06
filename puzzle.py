from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement_0_A = And(
    AKnight, AKnave
)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    Implication(AKnight, statement_0_A),
    Implication(AKnave, Not(statement_0_A))
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement_1_A = And(
    AKnave, BKnave
)

knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, statement_1_A),
    Implication(AKnave, Not(statement_1_A)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statement_2_A = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)
statement_2_B = Or(
    And(BKnight, AKnave),
    And(BKnave, AKnight),
)
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, statement_2_A),
    Implication(AKnave, Not(statement_2_A)),

    Implication(BKnight, statement_2_B),
    Implication(BKnave, Not(statement_2_B)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

statement_3_A = Or(AKnight, AKnave)

statement_3_B = And( 
    CKnave, 
    Biconditional(statement_3_A, AKnave)
)

statement_3_C = AKnight

knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, statement_3_A),
    Implication(AKnave, Not(statement_3_A)),

    Implication(BKnight, statement_3_B),
    Implication(BKnave, Not(statement_3_B)),

    Implication(CKnight, statement_3_C),
    Implication(CKnave, Not(statement_3_C)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
