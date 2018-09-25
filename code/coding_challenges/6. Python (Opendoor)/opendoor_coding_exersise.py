# We collected baby names from various published lists and put them into a JSON object as follows:
# 
# key: source list name (e.g. "2015-us-official-boys", "2015-baby-center-girls")
# value: a list of names in the order of popularity (e.g. [ "Sophia", "Emma", "Olivia", ... ])
# baby-names-data.json
# 
# {
#   "2016-baby-center-girls": [ "Sophia", "Emma", "Olivia", ... ],
#   "2016-baby-center-boys": [ "Jackson", "Aiden", "Lucas", ...],
#   "2015-baby-center-girls": [ "Sophia", "Emma", "Olivia", ... ],
#   ...
# }
# The question has two parts:
# 
# Write a function that given a name, returns an ascending rank sorted list of names of all lists where the given name appears.
# 
# For example, given "sophia", function returns:
# 
#  [
#    {list: "2016-baby-center-girls", rank: 1},
#    {list: "2015-baby-center-girls", rank: 1},
#    {list: "2015-us-official-girls", rank: 3}
#  ]
from operator import itemgetter

baby_names = {
  "2016-baby-center-girls": [ "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Riley", "Aria", "Zoe", "Charlotte", "Lily", "Layla", "Amelia", "Emily", "Madelyn", "Aubrey", "Adalyn", "Madison", "Chloe", "Harper", "Abigail", "Aaliyah", "Avery", "Evelyn", "Kaylee", "Ella", "Ellie", "Scarlett", "Arianna", "Hailey", "Nora", "Addison", "Brooklyn", "Hannah", "Mila", "Leah", "Elizabeth", "Sarah", "Eliana", "Mackenzie", "Peyton", "Maria", "Grace", "Adeline", "Elena", "Anna", "Victoria", "Camilla", "Lillian", "Natalie" ],
  "2016-baby-center-boys": [ "Jackson", "Aiden", "Lucas", "Liam", "Noah", "Ethan", "Mason", "Caden", "Oliver", "Elijah", "Grayson", "Jacob", "Michael", "Benjamin", "Carter", "James", "Jayden", "Logan", "Alexander", "Caleb", "Ryan", "Luke", "Daniel", "Jack", "William", "Owen", "Gabriel", "Matthew", "Connor", "Jayce", "Isaac", "Sebastian", "Henry", "Muhammad", "Cameron", "Wyatt", "Dylan", "Nathan", "Nicholas", "Julian", "Eli", "Levi", "Isaiah", "Landon", "David", "Christian", "Andrew", "Brayden", "John", "Lincoln" ],
  "2015-baby-center-girls": [ "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Zoe", "Lily", "Emily", "Madison", "Amelia", "Riley", "Madelyn", "Charlotte", "Chloe", "Aubrey", "Aria", "Layla", "Avery", "Abigail", "Harper", "Kaylee", "Aaliyah", "Evelyn", "Adalyn", "Ella", "Arianna", "Hailey", "Ellie", "Nora", "Hannah", "Addison", "Mackenzie", "Brooklyn", "Scarlett", "Anna", "Mila", "Audrey", "Isabelle", "Elizabeth", "Leah", "Sarah", "Lillian", "Grace", "Natalie", "Kylie", "Lucy", "Makayla", "Maya", "Kaitlyn" ],
  "2015-baby-center-boys": [ "Jackson", "Aiden", "Liam", "Lucas", "Noah", "Mason", "Ethan", "Caden", "Logan", "Jacob", "Jayden", "Oliver", "Elijah", "Alexander", "Michael", "Carter", "James", "Caleb", "Benjamin", "Jack", "Luke", "Grayson", "William", "Ryan", "Connor", "Daniel", "Gabriel", "Owen", "Henry", "Matthew", "Isaac", "Wyatt", "Jayce", "Cameron", "Landon", "Nicholas", "Dylan", "Nathan", "Muhammad", "Sebastian", "Eli", "David", "Brayden", "Andrew", "Joshua", "Samuel", "Hunter", "Anthony", "Julian", "Dominic" ],
  "2015-us-official-girls": [ "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte", "Harper" ],
  "2015-us-official-boys": [ "Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James", "Alexander", "Michael", "Benjamin" ]
}

def rank_name(name):
    res_dic = []
    for key, lst in baby_names.items():
        cnt = 0 
        for item in lst:
            cnt += 1
            if item == name:
                dic = {
                    "list": key,
                    "rank": cnt
                }
                res_dic.append(dic)
                break
    res_sorted = sorted(res_dic, key=itemgetter('rank')) #inner dictionaries in the list res_dic will be sorted by rank value
    return res_sorted

print(rank_name("Sophia"))

# Now, we would like to make our service more user friendly. We would like to provide a name prefix (e.g. "an") and get all baby names that start with that prefix (e.g. "anna", "anthony", etc.) along with the list name and relative ranking for each matching name.
# 
# For example, given "an", function returns something like this:
# 
# {
#   anna: [
#     { list: '2015-baby-center-girls', rank: 36 },
#     { list: '2016-baby-center-girls', rank: 46 }
#   ],
#   andrew: [
#     { list: '2015-baby-center-boys', rank: 44 },
#     { list: '2016-baby-center-boys', rank: 47 }
#   ],
#   anthony: [
#     { list: '2015-baby-center-boys', rank: 48 }
#   ]
# }
# 

def rank_name_2(prefix):
    res_dic = {}
    for key, lst in baby_names.items():
        cnt = 0 
        for name in lst:
            cnt += 1
            prefix_len = len(prefix)
            
            if prefix.lower() == name[0:prefix_len].lower():
                name_content = []
                if name in res_dic:
                    name_content = res_dic[name]
                
                inner_dic = {
                    "list": key,
                    "rank": cnt
                }
                
                name_content.append(inner_dic)
                name_content_sort = sorted(name_content, key=itemgetter("rank")) # inner dictionaries in the list name_content will ebsorted by rank 
                res_dic[name] = name_content_sort
                #break
                
    res_sorted = sorted(res_dic.items()) #items in the dictionary res_dic wille sorted by name
    return res_sorted

print(rank_name_2("an"))
