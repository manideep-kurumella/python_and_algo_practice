"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
print( +"is of type "+type())
"""

def set_data_type():
    #int
    a=5
    print( str(a) ," is of type ",type(a))

    #float
    b=6.5
    print(str(b) ," is of type ",type(b))

    #string
    c="Hello World!!"
    print( c ," is of type ",type(c))

    #list
    d=["apple","orange","banana"]
    print( d," is of type ",type(d))

    #tuple
    e=("apple","orange","banana")
    print( e," is of type ",type(e))

    #set
    f={"apple", "banana", "cherry"}
    print( f," is of type ",type(f))

    #frozen set
    g=frozenset({"apple", "banana", "cherry"})
    print( g," is of type ",type(g))

    #dict
    g = {"name" : "John", "age" : 36}
    print( g," is of type ",type(g))

    #range
    h = range(6)
    print( h," is of type ",type(h))

    #boolean
    i=True
    print( i," is of type ",type(i))


def specific_data_type():
    
    #assign a variable with string
    a=str("Hello World")
    print( str(a) ," is of type ",type(a))

    #assig


set_data_type()