# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for ContainerRegistryV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_container_registry.container_registry_v1 import *

account = 'testString'

service = ContainerRegistryV1(
    authenticator=NoAuthAuthenticator(),
    account=account
    )

base_url = 'https://us.icr.io'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Authorization
##############################################################################
# region

class TestGetAuth():
    """
    Test Class for get_auth
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_auth_all_params(self):
        """
        get_auth()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/auth')
        mock_response = '{"iam_authz": false, "private_only": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_auth()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_auth_value_error(self):
        """
        test_get_auth_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/auth')
        mock_response = '{"iam_authz": false, "private_only": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_auth(**req_copy)



class TestUpdateAuth():
    """
    Test Class for update_auth
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_auth_all_params(self):
        """
        update_auth()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/auth')
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        iam_authz = True
        private_only = True

        # Invoke method
        response = service.update_auth(
            iam_authz=iam_authz,
            private_only=private_only,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['iam_authz'] == True
        assert req_body['private_only'] == True


    @responses.activate
    def test_update_auth_value_error(self):
        """
        test_update_auth_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/auth')
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        iam_authz = True
        private_only = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_auth(**req_copy)



# endregion
##############################################################################
# End of Service: Authorization
##############################################################################

##############################################################################
# Start of Service: Images
##############################################################################
# region

class TestListImages():
    """
    Test Class for list_images
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_images_all_params(self):
        """
        list_images()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images')
        mock_response = '[{"ConfigurationIssueCount": 25, "Created": 7, "DigestTags": {"mapKey": ["inner"]}, "ExemptIssueCount": 18, "Id": "id", "IssueCount": 11, "Labels": {"mapKey": "inner"}, "ManifestType": "manifest_type", "ParentId": "parent_id", "RepoDigests": ["repo_digests"], "RepoTags": ["repo_tags"], "Size": 4, "VirtualSize": 12, "VulnerabilityCount": 19, "Vulnerable": "vulnerable"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'testString'
        include_ibm = True
        include_private = True
        include_manifest_lists = True
        vulnerabilities = True
        repository = 'testString'

        # Invoke method
        response = service.list_images(
            namespace=namespace,
            include_ibm=include_ibm,
            include_private=include_private,
            include_manifest_lists=include_manifest_lists,
            vulnerabilities=vulnerabilities,
            repository=repository,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'namespace={}'.format(namespace) in query_string
        assert 'includeIBM={}'.format('true' if include_ibm else 'false') in query_string
        assert 'includePrivate={}'.format('true' if include_private else 'false') in query_string
        assert 'includeManifestLists={}'.format('true' if include_manifest_lists else 'false') in query_string
        assert 'vulnerabilities={}'.format('true' if vulnerabilities else 'false') in query_string
        assert 'repository={}'.format(repository) in query_string


    @responses.activate
    def test_list_images_required_params(self):
        """
        test_list_images_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images')
        mock_response = '[{"ConfigurationIssueCount": 25, "Created": 7, "DigestTags": {"mapKey": ["inner"]}, "ExemptIssueCount": 18, "Id": "id", "IssueCount": 11, "Labels": {"mapKey": "inner"}, "ManifestType": "manifest_type", "ParentId": "parent_id", "RepoDigests": ["repo_digests"], "RepoTags": ["repo_tags"], "Size": 4, "VirtualSize": 12, "VulnerabilityCount": 19, "Vulnerable": "vulnerable"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_images()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_images_value_error(self):
        """
        test_list_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images')
        mock_response = '[{"ConfigurationIssueCount": 25, "Created": 7, "DigestTags": {"mapKey": ["inner"]}, "ExemptIssueCount": 18, "Id": "id", "IssueCount": 11, "Labels": {"mapKey": "inner"}, "ManifestType": "manifest_type", "ParentId": "parent_id", "RepoDigests": ["repo_digests"], "RepoTags": ["repo_tags"], "Size": 4, "VirtualSize": 12, "VulnerabilityCount": 19, "Vulnerable": "vulnerable"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_images(**req_copy)



class TestBulkDeleteImages():
    """
    Test Class for bulk_delete_images
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_bulk_delete_images_all_params(self):
        """
        bulk_delete_images()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/bulkdelete')
        mock_response = '{"error": {"mapKey": {"code": "code", "message": "message"}}, "success": ["success"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        bulk_delete = ['us.icr.io/birds/woodpecker@sha256:38f97dd92769b18ca82ad9ab6667af47306e66fea5b446937eea68b10ab4bbbb', 'us.icr.io/birds/bird@sha256:38f97dd92769b18ca82ad9ab6667af47306e66fea5b446937eea68b10ab4dddd']

        # Invoke method
        response = service.bulk_delete_images(
            bulk_delete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == bulk_delete


    @responses.activate
    def test_bulk_delete_images_value_error(self):
        """
        test_bulk_delete_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/bulkdelete')
        mock_response = '{"error": {"mapKey": {"code": "code", "message": "message"}}, "success": ["success"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        bulk_delete = ['us.icr.io/birds/woodpecker@sha256:38f97dd92769b18ca82ad9ab6667af47306e66fea5b446937eea68b10ab4bbbb', 'us.icr.io/birds/bird@sha256:38f97dd92769b18ca82ad9ab6667af47306e66fea5b446937eea68b10ab4dddd']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bulk_delete": bulk_delete,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.bulk_delete_images(**req_copy)



class TestListImageDigests():
    """
    Test Class for list_image_digests
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_image_digests_all_params(self):
        """
        list_image_digests()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/digests')
        mock_response = '[{"created": 7, "id": "id", "manifestType": "manifest_type", "repoTags": {"mapKey": {"mapKey": {"configurationIssueCount": 25, "exemptIssueCount": 18, "issueCount": 11, "vulnerabilityCount": 19, "vulnerable": "vulnerable"}}}, "size": 4}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        exclude_tagged = False
        exclude_va = False
        include_ibm = False
        repositories = ['testString']

        # Invoke method
        response = service.list_image_digests(
            exclude_tagged=exclude_tagged,
            exclude_va=exclude_va,
            include_ibm=include_ibm,
            repositories=repositories,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['exclude_tagged'] == False
        assert req_body['exclude_va'] == False
        assert req_body['include_ibm'] == False
        assert req_body['repositories'] == ['testString']


    @responses.activate
    def test_list_image_digests_value_error(self):
        """
        test_list_image_digests_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/digests')
        mock_response = '[{"created": 7, "id": "id", "manifestType": "manifest_type", "repoTags": {"mapKey": {"mapKey": {"configurationIssueCount": 25, "exemptIssueCount": 18, "issueCount": 11, "vulnerabilityCount": 19, "vulnerable": "vulnerable"}}}, "size": 4}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        exclude_tagged = False
        exclude_va = False
        include_ibm = False
        repositories = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_image_digests(**req_copy)



class TestTagImage():
    """
    Test Class for tag_image
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_tag_image_all_params(self):
        """
        tag_image()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/tags')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        fromimage = 'testString'
        toimage = 'testString'

        # Invoke method
        response = service.tag_image(
            fromimage,
            toimage,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'fromimage={}'.format(fromimage) in query_string
        assert 'toimage={}'.format(toimage) in query_string


    @responses.activate
    def test_tag_image_value_error(self):
        """
        test_tag_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/tags')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        fromimage = 'testString'
        toimage = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "fromimage": fromimage,
            "toimage": toimage,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.tag_image(**req_copy)



class TestDeleteImage():
    """
    Test Class for delete_image
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_image_all_params(self):
        """
        delete_image()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString')
        mock_response = '{"Untagged": "untagged"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Invoke method
        response = service.delete_image(
            image,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_image_value_error(self):
        """
        test_delete_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString')
        mock_response = '{"Untagged": "untagged"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image": image,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_image(**req_copy)



class TestInspectImage():
    """
    Test Class for inspect_image
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_inspect_image_all_params(self):
        """
        inspect_image()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString/json')
        mock_response = '{"Architecture": "architecture", "Author": "author", "Comment": "comment", "Config": {"ArgsEscaped": true, "AttachStderr": false, "AttachStdin": true, "AttachStdout": false, "Cmd": ["cmd"], "Domainname": "domainname", "Entrypoint": ["entrypoint"], "Env": ["env"], "ExposedPorts": {"mapKey": {"anyKey": "anyValue"}}, "Healthcheck": {"Interval": 8, "Retries": 7, "Test": ["test"], "Timeout": 7}, "Hostname": "hostname", "Image": "image", "Labels": {"mapKey": "inner"}, "MacAddress": "mac_address", "NetworkDisabled": true, "OnBuild": ["on_build"], "OpenStdin": true, "Shell": ["shell"], "StdinOnce": true, "StopSignal": "stop_signal", "StopTimeout": 12, "Tty": false, "User": "user", "Volumes": {"mapKey": {"anyKey": "anyValue"}}, "WorkingDir": "working_dir"}, "Container": "container", "ContainerConfig": {"ArgsEscaped": true, "AttachStderr": false, "AttachStdin": true, "AttachStdout": false, "Cmd": ["cmd"], "Domainname": "domainname", "Entrypoint": ["entrypoint"], "Env": ["env"], "ExposedPorts": {"mapKey": {"anyKey": "anyValue"}}, "Healthcheck": {"Interval": 8, "Retries": 7, "Test": ["test"], "Timeout": 7}, "Hostname": "hostname", "Image": "image", "Labels": {"mapKey": "inner"}, "MacAddress": "mac_address", "NetworkDisabled": true, "OnBuild": ["on_build"], "OpenStdin": true, "Shell": ["shell"], "StdinOnce": true, "StopSignal": "stop_signal", "StopTimeout": 12, "Tty": false, "User": "user", "Volumes": {"mapKey": {"anyKey": "anyValue"}}, "WorkingDir": "working_dir"}, "Created": "created", "DockerVersion": "docker_version", "Id": "id", "ManifestType": "manifest_type", "Os": "os", "OsVersion": "os_version", "Parent": "parent", "RootFS": {"BaseLayer": "base_layer", "Layers": ["layers"], "Type": "type"}, "Size": 4, "VirtualSize": 12}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Invoke method
        response = service.inspect_image(
            image,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_inspect_image_value_error(self):
        """
        test_inspect_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString/json')
        mock_response = '{"Architecture": "architecture", "Author": "author", "Comment": "comment", "Config": {"ArgsEscaped": true, "AttachStderr": false, "AttachStdin": true, "AttachStdout": false, "Cmd": ["cmd"], "Domainname": "domainname", "Entrypoint": ["entrypoint"], "Env": ["env"], "ExposedPorts": {"mapKey": {"anyKey": "anyValue"}}, "Healthcheck": {"Interval": 8, "Retries": 7, "Test": ["test"], "Timeout": 7}, "Hostname": "hostname", "Image": "image", "Labels": {"mapKey": "inner"}, "MacAddress": "mac_address", "NetworkDisabled": true, "OnBuild": ["on_build"], "OpenStdin": true, "Shell": ["shell"], "StdinOnce": true, "StopSignal": "stop_signal", "StopTimeout": 12, "Tty": false, "User": "user", "Volumes": {"mapKey": {"anyKey": "anyValue"}}, "WorkingDir": "working_dir"}, "Container": "container", "ContainerConfig": {"ArgsEscaped": true, "AttachStderr": false, "AttachStdin": true, "AttachStdout": false, "Cmd": ["cmd"], "Domainname": "domainname", "Entrypoint": ["entrypoint"], "Env": ["env"], "ExposedPorts": {"mapKey": {"anyKey": "anyValue"}}, "Healthcheck": {"Interval": 8, "Retries": 7, "Test": ["test"], "Timeout": 7}, "Hostname": "hostname", "Image": "image", "Labels": {"mapKey": "inner"}, "MacAddress": "mac_address", "NetworkDisabled": true, "OnBuild": ["on_build"], "OpenStdin": true, "Shell": ["shell"], "StdinOnce": true, "StopSignal": "stop_signal", "StopTimeout": 12, "Tty": false, "User": "user", "Volumes": {"mapKey": {"anyKey": "anyValue"}}, "WorkingDir": "working_dir"}, "Created": "created", "DockerVersion": "docker_version", "Id": "id", "ManifestType": "manifest_type", "Os": "os", "OsVersion": "os_version", "Parent": "parent", "RootFS": {"BaseLayer": "base_layer", "Layers": ["layers"], "Type": "type"}, "Size": 4, "VirtualSize": 12}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image": image,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.inspect_image(**req_copy)



class TestGetImageManifest():
    """
    Test Class for get_image_manifest
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_image_manifest_all_params(self):
        """
        get_image_manifest()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString/manifest')
        mock_response = '{"mapKey": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Invoke method
        response = service.get_image_manifest(
            image,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_image_manifest_value_error(self):
        """
        test_get_image_manifest_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/images/testString/manifest')
        mock_response = '{"mapKey": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image": image,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_image_manifest(**req_copy)



# endregion
##############################################################################
# End of Service: Images
##############################################################################

##############################################################################
# Start of Service: Messages
##############################################################################
# region

class TestGetMessages():
    """
    Test Class for get_messages
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_messages_all_params(self):
        """
        get_messages()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/messages')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_messages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Messages
##############################################################################

##############################################################################
# Start of Service: Namespaces
##############################################################################
# region

class TestListNamespaces():
    """
    Test Class for list_namespaces
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_namespaces_all_params(self):
        """
        list_namespaces()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces')
        mock_response = '["operation_response"]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_namespaces()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_namespaces_value_error(self):
        """
        test_list_namespaces_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces')
        mock_response = '["operation_response"]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_namespaces(**req_copy)



class TestListNamespaceDetails():
    """
    Test Class for list_namespace_details
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_namespace_details_all_params(self):
        """
        list_namespace_details()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/details')
        mock_response = '[{"account": "account", "created_date": "created_date", "crn": "crn", "name": "name", "resource_created_date": "resource_created_date", "resource_group": "resource_group", "updated_date": "updated_date"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_namespace_details()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_namespace_details_value_error(self):
        """
        test_list_namespace_details_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/details')
        mock_response = '[{"account": "account", "created_date": "created_date", "crn": "crn", "name": "name", "resource_created_date": "resource_created_date", "resource_group": "resource_group", "updated_date": "updated_date"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_namespace_details(**req_copy)



class TestCreateNamespace():
    """
    Test Class for create_namespace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_namespace_all_params(self):
        """
        create_namespace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        mock_response = '{"namespace": "namespace"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'
        x_auth_resource_group = 'testString'

        # Invoke method
        response = service.create_namespace(
            name,
            x_auth_resource_group=x_auth_resource_group,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_namespace_required_params(self):
        """
        test_create_namespace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        mock_response = '{"namespace": "namespace"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Invoke method
        response = service.create_namespace(
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_namespace_value_error(self):
        """
        test_create_namespace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        mock_response = '{"namespace": "namespace"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_namespace(**req_copy)



class TestAssignNamespace():
    """
    Test Class for assign_namespace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_assign_namespace_all_params(self):
        """
        assign_namespace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        mock_response = '{"namespace": "namespace"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_resource_group = 'testString'
        name = 'testString'

        # Invoke method
        response = service.assign_namespace(
            x_auth_resource_group,
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_assign_namespace_value_error(self):
        """
        test_assign_namespace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        mock_response = '{"namespace": "namespace"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_resource_group = 'testString'
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_resource_group": x_auth_resource_group,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.assign_namespace(**req_copy)



class TestDeleteNamespace():
    """
    Test Class for delete_namespace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_namespace_all_params(self):
        """
        delete_namespace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        name = 'testString'

        # Invoke method
        response = service.delete_namespace(
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_namespace_value_error(self):
        """
        test_delete_namespace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/namespaces/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_namespace(**req_copy)



# endregion
##############################################################################
# End of Service: Namespaces
##############################################################################

##############################################################################
# Start of Service: Plans
##############################################################################
# region

class TestGetPlans():
    """
    Test Class for get_plans
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_plans_all_params(self):
        """
        get_plans()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/plans')
        mock_response = '{"plan": "plan"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_plans()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_plans_value_error(self):
        """
        test_get_plans_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/plans')
        mock_response = '{"plan": "plan"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_plans(**req_copy)



class TestUpdatePlans():
    """
    Test Class for update_plans
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_plans_all_params(self):
        """
        update_plans()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/plans')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        plan = 'Standard'

        # Invoke method
        response = service.update_plans(
            plan=plan,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['plan'] == 'Standard'


    @responses.activate
    def test_update_plans_value_error(self):
        """
        test_update_plans_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/plans')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        plan = 'Standard'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_plans(**req_copy)



# endregion
##############################################################################
# End of Service: Plans
##############################################################################

##############################################################################
# Start of Service: Quotas
##############################################################################
# region

class TestGetQuota():
    """
    Test Class for get_quota
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_quota_all_params(self):
        """
        get_quota()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/quotas')
        mock_response = '{"limit": {"storage_bytes": 13, "traffic_bytes": 13}, "usage": {"storage_bytes": 13, "traffic_bytes": 13}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_quota()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_quota_value_error(self):
        """
        test_get_quota_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/quotas')
        mock_response = '{"limit": {"storage_bytes": 13, "traffic_bytes": 13}, "usage": {"storage_bytes": 13, "traffic_bytes": 13}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_quota(**req_copy)



class TestUpdateQuota():
    """
    Test Class for update_quota
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_quota_all_params(self):
        """
        update_quota()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/quotas')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        storage_megabytes = 26
        traffic_megabytes = 480

        # Invoke method
        response = service.update_quota(
            storage_megabytes=storage_megabytes,
            traffic_megabytes=traffic_megabytes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['storage_megabytes'] == 26
        assert req_body['traffic_megabytes'] == 480


    @responses.activate
    def test_update_quota_value_error(self):
        """
        test_update_quota_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/quotas')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        storage_megabytes = 26
        traffic_megabytes = 480

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_quota(**req_copy)



# endregion
##############################################################################
# End of Service: Quotas
##############################################################################

##############################################################################
# Start of Service: Retentions
##############################################################################
# region

class TestListRetentionPolicies():
    """
    Test Class for list_retention_policies
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_retention_policies_all_params(self):
        """
        list_retention_policies()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions')
        mock_response = '{"mapKey": {"images_per_repo": 15, "namespace": "namespace", "retain_untagged": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_retention_policies()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_retention_policies_value_error(self):
        """
        test_list_retention_policies_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions')
        mock_response = '{"mapKey": {"images_per_repo": 15, "namespace": "namespace", "retain_untagged": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_retention_policies(**req_copy)



class TestSetRetentionPolicy():
    """
    Test Class for set_retention_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_set_retention_policy_all_params(self):
        """
        set_retention_policy()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        namespace = 'birds'
        images_per_repo = 10
        retain_untagged = False

        # Invoke method
        response = service.set_retention_policy(
            namespace,
            images_per_repo=images_per_repo,
            retain_untagged=retain_untagged,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['namespace'] == 'birds'
        assert req_body['images_per_repo'] == 10
        assert req_body['retain_untagged'] == False


    @responses.activate
    def test_set_retention_policy_value_error(self):
        """
        test_set_retention_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        namespace = 'birds'
        images_per_repo = 10
        retain_untagged = False

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "namespace": namespace,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_retention_policy(**req_copy)



class TestAnalyzeRetentionPolicy():
    """
    Test Class for analyze_retention_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_analyze_retention_policy_all_params(self):
        """
        analyze_retention_policy()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions/analyze')
        mock_response = '{"mapKey": ["inner"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'birds'
        images_per_repo = 10
        retain_untagged = False

        # Invoke method
        response = service.analyze_retention_policy(
            namespace,
            images_per_repo=images_per_repo,
            retain_untagged=retain_untagged,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['namespace'] == 'birds'
        assert req_body['images_per_repo'] == 10
        assert req_body['retain_untagged'] == False


    @responses.activate
    def test_analyze_retention_policy_value_error(self):
        """
        test_analyze_retention_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions/analyze')
        mock_response = '{"mapKey": ["inner"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'birds'
        images_per_repo = 10
        retain_untagged = False

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "namespace": namespace,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.analyze_retention_policy(**req_copy)



class TestGetRetentionPolicy():
    """
    Test Class for get_retention_policy
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_retention_policy_all_params(self):
        """
        get_retention_policy()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions/testString')
        mock_response = '{"images_per_repo": 15, "namespace": "namespace", "retain_untagged": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'testString'

        # Invoke method
        response = service.get_retention_policy(
            namespace,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_retention_policy_value_error(self):
        """
        test_get_retention_policy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/retentions/testString')
        mock_response = '{"images_per_repo": 15, "namespace": "namespace", "retain_untagged": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "namespace": namespace,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_retention_policy(**req_copy)



# endregion
##############################################################################
# End of Service: Retentions
##############################################################################

##############################################################################
# Start of Service: Settings
##############################################################################
# region

class TestGetSettings():
    """
    Test Class for get_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_settings_all_params(self):
        """
        get_settings()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/settings')
        mock_response = '{"platform_metrics": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_settings_value_error(self):
        """
        test_get_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/settings')
        mock_response = '{"platform_metrics": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_settings(**req_copy)



class TestUpdateSettings():
    """
    Test Class for update_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_settings_all_params(self):
        """
        update_settings()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/settings')
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        platform_metrics = True

        # Invoke method
        response = service.update_settings(
            platform_metrics=platform_metrics,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['platform_metrics'] == True


    @responses.activate
    def test_update_settings_value_error(self):
        """
        test_update_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/settings')
        responses.add(responses.PATCH,
                      url,
                      status=204)

        # Set up parameter values
        platform_metrics = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_settings(**req_copy)



# endregion
##############################################################################
# End of Service: Settings
##############################################################################

##############################################################################
# Start of Service: Tags
##############################################################################
# region

class TestDeleteImageTag():
    """
    Test Class for delete_image_tag
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_image_tag_all_params(self):
        """
        delete_image_tag()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/tags/testString')
        mock_response = '{"Untagged": "untagged"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Invoke method
        response = service.delete_image_tag(
            image,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_image_tag_value_error(self):
        """
        test_delete_image_tag_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/tags/testString')
        mock_response = '{"Untagged": "untagged"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image": image,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_image_tag(**req_copy)



# endregion
##############################################################################
# End of Service: Tags
##############################################################################

##############################################################################
# Start of Service: Trash
##############################################################################
# region

class TestListDeletedImages():
    """
    Test Class for list_deleted_images
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_deleted_images_all_params(self):
        """
        list_deleted_images()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash')
        mock_response = '{"mapKey": {"daysUntilExpiry": 17, "tags": ["tags"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        namespace = 'testString'

        # Invoke method
        response = service.list_deleted_images(
            namespace=namespace,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'namespace={}'.format(namespace) in query_string


    @responses.activate
    def test_list_deleted_images_required_params(self):
        """
        test_list_deleted_images_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash')
        mock_response = '{"mapKey": {"daysUntilExpiry": 17, "tags": ["tags"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_deleted_images()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_deleted_images_value_error(self):
        """
        test_list_deleted_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash')
        mock_response = '{"mapKey": {"daysUntilExpiry": 17, "tags": ["tags"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_deleted_images(**req_copy)



class TestRestoreTags():
    """
    Test Class for restore_tags
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_restore_tags_all_params(self):
        """
        restore_tags()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash/testString/restoretags')
        mock_response = '{"successful": ["successful"], "unsuccessful": ["unsuccessful"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        digest = 'testString'

        # Invoke method
        response = service.restore_tags(
            digest,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_restore_tags_value_error(self):
        """
        test_restore_tags_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash/testString/restoretags')
        mock_response = '{"successful": ["successful"], "unsuccessful": ["unsuccessful"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        digest = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "digest": digest,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.restore_tags(**req_copy)



class TestRestoreImage():
    """
    Test Class for restore_image
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_restore_image_all_params(self):
        """
        restore_image()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash/testString/restore')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Invoke method
        response = service.restore_image(
            image,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_restore_image_value_error(self):
        """
        test_restore_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/api/v1/trash/testString/restore')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        image = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image": image,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.restore_image(**req_copy)



# endregion
##############################################################################
# End of Service: Trash
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestAccountSettings():
    """
    Test Class for AccountSettings
    """

    def test_account_settings_serialization(self):
        """
        Test serialization/deserialization for AccountSettings
        """

        # Construct a json representation of a AccountSettings model
        account_settings_model_json = {}
        account_settings_model_json['platform_metrics'] = True

        # Construct a model instance of AccountSettings by calling from_dict on the json representation
        account_settings_model = AccountSettings.from_dict(account_settings_model_json)
        assert account_settings_model != False

        # Construct a model instance of AccountSettings by calling from_dict on the json representation
        account_settings_model_dict = AccountSettings.from_dict(account_settings_model_json).__dict__
        account_settings_model2 = AccountSettings(**account_settings_model_dict)

        # Verify the model instances are equivalent
        assert account_settings_model == account_settings_model2

        # Convert model instance back to dict and verify no loss of data
        account_settings_model_json2 = account_settings_model.to_dict()
        assert account_settings_model_json2 == account_settings_model_json

class TestAuthOptions():
    """
    Test Class for AuthOptions
    """

    def test_auth_options_serialization(self):
        """
        Test serialization/deserialization for AuthOptions
        """

        # Construct a json representation of a AuthOptions model
        auth_options_model_json = {}
        auth_options_model_json['iam_authz'] = True
        auth_options_model_json['private_only'] = True

        # Construct a model instance of AuthOptions by calling from_dict on the json representation
        auth_options_model = AuthOptions.from_dict(auth_options_model_json)
        assert auth_options_model != False

        # Construct a model instance of AuthOptions by calling from_dict on the json representation
        auth_options_model_dict = AuthOptions.from_dict(auth_options_model_json).__dict__
        auth_options_model2 = AuthOptions(**auth_options_model_dict)

        # Verify the model instances are equivalent
        assert auth_options_model == auth_options_model2

        # Convert model instance back to dict and verify no loss of data
        auth_options_model_json2 = auth_options_model.to_dict()
        assert auth_options_model_json2 == auth_options_model_json

class TestConfig():
    """
    Test Class for Config
    """

    def test_config_serialization(self):
        """
        Test serialization/deserialization for Config
        """

        # Construct dict forms of any model objects needed in order to build this model.

        health_config_model = {} # HealthConfig
        health_config_model['Interval'] = 26
        health_config_model['Retries'] = 26
        health_config_model['Test'] = ['testString']
        health_config_model['Timeout'] = 26

        # Construct a json representation of a Config model
        config_model_json = {}
        config_model_json['ArgsEscaped'] = True
        config_model_json['AttachStderr'] = True
        config_model_json['AttachStdin'] = True
        config_model_json['AttachStdout'] = True
        config_model_json['Cmd'] = ['testString']
        config_model_json['Domainname'] = 'testString'
        config_model_json['Entrypoint'] = ['testString']
        config_model_json['Env'] = ['testString']
        config_model_json['ExposedPorts'] = {}
        config_model_json['Healthcheck'] = health_config_model
        config_model_json['Hostname'] = 'testString'
        config_model_json['Image'] = 'testString'
        config_model_json['Labels'] = {}
        config_model_json['MacAddress'] = 'testString'
        config_model_json['NetworkDisabled'] = True
        config_model_json['OnBuild'] = ['testString']
        config_model_json['OpenStdin'] = True
        config_model_json['Shell'] = ['testString']
        config_model_json['StdinOnce'] = True
        config_model_json['StopSignal'] = 'testString'
        config_model_json['StopTimeout'] = 26
        config_model_json['Tty'] = True
        config_model_json['User'] = 'testString'
        config_model_json['Volumes'] = {}
        config_model_json['WorkingDir'] = 'testString'

        # Construct a model instance of Config by calling from_dict on the json representation
        config_model = Config.from_dict(config_model_json)
        assert config_model != False

        # Construct a model instance of Config by calling from_dict on the json representation
        config_model_dict = Config.from_dict(config_model_json).__dict__
        config_model2 = Config(**config_model_dict)

        # Verify the model instances are equivalent
        assert config_model == config_model2

        # Convert model instance back to dict and verify no loss of data
        config_model_json2 = config_model.to_dict()
        assert config_model_json2 == config_model_json

class TestHealthConfig():
    """
    Test Class for HealthConfig
    """

    def test_health_config_serialization(self):
        """
        Test serialization/deserialization for HealthConfig
        """

        # Construct a json representation of a HealthConfig model
        health_config_model_json = {}
        health_config_model_json['Interval'] = 26
        health_config_model_json['Retries'] = 26
        health_config_model_json['Test'] = ['testString']
        health_config_model_json['Timeout'] = 26

        # Construct a model instance of HealthConfig by calling from_dict on the json representation
        health_config_model = HealthConfig.from_dict(health_config_model_json)
        assert health_config_model != False

        # Construct a model instance of HealthConfig by calling from_dict on the json representation
        health_config_model_dict = HealthConfig.from_dict(health_config_model_json).__dict__
        health_config_model2 = HealthConfig(**health_config_model_dict)

        # Verify the model instances are equivalent
        assert health_config_model == health_config_model2

        # Convert model instance back to dict and verify no loss of data
        health_config_model_json2 = health_config_model.to_dict()
        assert health_config_model_json2 == health_config_model_json

class TestImageBulkDeleteError():
    """
    Test Class for ImageBulkDeleteError
    """

    def test_image_bulk_delete_error_serialization(self):
        """
        Test serialization/deserialization for ImageBulkDeleteError
        """

        # Construct a json representation of a ImageBulkDeleteError model
        image_bulk_delete_error_model_json = {}
        image_bulk_delete_error_model_json['code'] = 'testString'
        image_bulk_delete_error_model_json['message'] = 'testString'

        # Construct a model instance of ImageBulkDeleteError by calling from_dict on the json representation
        image_bulk_delete_error_model = ImageBulkDeleteError.from_dict(image_bulk_delete_error_model_json)
        assert image_bulk_delete_error_model != False

        # Construct a model instance of ImageBulkDeleteError by calling from_dict on the json representation
        image_bulk_delete_error_model_dict = ImageBulkDeleteError.from_dict(image_bulk_delete_error_model_json).__dict__
        image_bulk_delete_error_model2 = ImageBulkDeleteError(**image_bulk_delete_error_model_dict)

        # Verify the model instances are equivalent
        assert image_bulk_delete_error_model == image_bulk_delete_error_model2

        # Convert model instance back to dict and verify no loss of data
        image_bulk_delete_error_model_json2 = image_bulk_delete_error_model.to_dict()
        assert image_bulk_delete_error_model_json2 == image_bulk_delete_error_model_json

class TestImageBulkDeleteResult():
    """
    Test Class for ImageBulkDeleteResult
    """

    def test_image_bulk_delete_result_serialization(self):
        """
        Test serialization/deserialization for ImageBulkDeleteResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_bulk_delete_error_model = {} # ImageBulkDeleteError
        image_bulk_delete_error_model['code'] = 'testString'
        image_bulk_delete_error_model['message'] = 'testString'

        # Construct a json representation of a ImageBulkDeleteResult model
        image_bulk_delete_result_model_json = {}
        image_bulk_delete_result_model_json['error'] = {}
        image_bulk_delete_result_model_json['success'] = ['testString']

        # Construct a model instance of ImageBulkDeleteResult by calling from_dict on the json representation
        image_bulk_delete_result_model = ImageBulkDeleteResult.from_dict(image_bulk_delete_result_model_json)
        assert image_bulk_delete_result_model != False

        # Construct a model instance of ImageBulkDeleteResult by calling from_dict on the json representation
        image_bulk_delete_result_model_dict = ImageBulkDeleteResult.from_dict(image_bulk_delete_result_model_json).__dict__
        image_bulk_delete_result_model2 = ImageBulkDeleteResult(**image_bulk_delete_result_model_dict)

        # Verify the model instances are equivalent
        assert image_bulk_delete_result_model == image_bulk_delete_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_bulk_delete_result_model_json2 = image_bulk_delete_result_model.to_dict()
        assert image_bulk_delete_result_model_json2 == image_bulk_delete_result_model_json

class TestImageDeleteResult():
    """
    Test Class for ImageDeleteResult
    """

    def test_image_delete_result_serialization(self):
        """
        Test serialization/deserialization for ImageDeleteResult
        """

        # Construct a json representation of a ImageDeleteResult model
        image_delete_result_model_json = {}
        image_delete_result_model_json['Untagged'] = 'testString'

        # Construct a model instance of ImageDeleteResult by calling from_dict on the json representation
        image_delete_result_model = ImageDeleteResult.from_dict(image_delete_result_model_json)
        assert image_delete_result_model != False

        # Construct a model instance of ImageDeleteResult by calling from_dict on the json representation
        image_delete_result_model_dict = ImageDeleteResult.from_dict(image_delete_result_model_json).__dict__
        image_delete_result_model2 = ImageDeleteResult(**image_delete_result_model_dict)

        # Verify the model instances are equivalent
        assert image_delete_result_model == image_delete_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_delete_result_model_json2 = image_delete_result_model.to_dict()
        assert image_delete_result_model_json2 == image_delete_result_model_json

class TestImageDigest():
    """
    Test Class for ImageDigest
    """

    def test_image_digest_serialization(self):
        """
        Test serialization/deserialization for ImageDigest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        va_report_model = {} # VAReport
        va_report_model['configurationIssueCount'] = 26
        va_report_model['exemptIssueCount'] = 26
        va_report_model['issueCount'] = 26
        va_report_model['vulnerabilityCount'] = 26
        va_report_model['vulnerable'] = 'testString'

        # Construct a json representation of a ImageDigest model
        image_digest_model_json = {}
        image_digest_model_json['created'] = 26
        image_digest_model_json['id'] = 'testString'
        image_digest_model_json['manifestType'] = 'testString'
        image_digest_model_json['repoTags'] = {}
        image_digest_model_json['size'] = 26

        # Construct a model instance of ImageDigest by calling from_dict on the json representation
        image_digest_model = ImageDigest.from_dict(image_digest_model_json)
        assert image_digest_model != False

        # Construct a model instance of ImageDigest by calling from_dict on the json representation
        image_digest_model_dict = ImageDigest.from_dict(image_digest_model_json).__dict__
        image_digest_model2 = ImageDigest(**image_digest_model_dict)

        # Verify the model instances are equivalent
        assert image_digest_model == image_digest_model2

        # Convert model instance back to dict and verify no loss of data
        image_digest_model_json2 = image_digest_model.to_dict()
        assert image_digest_model_json2 == image_digest_model_json

class TestImageInspection():
    """
    Test Class for ImageInspection
    """

    def test_image_inspection_serialization(self):
        """
        Test serialization/deserialization for ImageInspection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        health_config_model = {} # HealthConfig
        health_config_model['Interval'] = 26
        health_config_model['Retries'] = 26
        health_config_model['Test'] = ['testString']
        health_config_model['Timeout'] = 26

        config_model = {} # Config
        config_model['ArgsEscaped'] = True
        config_model['AttachStderr'] = True
        config_model['AttachStdin'] = True
        config_model['AttachStdout'] = True
        config_model['Cmd'] = ['testString']
        config_model['Domainname'] = 'testString'
        config_model['Entrypoint'] = ['testString']
        config_model['Env'] = ['testString']
        config_model['ExposedPorts'] = {}
        config_model['Healthcheck'] = health_config_model
        config_model['Hostname'] = 'testString'
        config_model['Image'] = 'testString'
        config_model['Labels'] = {}
        config_model['MacAddress'] = 'testString'
        config_model['NetworkDisabled'] = True
        config_model['OnBuild'] = ['testString']
        config_model['OpenStdin'] = True
        config_model['Shell'] = ['testString']
        config_model['StdinOnce'] = True
        config_model['StopSignal'] = 'testString'
        config_model['StopTimeout'] = 26
        config_model['Tty'] = True
        config_model['User'] = 'testString'
        config_model['Volumes'] = {}
        config_model['WorkingDir'] = 'testString'

        root_fs_model = {} # RootFS
        root_fs_model['BaseLayer'] = 'testString'
        root_fs_model['Layers'] = ['testString']
        root_fs_model['Type'] = 'testString'

        # Construct a json representation of a ImageInspection model
        image_inspection_model_json = {}
        image_inspection_model_json['Architecture'] = 'testString'
        image_inspection_model_json['Author'] = 'testString'
        image_inspection_model_json['Comment'] = 'testString'
        image_inspection_model_json['Config'] = config_model
        image_inspection_model_json['Container'] = 'testString'
        image_inspection_model_json['ContainerConfig'] = config_model
        image_inspection_model_json['Created'] = 'testString'
        image_inspection_model_json['DockerVersion'] = 'testString'
        image_inspection_model_json['Id'] = 'testString'
        image_inspection_model_json['ManifestType'] = 'testString'
        image_inspection_model_json['Os'] = 'testString'
        image_inspection_model_json['OsVersion'] = 'testString'
        image_inspection_model_json['Parent'] = 'testString'
        image_inspection_model_json['RootFS'] = root_fs_model
        image_inspection_model_json['Size'] = 26
        image_inspection_model_json['VirtualSize'] = 26

        # Construct a model instance of ImageInspection by calling from_dict on the json representation
        image_inspection_model = ImageInspection.from_dict(image_inspection_model_json)
        assert image_inspection_model != False

        # Construct a model instance of ImageInspection by calling from_dict on the json representation
        image_inspection_model_dict = ImageInspection.from_dict(image_inspection_model_json).__dict__
        image_inspection_model2 = ImageInspection(**image_inspection_model_dict)

        # Verify the model instances are equivalent
        assert image_inspection_model == image_inspection_model2

        # Convert model instance back to dict and verify no loss of data
        image_inspection_model_json2 = image_inspection_model.to_dict()
        assert image_inspection_model_json2 == image_inspection_model_json

class TestNamespace():
    """
    Test Class for Namespace
    """

    def test_namespace_serialization(self):
        """
        Test serialization/deserialization for Namespace
        """

        # Construct a json representation of a Namespace model
        namespace_model_json = {}
        namespace_model_json['namespace'] = 'testString'

        # Construct a model instance of Namespace by calling from_dict on the json representation
        namespace_model = Namespace.from_dict(namespace_model_json)
        assert namespace_model != False

        # Construct a model instance of Namespace by calling from_dict on the json representation
        namespace_model_dict = Namespace.from_dict(namespace_model_json).__dict__
        namespace_model2 = Namespace(**namespace_model_dict)

        # Verify the model instances are equivalent
        assert namespace_model == namespace_model2

        # Convert model instance back to dict and verify no loss of data
        namespace_model_json2 = namespace_model.to_dict()
        assert namespace_model_json2 == namespace_model_json

class TestNamespaceDetails():
    """
    Test Class for NamespaceDetails
    """

    def test_namespace_details_serialization(self):
        """
        Test serialization/deserialization for NamespaceDetails
        """

        # Construct a json representation of a NamespaceDetails model
        namespace_details_model_json = {}
        namespace_details_model_json['account'] = 'testString'
        namespace_details_model_json['created_date'] = 'testString'
        namespace_details_model_json['crn'] = 'testString'
        namespace_details_model_json['name'] = 'testString'
        namespace_details_model_json['resource_created_date'] = 'testString'
        namespace_details_model_json['resource_group'] = 'testString'
        namespace_details_model_json['updated_date'] = 'testString'

        # Construct a model instance of NamespaceDetails by calling from_dict on the json representation
        namespace_details_model = NamespaceDetails.from_dict(namespace_details_model_json)
        assert namespace_details_model != False

        # Construct a model instance of NamespaceDetails by calling from_dict on the json representation
        namespace_details_model_dict = NamespaceDetails.from_dict(namespace_details_model_json).__dict__
        namespace_details_model2 = NamespaceDetails(**namespace_details_model_dict)

        # Verify the model instances are equivalent
        assert namespace_details_model == namespace_details_model2

        # Convert model instance back to dict and verify no loss of data
        namespace_details_model_json2 = namespace_details_model.to_dict()
        assert namespace_details_model_json2 == namespace_details_model_json

class TestPlan():
    """
    Test Class for Plan
    """

    def test_plan_serialization(self):
        """
        Test serialization/deserialization for Plan
        """

        # Construct a json representation of a Plan model
        plan_model_json = {}
        plan_model_json['plan'] = 'testString'

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model = Plan.from_dict(plan_model_json)
        assert plan_model != False

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model_dict = Plan.from_dict(plan_model_json).__dict__
        plan_model2 = Plan(**plan_model_dict)

        # Verify the model instances are equivalent
        assert plan_model == plan_model2

        # Convert model instance back to dict and verify no loss of data
        plan_model_json2 = plan_model.to_dict()
        assert plan_model_json2 == plan_model_json

class TestQuota():
    """
    Test Class for Quota
    """

    def test_quota_serialization(self):
        """
        Test serialization/deserialization for Quota
        """

        # Construct dict forms of any model objects needed in order to build this model.

        quota_details_model = {} # QuotaDetails
        quota_details_model['storage_bytes'] = 26
        quota_details_model['traffic_bytes'] = 26

        # Construct a json representation of a Quota model
        quota_model_json = {}
        quota_model_json['limit'] = quota_details_model
        quota_model_json['usage'] = quota_details_model

        # Construct a model instance of Quota by calling from_dict on the json representation
        quota_model = Quota.from_dict(quota_model_json)
        assert quota_model != False

        # Construct a model instance of Quota by calling from_dict on the json representation
        quota_model_dict = Quota.from_dict(quota_model_json).__dict__
        quota_model2 = Quota(**quota_model_dict)

        # Verify the model instances are equivalent
        assert quota_model == quota_model2

        # Convert model instance back to dict and verify no loss of data
        quota_model_json2 = quota_model.to_dict()
        assert quota_model_json2 == quota_model_json

class TestQuotaDetails():
    """
    Test Class for QuotaDetails
    """

    def test_quota_details_serialization(self):
        """
        Test serialization/deserialization for QuotaDetails
        """

        # Construct a json representation of a QuotaDetails model
        quota_details_model_json = {}
        quota_details_model_json['storage_bytes'] = 26
        quota_details_model_json['traffic_bytes'] = 26

        # Construct a model instance of QuotaDetails by calling from_dict on the json representation
        quota_details_model = QuotaDetails.from_dict(quota_details_model_json)
        assert quota_details_model != False

        # Construct a model instance of QuotaDetails by calling from_dict on the json representation
        quota_details_model_dict = QuotaDetails.from_dict(quota_details_model_json).__dict__
        quota_details_model2 = QuotaDetails(**quota_details_model_dict)

        # Verify the model instances are equivalent
        assert quota_details_model == quota_details_model2

        # Convert model instance back to dict and verify no loss of data
        quota_details_model_json2 = quota_details_model.to_dict()
        assert quota_details_model_json2 == quota_details_model_json

class TestRemoteAPIImage():
    """
    Test Class for RemoteAPIImage
    """

    def test_remote_api_image_serialization(self):
        """
        Test serialization/deserialization for RemoteAPIImage
        """

        # Construct a json representation of a RemoteAPIImage model
        remote_api_image_model_json = {}
        remote_api_image_model_json['ConfigurationIssueCount'] = 26
        remote_api_image_model_json['Created'] = 26
        remote_api_image_model_json['DigestTags'] = {}
        remote_api_image_model_json['ExemptIssueCount'] = 26
        remote_api_image_model_json['Id'] = 'testString'
        remote_api_image_model_json['IssueCount'] = 26
        remote_api_image_model_json['Labels'] = {}
        remote_api_image_model_json['ManifestType'] = 'testString'
        remote_api_image_model_json['ParentId'] = 'testString'
        remote_api_image_model_json['RepoDigests'] = ['testString']
        remote_api_image_model_json['RepoTags'] = ['testString']
        remote_api_image_model_json['Size'] = 26
        remote_api_image_model_json['VirtualSize'] = 26
        remote_api_image_model_json['VulnerabilityCount'] = 26
        remote_api_image_model_json['Vulnerable'] = 'testString'

        # Construct a model instance of RemoteAPIImage by calling from_dict on the json representation
        remote_api_image_model = RemoteAPIImage.from_dict(remote_api_image_model_json)
        assert remote_api_image_model != False

        # Construct a model instance of RemoteAPIImage by calling from_dict on the json representation
        remote_api_image_model_dict = RemoteAPIImage.from_dict(remote_api_image_model_json).__dict__
        remote_api_image_model2 = RemoteAPIImage(**remote_api_image_model_dict)

        # Verify the model instances are equivalent
        assert remote_api_image_model == remote_api_image_model2

        # Convert model instance back to dict and verify no loss of data
        remote_api_image_model_json2 = remote_api_image_model.to_dict()
        assert remote_api_image_model_json2 == remote_api_image_model_json

class TestRestoreResult():
    """
    Test Class for RestoreResult
    """

    def test_restore_result_serialization(self):
        """
        Test serialization/deserialization for RestoreResult
        """

        # Construct a json representation of a RestoreResult model
        restore_result_model_json = {}
        restore_result_model_json['successful'] = ['testString']
        restore_result_model_json['unsuccessful'] = ['testString']

        # Construct a model instance of RestoreResult by calling from_dict on the json representation
        restore_result_model = RestoreResult.from_dict(restore_result_model_json)
        assert restore_result_model != False

        # Construct a model instance of RestoreResult by calling from_dict on the json representation
        restore_result_model_dict = RestoreResult.from_dict(restore_result_model_json).__dict__
        restore_result_model2 = RestoreResult(**restore_result_model_dict)

        # Verify the model instances are equivalent
        assert restore_result_model == restore_result_model2

        # Convert model instance back to dict and verify no loss of data
        restore_result_model_json2 = restore_result_model.to_dict()
        assert restore_result_model_json2 == restore_result_model_json

class TestRetentionPolicy():
    """
    Test Class for RetentionPolicy
    """

    def test_retention_policy_serialization(self):
        """
        Test serialization/deserialization for RetentionPolicy
        """

        # Construct a json representation of a RetentionPolicy model
        retention_policy_model_json = {}
        retention_policy_model_json['images_per_repo'] = 26
        retention_policy_model_json['namespace'] = 'testString'
        retention_policy_model_json['retain_untagged'] = True

        # Construct a model instance of RetentionPolicy by calling from_dict on the json representation
        retention_policy_model = RetentionPolicy.from_dict(retention_policy_model_json)
        assert retention_policy_model != False

        # Construct a model instance of RetentionPolicy by calling from_dict on the json representation
        retention_policy_model_dict = RetentionPolicy.from_dict(retention_policy_model_json).__dict__
        retention_policy_model2 = RetentionPolicy(**retention_policy_model_dict)

        # Verify the model instances are equivalent
        assert retention_policy_model == retention_policy_model2

        # Convert model instance back to dict and verify no loss of data
        retention_policy_model_json2 = retention_policy_model.to_dict()
        assert retention_policy_model_json2 == retention_policy_model_json

class TestRootFS():
    """
    Test Class for RootFS
    """

    def test_root_fs_serialization(self):
        """
        Test serialization/deserialization for RootFS
        """

        # Construct a json representation of a RootFS model
        root_fs_model_json = {}
        root_fs_model_json['BaseLayer'] = 'testString'
        root_fs_model_json['Layers'] = ['testString']
        root_fs_model_json['Type'] = 'testString'

        # Construct a model instance of RootFS by calling from_dict on the json representation
        root_fs_model = RootFS.from_dict(root_fs_model_json)
        assert root_fs_model != False

        # Construct a model instance of RootFS by calling from_dict on the json representation
        root_fs_model_dict = RootFS.from_dict(root_fs_model_json).__dict__
        root_fs_model2 = RootFS(**root_fs_model_dict)

        # Verify the model instances are equivalent
        assert root_fs_model == root_fs_model2

        # Convert model instance back to dict and verify no loss of data
        root_fs_model_json2 = root_fs_model.to_dict()
        assert root_fs_model_json2 == root_fs_model_json

class TestTrash():
    """
    Test Class for Trash
    """

    def test_trash_serialization(self):
        """
        Test serialization/deserialization for Trash
        """

        # Construct a json representation of a Trash model
        trash_model_json = {}
        trash_model_json['daysUntilExpiry'] = 26
        trash_model_json['tags'] = ['testString']

        # Construct a model instance of Trash by calling from_dict on the json representation
        trash_model = Trash.from_dict(trash_model_json)
        assert trash_model != False

        # Construct a model instance of Trash by calling from_dict on the json representation
        trash_model_dict = Trash.from_dict(trash_model_json).__dict__
        trash_model2 = Trash(**trash_model_dict)

        # Verify the model instances are equivalent
        assert trash_model == trash_model2

        # Convert model instance back to dict and verify no loss of data
        trash_model_json2 = trash_model.to_dict()
        assert trash_model_json2 == trash_model_json

class TestVAReport():
    """
    Test Class for VAReport
    """

    def test_va_report_serialization(self):
        """
        Test serialization/deserialization for VAReport
        """

        # Construct a json representation of a VAReport model
        va_report_model_json = {}
        va_report_model_json['configurationIssueCount'] = 26
        va_report_model_json['exemptIssueCount'] = 26
        va_report_model_json['issueCount'] = 26
        va_report_model_json['vulnerabilityCount'] = 26
        va_report_model_json['vulnerable'] = 'testString'

        # Construct a model instance of VAReport by calling from_dict on the json representation
        va_report_model = VAReport.from_dict(va_report_model_json)
        assert va_report_model != False

        # Construct a model instance of VAReport by calling from_dict on the json representation
        va_report_model_dict = VAReport.from_dict(va_report_model_json).__dict__
        va_report_model2 = VAReport(**va_report_model_dict)

        # Verify the model instances are equivalent
        assert va_report_model == va_report_model2

        # Convert model instance back to dict and verify no loss of data
        va_report_model_json2 = va_report_model.to_dict()
        assert va_report_model_json2 == va_report_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
