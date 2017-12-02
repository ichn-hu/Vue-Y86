class A:
    pass

a = A()
a.__dict__.update(**{
    'a': [1, 2, 3]
})
print(a.a[1:3])
b = {'b': [2, 3, 4]}
a.__dict__.update(**b)
print(a.b[0:3])