url = lambda amount : f"https://poetrydb.org/random/{amount}/lines,title"

user_amount = int(input("How many poems to train on? "))

import requests

data = requests.get(url(user_amount)).json()

import pandas as pd

df = pd.DataFrame({
    "prompt": [poem["title"] for poem in data],
    "completion": ["\n".join(poem["lines"]) for poem in data]
})

with open("output.csv", "w", newline="") as f:
    df.to_csv(f, index=False)

print("Finished")
