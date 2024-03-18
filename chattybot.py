# import the AutoModelForCausalLM class from the ctransformers library
from ctransformers import AutoModelForCausalLM

# import taipy library
from taipy.gui import Gui, notify

# load Mistral-7B-Instruct-v0.1-GGUF, Set gpu_layers to the number of layers to offload to GPU. The value is set to 0 because no GPU acceleration is available on my current system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

# call the model to generate text
prompt = ""
response = ""
conversation = {
    "Conversation": ["Hello", "Hi there!   What would you like to talk about today?"]
}

def chat(state):
    # Notify the user that the bot is thinking
    notify(state, 'info', 'Thinking...')

    # Generate a response using the loaded language model
    response = llm(state.prompt)

    # Add the user's prompt and the bot's response to the conversation history
    state.conversation["Conversation"].append(state.prompt)
    state.conversation["Conversation"].append(response)

    # Update the conversation object to contain the entire conversation history
    state.conversation = {"Conversation": state.conversation["Conversation"]}

    # Clear the user's input prompt
    state.prompt = ""

    # Notify the user that the bot has generated a response
    notify(state, 'info', 'Response received!')


def clear_conversation(state):
    state.conversation = {"Conversation": []}

page = """
<|layout|columns=300px 1|
<|part|render=True|class_name=sidebar|
# Taipy **Chat**{: .color-primary} # {: .logo-text}
<|New Chat|button|class_name=fullwidth plain|on_action=clear_conversation|>
### History
|>

<|part|render=True|class_name=p2 align-item-bottom table|
<|{conversation}|table|style=style_conv|show_all|width=100%|rebuild|>

<|part|class_name=card mt1|
<|{prompt}|input|label=Ask anything...|class_name=fullwidth|on_action=chat|>
<|Send Prompt|button|class_name=plain mt1 fullwidth|on_action=chat|>
|>
|>
|>
"""

Gui(page).run(debug=True, port=5001)