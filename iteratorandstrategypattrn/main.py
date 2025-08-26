from populartraversal import PopularTraversal
from chronotraversal import ChronoTraversal
from unreadtraversal import UnreadTraversal
from feed import Feed


def main():
    """A way to access the elements of an aggregate object like a list sequentially"""
    feed_items = ["post1", "ad1", "suggested1", "post2"]
    feed = Feed(feed_items)
    print("Chrono: ")
    for item in feed.get_iterator(ChronoTraversal()):
        print(item)


    print("\nMost popular:")
    for item in feed.get_iterator(PopularTraversal()):
        print(item)


    print("\nUnread:")
    for item in feed.get_iterator(UnreadTraversal()):
        print(item)


if __name__ == "__main__":
    main()