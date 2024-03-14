import webbrowser

def google_search(query):
    base_url = "https://www.google.com/search?q="
    search_url = base_url + query
    webbrowser.open(search_url)

def main():
    print("Welcome to Google Search!")
    print("Please enter your search query:")
    query = input("> ")

    print("Do you want to specify a file type? (yes/no)")
    filetype_option = input("> ")
    if filetype_option.lower() == "yes":
        print("Please enter the file type:")
        filetype = input("> ")
        query += f' filetype:{filetype}'

    print("Do you want to search within a specific webpage? (yes/no)")
    webpage_option = input("> ")
    if webpage_option.lower() == "yes":
        print("Please enter the webpage domain (e.g., jokes.com):")
        webpage = input("> ")
        query += f' site:"{webpage}"'

    print("Do you want to add any specific text to search for? (yes/no)")
    intext_option = input("> ")
    if intext_option.lower() == "yes":
        print("Please enter the text to search for:")
        intext = input("> ")
        query += f' intext:"{intext}"'

    print("Do you want to add any specific title to search for? (yes/no)")
    intitle_option = input("> ")
    if intitle_option.lower() == "yes":
        print("Please enter the title to search for:")
        intitle = input("> ")
        query += f' intitle:"{intitle}"'

    print("Do you want to add every type of Google hacking method? (yes/no)")
    hacking_option = input("> ")
    if hacking_option.lower() == "yes":
        query += ' ("inurl:.php?id=" OR "inurl:.asp?id=" OR "inurl:.jsp?id=" OR "inurl:.html?id=")'

    google_search(query)

if __name__ == "__main__":
    main()