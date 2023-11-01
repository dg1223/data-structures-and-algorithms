from treenode import Treenode
from bfs import bfs

sample_root_node = Treenode("Home")
docs = Treenode("Documents")
photos = Treenode("Photos")

sample_root_node.children = [docs, photos]

my_wish = Treenode("WishList.txt")
my_todo = Treenode("TodoList.txt")
my_cat = Treenode("Fluffy.jpg")
my_dog = Treenode("Spot.jpg")

docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)

path_to_target = bfs(sample_root_node, "Fluffy.jpg")
if not path_to_target:
    print("No path found")
else:
    print("Path found!")
    for node in path_to_target:
        print(node.value)