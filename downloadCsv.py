import requests
import datetime
from msvcrt import getch

ENCODING = "utf-8"
PATH = "./"

links = []

with open("links.txt", "r", encoding="utf-8") as fil:
    links = fil.readlines()
    # print(links)

print(f"--> {len(links)} link found. Download starting...")

for i, link in enumerate(links):
    try:
        link = link.strip()
        print(f"-> {str(i + 1).zfill(3)}: Downloading {link}")
        content = b""
        content = requests.get(link).content
        # print(content)
        customDT = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        fileName = customDT + "__" + link.split("/")[-1]
        # print(fileName)
        with open(PATH + fileName, "wb") as fil:
            fil.write(content)
    except Exception as ex:
        print("An error occured:")
        print(ex)
    else:
        print(f"-> saved file: {fileName}")

print("--> All links are downloaded. Press any key to exit.")
getch()
