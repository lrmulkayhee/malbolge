import sys

def crazy_op(a, b):
    return ((a // 81) % 3) * 81 + ((a // 9) % 9) * 9 + ((a // 1) % 9)

def malbolge_interpreter(code):
    memory = [0] * 59049
    for i in range(len(code)):
        memory[i] = ord(code[i])
    a = c = d = 0
    print("Starting interpretation...")  # Debug print
    while c < len(code):
        d = memory[c]
        if d < 33 or d > 126:
            break
        if d == 106:
            a = memory[a]
        elif d == 109:
            memory[a] = (memory[a] + 1) % 256
        elif d == 110:
            a = (a + 1) % 59049
        elif d == 112:
            a = (a - 1) % 59049
        elif d == 113:
            c = memory[a]
        elif d == 114:
            print(chr(memory[a]), end='')
        c += 1
    print("\nInterpretation finished.")  # Debug print

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 malbolge_interpreter.py <filename>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    malbolge_interpreter(code)