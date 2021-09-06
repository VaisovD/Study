# Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> line = 'SomethingZisZwrongZhere'
# >>> line.split('Z')
# ['Something', 'is', 'wrong', 'here']
# >>> line.isalpha()
# True
# >>> line = 'SomethingZisZwrongZhere\n'
# >>> line.rstrip
# <built-in method rstrip of str object at 0x000001C0572A7940>
# >>> line.rstrip().split('Z')
# ['Something', 'is', 'wrong', 'here']
# >>> '{1} is going {0} here?'.format('on', 'What')
# 'What is going on here?'
# >>> ord(y)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'y' is not defined
# >>> ord(\n)
#   File "<stdin>", line 1
#     ord(\n)
#           ^
# SyntaxError: unexpected character after line continuation character
# >>> ord('\n')
# 10
# >>> ord('y')
# 121
# >>> msg = """
# ... msg = """
# >>> msg = """
# ... aaaaaaaaaaaa
# ... bbbbbbbb
# ... ddddddddd
# ... cccccccccc
# ... msg = """
# >>> msg
# '\naaaaaaaaaaaa\nbbbbbbbb\nddddddddd\ncccccccccc\nmsg = '
# >>> len(msg)
# 50
# >>> print(len(2**100))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: object of type 'int' has no len()
# >>> print(len(str(2**100)))
# 31
# >>> msg.rstrip().split('\n')
# ['', 'aaaaaaaaaaaa', 'bbbbbbbb', 'ddddddddd', 'cccccccccc', 'msg =']
# >>> msg.strip().split('\n')
# ['aaaaaaaaaaaa', 'bbbbbbbb', 'ddddddddd', 'cccccccccc', 'msg =']
# >>> M = [12, 25, 33, 44]
# >>> m.sort
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'm' is not defined
# >>> M.sort
# <built-in method sort of list object at 0x000001C057262240>
# >>> M.sort()
# >>> M
# [12, 25, 33, 44]
# >>> M = [95, 77, 82, 55]
# >>> M.sort()
# >>> M
# [55, 77, 82, 95]
# >>> M.reverse()
# >>> M
# [95, 82, 77, 55]
# >>> M.reverse()
# >>> M
# [55, 77, 82, 95]
# >>>Soups = ['with rice', 'with beans', 'the clean one']
# >>> Meals = ['Palov', 'Qozon kabob', 'Kabob', 'Jiz']
# >>> Desserts = ['Strawberry cake', 'Random cake', 'Coockies']
# >>> Menu = {'First meal' : Soups, 'Second meal' : Meals, 'Dessert' : Desserts}
# >>> Menu
# {'First meal': ['with rice', 'with beans', 'the clean one'], 'Second meal': ['Palov', 'Qozon kabob', 'Kabob', 'Jiz'], 'Dessert': ['Strawberry cake', 'Random cake', 'Coockies']}  
