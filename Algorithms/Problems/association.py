"""
Constraints:
    - List of pairs of items (strings)
    - Each pair is an association
    
Goal:
    - Return the association group with highest number of elements
    - Two groups same size, return group that has lexicologocal smallest
      element between these 2
    - Return group in lexcological sorted order
Idea:
    - Association group is chain of elements with association between them
    - Some items would have no association - they are independent nodes of graph
    - Associated ones are having link between them
    - [[Item1, Item2], [Item3, Item4], [Item4, Item5]]
    - Item1: Item2,
      Item2: Item1
      Item3: Item4
      Item4: Item3, Item5
      Item5: Item4

"""
