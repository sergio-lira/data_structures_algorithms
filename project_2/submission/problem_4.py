import random

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group, cache=True):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if cache:
        visited = list()
        return recursive_user_search(user, group, visited)
    else:
        return recursive_user_search_no_cache(user, group)

def recursive_user_search(user, group, visited):
    if user in group.get_users():
        return True
    
    for group in group.get_groups():
        
        if group.get_name() not in visited:
            visited.append(group.get_name())
            return recursive_user_search(user, group, visited)
            
    return False

def recursive_user_search_no_cache(user, group):
    if user in group.get_users():
        return True
    
    for group in group.get_groups():
        return recursive_user_search_no_cache(user, group)
            
    return False

print("<<< Test Case 1 >>>")
lvl0 = Group("lvl0")
lvl1 = Group("lvl1")
lvl3 = Group("lvl3")

lvl3_user = "lvl3_user"
lvl3.add_user(lvl3_user)

lvl1.add_group(lvl3)
lvl0.add_group(lvl1)     
      
print("if the lvl2_user in group? {}".format(is_user_in_group('lvl2_user', lvl0)))
print("if the lvl3_user in group? {}".format(is_user_in_group('lvl3_user', lvl0)))

print("\n<<< Test Case 2 >>>")
print("Large scale randomized group, takes a few seconds.")

root = Group('root')
lvl_1 = [Group('A_{}'.format(g)) for g in range(0, 5) ]
lvl_2 = [Group('B_{}'.format(g)) for g in range(0, 100) ]
lvl_3 = [Group('C_{}'.format(g)) for g in range(0, 500) ]
random.seed(5)

user_limit = 1000
third = user_limit//3
users = ['user_{}'.format(u) for u in range(0, user_limit)]

for group_A in lvl_1:    
    for user in users[0:third]:
        if random.random() <0.5:
            group_A.add_user(user)
    root.add_group(group_A)
    
for group_A in lvl_1:   
    
    for group_B in lvl_2:
        for user in users[third:third*2]:
            if random.random() <0.4:
                group_B.add_user(user)
                    
        if random.random() < 0.4:
            group_A.add_group(group_B)
            
for group_B in lvl_2:        
        
    for group_C in lvl_3:
        for user in users[third*2:user_limit]:
            if random.random() <0.3:
                group_C.add_user(user)
        
        if random.random() < 0.3:
            group_B.add_group(group_C)
      
print("if the user_956 in group? {}".format(is_user_in_group('user_956', root)))

print("\n<<< Test Case 3 >>>")
print("Cyclic group membership")

lvl0 = Group("lvl0")
lvl1 = Group("lvl1")
lvl3 = Group("lvl3")

lvl3_user = "lvl3_user"
lvl3.add_user(lvl3_user)

lvl1.add_group(lvl3)
lvl0.add_group(lvl1)
lvl3.add_group(lvl0)
      
print("if the lvl2_user in group? {}".format(is_user_in_group('lvl2_user', lvl0)))
print("if the lvl3_user in group? {}".format(is_user_in_group('lvl3_user', lvl0)))
            