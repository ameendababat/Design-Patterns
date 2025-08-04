from traversalstrategy import TraversalStrategy


class UnreadTraversal(TraversalStrategy):
    
    def create_iterator(self, items):
        unread_item = [item for item in items if item.endswith("1")]
        return unread_item
        