from pathlib import Path
import subprocess


NOTEBOOK_DIR = Path("notebooks")


def main():

    notebooks = list(
        NOTEBOOK_DIR.rglob("*.ipynb")
    )

    for notebook in notebooks:

        print(
            f"Running {notebook}"
        )

        subprocess.run(
            [
                "poetry",
                "run",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                str(notebook),
            ],
            check=True,
        )


if __name__ == "__main__":
    main()