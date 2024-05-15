"""
    a grocery tracker class.
"""


class GroceryTracker:
    """
    A class to represent a grocery tracker.
    """

    def __init__(self, grocery_list: list[str] = None) -> None:
        """Initialises the grocery tracker with a grocery list.

        Args:
            grocery_list (list[str], optional): The list of previously added groceries. Defaults to None.
            Grocery list will contain a tuple with the item and the quantity.
        """
        if grocery_list is None:
            grocery_list = []

        self.grocery_list = grocery_list

    def add_item(self, item: str, quantity: int = 1) -> None:
        """Adds an item to the grocery list.

        Args:
            item (str): The item to add to the grocery list.
        """
        for item_tuple in self.grocery_list:
            if item_tuple[0] == item:
                self.grocery_list[self.grocery_list.index(item_tuple)] = (
                    item_tuple[0],
                    item_tuple[1] + quantity,
                )
                return
        self.grocery_list.append((item, quantity))

    def remove_item(self, item: str, quantity: int = None) -> None:
        """Removes an item from the grocery list.

        Args:
            item (str): The item to remove from the grocery list.
        """
        try:
            for item_tuple in self.grocery_list:
                if item_tuple[0] == item:
                    if quantity is None:
                        self.grocery_list.remove(item_tuple)
                    else:
                        if item_tuple[1] - quantity <= 0:
                            self.grocery_list.remove(item_tuple)
                        else:
                            self.grocery_list[self.grocery_list.index(item_tuple)] = (
                                item_tuple[0],
                                item_tuple[1] - quantity,
                            )

        except ValueError:
            return "Item does not exist in the grocery list."
