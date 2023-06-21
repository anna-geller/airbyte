#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from abc import abstractmethod
from typing import Any, Mapping


class AbstractSchemaValidationPolicies:
    @abstractmethod
    def record_passes_validation_policy(
        self, policy: "AbstractSchemaValidationPolicies", record: Mapping[str, Any], schema: Mapping[str, Any]
    ) -> bool:
        """
        Return True if the record passes the user's validation policy.
        """
        ...
