# agenticai
Learn more about various agentic ai systems
### UV Commands
uv init
uv venv [Activate the virtual environment .\.venv\Scripts\activate]
uv add python-dotenv [this is important to read the GEMINI_API_KEY]

## Email Agent Flow
1. Load environment variables from `.env` using `dotenv.load_dotenv()`.
2. `createLLM()` builds a Gemini LLM with:
   - `model="gemini-3-flash-preview"`
   - `api_key=os.getenv("GEMINI_API_KEY")`
   - `temperature=0.7`
   - `max_tokens=1024`
3. `createEmailAgent()` wraps the LLM in a `crewai.Agent` and defines:
   - `role`
   - `goal`
   - `backstory`
   - `verbose`
4. `formatEmailBody_Task()` creates an `Task`, defines an email body, and returns a `Task` with:
   - `name="Compose Email"`
   - a professional formatting description
   - `agent=email_agent`
   - `expected_output` describing the formatted email result
5. When run as a script, the main block:
   - calls `checkEnv()` to print the API key status
   - creates the email agent and task
   - builds a `Crew` with the agent and task
   - executes `crew.kickoff()` to start the workflow

### Note
Make sure `.env` contains `GEMINI_API_KEY=<your_key>` so the LLM can authenticate successfully.


