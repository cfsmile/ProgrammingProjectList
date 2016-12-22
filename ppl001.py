# using Python 3.5.2

# ppl001: 逆转字符串——输入一个字符串，将其逆转并输出。

# Ref : [1] http://blog.csdn.net/seetheworld518/article/details/46756639

# Solution 1: Slicing

text1 = "Hello"
print(text1[::-1])

# Solution2 : Change string to list, then use list.reverse()method.

text2 = "World"
l = list(text2)
l.reverse()
print(''.join(l))
