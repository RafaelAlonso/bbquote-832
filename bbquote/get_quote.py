import requests

def get_quote():
  query = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
  
  response = requests.get(query).json()
  
  return f"{response[0]['quote']} - {response[0]['author']}"

if __name__ == "__main__":
  print(get_quote())