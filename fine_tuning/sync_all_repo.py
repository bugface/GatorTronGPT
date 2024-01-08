from pathlib import Path
from subprocess import run


def run_git_update(p):
    _path = p.as_posix()
    print(f"cd {_path}; git pull")
    run(f"cd {_path}; git pull", shell=True)


if __name__ == "__main__":
    p = Path(__file__).parent

    for d in p.glob("*"):
        if d.is_dir():
            run_git_update(d)
