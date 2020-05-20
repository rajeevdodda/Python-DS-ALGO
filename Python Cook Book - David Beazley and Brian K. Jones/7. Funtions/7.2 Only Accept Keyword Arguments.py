def keyword_args(*args, x):
    print(args)
    print(x)


keyword_args(1, 2, 3, x=10)
keyword_args(x=10)
print(help(keyword_args))
