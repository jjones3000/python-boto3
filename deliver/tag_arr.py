

tag = 'bullshit'

tag_arr = [{'Key': 'fucking', 'Value': 'Bullshit'}, {'Key': 'name', 'Value': 'test account eip'}, {'Key': 'motherfucking', 'Value': 'bullshit'}]

for ctag in tag_arr:
  print(tag)
  print(ctag)
  if(tag in ctag['Value']):
    print("found")
  else:
    print("not found")
"""
if tag in tag_arr[0]:
  print("well maybe it is not a total pile of shit")

else:
  print("like i said before")
"""