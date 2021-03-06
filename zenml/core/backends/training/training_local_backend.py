#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Definition of the base Training Backend"""

from zenml.core.backends.base_backend import BaseBackend


class TrainingLocalBackend(BaseBackend):
    """
    Base class for all local Training ZenML backends.

    Every ZenML pipeline runs in backends.

    A training backend can be used to efficiently train a machine learning
    model on large amounts of data. Since most common machine learning models
    leverage mainly linear algebra operations under the hood, they can
    potentially benefit a lot from dedicated training hardware like Graphics
    Processing Units (GPUs) or application-specific integrated circuits
    (ASICs).
    """

    BACKEND_TYPE = 'local'
    BACKEND_KEY = 'training'
