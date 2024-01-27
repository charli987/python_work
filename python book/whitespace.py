#adding tabs
print("hello")
print("\thello")

#adding a new line
print("Hello my name is charlotte")
print("Hello \nmy name is \ncharlotte")

#combining adding tabs and new lines
print("foods I like: peas, chocolate, biscuits")
print("foods I like: \n\tpeas \n\tchocolate \n\tbiscuits")

#removing whitespace from the right side of a string permanently
favourite_food = "chocolate "
favourite_food = favourite_food.rstrip()
print(favourite_food)

#removing whitespace from the left side of a string permanently
favourite_food = " chocolate"
favourite_food = favourite_food.lstrip()
print(favourite_food)

#removing whitespace from both sides of a string permanently
favourite_food = " chocolate "
favourite_food = favourite_food.strip()
print(favourite_food)

#removing prefixes and suffixes
website_url = "https://website.com"
simple_website_url = website_url.removeprefix("https://")
print(simple_website_url)
simpler_website_url = simple_website_url.removesuffix(".com")
print(simpler_website_url)