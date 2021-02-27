# # Name: Nanthakumar J J
# # Date: 2/25/2021
# # Time spent: 20 minutes
# # Reference: Just a glance about consecutive regex in google not specific
# # Stackoverflow (but not used for this)

# import re, json

# text = input().strip() or "Hi I am nanthakumar! from Panimalar Engineering College Chennai phone number 8695255075"
# pattern = r"([aeiou]{5,})|([^aeiou]{8,})|([!])|([0-9]{3,})|(ATGC)"
# print(list(filter(lambda x: bool(re.search(pattern, x)),text.split())))
# # text = ""
# # with open('auth.txt') as f:
# #   text+=f.read()
# # To get words in a dictinoary format
# pattern1 = r'[aeiou]{5,}'
# pattern2 = r'[^aeiou]{8,}'
# pattern3 = r'[!]'
# pattern4 = r'[0-9]{3,}'
# pattern5 = r'ATGC'
# data={'pattern1':[], 'pattern2':[], 'pattern3':[],'pattern4':[], 'pattern5':[]}
# for word in text.split():
#     if bool(re.search(pattern1, word)):
#         data['pattern1'].append(word)
#     elif bool(re.search(pattern2, word)):
#         data['pattern2'].append(word)
#     elif bool(re.search(pattern3, word)):
#         data['pattern3'].append(word)
#     elif bool(re.search(pattern4, word)):
#         data['pattern4'].append(word)
#     elif bool(re.search(pattern5, word)):
#         data['pattern5'].append(word)
# print(json.dumps(data, indent=4))


import re
s=input()
patterns=[r"[A-Z]{1,}",r"[a-z]{1,}",r"[0-9]{1,}", r"[^a-zA-Z0-9]{1,}"]
if all(bool(re.search(pat,s)) for pat in patterns):
    print("Valid")
else:
    print("Invalid")































