def get_second_lowerest_grade(lst):

    # The line below does the following 
    # convert list to dictionary - dict(lst)
    # retrieves all values and return them in a list - dict(lst).values()
    # select distinct values by converting the list to a set - set(<list>)
    # sort the set - sorted(<set>)
    # extract second element (second lowerest) element - sorted(<set>)[1]
    second_lowerest = sorted(set(dict(lst).values()))[1]

    # Iterate through the original list (using list comprehension) and only select nested lists which (second) values are equal to second lowerest value 
    lst2 = [ k for k,v in lst if v == second_lowerest ] 

    lst2.sort()

    for n in lst2:
        print(n)

def prepare_list():

    lst = []

    lst.append(['Harry', 37.21])
    lst.append(['Berry', 37.21])
    lst.append(['Tina', 37.2])
    lst.append(['Akriti', 41])
    lst.append(['Harsh', 39])

    return lst

lst = prepare_list()

get_second_lowerest_grade(lst)