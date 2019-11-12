class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)
            
    def add_user(self, user):
        if len(user) != 0:
            self.users.append(user)
        else:
            print("empty user! please add new user!")

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # We here use recursion. 
    # First, we check if a user is already exist in the user lists of group, if it is, we return True
    # Then, if the user is not present in the user list of current group, we dive down to the groups under this group,
    #and check whether the user is in those groups. Here, we use the recursive method to re-run the function,
    #until we finally find the users.
    # Last, if we can't find the users in both cases, we return False
    if user in group.get_users():
        return True
    else:
        for group in group.get_groups():
            return is_user_in_group(user, group)
    return False

# Test case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
#parent.get_groups()
print(is_user_in_group("sub_child_user",child))
#True

# Test case 2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_2 = Group("subchild_2")

sub_child_user2 = "sub_child_user2"
sub_child_user3 = "sub_child_user3"
sub_child.add_user(sub_child_user2)
sub_child.add_user(sub_child_user3)

child.add_group(sub_child)
sub_child.add_group(sub_child_2)
parent.add_group(child)
print(is_user_in_group("sub_child_user",child))
#False

# Test case 3
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_2 = Group("subchild_2")
sub_child_4 = Group("subchild_4")

sub_child_user2 = "sub_child_user2"
sub_child_user3 = "sub_child_user3"
sub_child_user4 = "sub_child_user4"
sub_child.add_user(sub_child_user2)
sub_child.add_user(sub_child_user3)

child.add_group(sub_child)
sub_child.add_group(sub_child_4)
parent.add_group(child)
print(is_user_in_group("sub_child_user",child))
#False

# Test case 4
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = ""
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
is_user_in_group("sub_child_user",child)
#empty user! please add new user!
#False
