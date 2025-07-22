from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os 
from dotenv import load_dotenv
load_dotenv()

gimini_api_key = os.getenv("GEMINI_API_KEY")

externalClient = AsyncOpenAI(
    api_key=gimini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=externalClient,
)

config = RunConfig(
    model = model,
    model_provider = externalClient,
    tracing_disabled = True
)

agent = Agent(
    name= "Hello Agent",
    instructions = "You are a help ful assistant that helps to answer questions. You need to try answer in one line if is it possible and talk like human!"
)

prompt = input("Enter Your Question:")

result = Runner.run_sync(
    agent,
    input = prompt,
    run_config = config
)

print(result.final_output)

