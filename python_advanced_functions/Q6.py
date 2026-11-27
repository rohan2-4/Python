# Create a function that accepts:
# - Multiple subject marks using *args.
# - Student details using **kwargs.
def student(*args,**kwargs):
    if not args:
        return None
    print(kwargs)
    total_marks = sum(args)
    average_marks = total_marks/len(args)
    highest_marks = max(args)
    return{
        "total_marks":total_marks,
        "average_marks":average_marks,
        "highest_marks":highest_marks
    }
s1=student(35,40,50,60 ,name='Rohan',course='Python')
print(s1)