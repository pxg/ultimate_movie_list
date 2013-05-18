name = 'The Artist (2011/I)'
# could be problematic is there are brackets in the film name
year = name[name.find('(') + 1:name.find(')')]
name = name.replace('(' + year + ')', '')

print name
print year
