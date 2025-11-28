import typer

def main(name: str = "World"):
    print(f"Hello {name} from advent-of-code-2025!")

if __name__ == "__main__":
    typer.run(main)
