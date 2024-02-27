from abc import ABC, abstractmethod
from dataclasses import dataclass
# Single Responsibility Principle

STANDARD_TAX: float = 0.08

@dataclass
class Tax:
    taxPercent: float = STANDARD_TAX
@dataclass
class Cost:
    price: int # given in cents
    def __str__(self):
        dollars: int = self.price // 100
        cents: int = self.price % 100
        print(dollars + " dollars and " + cents + " cents")
@dataclass
class Discount:
    discountPercent: float

@dataclass
class Stock:
    count: int
    def check_if_stocked(self) -> bool:
        if (self.count > 0):
            print("Item is stocked")
            return True
        else:
            print("Item is not stocked")
            return False

@dataclass
class Customer:
    name: str
    userID: int

@dataclass
class Item(ABC):
    stock: Stock
    name: str

    @abstractmethod
    def get_cost() -> int:
        """returns the item cost in cents"""
        return 0

@dataclass
class PricedItem(Item):
    cost: Cost
    tax: Tax
    def get_cost(self) -> int:
        return int(self.cost.price + self.cost.price * self.tax.taxPercent)

@dataclass
class DiscountedItem(PricedItem):
    discount: Discount
    def get_cost(self) -> int:
        discountBeforeTax = self.cost.price - self.cost.price * self.discount.discountPercent
        return int(discountBeforeTax + discountBeforeTax * self.tax.taxPercent)

# we will only consider domestic shipping
@dataclass
class Address:
    street1: str
    street2: str
    city: str
    state: str
    zipCode: str

@dataclass
class Cart:
    items: list[Item]
    def __init__(self) -> None:
        self.items = []
        print("created new empty cart")
        
    def add_item(self, newItem: Item):
        """adds an item to cart \n\nwill accept discounted items and priced items"""
        if (newItem.stock.check_if_stocked()):
            self.items.append(newItem)
            print("added", newItem)
        else:
            print("item is not in stock, did not add to cart")
        
class Order:
    customer: Customer
    cart: Cart
    shippingAddress: Address

    def __init__(self, customer, cart, address) -> None:
        self.customer = customer
        self.cart = cart
        self.address = address
        self.order_num = 0 # TODO: get order num from database
        
        print("starting new order with id", self.order_num)

    def change_cart(self, cart) -> None:
        self.cart = cart
        print("attached current cart to order")

    def change_address(self, address) -> None:
        self.shippingAddress = address
        print("attached new address to order")

    def get_total(self) -> int:
        total = 0
        for item in self.cart.items:
            total += item.get_cost()
        return total

    def submit_order(self):
        print("submitted order. thank you!")
        

def main() -> None:
    # Some available items...
    carrot = PricedItem(name="carrot", cost=Cost(100), tax=Tax(), stock=Stock(56))
    print("carrot cost: ", carrot.get_cost()) # prints cost with added tax
    
    apple = PricedItem(name="apple", cost=Cost(70), tax=Tax(), stock=Stock(20))
    
    yogurt = PricedItem(name="yogurt", cost=Cost(119), tax=Tax(), stock=Stock(30))
    print("yogurt cost: ", yogurt.get_cost())

    soda = DiscountedItem(name="pop", cost=Cost(169), tax=Tax(), discount=Discount(0.20), stock=Stock(13))
    print("soda cost: ", soda.get_cost())

    cucumber = PricedItem(name="cucumber", cost=Cost(89), tax=Tax(), stock=Stock(0))
    print("soda cost: ", soda.get_cost())


    harold = Customer("harold", 392045)
    haroldAddress = Address("Bran St", "Apt C", "Edwardsville", "IL", 62025)
    myCart = Cart()
    
    print("trying to add carrot")
    myCart.add_item(carrot)
    print("trying to add cucumber (there are none in stock)")
    myCart.add_item(cucumber)
    print("trying to add soda")
    myCart.add_item(soda)


    myOrder = Order(harold, myCart, haroldAddress)
    print("order cost: ", myOrder.get_total())

    myOrder.submit_order()

if __name__ == "__main__":
    main()