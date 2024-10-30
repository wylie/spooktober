import random
while True:
    t_or_t = input("🎃 Trick or Treat? ").lower()
    if t_or_t == "trick":
        print("👻 B", end="")
        print("".join(random.choice(["O", "o"]) for _ in range(100)))
        break
    elif t_or_t == "treat":
        print("🍫 Happy Halloween! Have some candy 🍫")
        break
    else:
        print("💀 Hey, that's not an option!")
        continue