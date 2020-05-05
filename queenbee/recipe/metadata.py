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


class License(BaseModel):
    """License information for the workflow."""
    name: str = Field(
        ...,
        description='The license name used for the workflow.'
    )

    url: str = Field(
        None,
        description='A URL to the license used for the workflow.'
    )


class MetaData(BaseModel):
    """Workflow metadata information."""

    name: str = Field(
        ...,
        description='Workflow name. Make it descriptive and helpful ;)'
    )

    version: str = Field(
        ...,
        description='The version of the workflow'
    )

    keywords: List[str] = Field(
        None,
        description='A list of keywords to search the workflow by'
    )

    maintainers: List[Maintainer] = Field(
        None,
        description='A list of maintainers for the workflow'
    )

    home: str = Field(
        None,
        description='The URL of this workflow\'s home page'
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
        description='Whether this workflow is deprecated'
    )

    description: str = Field(
        None,
        description='A description of what this workflow does'
    )

    license: License = Field(
        None,
        description='The license information.'
    )
