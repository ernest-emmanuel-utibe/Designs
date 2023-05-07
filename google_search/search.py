import webbrowser

location = input("Enter the location: ")
url = "https://www.google.com/maps/search/?api=1&query=" + location
webbrowser.open(url)
