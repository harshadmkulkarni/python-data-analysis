import pandas as pd

#List of US States
states =['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
'Oregon','Pennsylvania', 'Rhode Island','South Carolina','South Dakota',
'Tennessee','Texas','Utah','Vermont','Virginia','Washington',
'West Virginia','Wisconsin','Wyoming']

#create string with value UNITED STATES OF AMERICA
country = "UNITED STATES OF AMERICA"

#create new Dictionary
usa = {'Country':country, 'State':states}

#create DataFrame from the Dictionary
df = pd.DataFrame(usa)

#display all 50 states in US within DataFrame
print(df)
