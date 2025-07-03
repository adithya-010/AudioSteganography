# 🎵 Audio Steganography

A simple Python GUI app to hide and extract secret messages in WAV audio files using Least Significant Bit (LSB) steganography.

## 🚀 How to Run

### On macOS or Linux
```
python3 lsb_steganography_gui.py
```

### On Windows
```
python lsb_steganography_gui.py
```

## 💡 Features

- Hide secret text inside 16-bit WAV files
- Extract hidden messages with a single click
- Checks if the WAV file is large enough to store your message
- Easy-to-use GUI built with Tkinter
- Message hidden using LSB encoding and ends with a delimiter (`###`)

## 📦 Requirements

- Python 3.x
- Tkinter (usually included with Python)

## 🛠 Usage

1. Run the script.
2. Enter the secret message.
3. Click **"Select WAV & Encode"** to embed it in an audio file.
4. Click **"Select WAV & Decode"** to extract a message from an encoded file.

## 🔗 GitHub

https://github.com/adithya-010/AudioSteganography
