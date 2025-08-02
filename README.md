---

## 🧮 GUI Calculator using Python Tkinter

This is a **simple and interactive GUI Calculator** built using **Python's Tkinter library**. It supports basic arithmetic operations, backspace, clear entry, and evaluates expressions dynamically using the `eval()` function.

---

### 📸 Demo

<img width="699" height="959" alt="image" src="https://github.com/user-attachments/assets/f0ecc647-4027-4738-9da0-daf4c9263782" />


---

### 🚀 Features

* User-friendly graphical interface
* Supports operations: `+`, `-`, `*`, `/`, `%`
* Special keys:

  * `CE` to clear the entire input
  * `c` to remove the last digit
  * `=` to evaluate the expression
* Real-time screen update
* Custom icon support (`.ico`)

---

### 📁 Project Structure

```
calculator/
├── calc_calculator_10824.ico      # Custom window icon
├── calculator.py                  # Main source code
├── README.md                      # Project documentation
```

---

### 💻 Technologies Used

* Python 3
* Tkinter (built-in GUI library)
* PIL (Optional, if using `iconphoto` with `.png`)

---

### 🔧 How to Run

1. Make sure Python is installed on your system.

2. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

3. Run the calculator:

   ```bash
   python calculator.py
   ```

> ✅ Make sure you have the icon file (`calc_calculator_10824.ico`) in the same directory. If not, either:
>
> * Place a valid `.ico` file in the directory, or
> * Remove or comment out the line: `root.wm_iconbitmap("calc_calculator_10824.ico")`
> * Or use PNG with `iconphoto()` method (with Pillow).

---

### 🧠 What You’ll Learn

* GUI development using Tkinter
* Event-driven programming (`bind()` events)
* Layout management using `pack()` and `Frame`
* Dynamic input handling and expression evaluation

---

### 📌 To-Do / Future Improvements

* Add keyboard support
* Include scientific operations (sin, cos, log)
* Input validation and safer evaluation method (avoid using `eval()` directly)
* Dark mode / theming support

---

### 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this project and improve it.

---

### 📜 License

This project is open-source and available under the **MIT License**.

---

### 📧 Contact

**Krushna Chandra Bindhani**
📬 [krushnachandrabindhani32@gmail.com](mailto:krushnachandrabindhani32@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/krushnachandrabindhani)

---
