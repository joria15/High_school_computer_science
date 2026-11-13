#1.
# Requirements:
# MenuItem Class:
# Attributes: name (str), price (float), category (str)
# __init__(self, name, price, category): Initialize menu item
# __str__(): Return "name - $price (category)"
# __eq__(self, other): Compare by name
# Menu Class:
# Attributes: restaurant_name (str), _items (dictionary with category as key, list of MenuItems as value)
# __init__(self, restaurant_name): Initialize menu
# add_item(self, item): Add MenuItem to appropriate category
# get_items_by_category(self, category): Return list of items in that category
# get_average_price(self): Return average price of all items
# __str__(): Return "restaurant_name Menu - X items"


class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category
   
    def __str__(self):
        return f"{self.name} - ${self.price} {self.category}"
   
    def __eq__(self, other):
        return self.name == other.name


class Menu:
    def __init__(self, restaurant_name: str):
        self.restaurant_name = restaurant_name
        self._items = {}


    def __str__(self):
        count = 0
        for value in self._items.values():
            for thing in value:
                count += 1
        return f"{self.restaurant_name} - {count} items"
   
    def add_item(self, item):
        if item.category not in self._items:
            self._items[item.category] = [item]
        else:    
            self._items[item.category].append(item)
   
    def get_items_by_category(self, category):
        categorize = []
        items = self._items.get(category, [])
        for item in items:
            categorize.append(item.name)
       
        return categorize
   


   
    def get_average_price(self):
        average = 0
        count = 0
        for value in self._items.values():
            for thing in value:
                average += thing.price
                count += 1
       
        return average / count
       
def main():
    menu = Menu("Joe's Diner")


    menu.add_item(MenuItem("Burger", 12.99, "Main"))
    menu.add_item(MenuItem("Fries", 4.99, "Side"))
    menu.add_item(MenuItem("Salad", 8.99, "Main"))
    menu.add_item(MenuItem("Soda", 2.99, "Drink"))


    print(menu)
    print(f"Average Price: ${menu.get_average_price():.2f}")
    print("Main dishes:", menu.get_items_by_category("Main"))


if __name__ == "__main__":
    main()


# Create a library book system using inheritance.
# Requirements:
# Media Class (Base Class):
# Attributes: title (str), media_id (str), is_available (bool)
# __init__(self, title, media_id): Initialize with is_available = True
# checkout(): Set is_available to False, return True if successful
# return_item(): Set is_available to True
# __str__(): Return "Media: title (ID: media_id)"

# Book Class (inherits from Media):
# Additional attributes: author (str), pages (int)
# __init__(self, title, media_id, author, pages): Call parent constructor
# __str__(): Return "Book: title by author (ID: media_id)"

# DVD Class (inherits from Media):
# Additional attributes: director (str), runtime (int)
# __init__(self, title, media_id, director, runtime): Call parent constructor
# __str__(): Return "DVD: title directed by director (ID: media_id)"

class Media:
    def __init__(self, title: str, media_id: str):
        self.title = title
        self.media_id = media_id
        self.is_available = True

   
    def checkout(self) -> bool:
        if self.is_available == True:
            self.is_available = False
            return True
        return False
        
    def return_item(self):
        self.is_available = True
    
    def __str__(self):
        return f"Media: {self.title} (ID: {self.media_id})"
    
class Book(Media):
    def __init__(self, title: str, media_id: str, author: str, pages: int):
        super().__init__(title, media_id)
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author} (ID: {self.media_id})"

class DVD(Media):
    def __init__(self, title: str, media_id: str, director: str, runtime: int):
        super().__init__(title, media_id)
        self.director = director
        self.runtime = runtime

    def __str__(self): 
        return f"DVD: {self.title} directed by {self.director} (ID: {self.media_id})"

#3
# Attributes: name (str), student_id (str), _grades (dictionary with subject as key, grade as value)
# __init__(self, name, student_id): Initialize with empty grades
# add_grade(self, subject, grade): Add a grade for a subject
# get_average(self): Return average of all grades
# get_highest_grade(self): Return tuple of (subject, grade) for highest grade
# __str__(): Return "Student: name (ID: student_id) - Average: X.X"

# Classroom Class:
# Attributes: class_name (str), _students (dictionary with student_id as key)
# __init__(self, class_name): Initialize classroom
# add_student(self, student): Add student to classroom
# load_grades_from_file(self, filename): Read grades file and add to students (use try-except)
# get_class_average(self): Return average of all student averages
# get_top_student(self): Return Student with highest average
class Classroom:
    def __init__(self, class_name: str):
        self.class_name = class_name
        self._students = {}
    
    def add_student(self, student):
        self._students[student.student_id] = student

    def get_class_average(self):
        sum = 0
        count = 0

        for value in self._students.values():
            sum += value.get_average()
            count += 1
        
        return sum / count

    
    def load_grades_from_file(self, filename):
        with open(filename, "r") as file:
            for read in file:
                id, sub, grd = read.split(",")
                self._students[id].add_grade(sub, float(grd))
                    
    
    def get_top_student(self):
        maxxed = 0
        student = ""

        for key, value in self._students.items():
            grade = value.get_average()
            if grade > maxxed:
                maxxed = grade
                student = key

        return (student, maxxed)


class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self._grades = {}

    def add_grade(self, subject, grade):
        if subject not in self._grades:
            self._grades[subject] = [grade]
        else:
            self._grades[subject].append(grade)

    def get_average(self):
        count = 0
        sum = 0
        for value in self._grades.values():
            for summed in value:
                sum += summed
                count += 1

        return sum / count if count > 0 else 0
    
    def get_highest_grade(self):
        grade = 0
        subject = ""
        for key, value in self._grades.items():
            for check in value:
                if check > grade:
                    grade = check
                    subject = key
        return (subject, grade)

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id}) - Average: {self.get_average()}"
    
    #4
    # Product Class:
    # Attributes: name (str), product_id (str), price (float), stock (int)
    # __init__(self, name, product_id, price, stock): Initialize product
    # reduce_stock(self, quantity): Reduce stock, raise ValueError if insufficient
    # __str__(): Return "name ($price) - stock in stock"
    # Order Class:
    # Attributes: order_id (str), _products (list of tuples: (Product, quantity))
    # __init__(self, order_id): Initialize order
    # add_product(self, product, quantity): Add product to order (use try-except for stock check)
    # get_total(self): Return total cost of order
    # get_product_count(self): Return total number of items
    # __str__(): Return "Order order_id: X items, Total: $Y.YY"

class Product:
    def __init__(self, name: str, product_id: str, price: float, stock: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Insufficient")
        else:
            self.stock -= quantity
        
    def __str__(self):
        return f"{self.name} (${self.price}) - {self.stock} in stock"
        
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self._products = []
    
    def add_product(self, product, quantity):
        find = False

        for i in range(len(self._products)):
            if self._products[i][0] == product:
                add = list(self._products[i])
                add[1] += quantity
                del self._products[i]
                self._products[i] = tuple(add)
                find = True
                
        if not find:
            self._products.append((product, quantity))

    def get_total(self):
        cost = 0
        for item in self._products:
            cost += item[0].price
        return cost
    
    def get_product_count(self):
        count = 0
        for item in self._products:
            count += item[1]
        return count
    
    def __str__(self):
        return f"Order {self.order_id}: {self.get_product_count()} items, Total: ${self.get_total()}"



def main():
    # menu = Menu("Joe's Diner")


    # menu.add_item(MenuItem("Burger", 12.99, "Main"))
    # menu.add_item(MenuItem("Fries", 4.99, "Side"))
    # menu.add_item(MenuItem("Salad", 8.99, "Main"))
    # menu.add_item(MenuItem("Soda", 2.99, "Drink"))


    # print(menu)
    # print(f"Average Price: ${menu.get_average_price():.2f}")
    # print("Main dishes:", menu.get_items_by_category("Main"))

    # #2
    # book = Book("Python Programming", "B001", "John Smith", 350)
    # dvd = DVD("The Matrix", "D001", "Wachowskis", 136)
    # print(book)
    # print(dvd)


    # book.checkout()
    # print(f"Book available: {book.is_available}")


    # book.return_item()
    # print(f"Book available: {book.is_available}")

    #3
    # classroom = Classroom("ICS4U")

    # classroom.add_student(Student("Alice", "S001"))
    # classroom.add_student(Student("Bob", "S002"))

    # try:
    #     classroom.load_grades_from_file("lab_12/grades.txt")
    #     print(f"Class Average: {classroom.get_class_average():.2f}")
    #     top = classroom.get_top_student()
    #     print(f"Top Student: {top}")
    # except FileNotFoundError:
    #     print("File not found")

    #4
    laptop = Product("Laptop", "P001", 999.99, 5)
    mouse = Product("Mouse", "P002", 29.99, 10)

    order = Order("ORD001")

    try:
        order.add_product(laptop, 2)
        order.add_product(mouse, 3)
        print(order)
        print(f"Total: ${order.get_total():.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

