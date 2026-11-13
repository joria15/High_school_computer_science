"""
author: anthony antczak
date: 11/13/2024
unit 2 review
"""

def main():
	#input
	with open ("cool_story.txt", mode="r") as f_in:
		numbered = f_in.readlines()
	#processing/Output
		with open ("cool_story_numbered.txt", mode="w") as f_out:
			for i in range (len(numbered)):
				f_out.write(f"{i+1}. {numbered[i]}")

if __name__ == "__main__":
	main()