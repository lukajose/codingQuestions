
class Node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.data = val
        self.right = right
        self.left = left


class Solution:

    def height(self,root) -> int:
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
        
    def print_lvl(self,root:Node,level:int):
        if root == None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1:
            self.print_lvl(root.left,level-1)
            self.print_lvl(root.right,level-1)
        

    def levelOrder(self,root):
        height = self.height(root)
        print("height of tree:" ,height)
        for i in range(1,height+1):
            self.print_lvl(root,i)
            
    
def main():
    sol = Solution()
    root = Node(val=1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    sol.levelOrder(root)


main()