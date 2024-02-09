import json
import os

from langchain_community.agent_toolkits import JsonToolkit, create_json_agent
from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_community.tools.json.tool import JsonSpec

# ------------------------------------------------------------------------------
# Initialize Variables - DO NOT TOUCH
# ------------------------------------------------------------------------------

json_path = "/resources/example.json"
questions = [
    "What does this json file contain?",
    "What is the title for this json file?",
]

# define chat model


with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/example.json')),
          encoding="utf8") as file:
    data = json.load(file)

# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def execute_json_agent():
    """
    TODO: This function executes a JSON agent using the langchain JSON toolkit, using the list of questions in the list
        above. It then returns all responses from the JSON agent as a list.

    Instructions:
    - Initialize an empty list named 'response' to store the responses from the JSON agent.
    - Create a JsonSpec class is used to create a specification for the
        toolkit providing two arguments 'dict_=data' dictionary and a 'max_value_length=1000'.
    - Create a JsonToolkit instance named 'json_toolkit', providing a single argument 'spec=json_spec'.
    - Create a JSON agent using the 'create_json_agent' function. USe 'chat_model' instance of ChatHuggingFace, the
        'json_toolkit', and a 'verbose=True' passed as arguments.
    - Loop through the 'questions' list. For each question, the 'run' method of the agent is called with the question as
        an argument. The response is appended to the 'response' list.
    - Return the 'response' list.

    :return: A list of responses from the JSON agent.
    """
    # Write Code Below

    # Replace with return statement
    raise NotImplementedError("This function has not been implemented yet.")
