# 🧠 AutoAnnotate AI

AI-powered Human-in-the-Loop Data Annotation Platform built with Streamlit and Hugging Face Inference API.

AutoAnnotate AI allows users to upload raw datasets (JSON, TXT, PDF) and automatically classify text using zero-shot learning, with confidence scoring and entropy-based uncertainty detection.

---

## 🚀 Features

- 📂 Upload JSON, TXT, or PDF files
- 🤖 Zero-shot text classification
- 🎯 Custom candidate labels
- 📊 Confidence score calculation
- 📉 Entropy-based uncertainty detection
- 🔍 Low-confidence filtering (Human-in-the-Loop workflow)
- ✏️ Editable annotation table
- 📥 Download annotated JSON output

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- Hugging Face Inference API (Router Endpoint)
- Pandas
- Requests

---

## 📦 Project Structure

```
autoannotate/
│
├── app.py
├── requirements.txt
│
└── services/
    ├── __init__.py
    ├── hf_api.py
    ├── annotator.py
    └── file_parser.py
```

---

# 🔧 Installation & Setup (One-Time Setup)

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/autoannotate-ai.git
cd autoannotate-ai
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Add Hugging Face API Token (Professional Method)

## Step 1: Create Token

Go to:

👉 https://huggingface.co/settings/tokens

- Click **New Token**
- Name it: `autoannotate`
- Select Role: **Read**
- Click **Generate**
- Copy the token (starts with `hf_`)

---

## Step 2: Set Environment Variable

### Windows (PowerShell)

```powershell
setx HF_API_TOKEN "hf_your_token_here"
```

Close terminal and open it again.

---

### Mac/Linux

```bash
export HF_API_TOKEN="hf_your_token_here"
```

---

## Step 3: Run the App

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

# 🧠 How It Works

1. User uploads dataset
2. Text is extracted and parsed
3. Hugging Face Zero-Shot Model:
   - `typeform/distilbert-base-uncased-mnli`
4. Model returns ranked labels with confidence scores
5. Entropy is calculated for uncertainty measurement
6. Low-confidence samples are flagged for human review

---

# 📊 Example Output

| id | text | label | confidence | entropy | needs_review |
|----|------|-------|------------|----------|--------------|
| 0 | AI is transforming healthcare | Healthcare | 0.87 | 0.34 | False |
| 1 | Stock market crashed | Finance | 0.51 | 1.12 | True |

---

# 🔬 Core Concepts Implemented

- Zero-Shot Learning
- Entropy-Based Uncertainty Estimation
- Human-in-the-Loop Annotation Workflow
- API Integration with Authentication
- Interactive Streamlit UI
- Production-Level Error Handling

---

# 🧩 Future Improvements

- Async API calls for faster processing
- Batch inference optimization
- Model selection dropdown
- Database integration
- Active learning loop
- Streamlit Cloud deployment

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Built with ❤️ using Streamlit and Hugging Face.
