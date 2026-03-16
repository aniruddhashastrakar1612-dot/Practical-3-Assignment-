class Employee:

    def getData(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def showData(self):
        print("\nEmployee Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


managers = []

for i in range(10):
    print("\nEnter Details of Manager", i+1)
    m = Manager()
    m.getData()
    managers.append(m)

print("\n----- Manager Details -----")

for i in managers:
    i.showData()