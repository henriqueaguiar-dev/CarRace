import sys

try:
    from code.Game import Game
except ModuleNotFoundError as exc:
    if exc.name == "pygame":
        sys.stderr.write(
            "Missing dependency: pygame.\n"
            "Install requirements with:\n"
            "  python -m pip install -r requirements.txt\n"
        )
        raise SystemExit(1) from exc
    raise


if __name__ == "__main__":
    game = Game()
    game.run()
