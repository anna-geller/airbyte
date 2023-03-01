#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from pathlib import Path

from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "click~=8.1.3",
    "requests",
    "PyYAML~=6.0",
    "GitPython~=3.1.29",
    "pandas~=1.5.3",
    "pandas-gbq~=0.19.0",
    "pydantic~=1.10.4",
    "fsspec~=2023.1.0",
    "gcsfs~=2023.1.0",
    "dagger-io==0.3.3",
    "pytablewriter~=0.64.2",
    "docker~=6.0.0",
]


def local_pkg(name: str) -> str:
    """Returns a path to a local package."""
    return f"{name} @ file://{Path.cwd().parent / name}"


# These internal packages are not yet published to a Pypi repository.
LOCAL_REQUIREMENTS = [local_pkg("ci_credentials")]

TEST_REQUIREMENTS = [
    "pytest~=6.2.5",
    "pytest-mock~=3.10.0",
    "freezegun",
]

DEV_REQUIREMENTS = ["pyinstrument"]

setup(
    version="0.1.14",
    name="ci_connector_ops",
    description="Packaged maintained by the connector operations team to perform CI for connectors",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS + LOCAL_REQUIREMENTS,
    extras_require={"tests": TEST_REQUIREMENTS, "dev": TEST_REQUIREMENTS + DEV_REQUIREMENTS},
    python_requires=">=3.10",
    package_data={"ci_connector_ops.qa_engine": ["connector_adoption.sql"]},
    entry_points={
        "console_scripts": [
            "check-test-strictness-level = ci_connector_ops.acceptance_test_config_checks:check_test_strictness_level",
            "write-review-requirements-file = ci_connector_ops.acceptance_test_config_checks:write_review_requirements_file",
            "print-mandatory-reviewers = ci_connector_ops.acceptance_test_config_checks:print_mandatory_reviewers",
            "allowed-hosts-checks = ci_connector_ops.allowed_hosts_checks:check_allowed_hosts",
            "run-qa-engine = ci_connector_ops.qa_engine.main:main",
            "run-qa-checks = ci_connector_ops.qa_checks:run_qa_checks",
            "connectors-ci = ci_connector_ops.pipelines.connectors_ci:connectors_ci",
        ],
    },
)
