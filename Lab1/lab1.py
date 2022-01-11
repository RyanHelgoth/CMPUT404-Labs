import requests as req


def main():
    url = "https://raw.githubusercontent.com/RyanHelgoth/CMPUT404-Labs/main/Lab1/lab1.py" 
    page = req.get(url)
    print(page.text)



main()
