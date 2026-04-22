from dotenv import load_dotenv
from pathlib import Path
import os
from crewai import LLM,Agent,Task,Crew

load_dotenv()

# Create a function to initialize the LLM with the API key from the environment variable
# LLM is the brain of the agent, it will be used to generate responses and perform tasks based on the prompts it receives.
def createLLM():
    print(f"API Key: {os.getenv('GEMINI_API_KEY')}  ")
    llm = LLM(
    model="gemini-3-flash-preview",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_tokens=1024
    )
    return llm

def checkEnv():
    print(f"API Key: {os.getenv('GEMINI_API_KEY')}  ")

def createEmailAgent(
    role: str = "Email Assistant",
    goal: str = "Compose, summarize, and manage email communications efficiently.",
    backstory: str = "You are a professional email assistant helping users write clear, concise, and well-structured emails while maintaining tone and context.",    
    verbose: bool = True,
):
    llm = createLLM()
    email_agent = Agent(
        llm=llm,
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=verbose,
    )
    return email_agent

def formatEmailBody_Task() -> Task:
    email_agent = createEmailAgent()
    body = (
        "I hope this email finds you well. I wanted to follow up on our previous conversation regarding the project timeline. "
        "Could you please provide an update on the current status and any potential roadblocks we should be aware of? "
        "Additionally, if there are any changes to the schedule, please let us know as soon as possible so we can adjust our plans accordingly. "
        "Thank you for your attention to this matter, and I look forward to your response."
    )
    task = Task(
        name="Compose Email",
        description=(
            "Format the email body professionally and clearly. "
            "Use a polite, concise tone, organize the content into short paragraphs, "
            "include a brief greeting and closing, and preserve the original meaning. "
            f"Email content to format: {body}"
        ),
        agent=email_agent,
        expected_output="A professionally formatted email body with greeting, concise paragraphs, and a polite closing.",
    )
    return task

if __name__ == "__main__":
    checkEnv()
    email_agent = createEmailAgent()
    email_task = formatEmailBody_Task()

    crew = Crew(
        name="Email Management Crew",
        description="A crew of agents specializing in email composition, summarization, and management.",
        agents=[email_agent],
        tasks=[email_task],
    )
    print(crew.kickoff())
    