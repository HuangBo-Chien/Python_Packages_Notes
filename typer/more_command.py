import typer

app = typer.Typer()

@app.command()
def add(number_1:str, number_2:str):
    if any((not number_1.isnumeric(), not number_2.isnumeric())):
        raise TypeError("Please check if both inputs are numeric.")
    convert_number = []
    for number in (number_1, number_2):
        if number.isdigit():
            convert_number.append(int(number))
        else:
            convert_number.append(float(number))
    print(convert_number[0] + convert_number[1])

@app.command()
def mod(number_1:str, number_2:str):
    if any((not number_1.isnumeric(), not number_2.isnumeric())):
        raise TypeError("Please check if both inputs are numeric.")
    convert_number = []
    for number in (number_1, number_2):
        if number.isdigit():
            convert_number.append(int(number))
        else:
            convert_number.append(float(number))
    
    print(convert_number[0] % convert_number[1])

@app.command()
def minus(number_1:str, number_2:str):
    if any((not number_1.isnumeric(), not number_2.isnumeric())):
        raise TypeError("Please check if both inputs are numeric.")
    convert_number = []
    for number in (number_1, number_2):
        if number.isdigit():
            convert_number.append(int(number))
        else:
            convert_number.append(float(number))
    
    print(convert_number[0] - convert_number[1])

@app.command()
def multiply(number_1:str, number_2:str):
    if any((not number_1.isnumeric(), not number_2.isnumeric())):
        raise TypeError("Please check if both inputs are numeric.")
    convert_number = []
    for number in (number_1, number_2):
        if number.isdigit():
            convert_number.append(int(number))
        else:
            convert_number.append(float(number))
    
    print(convert_number[0] * convert_number[1])

@app.command()
def divide(number_1:str, number_2:str):
    if any((not number_1.isnumeric(), not number_2.isnumeric())):
        raise TypeError("Please check if both inputs are numeric.")
    convert_number = []
    for number in (number_1, number_2):
        if number.isdigit():
            convert_number.append(int(number))
        else:
            convert_number.append(float(number))
    
    print(convert_number[0] / convert_number[1])

if __name__ == "__main__":
    app()

