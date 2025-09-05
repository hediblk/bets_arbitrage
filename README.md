# Sports Betting Arbitrage Calculator

This is a simple tkinter app to help you find and calculate sports betting arbitrage opportunities between two bookmakers given a set of odds and a total stake.

## How to build

To build a standalone executable (macOS, requires Python 3):

```sh
pip install pyinstaller
./build.sh
```

The built app will be in the `dist/` folder. Or simply run the app with:

```sh
python3 gui.py
```

## Next steps
- Handle 3 or more outcomes (e.g., football matches with win/draw/lose outcomes).
- Compute least possible loss even when no arbitrage exists.
