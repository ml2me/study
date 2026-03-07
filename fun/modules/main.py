import utils

def main():
    name = input("Как тебя зовут? ")
    print(utils.say_hello(name))

    year = int(input("В каком году ты родился? "))
    age = utils.calculate_age(year)
    print(f"Тебе примерно {age} лет.")

main()
