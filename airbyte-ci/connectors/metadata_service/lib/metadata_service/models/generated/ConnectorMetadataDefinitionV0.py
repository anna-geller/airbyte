# generated by datamodel-codegen:
#   filename:  ConnectorMetadataDefinitionV0.yaml

from __future__ import annotations

from datetime import date
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Extra, Field, constr
from typing_extensions import Literal


class AllowedHosts(BaseModel):
    class Config:
        extra = Extra.allow

    hosts: Optional[List[str]] = Field(
        None,
        description="An array of hosts that this connector can connect to.  AllowedHosts not being present for the source or destination means that access to all hosts is allowed.  An empty list here means that no network access is granted.",
    )


class NormalizationDestinationDefinitionConfig(BaseModel):
    class Config:
        extra = Extra.allow

    normalizationRepository: str = Field(
        ...,
        description="a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used.",
    )
    normalizationTag: str = Field(
        ...,
        description="a field indicating the tag of the docker repository to be used for normalization.",
    )
    normalizationIntegrationType: str = Field(
        ...,
        description="a field indicating the type of integration dialect to use for normalization.",
    )


class SuggestedStreams(BaseModel):
    class Config:
        extra = Extra.allow

    streams: Optional[List[str]] = Field(
        None,
        description="An array of streams that this connector suggests the average user will want.  SuggestedStreams not being present for the source means that all streams are suggested.  An empty list here means that no streams are suggested.",
    )


class ResourceRequirements(BaseModel):
    class Config:
        extra = Extra.forbid

    cpu_request: Optional[str] = None
    cpu_limit: Optional[str] = None
    memory_request: Optional[str] = None
    memory_limit: Optional[str] = None


class JobType(BaseModel):
    __root__: Literal[
        "get_spec",
        "check_connection",
        "discover_schema",
        "sync",
        "reset_connection",
        "connection_updater",
        "replicate",
    ] = Field(
        ...,
        description="enum that describes the different types of jobs that the platform runs.",
        title="JobType",
    )


class VersionBreakingChange(BaseModel):
    class Config:
        extra = Extra.forbid

    upgradeDeadline: date = Field(
        ...,
        description="The deadline by which to upgrade before the breaking change takes effect.",
    )
    message: str = Field(
        ..., description="Descriptive message detailing the breaking change."
    )
    migrationDocumentationUrl: Optional[AnyUrl] = Field(
        None,
        description="URL to documentation on how to migrate to the current version. Defaults to ${documentationUrl}-migrations#${version}",
    )


class JobTypeResourceLimit(BaseModel):
    class Config:
        extra = Extra.forbid

    jobType: JobType
    resourceRequirements: ResourceRequirements


class ConnectorBreakingChanges(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r"^\d+\.\d+\.\d+$"), VersionBreakingChange] = Field(
        ...,
        description="Each entry denotes a breaking change in a specific version of a connector that requires user action to upgrade.",
    )


class ActorDefinitionResourceRequirements(BaseModel):
    class Config:
        extra = Extra.forbid

    default: Optional[ResourceRequirements] = Field(
        None,
        description="if set, these are the requirements that should be set for ALL jobs run for this actor definition.",
    )
    jobSpecific: Optional[List[JobTypeResourceLimit]] = None


class ConnectorReleases(BaseModel):
    class Config:
        extra = Extra.forbid

    breakingChanges: ConnectorBreakingChanges
    migrationDocumentationUrl: Optional[AnyUrl] = Field(
        None,
        description="URL to documentation on how to migrate from the previous version to the current version. Defaults to ${documentationUrl}-migrations",
    )


class RegistryOverrides(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: bool
    name: Optional[str] = None
    dockerRepository: Optional[str] = None
    dockerImageTag: Optional[str] = None
    supportsDbt: Optional[bool] = None
    supportsNormalization: Optional[bool] = None
    license: Optional[str] = None
    documentationUrl: Optional[AnyUrl] = None
    connectorSubtype: Optional[str] = None
    allowedHosts: Optional[AllowedHosts] = None
    normalizationConfig: Optional[NormalizationDestinationDefinitionConfig] = None
    suggestedStreams: Optional[SuggestedStreams] = None
    resourceRequirements: Optional[ActorDefinitionResourceRequirements] = None


class Registry(BaseModel):
    class Config:
        extra = Extra.forbid

    oss: Optional[RegistryOverrides] = None
    cloud: Optional[RegistryOverrides] = None


class Data(BaseModel):
    name: str
    icon: Optional[str] = None
    definitionId: UUID
    connectorType: Literal["destination", "source"]
    dockerRepository: str
    dockerImageTag: str
    supportsDbt: Optional[bool] = None
    supportsNormalization: Optional[bool] = None
    license: str
    documentationUrl: AnyUrl
    githubIssueLabel: str
    maxSecondsBetweenMessages: Optional[int] = Field(
        None,
        description="Maximum delay between 2 airbyte protocol messages, in second. The source will timeout if this delay is reached",
    )
    releaseDate: Optional[date] = Field(
        None,
        description="The date when this connector was first released, in yyyy-mm-dd format.",
    )
    protocolVersion: Optional[str] = Field(
        None, description="the Airbyte Protocol version supported by the connector"
    )
    connectorSubtype: Literal[
        "api", "database", "file", "custom", "message_queue", "unknown"
    ]
    releaseStage: Literal["alpha", "beta", "generally_available", "source"]
    tags: Optional[List[str]] = Field(
        None,
        description="An array of tags that describe the connector. E.g: language:python, keyword:rds, etc.",
    )
    registries: Optional[Registry] = None
    allowedHosts: Optional[AllowedHosts] = None
    releases: Optional[ConnectorReleases] = None
    normalizationConfig: Optional[NormalizationDestinationDefinitionConfig] = None
    suggestedStreams: Optional[SuggestedStreams] = None
    resourceRequirements: Optional[ActorDefinitionResourceRequirements] = None


class ConnectorMetadataDefinitionV0(BaseModel):
    class Config:
        extra = Extra.forbid

    metadataSpecVersion: str
    data: Data
