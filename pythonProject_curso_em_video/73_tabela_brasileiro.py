time = ("flamengo", "juventude", "vasco", "palmeiras",
        "chapecoense", "atletico mg", "fluminense", "botafogo", "gremio", "corintians",
        "inter", "sao paulo")
print("=-"*15)
print(f"lista de times {time}")
print("=-"*15)
print(f"os 5 primeiros {time[:5]}")
print("=-"*15)
print(f"os 4 ultimos {time[-4:]}")
print("=-"*15)
print(f"times em ordem alfabetica {sorted(time)}")
print("=-"*15)
print(f"A chape esta em {time.index('chapecoense')+1} posição")