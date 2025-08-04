from traversalstrategy import TraversalStrategy


class PopularTraversal(TraversalStrategy):
    
    def create_iterator(self, items):
        
        return iter(sorted(items,key=lambda x: 0 if "ad" in x else 1))