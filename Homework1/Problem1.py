import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text",  type = str)
parser.add_argument("word1", type = str)
parser.add_argument("word2", type = str)

args = parser.parse_args()

print("The given text: " + args.text)
print("First word: " + args.word1)
print("Second word: " + args.word2)
print("Output string: " + args.text.replace(args.word1,args.word2))
