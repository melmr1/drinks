class Drink:
    
    valid_bases = {'chai', 'milk', 'OJ', 'hazelnut tea'}
    valid_flavors = {'vanilla', 'cocoa', 'coconut', 'mint'}

    def __init__(self):
        """Initialize a Drink with a base and an empty list of flavors."""
        self._base = None
        self._flavors = ()

    def get_base(self):
        """Return the base of the drink."""
        return self._base

    def get_flavors(self):
        """Return the list of flavors for the drink."""
        return self._flavors

    def get_num_flavors(self):
        """Return the number of flavors added to the drink."""
        return len(self._flavors)

    def set_flavors(self, flavors):
        """Set multiple flavors at once, ensuring no duplicates and valid flavors."""
        if len(set(flavors)) != len(flavors):
            raise ValueError("Flavors cannot have duplicates.")
        invalid_flavors = [flavor for flavor in flavors if flavor not in Drink.valid_flavors]
        if invalid_flavors:
            raise ValueError(f"Invalid flavors: {', '.join(invalid_flavors)}")
        self._flavors = flavors

    def add_flavor(self, flavor):
        """Add a single flavor to the drink, ensuring it is valid and not a duplicate."""
        if flavor not in Drink.valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        if flavor in self._flavors:
            raise ValueError(f"Flavor {flavor} is already added.")
        self._flavors.append(flavor)
       
class Order:
    def __init__(self):
        """Initialize an empty order."""
        self._items = []

    def get_items(self):
        """Return the list of items (drinks) in the order."""
        return self._items

    def get_total(self):
        """Calculate and return the total cost of the order. Assuming each drink costs 5 units."""
        return len(self._items)

    def get_num_items(self):
        """Return the number of items (drinks) in the order."""
        return len(self._items)

    def get_receipt(self):
        """Generate a receipt with details of each drink and the total cost."""
        receipt = []
        for i, item in enumerate(self._items):
            receipt.append(f"Item {i + 1}: {item.get_base()} with flavors {', '.join(item.get_flavors())}")
        receipt.append(f"Total: {self.get_total()} units")
        return "\n".join(receipt)

    def add_item(self, drink):
        """Add a drink to the order."""
        if not isinstance(drink, Drink):
            raise ValueError("Item must be an instance of Drink.")
        self._items.append(drink)

    def remove_item(self, index):
        """Remove a drink from the order by its index."""
        if index <= 0 or index >= len(self._items):
            raise IndexError("Invalid index.")
        del self._items[index]

