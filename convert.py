# Python code to convert into dictionary
def Convert(tup, di):
	for a, b, c in tup:
         di.setdefault("name",'').append(a)
         di.setdefault("password",'').append(b)
         di.setdefault("email",'').append(c)
	return di


# Driver Code
tups = [("akash", "pa0","hello"), ("gaurav", "12","asd"), ("anand", "14" ,"mysql") ]
dictionary = {}
print(Convert(tups, dictionary))
