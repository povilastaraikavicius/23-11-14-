# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc..
# Initiate class and show up some calculations.
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="exercises.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# class Calculator:
#     def sum_two_numbers(self, number_a: float, number_b: float) -> float:
#         return number_a + number_b

#     def divide_two_numbers(self, number_a: float, number_b: float) -> float:
#         if number_b == 0:
#             return "Error: Cannot divide by zero"
#         return number_a / number_b

#     def multiply_two_numbers(self, number_a: float, number_b: float) -> float:
#         return number_a * number_b

#     def subtract_two_numbers(self, number_a: float, number_b: float) -> float:
#         return number_a - number_b


# calc = Calculator()
# try:
#     result_sum = calc.sum_two_numbers(5.5, 3)
#     result_subtraction = calc.subtract_two_numbers(10, 4)
#     result_multiplication = calc.multiply_two_numbers(7, 2)
#     result_division = calc.divide_two_numbers(8, 0)

#     print("Sum:", result_sum)
#     print("Subtraction:", result_subtraction)
#     print("Multiplication:", result_multiplication)
#     print("Division:", result_division)
# except Exception as err:
#     logging.error(f"you got {err} error")
#     print("You got error")


# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow
# it with @company.com at the end. Make sure the entire email is in lowercase.


# class Employee:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname
#         self.email = None
#         self.fulname = self.create_fulname()

#     def create_fulname(self) -> str:
#         return self.name + " " + self.surname

#     def create_email(self) -> str:
#         self.email = self.name + "." + self.surname + "@company.com"
#         return self.email


# employee = Employee(name="Povilas", surname="Taraika")
# print(employee.fulname)
# print(employee.create_email())


# A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

# Population is greater than 20 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object.
#  Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}
# Examples:

# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"


class Country:
    def __init__(self, country: str, area: int, population: int) -> None:
        self.country = country
        self.area = area
        self.population = population

    def is_big(self) -> bool:
        if self.area > 20000000 or self.population > 3000000:
            return True
        else:
            return False

    def compare_pd(self, other_country: "Country") -> str:
        if self.population / self.area > other_country.population / other_country.area:
            return f"{self.country} has a bigger population density than {other_country.country}"
        else:
            return f"{self.country} has a smaller population density than {other_country.country}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big())
print(andorra.is_big())
print(andorra.compare_pd(australia))






