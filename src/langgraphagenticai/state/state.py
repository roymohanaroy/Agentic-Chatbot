from typing_extensions import Annotated, TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict) :
    """_summary_

    Represent the structure of the state used in graph
   
    """
    
    messages : Annotated[List, add_messages]
    