import os

def load():
    data = []
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    desc, amt = parts
                    data.append((desc, float(amt)))
    return data

def save(desc, amt):
    with open("expenses.txt", "a") as f:
        f.write(f"{desc}|{amt}\n")

def show(data):
    print("\nYour expenses:")
    total = 0
    for d, a in data:
        print(f"{d} - ₹{a}")
        total += a
    print(f"Total: ₹{total}\n")

def main():
    expenses = load()
    while True:
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("What is it for? ")
            amt = input("How much? ₹")
            try:
                amt = float(amt)
                save(desc, amt)
                expenses.append((desc, amt))
                print("Added!\n")
            except:
                print("Please enter a valid amount.\n")
        
        elif choice == "2":
            show(expenses)
        
        elif choice == "3":
            print("Bye!")
            break
        
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
