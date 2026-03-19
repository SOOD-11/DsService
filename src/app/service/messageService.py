from utils.MessageUtil import MessageUtil
from serivce.LLMService import LLMService
class MessageService:
    def __init__(self):

       self.messageUtil=MessageUtil()
       self.llmService=LLMService()
    def    process_message(self,message):
        return self.llmService.runLLM(message=)