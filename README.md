# Medical Diagnostic Assistant

## Overview

The Medical Diagnostic Assistant is a lightweight Streamlit application that accepts medical images and produces AI-assisted, structured analyses using a hosted large language model. The application is designed for experimentation, research, and informational use only; it is not a medical device and does not provide definitive clinical diagnoses. Users must consult qualified healthcare professionals for clinical interpretation and decision-making.

## Key Features

- Web-based image upload UI supporting common image formats (jpg, jpeg, png, bmp, tiff).
- Client-side image encoding to data URLs and server-side forwarding to a generative model (via OpenRouter/OpenAI API) for analysis.
- Structured system prompt to ensure the model communicates uncertainty, limitations, and recommendations to consult clinicians.
- Basic runtime checks for required configuration (API key) and graceful handling of empty or failed model responses.
- Simple, local-first deployment with `streamlit run main.py` for rapid testing.

## Architecture Overview

- Frontend: Streamlit application providing the user interface and image upload capability.
- Model Integration: Uses the OpenAI client configured to call OpenRouter endpoints for chat/completion requests.
- Image Handling: Uploaded images are encoded into base64 data URLs and embedded in the model prompt.
- Configuration: Runtime configuration is provided via environment variables (loaded with `python-dotenv`).

## Tools & Technologies

- Python (recommended 3.12)
- Streamlit
- OpenAI Python client (used for OpenRouter-compatible API calls)
- python-dotenv
- Standard Python libraries: `base64`, `os`
- See `requirements.txt` for the full dependency list and exact versions.

## How to Run This Project

### Prerequisites

- Python 3.10+ (3.12 recommended)
- Git (optional, for cloning)
- An OpenRouter/OpenAI-compatible API key

### Setup

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install project dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the repository root and add your API key:

```text
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### Run Locally

Start the Streamlit application:

```bash
streamlit run main.py
```

Open the URL printed by Streamlit in your browser (typically `http://localhost:8501`). Upload an image and click "Generate image analysis" to receive the model's structured response.

### Notes for Deployment

- When deploying, ensure environment variables are set securely through your hosting provider (do not commit `.env` to source control).
- Review provider terms and data processing agreements before sending medical content to external services.

---


