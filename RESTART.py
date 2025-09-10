import tkinter as tk

def replay(canvas, window, score, restart_callback):
    # Delete score text
    canvas.delete("score")

    # Show "Game Over" message
    label2 = canvas.create_text(
        350, 250,
        text=f"YOUR SCORE: {score}",
        font=("Times New Roman", 30),
        fill='#088F8F'
    )

    # Replay button (normal Tk widget)
    button_replay = tk.Button(
        window,
        text="REPLAY?",
        font=("Arial", 25),
        fg="black",
        bg="white",
        command=lambda: restart_callback(label2, button_replay)   # <-- pass self
    )
    button_replay.place(relx=0.4, rely=0.7)

    return label2, button_replay
