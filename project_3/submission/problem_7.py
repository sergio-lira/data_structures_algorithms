class RouteTrie:
    def __init__(self):
       self.root=RouteTrieNode()

    def insert(self, path, handler):
        current_node = self.root

        #Split the path by / and iterate the nodes generated
        for node in path:
            if node not in current_node.children:
                current_node.insert(node)
            current_node = current_node.children[node]

        #The end node will be the leaf node that will contain the handler
        current_node.handler = handler

    def find(self, path):
        current_node = self.root

        for node in path:
            if node not in current_node.children:
                return False
            current_node = current_node.children[node]

        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = None
        self.children = {}

    def insert(self, node):
        self.children[node] = RouteTrieNode()

#The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler):
        self.route_trie = RouteTrie()
        self.add_handler("/", root_handler)

    def add_handler(self, path, handler):
        path = self.split_path(path)
        if len(path) > 0:
            self.route_trie.insert(path, handler)

    def lookup(self, path):

        handler = self.route_trie.find(self.split_path(path))
        if handler:
            return handler
        else:
            return 'not found handler'

    def split_path(self, path):
        if len(path) > 1:
            path = '/'+ path.strip('/')
        return path.split('/')

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print('<< Basic Test Cases >>')
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one\\

print('\n<< More Test Cases >>')
router.add_handler("/home/about/me/contact", "contact handler")  # add a route
print(router.lookup("/home/about/me/contact")) #should print contact handler

router.add_handler("/home/social_media/facebook", "facebook handler")  # add a route
print(router.lookup("/home/social_media/facebook"))  # should print facebook handler

router.add_handler("/home/social_media/twitter", "twitter handler")  # add a route
print(router.lookup("/home/social_media/twitter"))  # should print twitter handle


router.add_handler("/home/sub_dir///", "sub_dir handler")  # add a by ignoring trailing '/'
print(router.lookup("/home/sub_dir///"))  #should print sub_dir handler

print(router.lookup("/////"))  #Should print root found handler
