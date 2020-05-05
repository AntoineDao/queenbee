"""Queenbee MetaData class.

This object provides metadata information for a workflow.

The specification is designed based on openapi info object:
https://swagger.io/specification/#infoObject
"""

from typing import List, Union
from pydantic import Field

from ..base.basemodel import BaseModel

class Maintainer(BaseModel):
    """Author information."""
    name: str = Field(
        ...,
        description='The name of the author person or organization.'
    )

    email: str = Field(
        None,
        description='The email address of the author person or organization.'
    )

class MetaData(BaseModel):
    """Workflow metadata information."""

    
    name: str = Field(
        ...,
        description='Operator name. This name should be unique among all the operators'
        ' in your workflow.'
    )

    version: str = Field(
        ...,
        description='The version of the operator'
    )

    appVersion: str = Field(
        None,
        description='The version of the app binary backing the operator (CLI tool or container)'
    )

    keywords: List[str] = Field(
        None,
        description='A list of keywords to search the operator by'
    )

    maintainers: List[Maintainer] = Field(
        None,
        description='A list of maintainers for the operator'
    )

    home: str = Field(
        None,
        description='The URL of this projects home page'
    )

    sources: List[str] = Field(
        None,
        description='A list of URLs to source code for this project'
    )

    icon: str = Field(
        None,
        description='A URL to an SVG or PNG image to be used as an icon'
    )

    deprecated: bool = Field(
        None,
        description='Whether this chart is deprecated'
    )

    description: str = Field(
        None,
        description='A description of what this operator does'
    )
