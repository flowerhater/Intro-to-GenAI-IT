from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

from bot.prompts import translation_prompt
from bot.config import OPENAI_API_KEY


class ContextTranslator:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0.2
        )

        self.memory = ConversationBufferMemory(
            memory_key="history",
            return_messages=True
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=translation_prompt,
            memory=self.memory,
            verbose=True
        )

    def translate(self, text: str) -> str:
        if not text.strip():
            return "⚠️ Empty message"

        try:
            return self.chain.run(input=text)
        except Exception as e:
            return f"❌ Ошибка перевода: {str(e)}"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']