# As a standalone utility:
from langchain_google_community import GoogleSearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()

search = GoogleSearchAPIWrapper()
result = search.results("Who won won the 2023 world series?", 3)

print ("Result")
print (result)