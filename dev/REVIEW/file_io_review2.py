"""
author: Anthony Antczak
date: 11/19/2024
REVIEW 2 IO
"""
#processing
def proper_sentence(line):
    return line[0].upper()+line[1:] + "."+'\n'
#input
def main():
    with open ("input.txt", mode="r") as f_in:
        input = f_in.read().splitlines()
    proper_input = []
    for line in input:
        proper_input.append(proper_sentence(line))
    # print(proper_input)
    #output
    with open ("output.txt", mode="w") as f_out:
        f_out.writelines(proper_input)

if __name__ == "__main__":
    main()