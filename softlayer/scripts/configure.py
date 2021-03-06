########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

import tempfile
import json

import fabric
import fabric.api

from cloudify import ctx
from softlayer_plugin import properties_constants

PROVIDER_CONTEXT_RUNTIME_PROPERTY = 'provider_context'


def configure(softlayer_api_config, ssh_keys):

    _set_provider_context(ssh_keys)

    _copy_softlayer_configuration_to_manager(softlayer_api_config)


def _set_provider_context(ssh_keys):
    provider = {
        'ssh_keys': ssh_keys
    }
    ctx.instance.runtime_properties[
        PROVIDER_CONTEXT_RUNTIME_PROPERTY] = provider


def _copy_softlayer_configuration_to_manager(softlayer_api_config):
    tmp = tempfile.mktemp()
    with open(tmp, 'w') as f:
        json.dump(softlayer_api_config, f)
    fabric.api.put(tmp, properties_constants.DEFAULT_SOFTLAYER_CONFIG_PATH)
