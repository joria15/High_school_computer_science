"""
author: Mr. Habib
date: 11/08/2024
A skeleton file for a python project
"""

def main():
    # Input
    eipm = str(input("Explore, investigate, practice or make? "))
    name = str(input("Enter the file name: "))
    author = str(input("enter an author: "))
    discription = str(input("enter a discription: "))
    import datetime
    todays_date = datetime.datetime.today().strftime("%m/%d/%Y")
    # Processing
    headers = '"""'+"\n"+"author: "+author+"\n"+"date: "+todays_date+"\n"+discription+"\n"+'"""'+"\n"+"\n"+"def main():"+"\n"+"\t"+"#input"+"\n"+"\t"+"#processing"+"\n"+"\t"+"#output"+"\n"+"\n"+'if __name__ == "__main__":'+"\n"+"\t"+"main()"
    # Output
    with open(name+"_"+eipm+".py", mode="w") as f_out:
        f_out.write(headers)   


if __name__ == "__main__":
    main()