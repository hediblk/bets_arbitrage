import tkinter as tk
from tkinter import ttk
from arb import is_arbitrage, arbitrage_stakes


def check_arb():
    """Validate inputs, compute arbitrage result, and display inline."""
    # Reset styling
    result_label.configure(foreground="#222")
    try:
        odds_a = float(entry_odds_a.get().strip())
        odds_b = float(entry_odds_b.get().strip())
        max_bet = float(entry_max_bet.get().strip())
    except ValueError:
        result_var.set("Please enter valid numeric values.")
        result_label.configure(foreground="#b00020")
        return

    if odds_a <= 1 or odds_b <= 1:
        result_var.set("Odds must be greater than 1.00 (decimal format).")
        result_label.configure(foreground="#b00020")
        return
    if max_bet <= 0:
        result_var.set("Max bet must be positive.")
        result_label.configure(foreground="#b00020")
        return

    if is_arbitrage(odds_a, odds_b):
        stake_a, stake_b = arbitrage_stakes(odds_a, odds_b, max_bet)
        total_return = stake_a * odds_a  # should equal stake_b * odds_b
        profit = total_return - max_bet
        result_var.set(
            f"Arbitrage found:\nStake A: ${stake_a:.2f} @ {odds_a:.2f}\n"
            f"Stake B: ${stake_b:.2f} @ {odds_b:.2f}\nGuaranteed Profit: ${profit:.2f}"
        )
        result_label.configure(foreground="#0a6b18")
    else:
        result_var.set("No arbitrage opportunity.")
        result_label.configure(foreground="#b00020")


def clear_fields():
    entry_odds_a.delete(0, tk.END)
    entry_odds_b.delete(0, tk.END)
    entry_max_bet.delete(0, tk.END)
    result_var.set("")
    result_label.configure(foreground="#444")
    entry_odds_a.focus()


# --- GUI Setup ---
root = tk.Tk()
root.title("Arbitrage Calculator")
root.resizable(False, False)

try:
    # Use a nicer built-in theme if available
    style = ttk.Style()
    for theme in ("clam", "alt", "default", "classic"):
        if theme in style.theme_names():
            style.theme_use(theme)
            break
except Exception:
    pass

main = ttk.Frame(root, padding=16)
main.grid(sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

lbl_title = ttk.Label(main, text="Sports Betting Arbitrage",
                      font=("Helvetica", 14, "bold"))
lbl_title.grid(row=0, column=0, columnspan=3, pady=(0, 12))

ttk.Label(main, text="Odds Team A").grid(
    row=1, column=0, sticky="e", pady=4, padx=(0, 6))
entry_odds_a = ttk.Entry(main, width=14)
entry_odds_a.grid(row=1, column=1, sticky="w", pady=4)

ttk.Label(main, text="Odds Team B").grid(
    row=2, column=0, sticky="e", pady=4, padx=(0, 6))
entry_odds_b = ttk.Entry(main, width=14)
entry_odds_b.grid(row=2, column=1, sticky="w", pady=4)

ttk.Label(main, text="Max Bankroll ($)").grid(
    row=3, column=0, sticky="e", pady=4, padx=(0, 6))
entry_max_bet = ttk.Entry(main, width=14)
entry_max_bet.grid(row=3, column=1, sticky="w", pady=4)

btn_frame = ttk.Frame(main)
btn_frame.grid(row=4, column=0, columnspan=3, pady=(10, 6))

calc_btn = ttk.Button(btn_frame, text="Calculate", command=check_arb)
calc_btn.grid(row=0, column=0, padx=4)

clear_btn = ttk.Button(btn_frame, text="Clear", command=clear_fields)
clear_btn.grid(row=0, column=1, padx=4)

result_var = tk.StringVar(value="")
result_label = ttk.Label(main, textvariable=result_var,
                         justify="left", anchor="w")
result_label.grid(row=5, column=0, columnspan=3, sticky="we", pady=(8, 0))

for i in range(3):
    main.columnconfigure(i, weight=1)

entry_odds_a.focus()

# Bind Enter key to compute
root.bind('<Return>', lambda _evt: check_arb())

root.mainloop()
