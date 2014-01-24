"""

"""

import httplib as http

from framework import request
from framework.exceptions import HTTPError
from website.addons.dataverse.config import TEST_CERT, TEST_HOST
from website.addons.dataverse.dvn.connection import DvnConnection
from website.project import decorators
from website.project.views.node import _view_project


@decorators.must_be_contributor
@decorators.must_have_addon('dataverse', 'user')
def dataverse_set_user_config(*args, **kwargs):

    user_settings = kwargs['user_addon']

    # Log in with DATAVERSE
    username = request.json.get('dataverse_username')
    password = request.json.get('dataverse_password')
    print username
    connection = DvnConnection(
        username=username,
        password=password,
        host=TEST_HOST,
        cert=TEST_CERT,
    )
    print connection

    # If success, save params
    if connection:
        user_settings.dataverse_username = username
        user_settings.dataverse_password = password

        user_settings.save()

    # If fail, error msg
    else:
        raise HTTPError(http.BAD_REQUEST)



@decorators.must_be_contributor
@decorators.must_have_addon('dataverse', 'node')
def dataverse_set_node_config(*args, **kwargs):
    # TODO: Validate
    node_settings = kwargs['node_addon']



    # Log in with DATAVERSE

    # If success, save params

    # If fail, error msg



    node_settings.save()


@decorators.must_be_contributor_or_public
@decorators.must_have_addon('dataverse', 'node')
def dataverse_widget(*args, **kwargs):

    node = kwargs['node'] or kwargs['project']
    dataverse = node.get_addon('dataverse')

    rv = {
        'complete': True,
        'dataverse_url': dataverse.dataverse_url,
    }
    rv.update(dataverse.config.to_json())
    return rv

@decorators.must_be_contributor_or_public
def dataverse_page(**kwargs):

    user = kwargs['user']
    node = kwargs['node'] or kwargs['project']
    dataverse= node.get_addon('dataverse')

    data = _view_project(node, user)

    rv = {
        'complete': True,
        'dataverse_url': dataverse.dataverse_url,
    }
    rv.update(data)
    return rv