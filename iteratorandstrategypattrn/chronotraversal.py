from traversalstrategy import TraversalStrategy


class ChronoTraversal(TraversalStrategy):
    
    def create_iterator(self, items):
        
        return iter(items)