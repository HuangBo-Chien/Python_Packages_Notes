import typer

app = typer.Typer()

@app.command()
def Hello(name: str = typer.Option(help = 'To whom I will say hello')):
    print(f"Hello {name}!!")

if __name__ == "__main__":
    app()