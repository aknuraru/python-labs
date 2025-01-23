#Python: tuples

#Tuples are similar topic with lists. But tuples are unchangeable!

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "History of Kazakhstan")
print(mytuple)

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "History of Kazakhstan")
print(len(mytuple)) #Result: 7. Using this operation we can define the length of the tuple. 

mytuple = ("PP1")
print(type(mytuple)) #Result: str.

mytuple = ("PP2",)
print(type(mytuple)) #Result: tuple.

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "History of Kazakhstan")
print(mytuple[1]) #Result: Using this operation we can print first element of the tuple. In program counting starts from zero.

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "History of Kazakhstan")
print(mytuple[-1]) #Result: Using this operation we can print last element of the tuple. 

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language")
print(mytuple[:4]) #Result: All elements until fourth element (not including)

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language")
print(mytuple[2:]) #All element from second index.

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language")
print(mytuple[-4:-1]) 

mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language")
if "PP1" in mytuple: 
    print("Yes, 'PP1' is in the tuple.")
    
a = ("BMW", "Mercedes", "Rolls Royce")
b = list(a)
b.insert(1, "Sonata") #b.append("Sonata") Соңына барып қосылады. 
a = tuple(b)
print(a) #Tuple is not changeable. If we want to add something new to tuple, we use this form. 

#Adding tuples with eachother: 
a = ("BMW", "Mercedes", "Rolls Royce")
b = ("Sonata", "Changan")
c = a+b
print(c) 

mytuple =("BMW", "Mercedes", "Rolls Royce")
for i in mytuple:
    print(i)
    
tuple1 = ("BMW", "Mercedes", "Rolls Royce")
tuple2 = ("Sonata", "Changan")
tuple3 = tuple1+tuple2
print(tuple3)

tuple1 = ("BMW", "Mercedes", "Rolls Royce")
tuple2 = tuple1 * 2
print(tuple2)

tuple1 = ("BMW", "Changan", "Rolls Royce", "BMW")
x = tuple1.count("BMW")
print(x) #5 cаны неше рет кездесетінін санау. Result: 2