import wave
import tkinter as tk
from tkinter import filedialog, messagebox

def encode_audio(filepath, message):
    try:
        # Read audio frames
        song = wave.open(filepath, mode='rb')
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
        song_params = song.getparams()
        song.close()

        # Append delimiter and convert message to bits
        message += '###'
        message_bits = ''.join(format(ord(c), '08b') for c in message)

        if len(message_bits) > len(frame_bytes):
            messagebox.showerror("Error", "WAV file is too small to hold the message.")
            return

        # Modify LSBs
        for i in range(len(message_bits)):
            frame_bytes[i] = (frame_bytes[i] & 254) | int(message_bits[i])

        # Save encoded WAV
        output_path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")],
            title="Save Encoded WAV"
        )
        if output_path:
            with wave.open(output_path, 'wb') as encoded:
                encoded.setparams(song_params)
                encoded.writeframes(bytes(frame_bytes))
            messagebox.showinfo("Success", f"Message encoded and saved to:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def decode_audio(filepath):
    try:
        song = wave.open(filepath, mode='rb')
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
        song.close()

        bits = [str(byte & 1) for byte in frame_bytes]
        binary_str = ''.join(bits)

        decoded = ''
        for i in range(0, len(binary_str), 8):
            byte = binary_str[i:i+8]
            char = chr(int(byte, 2))
            decoded += char
            if decoded.endswith('###'):
                break

        if '###' in decoded:
            messagebox.showinfo("Decoded Message", decoded[:-3])
        else:
            messagebox.showerror("Error", "No hidden message found or file is not encoded.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def select_file_and_encode():
    filepath = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Select WAV File to Encode"
    )
    if filepath:
        msg = text_input.get("1.0", "end").strip()
        if msg:
            encode_audio(filepath, msg)
        else:
            messagebox.showerror("Error", "Please enter a message to encode.")


def select_file_and_decode():
    filepath = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Select Encoded WAV File"
    )
    if filepath:
        decode_audio(filepath)


# -------- GUI Setup --------
window = tk.Tk()
window.title("🎵 Audio Steganography (LSB)")
window.geometry("550x300")

# Force the entire window to white
window.configure(bg="#ffffff")

label = tk.Label(
    window,
    text="Enter secret message to hide:",
    font=("Helvetica", 12),
    bg="#ffffff",
    fg="#000000"
)
label.pack(pady=10)

# Strongly enforce colors and borders
text_input = tk.Text(
    window,
    height=5,
    width=60,
    bg="#ffffff",             # White background
    fg="#000000",             # Black text
    insertbackground="#000000",  # Black blinking cursor
    relief="solid",
    bd=2,
    font=("Helvetica", 12),
    highlightbackground="#000000", # Border color when unfocused
    highlightcolor="#000000",      # Border color when focused
    highlightthickness=1,
    selectbackground="#cceeff",    # Light blue selection
    selectforeground="#000000"
)
text_input.pack(pady=5)

encode_btn = tk.Button(
    window,
    text="🔐 Select WAV & Encode",
    command=select_file_and_encode,
    bg="#4CAF50",
    fg="white",
    height=2,
    width=30,
    activebackground="#45a049"
)
encode_btn.pack(pady=10)

decode_btn = tk.Button(
    window,
    text="🔓 Select WAV & Decode",
    command=select_file_and_decode,
    bg="#2196F3",
    fg="white",
    height=2,
    width=30,
    activebackground="#1e88e5"
)
decode_btn.pack()

window.mainloop()