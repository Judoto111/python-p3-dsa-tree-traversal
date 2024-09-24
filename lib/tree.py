class Tree:
    def __init__(self, root):
        self.root = root
    
    def get_element_by_id(self, node_id):
        return self._depth_first_search(node_id)
    
    def _depth_first_search(self, node_id):
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if current_node['id'] == node_id:
                return current_node
            stack = current_node['children'] + stack
        return None
    
    def _breadth_first_search(self, node_id):
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node['id'] == node_id:
                return current_node
            queue.extend(current_node['children'])
        return None
    
    def breadth_first_traversal(self):
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node['value'])
            queue.extend(current_node['children'])
        return result
    
    def depth_first_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            result.append(current_node['value'])
            stack = current_node['children'] + stack
        return result
