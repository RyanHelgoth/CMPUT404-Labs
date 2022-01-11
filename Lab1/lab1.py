import requests as req


def main():
    page = req.get("https://www.google.com/")
    print(page.text)



main()
