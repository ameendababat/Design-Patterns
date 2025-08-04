from npc import NPC


def main():
    """
    When creating new objects is more complex or costly than copying existing ones
    
    """
    npc1 = NPC("Goblin", {"type": "club", "damage": 10})
    npc2 = npc1.clone()
    npc2.name = "ameen"
    npc2.weapon["damage"] = 35
    print(npc1)
    print(npc2)
    
if __name__ == "__main__":
        main()