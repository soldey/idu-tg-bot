from iduconfig import Config


class LlmService:
    def __init__(self, config: Config):
        self.url = f"http://{config.get('LLM_HOST')}:{config.get('LLM_PORT')}"
        self.model_name = config.get('LLM_MODEL')

    async def generate_request_data(self, message: str, context: str) -> tuple[dict, dict]:
        data = {
            "model": self.model_name,
            "prompt": f"НАЧАЛО ВОПРОСА | {message} | КОНЕЦ ВОПРОСА",
            "stream": True,
            "system": "Ты отвечаешь на вопросы по документу \"Региональные нормативы градостроительного проектирования Ленинградской области\" (или РНГП)"
                      "инструкция: Ответь на вопрос на основе документа."
                      "Если он не подходит, скажи об этом. Если в тексте не было вопроса или просьбы, попроси уточнить запрос."
                      "Отвечай вежливо. Отвечай только на русском языке."
                      "Если с тобой здороваются, здоровайся в ответ. Если тебя спрашивают, что ты умеешь делать,"
                      "отвечай, что ты анализируешь документы и отвечаешь на вопросы по ним.\n"
                      f"НАЧАЛО ДОКУМЕНТА | {context} | КОНЕЦ ДОКУМЕНТА",
            "options": {
                "temperature": 0.2
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        return headers, data
