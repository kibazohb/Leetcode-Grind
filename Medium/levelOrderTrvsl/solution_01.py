from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #the queue contains a list of lists
        #each list carrying the elements of every level
        levels = []
        if root is None:
            return levels
        #this queue will handle all the nodes from the tree
        queue = deque([root])
        stage = 0
        while queue:
            level_lengths = len(queue)
            #always append empty list to store values of each level
            levels.append([])
            
            for _ in range(level_lengths):
                curr = queue.popleft()
                levels[stage].append(curr.val)
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        
            stage+=1
            
        return levels 
