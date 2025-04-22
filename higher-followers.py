import random
data = [
    {"name": "Cristiano Ronaldo", "followers": 630_000_000, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 520_000_000, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 430_000_000, "description": "Singer and Actress", "country": "USA"},
    {"name": "Kylie Jenner", "followers": 420_000_000, "description": "Reality Star and Entrepreneur", "country": "USA"},
    {"name": "Dwayne Johnson", "followers": 410_000_000, "description": "Actor and Former Wrestler", "country": "USA"},
    {"name": "Ariana Grande", "followers": 380_000_000, "description": "Singer and Actress", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 360_000_000, "description": "Reality Star and Entrepreneur", "country": "USA"},
    {"name": "Beyoncé", "followers": 320_000_000, "description": "Singer and Performer", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 310_000_000, "description": "Reality Star", "country": "USA"},
    {"name": "Justin Bieber", "followers": 290_000_000, "description": "Singer", "country": "Canada"},
    {"name": "Taylor Swift", "followers": 280_000_000, "description": "Singer and Songwriter", "country": "USA"},
    {"name": "Kendall Jenner", "followers": 290_000_000, "description": "Model and TV Personality", "country": "USA"},
    {"name": "Neymar Jr", "followers": 220_000_000, "description": "Footballer", "country": "Brazil"},
    {"name": "Virat Kohli", "followers": 265_000_000, "description": "Cricketer", "country": "India"},
    {"name": "Zendaya", "followers": 185_000_000, "description": "Actress and Singer", "country": "USA"},
    {"name": "Kourtney Kardashian", "followers": 220_000_000, "description": "Reality Star", "country": "USA"},
    {"name": "Billie Eilish", "followers": 110_000_000, "description": "Singer and Songwriter", "country": "USA"},
    {"name": "Shakira", "followers": 150_000_000, "description": "Singer", "country": "Colombia"},
    {"name": "Chris Hemsworth", "followers": 100_000_000, "description": "Actor", "country": "Australia"},
    {"name": "Emma Watson", "followers": 75_000_000, "description": "Actress and Activist", "country": "UK"},
]

score = 0
lost = True
print()
while lost is True:
  a = random.randint(0, 19)
  b = random.randint(0, 19)

  while b == a:
      b = random.randint(0, 19)

  print(f"Compare A: {data[a]['name']} a {data[a]['description']}, from {data[a]['country']}.")
  print()
  print()
  print(f"Compare B: {data[b]['name']} a {data[b]['description']}, from {data[b]['country']}.")
  print()

  choice = input("Who has more followers: 'A' or 'B': ").upper()
  print()

  if choice == 'A' and data[a]['followers']>data[b]['followers']:
    score +=1
    print(f"You're right! Current score: {score}")
    print()
  elif choice == 'B' and data[a]['followers']>data[b]['followers']:
     print(f"Sorry, that's wrong. Final score: {score}")
     print()
     lost = False
  elif choice == 'A' and data[b]['followers']>data[a]['followers']:
     print(f"Sorry, that's wrong. Final score: {score}")
     print()
     lost = False
  elif choice == 'B' and data[b]['followers']>data[a]['followers']:
    score +=1
    print(f"You're right! Current score: {score}")
    print()
  else:
     print(f"Sorry didn't get that, Current score: {score}")  
     print()