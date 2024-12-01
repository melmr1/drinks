valid_bases = {'chai', 'milk', 'OJ', 'hazelnut tea'}
    valid_flavors = {'vanilla', 'cocoa', 'coconut', 'mint'}
    size_costs = {
        "small": 1.00,
        "medium": 2.00,
        "large": 3.00,
        "xlarge":4.00,
    }
    def __init__(self):
        """Initialize a Drink with a base and an empty list of flavors."""
        self._base = None
        self._flavors = ()
        self._cost = 0.0
        self._size = None 
        self.set_size(size)
    def get_base(self):
        """Return the base of the drink."""
        return self._base

    def get_flavors(self):
        """Return the list of flavors for the drink."""
        return self._flavors

    def get_num_flavors(self):
        """Return the number of flavors added to the drink."""
        return len(self._flavors)

    def get_total(self):
        return self._cost



    def set_flavors(self, flavors):
        if len(set(flavors)) != len(flavors):
            raise ValueError("Flavors cannot have duplicates.")
            new_flavors = set(flavors) - self._flavors
            self._cost += .015 * len(new_flavors)
            self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in Drink.valid_flavors]
            raise ValueError(f"Invalid flavors: {', '.join(invalid_flavors)}")
        

    def add_flavor(self, flavor):
        if flavor not in Drink.valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        if flavor in self._flavors:
            self._ += 0.15 
            raise ValueError(f"Flavor {flavor} is already added.")
        self._flavors.append(flavor)

    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs: 
            size._size = size
            self._cost = size._size_costs[size] * 15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size}. choose a different size from {list{self._size_cost.keys()}}.")


class Order:

    _tax_rate = 0.0725 # taxrate 

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

    def get_total(self):
        return sum(drink.get_total() for drink in self._item)

    def get_tax(self):
        return self.get_total() * (1 + self._tax_rate)

    def get_receipt(self):
        receipt_data = {
            "number_drinks": self.get_num_items(),
            "drinks": [],
            "subtotal": self.get_num_total(),
            "tax": self.get_total() * self._tax_rate,
            "grand total": self.get_tax() 
        }

        for i, drink in enumerate(self._items):
           drink_data = {
            "number_drinks": i + 1,
            "base": drink.get_base(),
            "size": drink.get_size(),
            "flavors": drink.get_flavors(),
            "total_cost": drink.get_total()
           }
        receipt_data["drinks"].appeend(drink_data)
        return receipt_data
        
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

