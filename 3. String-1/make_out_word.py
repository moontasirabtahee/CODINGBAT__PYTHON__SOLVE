# Created by Moontasir Abtahee at 5/29/2021
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
    newOut = [char for char in out]
    newOut.insert(2,word)
    str = "".join(newOut)
    return str

print(make_out_word('<<>>', 'Yay') )
