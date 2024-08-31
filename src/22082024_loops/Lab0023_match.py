#match statement
"""match variable:
case pattern1:
#code block
case patttern2:
#code bloak"""
#Write the programme to ask the user which browser he wants to run automation
browser_name = input("enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firfox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case _:
        print("Browser not found")


