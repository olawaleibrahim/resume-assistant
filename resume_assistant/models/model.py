from langchain_google_vertexai import ChatVertexAI


def get_model(model_name="gemini-1.5-flash"):
    return ChatVertexAI(model_name=model_name)