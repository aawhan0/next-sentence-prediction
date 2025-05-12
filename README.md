# Next Sentence Prediction using Generative AI

## Project Overview

The **Next Sentence Prediction using Generative AI** project aims to build a system that predicts the next sentence based on a user-provided input. It leverages transformer-based models, specifically GPT-2, to generate coherent and contextually appropriate next sentences. The system is integrated with a user-friendly **Streamlit** interface for real-time interaction, making it suitable for applications in chatbots, content generation, smart editors, and summarization tools.

### Key Features:
- Accepts a user-provided sentence or paragraph.
- Generates one or more contextually relevant next sentences using GPT-2.
- Filters and ranks suggestions based on coherence and fluency.
- Easy-to-use web interface built with Streamlit.

---

## Setup and Installation Instructions

Follow the steps below to set up the project locally.

### Prerequisites

- **Python 3.7 or higher** is required to run the project.
- Install the dependencies listed in the `requirements.txt` file.

### Steps:

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/aawhan0/next-sentence-prediction>
   cd next-sentence-prediction



python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt


streamlit run app.py

https://next-sentence-prediction-n6dzwnvdpd8rphgglm4h9v.streamlit.app/
