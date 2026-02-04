#valid float input
def get_valid_float(prompt, min_value = 0):
    while True:
        user_input = input(prompt)
        try: 
            value = float(user_input)
            if value > min_value:
                return value
            else:
                print(f"Vsota mora biti vsaj {min_value}")
        except ValueError:
            print("Napaka! Vnesi Veljavno Število.")

#valid int (izbire) input
def get_valid_int(prompt, min_value = 1, max_value = None):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value < min_value:
                print(f"Izbira mora biti vsaj >{min_value}<.")
            elif max_value and value > max_value:
                print(f"Izbira nesme biti večja od >{max_value}<.")
            else:
                return value
        except ValueError:
            print("Napaka! Vnesi veljavno Število.")


if __name__ == "__main__":
    amount = get_valid_float("vnesi vsoto: ", min_value = 0.01)
    print(f"Uspešno! Vnesena vsota: {amount}")
    choice = get_valid_int("Izberi (1-6)", min_value = 1, max_value = 6)
    print(f"Izbral si: {choice}")
