"""
author: Anthony Antczak
date: 11/20/2024
LAB 2 Silver
"""

def proper_sentence(line):
    return line+" DONE"+'\n'
#input
def main():
    with open ("todos.txt", mode="r") as f_in:
        input = f_in.read().splitlines()
    proper_input = []
#processing
    for i in range(len(input)):
            if i < len(input)-1:
                proper_input.append(proper_sentence(input[i]))
            else:
                print(len(proper_input))

    #output
    with open ("completed_todos.txt", mode="w") as f_out:
        f_out.writelines(proper_input)

if __name__ == "__main__":
    main()