# malbolge.py
import sys

def rotate_char(c):
    return chr((ord(c) + 1) % 256)

def malbolge_interpreter(code):
    memory = [0] * 59049
    for i in range(len(code)):
        memory[i] = ord(code[i])
    a = c = d = 0
    while c < len(code):
        d = memory[c]
        if d < 33 or d > 126:
            break
        if d == 106:
            a = memory[a]
        elif d == 109:
            memory[a] = rotate_char(memory[a])
        elif d == 110:
            a = (a + 1) % 59049
        elif d == 112:
            a = (a - 1) % 59049
        elif d == 113:
            c = memory[a]
        elif d == 114:
            print(chr(memory[a]), end='')
        c += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python malbolge.py <filename>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    malbolge_interpreter(code)