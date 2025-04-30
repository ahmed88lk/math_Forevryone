# AL-KHWARIZMI

**AL-KHWARIZMI** is a Python application that generates and visualizes math animations from natural language concepts, powered by Google Gemini and ManimGL.

---

## 🚀 Features

- **Automatic ManimGL code generation** from a simple math description.
- **Instant visualization** of math concepts as animations.
- **No programming knowledge required** for the end user.
- **Simple interface** (Streamlit or CLI).
- **Supports most ManimGL objects** (Text, Graphs, Shapes, etc.).
- **No LaTeX dependency** for simple text (uses `Text()` only).

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- [ManimGL (manimlib)](https://github.com/3b1b/manim)
- [Streamlit](https://streamlit.io/)
- [Google Gemini Python SDK](https://ai.google.dev/)
- FFmpeg (for video encoding)
- (Optional) LaTeX (for some advanced use cases, but not required here)

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/your-username/AL-KHWARIZMI.git
cd AL-KHWARIZMI

# Install Python dependencies
pip install -r requirements.txt

# Install ManimGL
pip install manimgl

# (Optional) Install LaTeX if needed
# For Windows: https://miktex.org/download
# For Mac: brew install mactex
```

---

## 💡 Usage

### Launch the Streamlit App

```bash
streamlit run app.py
```

- Enter a math concept (e.g. `The derivative of a function`)
- Click "Generate"
- The animation will automatically appear in a ManimGL window

### Command Line Usage

```python
from utils.manim_utils import generate_and_render_manim_video
generate_and_render_manim_video("Your math concept")
```

---

## 🤖 How It Works

1. **The user enters a math concept**
2. **Gemini** generates a ManimGL-compatible Python script
3. The script is automatically executed with **manimgl**
4. The animation is displayed locally (no manual video conversion needed)

---

## 📦 Project Structure

```
AL-KHWARIZMI/
│
├── app.py                # Main Streamlit interface
├── utils/
│   ├── gemini_utils.py   # Code generation via Gemini
│   └── manim_utils.py    # Execution and management of ManimGL scripts
├── requirements.txt
├── README.md
└── ...
```

---

## 📝 Example Inputs

- `Visualize the Riemann sum`
- `Show the parabola y = x^2`
- `Explain the concept of a derivative`
- `Display a circle and its radius`

---

## ❗ Tips & Limitations

- **Do not use LaTeX formulas** in your concepts; the system uses `Text()` to avoid LaTeX-related errors.
- **Only ManimGL classes and methods are supported** (not Manim Community).
- If you see an error, check that your concept is well-phrased and simple.

---

## 🧑‍💻 Contributing

Contributions are welcome!  
Open an issue or pull request to suggest improvements, fix bugs, or add examples.

---

## 📄 License

MIT

---

## 🙏 Credits

- [3Blue1Brown](https://www.3blue1brown.com/) for ManimGL
- [Google Gemini](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)