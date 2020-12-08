string = input("Enter test score's: ").split(',')
string = [c.strip() for c in string]
print('\n'.join(string))
