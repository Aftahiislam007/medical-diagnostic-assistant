# import os
# import base64

# import streamlit as st
# from dotenv import load_dotenv
# from openai import OpenAI


# # -------------------- Configuration --------------------
# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# if not OPENROUTER_API_KEY:
#     st.error("OPENROUTER_API_KEY is not configured.")
#     st.info("Please add OPENROUTER_API_KEY to your .env file.")
#     st.stop()

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY,
# )

# st.write("Upload a medical image to receive an AI-assisted analysis.")


# # -------------------- System Prompt --------------------
# system_prompt = """
# You are an advanced AI medical diagnostic assistant.

# Your role is to analyze the information provided by the user and
# provide a careful, structured response.

# Important:
# - Do not claim to provide a definitive medical diagnosis.
# - Clearly explain uncertainty and limitations.
# - Identify potentially important findings.
# - Recommend consulting a qualified healthcare professional.
# - If the information is insufficient, say so clearly.
# """

# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mine_type": "text/plain",
# }

# # safety settings
# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARRASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
# ]

# # -------------------- Page Config --------------------
# st.set_page_config(
#     page_title="Medical Diagnostic Assistant",
#     page_icon="🩺",
#     layout="wide",
# )

# # -------------------- Header --------------------
# col1, col2, col3 = st.columns([1, 2, 1])

# with col2:
#     st.image("assistant.jpeg", width=400)
#     st.image("medass.jpeg", width=400)

# # -------------------- Image Upload --------------------
# uploaded_file = st.file_uploader(
#     "Please upload a medical image for analysis",
#     type=["jpg", "jpeg", "png", "bmp", "tiff"],
# )

# submit_button = st.button(
#     "Generate image analysis",
#     type="primary",
# )

# if submit_button:
#     # process the uploaded image
#     image_data = uploaded_file.getvalue()

#     # making our image ready
#     image_parts = [
#         {
#             "mime_type": "image/jpeg",
#             "data": image_data
#         },
#     ]

#     # making our prompt ready
#     prompt_parts = [
#         image_parts[0],
#         system_prompt,
#     ]

#     # generate a response based on prompt and image 
#     reponse = model.generate_content(prompt_parts)
#     print(reponse.text)

#     st.write(reponse.text)


# # # -------------------- Generate Analysis --------------------
# # if submit_button:

# #     if uploaded_file is None:
# #         st.warning(
# #             "Please upload a medical image before generating the analysis."
# #         )
# #         st.stop()

# #     # Convert image to base64
# #     image_data = base64.b64encode(
# #         uploaded_file.read()
# #     ).decode("utf-8")

# #     mime_type = uploaded_file.type

# #     # Text + image content
# #     user_content = [
# #         {
# #             "type": "text",
# #             "text": "Please analyze this medical image.",
# #         },
# #         {
# #             "type": "image_url",
# #             "image_url": {
# #                 "url": f"data:{mime_type};base64,{image_data}"
# #             },
# #         },
# #     ]

# #     messages = [
# #         {
# #             "role": "system",
# #             "content": SYSTEM_PROMPT,
# #         },
# #         {
# #             "role": "user",
# #             "content": user_content,
# #         },
# #     ]

# #     try:
# #         with st.spinner("Analyzing image..."):

# #             response = client.chat.completions.create(
# #                 model="openai/gpt-4o",
# #                 messages=messages,
# #                 temperature=0.7,
# #                 max_tokens=2048,
# #             )

# #         analysis = response.choices[0].message.content

# #         if analysis:
# #             st.write(analysis)
# #         else:
# #             st.warning("The model returned an empty response.")

# #     except Exception as e:
# #         st.error(f"An error occurred: {e}")


import os
import base64

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# -------------------- Configuration --------------------
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    st.error("OPENROUTER_API_KEY is not configured.")
    st.info("Please add OPENROUTER_API_KEY to your .env file.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

st.write("Upload a medical image to receive an AI-assisted analysis.")


# -------------------- System Prompt --------------------
SYSTEM_PROMPT = """
You are an advanced AI medical diagnostic assistant.

Your role is to analyze the information provided by the user and
provide a careful, structured response.

Important:
- Do not claim to provide a definitive medical diagnosis.
- Clearly explain uncertainty and limitations.
- Identify potentially important findings.
- Recommend consulting a qualified healthcare professional.
- If the information is insufficient, say so clearly.
"""

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Medical Diagnostic Assistant",
    page_icon="🩺",
    layout="wide",
)

# -------------------- Header --------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assistant.jpeg", width=400)
    st.image("medass.jpeg", width=400)

# -------------------- Image Upload --------------------
uploaded_file = st.file_uploader(
    "Please upload a medical image for analysis",
    type=["jpg", "jpeg", "png", "bmp", "tiff"],
)

submit_button = st.button(
    "Generate image analysis",
    type="primary",
)

# -------------------- Generate Analysis --------------------
if submit_button:

    if uploaded_file is None:
        st.warning(
            "Please upload a medical image before generating the analysis."
        )
        st.stop()

    # Convert image to base64
    image_data = base64.b64encode(
        uploaded_file.read()
    ).decode("utf-8")

    mime_type = uploaded_file.type

    # Text + image content
    user_content = [
        {
            "type": "text",
            "text": "Please analyze this medical image.",
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:{mime_type};base64,{image_data}"
            },
        },
    ]

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": user_content,
        },
    ]

    try:
        with st.spinner("Analyzing image..."):

            response = client.chat.completions.create(
                model="openai/gpt-4o",
                messages=messages,
                temperature=0.7,
                max_tokens=2048,
            )

        analysis = response.choices[0].message.content

        if analysis:
            st.write(analysis)
        else:
            st.warning("The model returned an empty response.")

    except Exception as e:
        st.error(f"An error occurred: {e}")