import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class MusicLLM:
    def __init__(self, temperature=0.7):
        use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
        
        if use_ollama:
            self.llm = ChatOllama(
                temperature=temperature,
                model="qwen3-vl:30b-a3b-instruct"  
            )
        else:
            self.llm = ChatGroq(
                temperature=temperature,
                groq_api_key=os.getenv("GROQ_API_KEY"),
                model_name="llama-3.3-70b-versatile"
            )

    def generate_melody(self, user_input):
        prompt = ChatPromptTemplate.from_template(
            """
            Generate a melody based on the user's input: {input}.
            Represent it as a space seperated notes (e.g., C4 D4 E4 F4 G4 A4 B4 C5).
            """
        )
        chain = prompt | self.llm
        return chain.invoke({"input": user_input}).content.strip()
    
    def generate_harmony(self, melody):
        prompt = ChatPromptTemplate.from_template(
            """
            Create harmony chords for the following melody: {melody}.
            Represent it as  (e.g., C4-D4-E4 F4-G4-A4).
            """
        )
        chain = prompt | self.llm
        return chain.invoke({"melody": melody}).content.strip()
    
    def generate_rhythm(self, melody):
        prompt = ChatPromptTemplate.from_template(
            """
            Suggest a rhythmic duration (in beats) for this melody: {melody}.
            Represent it as  (e.g., 0.5 1.0 0.5 2.0).
            """
        )
        chain = prompt | self.llm
        return chain.invoke({"melody": melody}).content.strip()

    def adapt_style(self, style, melody, harmony, rhythm):
        prompt = ChatPromptTemplate.from_template(
            """
            Adapt to {style} style : \n Melody: {melody} \n Harmony: {harmony} \n Rhythm: {rhythm}
            Output as single string summary.
            """
        )
        chain = prompt | self.llm
        return chain.invoke({"style": style, "melody": melody, "harmony": harmony, "rhythm": rhythm}).content.strip()
        
