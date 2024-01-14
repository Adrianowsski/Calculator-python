def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y == 0:
        return "Dzielenie przez zero!"
    return x / y

print("Prosty Kalkulator")
print("Wpisz odpowiednią operację, którą chcesz wykonać:")
print("+ dla dodawania")
print("- dla odejmowania")
print("* dla mnożenia")
print("/ dla dzielenia")

while True:
    # Pobranie od użytkownika wyboru operacji
    operacja = input("Wybierz operację (+, -, *, /): ")

    # Sprawdzenie, czy wybór jest jednym z dozwolonych operatorów
    if operacja in ('+', '-', '*', '/'):
        num1 = float(input("Wpisz pierwszą liczbę: "))
        num2 = float(input("Wpisz drugą liczbę: "))

        if operacja == '+':
            print(num1, "+", num2, "=", dodawanie(num1, num2))

        elif operacja == '-':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))

        elif operacja == '*':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif operacja == '/':
            wynik = dzielenie(num1, num2)
            print(num1, "/", num2, "=", wynik)

        # Opcja wyjścia z pętli
        next_calculation = input("Czy chcesz wykonać nową operację? (tak/nie): ")
        if next_calculation.lower() != 'tak':
            break
    else:
        print("Nieprawidłowy wybór")
