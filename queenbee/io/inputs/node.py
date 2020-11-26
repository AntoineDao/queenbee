"""Queenbee input types for status nodes.

For more information on plugins see plugin module.
"""

import os
from typing import Union, List, Dict, Any
from pydantic import constr, Field

from .function import FunctionStringInput, FunctionIntegerInput, FunctionNumberInput, FunctionBooleanInput, \
    FunctionFolderInput, FunctionFileInput, FunctionPathInput, FunctionArrayInput, FunctionJSONObjectInput, \
    FunctionInputs

from .dag import DAGStringInput, DAGIntegerInput, DAGNumberInput, DAGBooleanInput, \
    DAGFolderInput, DAGFileInput, DAGPathInput, DAGArrayInput, DAGJSONObjectInput, \
    DAGInputs

from ..artifact_source import HTTP, S3, ProjectFolder


class NodeStringInput(FunctionStringInput):
    """A String input."""

    type: constr(regex='^NodeStringInput$') = 'NodeStringInput'

    value: str


class NodeIntegerInput(FunctionIntegerInput):
    """An integer input."""

    type: constr(regex='^NodeIntegerInput$') = 'NodeIntegerInput'

    value: int


class NodeNumberInput(FunctionNumberInput):
    """A number input."""

    type: constr(regex='^NodeNumberInput$') = 'NodeNumberInput'

    value: float


class NodeBooleanInput(FunctionBooleanInput):
    """The boolean type matches only two special values: True and False."""

    type: constr(regex='^NodeBooleanInput$') = 'NodeBooleanInput'

    value: bool


class NodeFolderInput(FunctionFolderInput):
    """A folder input."""
    type: constr(regex='^NodeFolderInput$') = 'NodeFolderInput'

    source: Union[HTTP, S3, ProjectFolder] = Field(
        ...,
        description='The path to source the file from.'
    )

class NodeFileInput(FunctionFileInput):
    """A file input."""

    type: constr(regex='^NodeFileInput$') = 'NodeFileInput'

    source: Union[HTTP, S3, ProjectFolder] = Field(
        ...,
        description='The path to source the file from.'
    )


class NodePathInput(FunctionPathInput):
    """A file or a folder input."""

    type: constr(regex='^NodePathInput$') = 'NodePathInput'

    source: Union[HTTP, S3, ProjectFolder] = Field(
        ...,
        description='The path to source the file from.'
    )

class NodeArrayInput(FunctionArrayInput):
    """An array input."""

    type: constr(regex='^NodeArrayInput$') = 'NodeArrayInput'

    value: List


class NodeJSONObjectInput(FunctionJSONObjectInput):
    """A JSON object input."""

    type: constr(regex='^NodeJSONObjectInput$') = 'NodeJSONObjectInput'

    value: Dict

NodeInputs = Union[
    NodeStringInput, NodeIntegerInput, NodeNumberInput,
    NodeBooleanInput, NodeFolderInput, NodeFileInput, NodePathInput,
    NodeArrayInput, NodeJSONObjectInput
]

def from_template(template: Union[DAGInputs, FunctionInputs], value: Any) -> NodeInputs:
    """Generate a node input from a template input type and a value

    Args:
        template {Union[DAGInputs, FunctionInputs]} -- An input from a template (DAG or Function)
        value {Any} -- The input value calculated for this template in the workflow node

    Returns:
        NodeInputs -- A Node Input object
    """

    input_dict = template.to_dict()
    input_dict['value'] = value

    if template.__class__ in [DAGStringInput, FunctionStringInput]:
        return NodeStringInput.parse_obj(input_dict)

    if template.__class__ in [DAGIntegerInput, FunctionIntegerInput]:
        return NodeIntegerInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGNumberInput, FunctionNumberInput]:
        return NodeNumberInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGBooleanInput, FunctionBooleanInput]:
        return NodeBooleanInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGFolderInput, FunctionFolderInput]:
        return NodeFolderInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGFileInput, FunctionFileInput]:
        return NodeFileInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGPathInput, FunctionPathInput]:
        return NodePathInput.parse_obj(input_dict)
    
    if template.__class__ in [DAGArrayInput, FunctionArrayInput]:
        return NodeArrayInput.parse_obj(input_dict)
         
    if template.__class__ in [DAGJSONObjectInput, FunctionJSONObjectInput]:
        return NodeJSONObjectInput.parse_obj(input_dict)

