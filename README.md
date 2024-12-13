# AutoWhats

![Python](https://img.shields.io/badge/Python-3.12.5-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## About AutoWhats

AutoWhats is a Python application designed to send WhatsApp messages automatically with minimal effort. By simply preparing an Excel sheet with the recipient's name and phone number, users can automate bulk messaging with ease. It’s built with a combination of powerful libraries to deliver a smooth and efficient user experience.

## Features

- **Automated messaging**: Send bulk WhatsApp messages in just a few clicks.
- **Excel integration**: Easily upload a contact list in `.xlsx` format with columns `Nome` and `Telefone`.
- **Custom operator name**: Personalize your messages with an operator's name.
- **User-friendly interface**: Designed using `customtkinter` and `tkinter` for a modern and intuitive GUI.

## Installation

### Requirements

- Python 3.12^
- Required libraries:
  - `pandas`
  - `pyautogui`
  - `pyperclip`
  - `Pillow`
  - `customtkinter`
  - `tkinter`
  - `random`
  - `webbrowser`
  - `time`
  - `threading`

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nicro01/AutoWhats.git
   cd AutoWhats
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   cd src
   python main.py
   ```

## Usage

1. **Prepare an Excel sheet:**
   - Create an `.xlsx` file with two columns named exactly:
     - `Nome`
     - `Telefone`
2. **Start the application:**
   - Launch the app by running `main.py`.
3. **Upload the sheet:**

   - Use the GUI to upload your prepared Excel sheet.

4. **Optional operator name:**

   - Input an operator's name if desired for personalized messaging.

5. **Send messages:**
   - Click the "Start" button to begin sending messages automatically.

## Documentation

### 1. Dependencies

AutoWhats relies on the following Python libraries:

- **`pandas`**: For reading and handling the Excel sheet.
- **`pyautogui`**: To automate UI interactions like mouse clicks and typing.
- **`pyperclip`**: For efficient copying and pasting of text.
- **`Pillow`**: For handling image-related tasks.
- **`customtkinter` & `tkinter`**: For building the GUI.
- **`random`**: For introducing randomness if needed (e.g., delays).
- **`webbrowser`**: For launching WhatsApp Web.
- **`time`**: To manage delays between actions.
- **`threading`**: For enabling asynchronous operations.

### 2. Example Excel Sheet Format

| Nome     | Telefone     |
| -------- | ------------ |
| John Doe | +12345678901 |
| Jane Doe | +19876543210 |

Ensure the column headers are **exactly** `Nome` and `Telefone`.

### 3. GUI Features

- **File Selection**: Upload your `.xlsx` file containing contact details.
- **Operator Input**: Add an optional operator name for personalization.
- **Start Button**: Initiates the messaging process.

### 4. Error Handling

- If the Excel file has incorrect headers or missing columns, the app will prompt an error.
- Ensure all phone numbers follow the international format (e.g., `+1234567890`).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Author

Developed by Nicro01. For questions or suggestions, please contact me at [nicolasmagalhaes2003@gmail.com].
