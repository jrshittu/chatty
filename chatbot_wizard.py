# import the AutoModelForCausalLM class from the ctransformers library
from ctransformers import AutoModelForCausalLM

# import taipy library
from taipy.gui import Gui, notify

# load Mistral-7B-Instruct-v0.1-GGUF, Set gpu_layers to the number of layers to offload to GPU. The value is set to 0 because no GPU acceleration is available on my current system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

# call the model to generate text, starting with the prompt "AI is going to"
prompt = ""
response = ""

def chat(state):
    notify(state, 'info', 'Thinking...')
    state.response = llm(state.prompt)

page = """
# Chatbot Wizard! {: .color-primary}
Enter Prompt: <|{prompt}|input|>
<|Send Prompt|button|class_name=plain mt1|on_action=chat|> <br />
MistralAI: <br /> <|{response}|>
""" 

Gui(page).run(debug=True)