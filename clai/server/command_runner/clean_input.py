#
# Copyright (C) 2020 IBM. All Rights Reserved.
#
# See LICENSE.txt file in the root directory
# of this source tree for licensing information.
#

def extract_quoted_agent_name(plugin_to_select):
    if plugin_to_select.startswith('"'):
        if names := plugin_to_select.split('"')[1::2]:
            return names[0]

    return plugin_to_select
