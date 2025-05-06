class Counter:
    # Class variable to store the count of objects
    count = 0

    def __init__(self):
        Counter.count += 1  # Increment count whenever a new object is created

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

        # Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Displaying count
Counter.show_count()


