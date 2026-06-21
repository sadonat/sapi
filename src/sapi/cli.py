import typer
from sapi import tester

app = typer.Typer()


@app.command()
def say(text: str):
    print(f"User say: {text}")

@app.command()
def test(
        name: str,
        file: str = typer.Option("sapilection.yaml", "--file", "-f")):
    tester.test(name, file) 

@app.command()
def multitest( file: str = typer.Option("sapilection.yaml", "--file", "-f")):
    tester.multi_test(file)



if __name__ == "__main__":
    app()
