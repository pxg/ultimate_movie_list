import re

name = 'The Artist (2011/I)'
# match = re.search(r'\([^)]*\)', name)
# #year_match = re.search('2011', name)
# # name = re.sub(r'\([^)]*\)', '', name)
# # print name
# if match:
#     print 'match!'
#     print match.groups()
# else:
#     print 'no match'

# could be problematic is there are brackets in the film name
year = name[name.find('(') + 1:name.find(')')]
name = name.replace('(' + year + ')', '')

#name = str.replace(name, '(' + year + ')')
print name
print year
