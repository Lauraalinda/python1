def hello(name,age):
    year=2022-age
    print(f"Hello {name} you were born in {year}")

def mycountry(country="Uganda"):
    return f"My country is {country}"

def greet(*names):
    for name in names:
      print(f"Hello{name}")
   
def sum(*numbers):
    total=0
    for number in numbers:
        total +=number
    return total

def multiply(*numbers):
    multiple=1
    for number in numbers:
        multiple *=number
    return multiple

def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
    elif "age" in keys:
        year= 2022-kwargs['age']
        return f"Hello {kwargs['name']} you were born in {year}"
    elif "name" in keys:
        return f"Hello {kwargs['name']}"
    else:
        return f"Hello Anonymous"
    
def sum_and_greet(*args,**kwargs):
    print(args)
    print(kwargs)

def multiply_and_greet(*args,**kwargs):
    multiple=1
    for number in args:
        multiple *=number
    print(multiple)
    keys=kwargs.keys()
    if "country" in keys:
        print(f"Hello {kwargs['name']} from {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif "name" in keys:
        print(f"Hello {kwargs['name']}")
    else:
        print (f"Hello Anonymous")
    
    
    
    





