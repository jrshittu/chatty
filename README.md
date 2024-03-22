## Creating a Chatbot Wizard With Mistral AI🤖
![chat](https://github.com/jrshittu/chatty/assets/110542235/5b5cc756-1d6c-4de6-beac-1a1f2f3fd15d)

In this technical article, we will learn how to build a simple chatbot using the Taipy GUI library and the Mistral-7B-Instruct-v0.1-GGUF language model from the ctransformers library. We will walk through the process of loading the language model, generating responses to user prompts, updating the conversation history, and clearing the conversation history. By the end of this article, we will have a basic understanding of how to build a chatbot using these tools.

## Contents
[Introduction](#intro)

[Download GGUF files using ctransformers](#download)

[Load the model](#load)

[Say Hello Taipy!](#hi)

[Create a chat interface with TaipyGUI](#create)

[Mistral AI Chatbot🤖](#bonus)

[Styling With CSS](#style)

[Conclusion](#conc)


## Introduction
Mistral 7B is a super-smart language model with 7 billion parameters! It beats the best 13B model, Llama 2, in all tests and even outperforms the powerful 34B model, Llama 1, in reasoning, math, and code generation. How? Mistral 7B uses smart tricks like grouped-query attention (GQA) for quick thinking and sliding window attention (SWA) to handle all sorts of text lengths without slowing down.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9dmy24ao6nnz66w5qc1x.PNG)

Source: [Mistral.AI Docs](https://mistral.ai/news/announcing-mistral-7b/)

And there's more! Mistral AI Team fine-tuned Mistral 7B for specific tasks with Mistral 7B – Instruct. It not only outshines Llama 2 13B in chat but also rocks both human and automated tests. Best part? Mistral 7B – was released under the Apache 2.0 license. 

## Download GGUF files using ctransformers <a name="download"></a>

**Step 1: Install ctransformers**

With no GPU acceleration
```bash
pip install ctransformers
```
or install with ctransformers with CUDA GPU acceleration
```bash
pip install ctransformers[cuda]
```
or install with ctransformers with AMD ROCm GPU acceleration (Linux only)
```bash
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
```
or install with ctransformers with Metal GPU acceleration for macOS systems only
```bash
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

**Step 2: Install Langchain**

```bash
pip install langchain
```

## Load the model: <a name="load"></a>
All set? let's run the code below to download and send a prompt to the model. Make sure to free up space on your computer and connect to a good internet connection.

```python
# import the AutoModelForCausalLM class from the ctransformers library
from ctransformers import AutoModelForCausalLM

# load Mistral-7B-Instruct-v0.1-GGUF, Set gpu_layers to the number of layers to offload to GPU. The value is set to 0 because no GPU acceleration is available on my current system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

# call the model to generate text.
ask = 1000 
turn = 0
while turn < ask:
    user = input("Enter your message: ")
    print(llm(user))
```
**Terminal Output**
![terminal load model](https://github.com/jrshittu/build_with_taipy/assets/110542235/bc6943a9-1512-4480-81c2-33ee3ceedb7c)

## Say Hello Taipy! <a name="hi"></a>
Taipy is a Python open-source library that makes it simple to create data-driven web applications. It takes care of both the visible part(Frontend) and the behind-the-scenes(Backend) operations. Its goal is to speed up the process of developing applications, from the early design stages to having a fully functional product ready for use.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k24u6ko4tkjffice6thz.gif)

Source: [Taipy Docs](https://docs.taipy.io/en/latest/)

**Requirement:** Python 3.8 or later on Linux, Windows, and Mac. 

**Installing Taipy:** Open up a terminal and run the following command, which will install Taipy with all its dependencies.

```bash
pip install taipy
```
We're set, let say hello to Taipy...

```python
# import the library
from taipy import Gui

hello = "# Hello Taipy!" 

# run the gui
Gui(hello).run()
```

Save the code as a Python file: e.g., `hi_taipy.py`. 
Run the code and wait for the client link `http://127.0.0.1:5000` to display and pop up in your browser. 
You can change the port if you want to run multiple servers at the same time with `Gui(...).run(port=xxxx)`.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6w2h2jryumg8kumid3ms.PNG)


## Create a chat interface with TaipyGUI: <a name="create"></a>
Since we are familiar with Taipy, Let's get our hands dirty and build our chat interface. 

**Step 1**: Import the AutoModelForCausalLM class from the ctransformers library

In this step, we import the AutoModelForCausalLM class from the ctransformers library, which is used for generating text using pre-trained language models.
```python
from ctransformers import AutoModelForCausalLM
```
**Step 2:** Import the Taipy GUI library

In this step, we import the Taipy GUI library, which is used for building the user interface for our chatbot.
```python
from taipy.gui import Gui, notify
```
**Step 3:** Load the Mistral-7B-Instruct-v0.1-GGUF model

In this step, we load the Mistral-7B-Instruct-v0.1-GGUF model, which is a pre-trained language model that we will use to generate text. We set the `gpu_layers` parameter to 0 because we don't have GPU acceleration available on our current system.
```python
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)
```
**Step 4:** Initialize the prompt and response variables

In this step, we initialize the `prompt` and `response` variables as empty strings.
```python
prompt = ""
response = ""
```
**Step 5:** Define the `chat` function

In this step, we define the `chat` function, which is called when the user clicks the "Chat" button in the user interface. This function takes the current state of the GUI as an input, generates text using the pre-trained language model based on the user's prompt, and updates the response variable in the state.
```python
def chat(state):
    notify(state, 'info', 'Thinking...')
    state.response = llm(state.prompt)
```
**Step 6:** Define the user interface

Time to define the user interface for our chatbot using the Taipy GUI library. The user interface consists of an input field where the user can enter a prompt, a "Chat" button that triggers the `chat` function, and a display area where the chatbot's response is shown.
```python
page = """
# Chatbot Wizard! {: .color-primary}
Enter Prompt: <|{prompt}|input|> <br />
<|Chat|button|class_name=plain mt1|on_action=chat|> <br />
MistralAI: <br /> <|{response}|>
"""
```
**Step 7:** Run the Taipy GUI application

Now let's run the Taipy GUI application using the `run` method.
```python
Gui(page).run(debug=True)
```
**Chat Interface**
![chat_wizard](https://github.com/jrshittu/build_with_taipy/assets/110542235/22d58387-013f-4286-a19e-30e4aa8c3772)

**Full Code**
```python
# import the AutoModelForCausalLM class from the ctransformers library
from ctransformers import AutoModelForCausalLM

# import taipy library
from taipy.gui import Gui, notify

# load Mistral-7B-Instruct-v0.1-GGUF, Set gpu_layers to the number of layers to offload to GPU. The value is set to 0 because no GPU acceleration is available on my current system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

# initialize the `prompt` and `response` variables as empty strings.
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
```

## Mistral AI Chatbot🤖 <a name="bonus"></a>

**Step 1**. In this step, we initialize the `prompt` and `response` and the `conversation`.
![taipee](https://github.com/jrshittu/chatty/assets/110542235/e417fabf-3003-4c33-afdd-274f899113e4)

```python
prompt = ""
response = ""
conversation = {
    "Conversation": ["Hello", "Hi there!   What would you like to talk about today?"]
}
```


**Step 2**. Update the `chat` function.
```python
def chat(state):
    # Notify the user that the chatbot is thinking
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
```

**Step 3.**  Add `clear_conversation` function to clear the conversation history. The function sets the `state.conversation` object to a new dictionary with a single key-value pair, where the key is "Conversation" and the value is an empty list. This effectively clears the conversation history, as the `state.conversation` object is now an empty dictionary with a single key-value pair containing an empty list. The updated `state.conversation` object will be reflected in the chatbot UI, showing an empty conversation history.

```python
def clear_conversation(state):
    state.conversation = {"Conversation": []}
```

**Step 4.** Define the layout of the user interface for the Chatbot, Add the logo Image and attach `clear_conversation` to the `New chat` button.

```python
page = """
<|layout|columns=1|
<|part|class_name=card p2 mt1 mb2 flexy|
<|taipy.png|image|width=110px|>
# Chat **Wizard**{: .color-primary} # {: .logo-text}
|>
<|part|render=True|class_name=p2 align-item-bottom table|
<|{conversation}|table|style=style_conv|show_all|width=100%|rebuild|>

<|part|class_name=card mt1 align-item-bottom table|
<|{prompt}|input|label=Ask anything...|class_name=fullwidth|on_action=chat|>
<|Send Prompt|button|class_name=plain mt1 fullwidth|on_action=chat|>
|>
|>
|>
"""
```

**Updated Fullcode:**
```python
# import the AutoModelForCausalLM class from the ctransformers library
from ctransformers import AutoModelForCausalLM

# import taipy library
from taipy.gui import Gui, notify

# load Mistral-7B-Instruct-v0.1-GGUF, Set gpu_layers to the number of layers to offload to GPU. The value is set to 0 because no GPU acceleration is available on my current system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

# initialize variables
prompt = ""
response = ""
conversation = {
    "Conversation": []
}

def chat(state):
    # Notify the user that the chatbot is thinking
    notify(state, 'info', 'Thinking...')

    # Generate a response using the loaded language model
    response = llm(state.prompt)

    # Add the user's prompt and the chatbot's response to the conversation history
    state.conversation["Conversation"].append(state.prompt)
    state.conversation["Conversation"].append(response)

    # Update the conversation object to contain the entire conversation history
    state.conversation = {"Conversation": state.conversation["Conversation"]}

    # Clear the user's input prompt
    state.prompt = ""

    # Notify the user that the chatbot has generated a response
    notify(state, 'info', 'Response received!')


def clear_conversation(state):
    state.conversation = {"Conversation": []}

def style_conv(state, idx: int, row: int) -> str:
    if idx is None:
        return None
    elif idx % 2 == 0:
        return "user_mssg" # return user_mssg style
    else:
        return "mistral_mssg" # return mistral_mssg style


page = """
<|layout|columns=1|
<|part|class_name=card p2 mt1 mb2 flexy|
<|taipy.png|image|width=110px|>
# Chat **Wizard**{: .color-primary} # {: .logo-text}
|>
<|part|render=True|class_name=p2 align-item-bottom table|
<|{conversation}|table|style=style_conv|show_all|width=100%|rebuild|>

<|part|class_name=card mt1 align-item-bottom table|
<|{prompt}|input|label=Ask anything...|class_name=fullwidth|on_action=chat|>
<|Send Prompt|button|class_name=plain mt1 fullwidth|on_action=chat|>
|>
|>
|>
"""

Gui(page).run(debug=True, port=5001, title="Chatbot Wizard")
```

## Styling With CSS <a name="style"></a>
Now, let's style our chat ui by floating the response the left and the prompt to the right hand side. 
![chatty](https://github.com/jrshittu/chatty/assets/110542235/372bf3e7-3fed-44ff-a054-9830ff44aded)

**Step 1**: Create a CSS file with the same title as the python file and save it in the same directory.
```css
.mistral_mssg td {
  position: relative;
  display: inline-block;
  margin: 10px 10px;
  padding: 20px;
  background-color: #ff8c00;
  border-radius: 20px;
  max-width: 80%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  font-size: medium;
}

.user_mssg td {
  position: relative;
  display: inline-block;
  float: right;
  margin: 10px 10px;
  padding: 20px;
  background-color: #9400D3;
  border-radius: 20px;
  max-width: 80%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  font-size: medium;
}
```

**Step 2:** Create the `style_conv` function, a callback function that is used to apply styles to the conversation history table in the Taipy GUI. It takes three arguments: `state`, `idx`, and `row`.

The `state` argument is a dictionary that contains the current state of the GUI, including the conversation history. The `idx` argument is the index of the current row in the table, and the `row` argument is the index of the current column in the table.

The function checks the value of the `idx` argument to determine which style to apply to the current row. If `idx` is `None`, the function returns `None`, indicating that no style should be applied.

If `idx` is an even number, the function returns the string `"user_mssg"`, which corresponds to the CSS class for the user's prompts. If `idx` is an odd number, the function returns the string `"mistral_mssg"`, which corresponds to the CSS class for the chatbot's responses.

Here is the code for the `style_conv` function:
```
def style_conv(state, idx: int, row: int) -> str:
    if idx is None:
        return None
    elif idx % 2 == 0:
        return "user_mssg"  # return user_mssg style
    else:
        return "mistral_mssg"  # return mistral_mssg style
```
To use the `style_conv` function in the Taipy GUI, we need to pass it as the value of the `style` attribute in the `table` element. For example:
```
<|{conversation}|table|style=style_conv|show_all|width=100%|rebuild|>
```


## Conclusion <a name="conc"></a>
In conclusion, this article demonstrated how to build a simple chatbot using the Taipy GUI library and the Mistral-7B-Instruct-v0.1-GGUF language model from the ctransformers library. The code provided shows how to load the language model, generate responses to user prompts, update the conversation history, and clear the conversation history. The chatbot's UI, built using the Taipy GUI library, provides a user-friendly interface for interacting with the chatbot. Overall, this article provides a useful starting point for building more sophisticated chatbots using these Taipy.
