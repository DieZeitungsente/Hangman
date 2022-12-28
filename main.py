import random, os, sys
print("HANGMAN")
print("\n\n\nPress enter to start")
input()
def startgame():
    words = [    "ALGORITHM",    "BINARY",    "CACHE",    "CODE",    "COMPILER",    "CONDITIONAL",    "DEBUGGING",    "DECLARATION",    "ENCRYPTION",    "EXCEPTION",    "FUNCTION",    "HASH",    "INTEGER",    "INTERPRETER",    "ITERATION",    "KEYWORD",    "LOOP",    "METHOD",    "OBJECT",    "OPERATOR",    "PARAMETER",    "POINTER",    "RECURSION",    "REFERENCE",    "REGEX",    "SCRIPT",    "SORTING",    "STRING",    "SYNTAX",    "THREAD",    "TYPE",    "VARIABLE",    "VIRTUAL",    "ABSTRACT",    "BOOLEAN",    "BREAK",    "CLASS",    "CONSTANT",    "DATA",    "DYNAMIC",    "ENCAPSULATION",    "EVENT",    "FINALLY",    "GARBAGE",    "HANDLER",    "INHERITANCE",    "INTERFACE",    "LAMBDA",    "LIBRARY",    "MESSAGE",    "NAMESPACE",    "NULL",    "OVERRIDE",    "PRIVATE",    "PROTECTED",    "PUBLIC",    "QUEUE",    "RECORD",    "REENTRANT",    "RESOURCE",    "RETURN",    "STACK",    "STATIC",    "STRUCTURE",    "SWITCH",    "TEMPLATE",    "TRY",    "TUPLE",    "TYPE",    "UNION",    "VALUE",    "VECTOR",    "VOID",    "VOLATILE",    "WHILE",    "YIELD",    "ARRAY",    "BLOCK",    "BYTE",    "CHAR",    "CONTEXT",    "DELEGATE",    "DOUBLE",    "ENUM",    "FLOAT",    "GOTO",    "INLINE",    "LONG",    "POOL",    "SHORT",    "SINGLE",    "STREAM",    "SYNC",    "TASK",    "TRACE",    "TYPE",    "UNICODE",    "USHORT",    "UTF8",    "VOID"]
    rdm = random.choice(words)
    os.system("cls")
    wrong = 0
    progress = ""
    for letter in rdm:
        progress += '_'
    while "_" in progress:
        newValue = ''
        print(progress)
        inp = input()
        for i in range(len(progress)):
            if rdm[i] == inp.upper():
                newValue += inp.upper()
            elif progress[i] != '_':
                newValue += progress[i]
            else:
                newValue += '_'
        if progress == newValue:
            wrong += 1
        if wrong == 10:
            print(f"You lost! The word was {rdm.lower()}")
            again = input('Play again? [y/n]: ')
            if again == 'y':
                startgame()
            else:
                sys.exit()
        progress = newValue
        os.system("cls")
    print(rdm)
    print("\nYOU WIN!")
    again = input('Play again? [y/n]: ')
    if again == 'y':
        startgame()
    else:
        sys.exit()
startgame()