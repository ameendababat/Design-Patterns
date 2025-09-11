from traversalstrategy import TraversalStrategy


class Feed:
    def __init__(self, items):
        self.items = items


    def get_iterator(self, strategy:TraversalStrategy):
        return strategy.create_iterator(self.items)
