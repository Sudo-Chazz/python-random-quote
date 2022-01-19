import secrets
import sys

def primary():
 
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


# ask the user how many quotes they want printed
# also make sure the user provides an int within range
  try:
    num_q = int(input("Enter the number of quotes you want: "))
    if num_q > len(quotes):
      raise Exception()
  except:
    print(f"please only provide integers less than {len(quotes) + 1}")
    sys.exit()
    
  
  for num in range(num_q):
    # random int for randomness
    rnd = secrets.randbelow(len(quotes))
    # remove newline character
    quote = quotes[rnd].rstrip("\n")
    # add quotes to quote
    print(f"\"{quote}\"")


if __name__== "__main__":
  primary()
