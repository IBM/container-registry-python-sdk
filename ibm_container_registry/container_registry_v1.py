# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.29.1-b338fb38-20210313-010605
 
"""
Management interface for IBM Cloud Container Registry
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ContainerRegistryV1(BaseService):
    """The Container Registry V1 service."""

    DEFAULT_SERVICE_URL = 'https://us.icr.io'
    DEFAULT_SERVICE_NAME = 'container_registry'

    @classmethod
    def new_instance(cls,
                     account: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ContainerRegistryV1':
        """
        Return a new client for the Container Registry service using the specified
               parameters and external configuration.

        :param str account: The unique ID for your IBM Cloud account.
        """
        if account is None:
            raise ValueError('account must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            account,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 account: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Container Registry service.

        :param str account: The unique ID for your IBM Cloud account.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if account is None:
            raise ValueError('account must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.account = account


    #########################
    # Authorization
    #########################


    def get_auth(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get authorization options.

        Get authorization options for the targeted account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AuthOptions` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_auth')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/auth'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_auth(self,
        *,
        iam_authz: bool = None,
        private_only: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update authorization options.

        Update authorization options for the targeted account.

        :param bool iam_authz: (optional) Enable role based authorization when
               authenticating with IBM Cloud IAM.
        :param bool private_only: (optional) Restrict account to only be able to
               push and pull images over private connections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_auth')
        headers.update(sdk_headers)

        data = {
            'iam_authz': iam_authz,
            'private_only': private_only
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/auth'
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Images
    #########################


    def list_images(self,
        *,
        namespace: str = None,
        include_ibm: bool = None,
        include_private: bool = None,
        include_manifest_lists: bool = None,
        vulnerabilities: bool = None,
        repository: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List images.

        List all images in namespaces in a targeted IBM Cloud account.

        :param str namespace: (optional) Lists images that are stored in the
               specified namespace only. Query multiple namespaces by specifying this
               option for each namespace. If this option is not specified, images from all
               namespaces in the specified IBM Cloud account are listed.
        :param bool include_ibm: (optional) Includes IBM-provided public images in
               the list of images. If this option is not specified, private images are
               listed only. If this option is specified more than once, the last parsed
               setting is the setting that is used.
        :param bool include_private: (optional) Includes private images in the list
               of images. If this option is not specified, private images are listed. If
               this option is specified more than once, the last parsed setting is the
               setting that is used.
        :param bool include_manifest_lists: (optional) Includes tags that reference
               multi-architecture manifest lists in the image list. If this option is not
               specified, tagged manifest lists are not shown in the list. If this option
               is specified more than once, the last parsed setting is the setting that is
               used.
        :param bool vulnerabilities: (optional) Displays Vulnerability Advisor
               status for the listed images. If this option is specified more than once,
               the last parsed setting is the setting that is used.
        :param str repository: (optional) Lists images that are stored in the
               specified repository, under your namespaces. Query multiple repositories by
               specifying this option for each repository. If this option is not
               specified, images from all repos are listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[RemoteAPIImage]` result
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_images')
        headers.update(sdk_headers)

        params = {
            'namespace': namespace,
            'includeIBM': include_ibm,
            'includePrivate': include_private,
            'includeManifestLists': include_manifest_lists,
            'vulnerabilities': vulnerabilities,
            'repository': repository
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/images'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def bulk_delete_images(self,
        bulk_delete: List[str],
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk delete images.

        Remove multiple container images from the registry.

        :param List[str] bulk_delete: The full IBM Cloud registry path to the
               images that you want to delete, including its digest. All tags for the
               supplied digest are removed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageBulkDeleteResult` object
        """

        if bulk_delete is None:
            raise ValueError('bulk_delete must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='bulk_delete_images')
        headers.update(sdk_headers)

        data = json.dumps(bulk_delete)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/images/bulkdelete'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_image_digests(self,
        *,
        exclude_tagged: bool = None,
        exclude_va: bool = None,
        include_ibm: bool = None,
        repositories: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List images by digest.

        List all images by digest in namespaces in a targeted IBM Cloud account.

        :param bool exclude_tagged: (optional) ExcludeTagged returns only untagged
               digests.
        :param bool exclude_va: (optional) ExcludeVA returns the digest list with
               no VA scan results.
        :param bool include_ibm: (optional) When true, API will return the IBM
               public images if they exist in the targeted region.
        :param List[str] repositories: (optional) Repositories in which to restrict
               the output. If left empty all images for the account will be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[ImageDigest]` result
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_image_digests')
        headers.update(sdk_headers)

        data = {
            'exclude_tagged': exclude_tagged,
            'exclude_va': exclude_va,
            'include_ibm': include_ibm,
            'repositories': repositories
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/images/digests'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def tag_image(self,
        fromimage: str,
        toimage: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Create tag.

        Create a new tag in a private registry that refers to an existing image in the
        same region.

        :param str fromimage: The name of the image that you want to create a new
               tag for, in the format &lt;REPOSITORY&gt;:&lt;TAG&gt;. Run `ibmcloud cr
               images` or call the `GET /images/json` endpoint to review images that are
               in the registry.
        :param str toimage: The new tag for the image, in the format
               &lt;REPOSITORY&gt;:&lt;TAG&gt;.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if fromimage is None:
            raise ValueError('fromimage must be provided')
        if toimage is None:
            raise ValueError('toimage must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='tag_image')
        headers.update(sdk_headers)

        params = {
            'fromimage': fromimage,
            'toimage': toimage
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/images/tags'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_image(self,
        image: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete image.

        Delete a container image from the registry.

        :param str image: The full IBM Cloud registry path to the image that you
               want to delete, including its tag. If you do not provide a specific tag,
               the version with the `latest` tag is removed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageDeleteResult` object
        """

        if image is None:
            raise ValueError('image must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_image')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['image']
        path_param_values = self.encode_path_vars(image)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/images/{image}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def inspect_image(self,
        image: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Inspect an image.

        Inspect a container image in the private registry.

        :param str image: The full IBM Cloud registry path to the image that you
               want to inspect. Run `ibmcloud cr images` or call the `GET /images/json`
               endpoint to review images that are in the registry.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageInspection` object
        """

        if image is None:
            raise ValueError('image must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='inspect_image')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['image']
        path_param_values = self.encode_path_vars(image)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/images/{image}/json'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_image_manifest(self,
        image: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get image manifest.

        Get the manifest for a container image in the private registry.

        :param str image: The full IBM Cloud registry path to the image that you
               want to inspect. Run `ibmcloud cr images` or call the `GET /images/json`
               endpoint to review images that are in the registry.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if image is None:
            raise ValueError('image must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_image_manifest')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['image']
        path_param_values = self.encode_path_vars(image)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/images/{image}/manifest'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Messages
    #########################


    def get_messages(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get messages.

        Return any published system messages.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_messages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/messages'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Namespaces
    #########################


    def list_namespaces(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List namespaces.

        List authorized namespaces in the targeted IBM Cloud account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_namespaces')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/namespaces'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_namespace_details(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Detailed namespace list.

        Retrieves details, such as resource group, for all your namespaces in the targeted
        registry.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[NamespaceDetails]` result
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_namespace_details')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/namespaces/details'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_namespace(self,
        name: str,
        *,
        x_auth_resource_group: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create namespace.

        Add a namespace to the targeted IBM Cloud account.

        :param str name: The name of the namespace.
        :param str x_auth_resource_group: (optional) The ID of the resource group
               that the namespace will be created within.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Namespace` object
        """

        if name is None:
            raise ValueError('name must be provided')
        headers = {
            'Account': self.account,
            'X-Auth-Resource-Group': x_auth_resource_group
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_namespace')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['name']
        path_param_values = self.encode_path_vars(name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/namespaces/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def assign_namespace(self,
        x_auth_resource_group: str,
        name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Assign namespace.

        Assign a namespace to the specified resource group in the targeted IBM Cloud
        account.

        :param str x_auth_resource_group: The ID of the resource group that the
               namespace will be created within.
        :param str name: The name of the namespace to be updated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Namespace` object
        """

        if x_auth_resource_group is None:
            raise ValueError('x_auth_resource_group must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {
            'Account': self.account,
            'X-Auth-Resource-Group': x_auth_resource_group
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='assign_namespace')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['name']
        path_param_values = self.encode_path_vars(name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/namespaces/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_namespace(self,
        name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete namespace.

        Delete the IBM Cloud Container Registry namespace from the targeted IBM Cloud
        account, and removes all images that were in that namespace.

        :param str name: The name of the namespace that you want to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_namespace')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['name']
        path_param_values = self.encode_path_vars(name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/namespaces/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Plans
    #########################


    def get_plans(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get plans.

        Get plans for the targeted account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Plan` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_plans')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/plans'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_plans(self,
        *,
        plan: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update plans.

        Update plans for the targeted account.

        :param str plan: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_plans')
        headers.update(sdk_headers)

        data = {
            'plan': plan
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/plans'
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Quotas
    #########################


    def get_quota(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get quotas.

        Get quotas for the targeted account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Quota` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_quota')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/quotas'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_quota(self,
        *,
        storage_megabytes: int = None,
        traffic_megabytes: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update quotas.

        Update quotas for the targeted account.

        :param int storage_megabytes: (optional) Storage quota in megabytes. The
               value -1 denotes "Unlimited".
        :param int traffic_megabytes: (optional) Traffic quota in megabytes. The
               value -1 denotes "Unlimited".
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_quota')
        headers.update(sdk_headers)

        data = {
            'storage_megabytes': storage_megabytes,
            'traffic_megabytes': traffic_megabytes
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/quotas'
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Retentions
    #########################


    def list_retention_policies(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List retention policies.

        List retention policies for all namespaces in the targeted IBM Cloud account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `dict` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_retention_policies')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/retentions'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_retention_policy(self,
        namespace: str,
        *,
        images_per_repo: int = None,
        retain_untagged: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set retention policy.

        Set the retention policy for the specified namespace.

        :param str namespace: The namespace to which the retention policy is
               attached.
        :param int images_per_repo: (optional) Determines how many images will be
               retained for each repository when the retention policy is executed. The
               value -1 denotes 'Unlimited' (all images are retained).
        :param bool retain_untagged: (optional) Determines if untagged images are
               retained when executing the retention policy. This is false by default
               meaning untagged images will be deleted when the policy is executed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if namespace is None:
            raise ValueError('namespace must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='set_retention_policy')
        headers.update(sdk_headers)

        data = {
            'namespace': namespace,
            'images_per_repo': images_per_repo,
            'retain_untagged': retain_untagged
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/retentions'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def analyze_retention_policy(self,
        namespace: str,
        *,
        images_per_repo: int = None,
        retain_untagged: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Analyze retention policy.

        Analyze a retention policy, and get a list of what would be deleted by it.

        :param str namespace: The namespace to which the retention policy is
               attached.
        :param int images_per_repo: (optional) Determines how many images will be
               retained for each repository when the retention policy is executed. The
               value -1 denotes 'Unlimited' (all images are retained).
        :param bool retain_untagged: (optional) Determines if untagged images are
               retained when executing the retention policy. This is false by default
               meaning untagged images will be deleted when the policy is executed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if namespace is None:
            raise ValueError('namespace must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='analyze_retention_policy')
        headers.update(sdk_headers)

        data = {
            'namespace': namespace,
            'images_per_repo': images_per_repo,
            'retain_untagged': retain_untagged
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/retentions/analyze'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_retention_policy(self,
        namespace: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get retention policy.

        Get the retention policy for the specified namespace.

        :param str namespace: Gets the retention policy for the specified
               namespace.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RetentionPolicy` object
        """

        if namespace is None:
            raise ValueError('namespace must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_retention_policy')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['namespace']
        path_param_values = self.encode_path_vars(namespace)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/retentions/{namespace}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Settings
    #########################


    def get_settings(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get account settings.

        Get account settings for the targeted account.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountSettings` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/settings'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_settings(self,
        *,
        platform_metrics: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update account settings.

        Update settings for the targeted account.

        :param bool platform_metrics: (optional) Opt in to IBM Cloud Container
               Registry publishing platform metrics.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_settings')
        headers.update(sdk_headers)

        data = {
            'platform_metrics': platform_metrics
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/api/v1/settings'
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Tags
    #########################


    def delete_image_tag(self,
        image: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete tag.

        Untag a container image in the registry.

        :param str image: The name of the image that you want to delete, in the
               format &lt;REPOSITORY&gt;:&lt;TAG&gt;.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageDeleteResult` object
        """

        if image is None:
            raise ValueError('image must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_image_tag')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['image']
        path_param_values = self.encode_path_vars(image)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/tags/{image}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Trash
    #########################


    def list_deleted_images(self,
        *,
        namespace: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List deleted images.

        List all images that are in the trash can.

        :param str namespace: (optional) Limit results to trash can images in the
               given namespace only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `dict` object
        """

        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_deleted_images')
        headers.update(sdk_headers)

        params = {
            'namespace': namespace
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/api/v1/trash'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def restore_tags(self,
        digest: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Restore a digest and all associated tags.

        In the targeted region, restore a digest, and all of its tags in the same
        repository, from the trash.

        :param str digest: The full IBM Cloud registry digest reference for the
               digest that you want to restore such as
               `icr.io/namespace/repo@sha256:a9be...`. Call the `GET /trash/json` endpoint
               to review digests that are in the trash and their tags in the same
               repository.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RestoreResult` object
        """

        if digest is None:
            raise ValueError('digest must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='restore_tags')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['digest']
        path_param_values = self.encode_path_vars(digest)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/trash/{digest}/restoretags'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def restore_image(self,
        image: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Restore deleted image.

        Restore an image from the trash can.

        :param str image: The name of the image that you want to restore, in the
               format &lt;REPOSITORY&gt;:&lt;TAG&gt;. Run `ibmcloud cr trash-list` or call
               the `GET /trash/json` endpoint to review images that are in the trash.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if image is None:
            raise ValueError('image must be provided')
        headers = {
            'Account': self.account
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='restore_image')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['image']
        path_param_values = self.encode_path_vars(image)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/trash/{image}/restore'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class AccountSettings():
    """
    Account settings for the targeted IBM Cloud account.

    :attr bool platform_metrics: (optional) Opt in to IBM Cloud Container Registry
          publishing platform metrics.
    """

    def __init__(self,
                 *,
                 platform_metrics: bool = None) -> None:
        """
        Initialize a AccountSettings object.

        :param bool platform_metrics: (optional) Opt in to IBM Cloud Container
               Registry publishing platform metrics.
        """
        self.platform_metrics = platform_metrics

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountSettings':
        """Initialize a AccountSettings object from a json dictionary."""
        args = {}
        if 'platform_metrics' in _dict:
            args['platform_metrics'] = _dict.get('platform_metrics')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'platform_metrics') and self.platform_metrics is not None:
            _dict['platform_metrics'] = self.platform_metrics
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AuthOptions():
    """
    The authorization options for the targeted IBM Cloud account.

    :attr bool iam_authz: (optional) Enable role based authorization when
          authenticating with IBM Cloud IAM.
    :attr bool private_only: (optional) Restrict account to only be able to push and
          pull images over private connections.
    """

    def __init__(self,
                 *,
                 iam_authz: bool = None,
                 private_only: bool = None) -> None:
        """
        Initialize a AuthOptions object.

        :param bool iam_authz: (optional) Enable role based authorization when
               authenticating with IBM Cloud IAM.
        :param bool private_only: (optional) Restrict account to only be able to
               push and pull images over private connections.
        """
        self.iam_authz = iam_authz
        self.private_only = private_only

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AuthOptions':
        """Initialize a AuthOptions object from a json dictionary."""
        args = {}
        if 'iam_authz' in _dict:
            args['iam_authz'] = _dict.get('iam_authz')
        if 'private_only' in _dict:
            args['private_only'] = _dict.get('private_only')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AuthOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_authz') and self.iam_authz is not None:
            _dict['iam_authz'] = self.iam_authz
        if hasattr(self, 'private_only') and self.private_only is not None:
            _dict['private_only'] = self.private_only
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AuthOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AuthOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AuthOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Config():
    """
    The configuration data about a container.

    :attr bool args_escaped: (optional) True if command is already escaped (Windows
          specific).
    :attr bool attach_stderr: (optional) If true, standard error is attached.
    :attr bool attach_stdin: (optional) If true, standard input is attached, which
          makes possible user interaction.
    :attr bool attach_stdout: (optional) If true, standard output is attached.
    :attr List[str] cmd: (optional) Command that is run when starting the container.
    :attr str domainname: (optional) The FQDN for the container.
    :attr List[str] entrypoint: (optional) Entrypoint to run when starting the
          container.
    :attr List[str] env: (optional) List of environment variables to set in the
          container.
    :attr dict exposed_ports: (optional) A list of exposed ports in a format
          [123:{},456:{}].
    :attr HealthConfig healthcheck: (optional)
    :attr str hostname: (optional) The host name of the container.
    :attr str image: (optional) Name of the image as it was passed by the operator
          (eg. could be symbolic).
    :attr dict labels: (optional) List of labels set to this container.
    :attr str mac_address: (optional) The MAC Address of the container.
    :attr bool network_disabled: (optional) If true, containers are not given
          network access.
    :attr List[str] on_build: (optional) ONBUILD metadata that were defined on the
          image Dockerfile https://docs.docker.com/engine/reference/builder/#onbuild.
    :attr bool open_stdin: (optional) Open stdin.
    :attr List[str] shell: (optional) Shell for shell-form of RUN, CMD, ENTRYPOINT.
    :attr bool stdin_once: (optional) If true, close stdin after the 1 attached
          client disconnects.
    :attr str stop_signal: (optional) Signal to stop a container.
    :attr int stop_timeout: (optional) Timeout (in seconds) to stop a container.
    :attr bool tty: (optional) Attach standard streams to a tty, including stdin if
          it is not closed.
    :attr str user: (optional) The user that will run the command(s) inside the
          container.
    :attr dict volumes: (optional) List of volumes (mounts) used for the container.
    :attr str working_dir: (optional) Current working directory (PWD) in the command
          will be launched.
    """

    def __init__(self,
                 *,
                 args_escaped: bool = None,
                 attach_stderr: bool = None,
                 attach_stdin: bool = None,
                 attach_stdout: bool = None,
                 cmd: List[str] = None,
                 domainname: str = None,
                 entrypoint: List[str] = None,
                 env: List[str] = None,
                 exposed_ports: dict = None,
                 healthcheck: 'HealthConfig' = None,
                 hostname: str = None,
                 image: str = None,
                 labels: dict = None,
                 mac_address: str = None,
                 network_disabled: bool = None,
                 on_build: List[str] = None,
                 open_stdin: bool = None,
                 shell: List[str] = None,
                 stdin_once: bool = None,
                 stop_signal: str = None,
                 stop_timeout: int = None,
                 tty: bool = None,
                 user: str = None,
                 volumes: dict = None,
                 working_dir: str = None) -> None:
        """
        Initialize a Config object.

        :param bool args_escaped: (optional) True if command is already escaped
               (Windows specific).
        :param bool attach_stderr: (optional) If true, standard error is attached.
        :param bool attach_stdin: (optional) If true, standard input is attached,
               which makes possible user interaction.
        :param bool attach_stdout: (optional) If true, standard output is attached.
        :param List[str] cmd: (optional) Command that is run when starting the
               container.
        :param str domainname: (optional) The FQDN for the container.
        :param List[str] entrypoint: (optional) Entrypoint to run when starting the
               container.
        :param List[str] env: (optional) List of environment variables to set in
               the container.
        :param dict exposed_ports: (optional) A list of exposed ports in a format
               [123:{},456:{}].
        :param HealthConfig healthcheck: (optional)
        :param str hostname: (optional) The host name of the container.
        :param str image: (optional) Name of the image as it was passed by the
               operator (eg. could be symbolic).
        :param dict labels: (optional) List of labels set to this container.
        :param str mac_address: (optional) The MAC Address of the container.
        :param bool network_disabled: (optional) If true, containers are not given
               network access.
        :param List[str] on_build: (optional) ONBUILD metadata that were defined on
               the image Dockerfile
               https://docs.docker.com/engine/reference/builder/#onbuild.
        :param bool open_stdin: (optional) Open stdin.
        :param List[str] shell: (optional) Shell for shell-form of RUN, CMD,
               ENTRYPOINT.
        :param bool stdin_once: (optional) If true, close stdin after the 1
               attached client disconnects.
        :param str stop_signal: (optional) Signal to stop a container.
        :param int stop_timeout: (optional) Timeout (in seconds) to stop a
               container.
        :param bool tty: (optional) Attach standard streams to a tty, including
               stdin if it is not closed.
        :param str user: (optional) The user that will run the command(s) inside
               the container.
        :param dict volumes: (optional) List of volumes (mounts) used for the
               container.
        :param str working_dir: (optional) Current working directory (PWD) in the
               command will be launched.
        """
        self.args_escaped = args_escaped
        self.attach_stderr = attach_stderr
        self.attach_stdin = attach_stdin
        self.attach_stdout = attach_stdout
        self.cmd = cmd
        self.domainname = domainname
        self.entrypoint = entrypoint
        self.env = env
        self.exposed_ports = exposed_ports
        self.healthcheck = healthcheck
        self.hostname = hostname
        self.image = image
        self.labels = labels
        self.mac_address = mac_address
        self.network_disabled = network_disabled
        self.on_build = on_build
        self.open_stdin = open_stdin
        self.shell = shell
        self.stdin_once = stdin_once
        self.stop_signal = stop_signal
        self.stop_timeout = stop_timeout
        self.tty = tty
        self.user = user
        self.volumes = volumes
        self.working_dir = working_dir

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Config':
        """Initialize a Config object from a json dictionary."""
        args = {}
        if 'ArgsEscaped' in _dict:
            args['args_escaped'] = _dict.get('ArgsEscaped')
        if 'AttachStderr' in _dict:
            args['attach_stderr'] = _dict.get('AttachStderr')
        if 'AttachStdin' in _dict:
            args['attach_stdin'] = _dict.get('AttachStdin')
        if 'AttachStdout' in _dict:
            args['attach_stdout'] = _dict.get('AttachStdout')
        if 'Cmd' in _dict:
            args['cmd'] = _dict.get('Cmd')
        if 'Domainname' in _dict:
            args['domainname'] = _dict.get('Domainname')
        if 'Entrypoint' in _dict:
            args['entrypoint'] = _dict.get('Entrypoint')
        if 'Env' in _dict:
            args['env'] = _dict.get('Env')
        if 'ExposedPorts' in _dict:
            args['exposed_ports'] = _dict.get('ExposedPorts')
        if 'Healthcheck' in _dict:
            args['healthcheck'] = HealthConfig.from_dict(_dict.get('Healthcheck'))
        if 'Hostname' in _dict:
            args['hostname'] = _dict.get('Hostname')
        if 'Image' in _dict:
            args['image'] = _dict.get('Image')
        if 'Labels' in _dict:
            args['labels'] = _dict.get('Labels')
        if 'MacAddress' in _dict:
            args['mac_address'] = _dict.get('MacAddress')
        if 'NetworkDisabled' in _dict:
            args['network_disabled'] = _dict.get('NetworkDisabled')
        if 'OnBuild' in _dict:
            args['on_build'] = _dict.get('OnBuild')
        if 'OpenStdin' in _dict:
            args['open_stdin'] = _dict.get('OpenStdin')
        if 'Shell' in _dict:
            args['shell'] = _dict.get('Shell')
        if 'StdinOnce' in _dict:
            args['stdin_once'] = _dict.get('StdinOnce')
        if 'StopSignal' in _dict:
            args['stop_signal'] = _dict.get('StopSignal')
        if 'StopTimeout' in _dict:
            args['stop_timeout'] = _dict.get('StopTimeout')
        if 'Tty' in _dict:
            args['tty'] = _dict.get('Tty')
        if 'User' in _dict:
            args['user'] = _dict.get('User')
        if 'Volumes' in _dict:
            args['volumes'] = _dict.get('Volumes')
        if 'WorkingDir' in _dict:
            args['working_dir'] = _dict.get('WorkingDir')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Config object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'args_escaped') and self.args_escaped is not None:
            _dict['ArgsEscaped'] = self.args_escaped
        if hasattr(self, 'attach_stderr') and self.attach_stderr is not None:
            _dict['AttachStderr'] = self.attach_stderr
        if hasattr(self, 'attach_stdin') and self.attach_stdin is not None:
            _dict['AttachStdin'] = self.attach_stdin
        if hasattr(self, 'attach_stdout') and self.attach_stdout is not None:
            _dict['AttachStdout'] = self.attach_stdout
        if hasattr(self, 'cmd') and self.cmd is not None:
            _dict['Cmd'] = self.cmd
        if hasattr(self, 'domainname') and self.domainname is not None:
            _dict['Domainname'] = self.domainname
        if hasattr(self, 'entrypoint') and self.entrypoint is not None:
            _dict['Entrypoint'] = self.entrypoint
        if hasattr(self, 'env') and self.env is not None:
            _dict['Env'] = self.env
        if hasattr(self, 'exposed_ports') and self.exposed_ports is not None:
            _dict['ExposedPorts'] = self.exposed_ports
        if hasattr(self, 'healthcheck') and self.healthcheck is not None:
            _dict['Healthcheck'] = self.healthcheck.to_dict()
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['Hostname'] = self.hostname
        if hasattr(self, 'image') and self.image is not None:
            _dict['Image'] = self.image
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['Labels'] = self.labels
        if hasattr(self, 'mac_address') and self.mac_address is not None:
            _dict['MacAddress'] = self.mac_address
        if hasattr(self, 'network_disabled') and self.network_disabled is not None:
            _dict['NetworkDisabled'] = self.network_disabled
        if hasattr(self, 'on_build') and self.on_build is not None:
            _dict['OnBuild'] = self.on_build
        if hasattr(self, 'open_stdin') and self.open_stdin is not None:
            _dict['OpenStdin'] = self.open_stdin
        if hasattr(self, 'shell') and self.shell is not None:
            _dict['Shell'] = self.shell
        if hasattr(self, 'stdin_once') and self.stdin_once is not None:
            _dict['StdinOnce'] = self.stdin_once
        if hasattr(self, 'stop_signal') and self.stop_signal is not None:
            _dict['StopSignal'] = self.stop_signal
        if hasattr(self, 'stop_timeout') and self.stop_timeout is not None:
            _dict['StopTimeout'] = self.stop_timeout
        if hasattr(self, 'tty') and self.tty is not None:
            _dict['Tty'] = self.tty
        if hasattr(self, 'user') and self.user is not None:
            _dict['User'] = self.user
        if hasattr(self, 'volumes') and self.volumes is not None:
            _dict['Volumes'] = self.volumes
        if hasattr(self, 'working_dir') and self.working_dir is not None:
            _dict['WorkingDir'] = self.working_dir
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Config object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Config') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Config') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HealthConfig():
    """
    HealthConfig.

    :attr int interval: (optional) A Duration represents the elapsed time between
          two instants as an int64 nanosecond count.
    :attr int retries: (optional) The number of consecutive failures needed to
          consider a container as unhealthy. Zero means inherit.
    :attr List[str] test: (optional) The test to perform to check that the container
          is healthy. An empty slice means to inherit the default. The options are:
          {} : inherit healthcheck
          {"NONE"} : disable healthcheck
          {"CMD", args...} : exec arguments directly
          {"CMD-SHELL", command} : run command with system's default shell.
    :attr int timeout: (optional) A Duration represents the elapsed time between two
          instants as an int64 nanosecond count.
    """

    def __init__(self,
                 *,
                 interval: int = None,
                 retries: int = None,
                 test: List[str] = None,
                 timeout: int = None) -> None:
        """
        Initialize a HealthConfig object.

        :param int interval: (optional) A Duration represents the elapsed time
               between two instants as an int64 nanosecond count.
        :param int retries: (optional) The number of consecutive failures needed to
               consider a container as unhealthy. Zero means inherit.
        :param List[str] test: (optional) The test to perform to check that the
               container is healthy. An empty slice means to inherit the default. The
               options are:
               {} : inherit healthcheck
               {"NONE"} : disable healthcheck
               {"CMD", args...} : exec arguments directly
               {"CMD-SHELL", command} : run command with system's default shell.
        :param int timeout: (optional) A Duration represents the elapsed time
               between two instants as an int64 nanosecond count.
        """
        self.interval = interval
        self.retries = retries
        self.test = test
        self.timeout = timeout

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthConfig':
        """Initialize a HealthConfig object from a json dictionary."""
        args = {}
        if 'Interval' in _dict:
            args['interval'] = _dict.get('Interval')
        if 'Retries' in _dict:
            args['retries'] = _dict.get('Retries')
        if 'Test' in _dict:
            args['test'] = _dict.get('Test')
        if 'Timeout' in _dict:
            args['timeout'] = _dict.get('Timeout')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthConfig object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['Interval'] = self.interval
        if hasattr(self, 'retries') and self.retries is not None:
            _dict['Retries'] = self.retries
        if hasattr(self, 'test') and self.test is not None:
            _dict['Test'] = self.test
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['Timeout'] = self.timeout
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthConfig object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthConfig') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthConfig') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageBulkDeleteError():
    """
    Information about a failure to delete an image as part of a bulk delete.

    :attr str code: (optional) An API error code.
    :attr str message: (optional) The English text message associated with the error
          code.
    """

    def __init__(self,
                 *,
                 code: str = None,
                 message: str = None) -> None:
        """
        Initialize a ImageBulkDeleteError object.

        :param str code: (optional) An API error code.
        :param str message: (optional) The English text message associated with the
               error code.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageBulkDeleteError':
        """Initialize a ImageBulkDeleteError object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageBulkDeleteError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageBulkDeleteError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageBulkDeleteError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageBulkDeleteError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageBulkDeleteResult():
    """
    The results of a bulk image delete request.

    :attr dict error: (optional) A map of digests to the error object that explains
          the failure.
    :attr List[str] success: (optional) A list of digests which were deleted
          successfully.
    """

    def __init__(self,
                 *,
                 error: dict = None,
                 success: List[str] = None) -> None:
        """
        Initialize a ImageBulkDeleteResult object.

        :param dict error: (optional) A map of digests to the error object that
               explains the failure.
        :param List[str] success: (optional) A list of digests which were deleted
               successfully.
        """
        self.error = error
        self.success = success

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageBulkDeleteResult':
        """Initialize a ImageBulkDeleteResult object from a json dictionary."""
        args = {}
        if 'error' in _dict:
            args['error'] = {k : ImageBulkDeleteError.from_dict(v) for k, v in _dict.get('error').items()}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageBulkDeleteResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = {k : v.to_dict() for k, v in self.error.items()}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageBulkDeleteResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageBulkDeleteResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageBulkDeleteResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageDeleteResult():
    """
    ImageDeleteResult.

    :attr str untagged: (optional)
    """

    def __init__(self,
                 *,
                 untagged: str = None) -> None:
        """
        Initialize a ImageDeleteResult object.

        :param str untagged: (optional)
        """
        self.untagged = untagged

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDeleteResult':
        """Initialize a ImageDeleteResult object from a json dictionary."""
        args = {}
        if 'Untagged' in _dict:
            args['untagged'] = _dict.get('Untagged')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDeleteResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'untagged') and self.untagged is not None:
            _dict['Untagged'] = self.untagged
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDeleteResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageDeleteResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDeleteResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageDigest():
    """
    Important information about an image.

    :attr int created: (optional) The build date of the image.
    :attr str id: (optional) The image digest.
    :attr str manifest_type: (optional) The type of the image, such as 'Docker Image
          Manifest V2, Schema 2' or 'OCI Image Manifest v1'.
    :attr dict repo_tags: (optional) A map of image repositories to tags.
    :attr int size: (optional) The size of the image in bytes.
    """

    def __init__(self,
                 *,
                 created: int = None,
                 id: str = None,
                 manifest_type: str = None,
                 repo_tags: dict = None,
                 size: int = None) -> None:
        """
        Initialize a ImageDigest object.

        :param int created: (optional) The build date of the image.
        :param str id: (optional) The image digest.
        :param str manifest_type: (optional) The type of the image, such as 'Docker
               Image Manifest V2, Schema 2' or 'OCI Image Manifest v1'.
        :param dict repo_tags: (optional) A map of image repositories to tags.
        :param int size: (optional) The size of the image in bytes.
        """
        self.created = created
        self.id = id
        self.manifest_type = manifest_type
        self.repo_tags = repo_tags
        self.size = size

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDigest':
        """Initialize a ImageDigest object from a json dictionary."""
        args = {}
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'manifestType' in _dict:
            args['manifest_type'] = _dict.get('manifestType')
        if 'repoTags' in _dict:
            args['repo_tags'] = _dict.get('repoTags')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDigest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'manifest_type') and self.manifest_type is not None:
            _dict['manifestType'] = self.manifest_type
        if hasattr(self, 'repo_tags') and self.repo_tags is not None:
            _dict['repoTags'] = self.repo_tags
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDigest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageDigest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDigest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageInspection():
    """
    An image JSON output consistent with the Docker Remote API.

    :attr str architecture: (optional) The processor architecture used to build this
          image, and required to run it.
    :attr str author: (optional) The author of the image.
    :attr str comment: (optional) A plain text description of the image.
    :attr Config config: (optional) The configuration data about a container.
    :attr str container: (optional) The ID of the container which created this
          image.
    :attr Config container_config: (optional) The configuration data about a
          container.
    :attr str created: (optional) The unix timestamp for the date when the image was
          created.
    :attr str docker_version: (optional) The Docker version used to build this
          image.
    :attr str id: (optional) The image ID.
    :attr str manifest_type: (optional) Media type of the manifest for the image.
    :attr str os: (optional) The operating system family used to build this image,
          and required to run it.
    :attr str os_version: (optional) The version of the operating system used to
          build this image.
    :attr str parent: (optional) The ID of the base image for this image.
    :attr RootFS root_fs: (optional) RootFS contains information about the root
          filesystem of a container image.
    :attr int size: (optional) The size of the image in bytes.
    :attr int virtual_size: (optional) The sum of the size of each layer in the
          image in bytes.
    """

    def __init__(self,
                 *,
                 architecture: str = None,
                 author: str = None,
                 comment: str = None,
                 config: 'Config' = None,
                 container: str = None,
                 container_config: 'Config' = None,
                 created: str = None,
                 docker_version: str = None,
                 id: str = None,
                 manifest_type: str = None,
                 os: str = None,
                 os_version: str = None,
                 parent: str = None,
                 root_fs: 'RootFS' = None,
                 size: int = None,
                 virtual_size: int = None) -> None:
        """
        Initialize a ImageInspection object.

        :param str architecture: (optional) The processor architecture used to
               build this image, and required to run it.
        :param str author: (optional) The author of the image.
        :param str comment: (optional) A plain text description of the image.
        :param Config config: (optional) The configuration data about a container.
        :param str container: (optional) The ID of the container which created this
               image.
        :param Config container_config: (optional) The configuration data about a
               container.
        :param str created: (optional) The unix timestamp for the date when the
               image was created.
        :param str docker_version: (optional) The Docker version used to build this
               image.
        :param str id: (optional) The image ID.
        :param str manifest_type: (optional) Media type of the manifest for the
               image.
        :param str os: (optional) The operating system family used to build this
               image, and required to run it.
        :param str os_version: (optional) The version of the operating system used
               to build this image.
        :param str parent: (optional) The ID of the base image for this image.
        :param RootFS root_fs: (optional) RootFS contains information about the
               root filesystem of a container image.
        :param int size: (optional) The size of the image in bytes.
        :param int virtual_size: (optional) The sum of the size of each layer in
               the image in bytes.
        """
        self.architecture = architecture
        self.author = author
        self.comment = comment
        self.config = config
        self.container = container
        self.container_config = container_config
        self.created = created
        self.docker_version = docker_version
        self.id = id
        self.manifest_type = manifest_type
        self.os = os
        self.os_version = os_version
        self.parent = parent
        self.root_fs = root_fs
        self.size = size
        self.virtual_size = virtual_size

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageInspection':
        """Initialize a ImageInspection object from a json dictionary."""
        args = {}
        if 'Architecture' in _dict:
            args['architecture'] = _dict.get('Architecture')
        if 'Author' in _dict:
            args['author'] = _dict.get('Author')
        if 'Comment' in _dict:
            args['comment'] = _dict.get('Comment')
        if 'Config' in _dict:
            args['config'] = Config.from_dict(_dict.get('Config'))
        if 'Container' in _dict:
            args['container'] = _dict.get('Container')
        if 'ContainerConfig' in _dict:
            args['container_config'] = Config.from_dict(_dict.get('ContainerConfig'))
        if 'Created' in _dict:
            args['created'] = _dict.get('Created')
        if 'DockerVersion' in _dict:
            args['docker_version'] = _dict.get('DockerVersion')
        if 'Id' in _dict:
            args['id'] = _dict.get('Id')
        if 'ManifestType' in _dict:
            args['manifest_type'] = _dict.get('ManifestType')
        if 'Os' in _dict:
            args['os'] = _dict.get('Os')
        if 'OsVersion' in _dict:
            args['os_version'] = _dict.get('OsVersion')
        if 'Parent' in _dict:
            args['parent'] = _dict.get('Parent')
        if 'RootFS' in _dict:
            args['root_fs'] = RootFS.from_dict(_dict.get('RootFS'))
        if 'Size' in _dict:
            args['size'] = _dict.get('Size')
        if 'VirtualSize' in _dict:
            args['virtual_size'] = _dict.get('VirtualSize')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageInspection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'architecture') and self.architecture is not None:
            _dict['Architecture'] = self.architecture
        if hasattr(self, 'author') and self.author is not None:
            _dict['Author'] = self.author
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['Comment'] = self.comment
        if hasattr(self, 'config') and self.config is not None:
            _dict['Config'] = self.config.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            _dict['Container'] = self.container
        if hasattr(self, 'container_config') and self.container_config is not None:
            _dict['ContainerConfig'] = self.container_config.to_dict()
        if hasattr(self, 'created') and self.created is not None:
            _dict['Created'] = self.created
        if hasattr(self, 'docker_version') and self.docker_version is not None:
            _dict['DockerVersion'] = self.docker_version
        if hasattr(self, 'id') and self.id is not None:
            _dict['Id'] = self.id
        if hasattr(self, 'manifest_type') and self.manifest_type is not None:
            _dict['ManifestType'] = self.manifest_type
        if hasattr(self, 'os') and self.os is not None:
            _dict['Os'] = self.os
        if hasattr(self, 'os_version') and self.os_version is not None:
            _dict['OsVersion'] = self.os_version
        if hasattr(self, 'parent') and self.parent is not None:
            _dict['Parent'] = self.parent
        if hasattr(self, 'root_fs') and self.root_fs is not None:
            _dict['RootFS'] = self.root_fs.to_dict()
        if hasattr(self, 'size') and self.size is not None:
            _dict['Size'] = self.size
        if hasattr(self, 'virtual_size') and self.virtual_size is not None:
            _dict['VirtualSize'] = self.virtual_size
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageInspection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageInspection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageInspection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Namespace():
    """
    Namespace.

    :attr str namespace: (optional)
    """

    def __init__(self,
                 *,
                 namespace: str = None) -> None:
        """
        Initialize a Namespace object.

        :param str namespace: (optional)
        """
        self.namespace = namespace

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Namespace':
        """Initialize a Namespace object from a json dictionary."""
        args = {}
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Namespace object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Namespace object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Namespace') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Namespace') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NamespaceDetails():
    """
    Details of a namespace.

    :attr str account: (optional) The IBM Cloud account that owns the namespace.
    :attr str created_date: (optional) When the namespace was created.
    :attr str crn: (optional) If the namespace has been assigned to a resource
          group, this is the IBM Cloud CRN representing the namespace.
    :attr str name: (optional)
    :attr str resource_created_date: (optional) When the namespace was assigned to a
          resource group.
    :attr str resource_group: (optional) The resource group that the namespace is
          assigned to.
    :attr str updated_date: (optional) When the namespace was last updated.
    """

    def __init__(self,
                 *,
                 account: str = None,
                 created_date: str = None,
                 crn: str = None,
                 name: str = None,
                 resource_created_date: str = None,
                 resource_group: str = None,
                 updated_date: str = None) -> None:
        """
        Initialize a NamespaceDetails object.

        :param str account: (optional) The IBM Cloud account that owns the
               namespace.
        :param str created_date: (optional) When the namespace was created.
        :param str crn: (optional) If the namespace has been assigned to a resource
               group, this is the IBM Cloud CRN representing the namespace.
        :param str name: (optional)
        :param str resource_created_date: (optional) When the namespace was
               assigned to a resource group.
        :param str resource_group: (optional) The resource group that the namespace
               is assigned to.
        :param str updated_date: (optional) When the namespace was last updated.
        """
        self.account = account
        self.created_date = created_date
        self.crn = crn
        self.name = name
        self.resource_created_date = resource_created_date
        self.resource_group = resource_group
        self.updated_date = updated_date

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NamespaceDetails':
        """Initialize a NamespaceDetails object from a json dictionary."""
        args = {}
        if 'account' in _dict:
            args['account'] = _dict.get('account')
        if 'created_date' in _dict:
            args['created_date'] = _dict.get('created_date')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'resource_created_date' in _dict:
            args['resource_created_date'] = _dict.get('resource_created_date')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        if 'updated_date' in _dict:
            args['updated_date'] = _dict.get('updated_date')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NamespaceDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account') and self.account is not None:
            _dict['account'] = self.account
        if hasattr(self, 'created_date') and self.created_date is not None:
            _dict['created_date'] = self.created_date
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'resource_created_date') and self.resource_created_date is not None:
            _dict['resource_created_date'] = self.resource_created_date
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'updated_date') and self.updated_date is not None:
            _dict['updated_date'] = self.updated_date
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NamespaceDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NamespaceDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NamespaceDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Plan():
    """
    The plan for the targeted IBM Cloud account.

    :attr str plan: (optional)
    """

    def __init__(self,
                 *,
                 plan: str = None) -> None:
        """
        Initialize a Plan object.

        :param str plan: (optional)
        """
        self.plan = plan

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Plan':
        """Initialize a Plan object from a json dictionary."""
        args = {}
        if 'plan' in _dict:
            args['plan'] = _dict.get('plan')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Plan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan') and self.plan is not None:
            _dict['plan'] = self.plan
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Plan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Plan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Plan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Quota():
    """
    Current usage and limits for the targeted IBM Cloud account.

    :attr QuotaDetails limit: (optional)
    :attr QuotaDetails usage: (optional)
    """

    def __init__(self,
                 *,
                 limit: 'QuotaDetails' = None,
                 usage: 'QuotaDetails' = None) -> None:
        """
        Initialize a Quota object.

        :param QuotaDetails limit: (optional)
        :param QuotaDetails usage: (optional)
        """
        self.limit = limit
        self.usage = usage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Quota':
        """Initialize a Quota object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = QuotaDetails.from_dict(_dict.get('limit'))
        if 'usage' in _dict:
            args['usage'] = QuotaDetails.from_dict(_dict.get('usage'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Quota object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit.to_dict()
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = self.usage.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Quota object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Quota') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Quota') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class QuotaDetails():
    """
    QuotaDetails.

    :attr int storage_bytes: (optional) Storage quota or usage in bytes. The value
          -1 denotes "Unlimited".
    :attr int traffic_bytes: (optional) Traffic quota or usage in bytes. The value
          -1 denotes "Unlimited".
    """

    def __init__(self,
                 *,
                 storage_bytes: int = None,
                 traffic_bytes: int = None) -> None:
        """
        Initialize a QuotaDetails object.

        :param int storage_bytes: (optional) Storage quota or usage in bytes. The
               value -1 denotes "Unlimited".
        :param int traffic_bytes: (optional) Traffic quota or usage in bytes. The
               value -1 denotes "Unlimited".
        """
        self.storage_bytes = storage_bytes
        self.traffic_bytes = traffic_bytes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuotaDetails':
        """Initialize a QuotaDetails object from a json dictionary."""
        args = {}
        if 'storage_bytes' in _dict:
            args['storage_bytes'] = _dict.get('storage_bytes')
        if 'traffic_bytes' in _dict:
            args['traffic_bytes'] = _dict.get('traffic_bytes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuotaDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'storage_bytes') and self.storage_bytes is not None:
            _dict['storage_bytes'] = self.storage_bytes
        if hasattr(self, 'traffic_bytes') and self.traffic_bytes is not None:
            _dict['traffic_bytes'] = self.traffic_bytes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuotaDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuotaDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuotaDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RemoteAPIImage():
    """
    Information about an image, in a format consistent with the Docker Remote API format.

    :attr int configuration_issue_count: (optional)
    :attr int created: (optional)
    :attr dict digest_tags: (optional)
    :attr int exempt_issue_count: (optional)
    :attr str id: (optional)
    :attr int issue_count: (optional)
    :attr dict labels: (optional)
    :attr str manifest_type: (optional)
    :attr str parent_id: (optional)
    :attr List[str] repo_digests: (optional)
    :attr List[str] repo_tags: (optional)
    :attr int size: (optional)
    :attr int virtual_size: (optional)
    :attr int vulnerability_count: (optional)
    :attr str vulnerable: (optional)
    """

    def __init__(self,
                 *,
                 configuration_issue_count: int = None,
                 created: int = None,
                 digest_tags: dict = None,
                 exempt_issue_count: int = None,
                 id: str = None,
                 issue_count: int = None,
                 labels: dict = None,
                 manifest_type: str = None,
                 parent_id: str = None,
                 repo_digests: List[str] = None,
                 repo_tags: List[str] = None,
                 size: int = None,
                 virtual_size: int = None,
                 vulnerability_count: int = None,
                 vulnerable: str = None) -> None:
        """
        Initialize a RemoteAPIImage object.

        :param int configuration_issue_count: (optional)
        :param int created: (optional)
        :param dict digest_tags: (optional)
        :param int exempt_issue_count: (optional)
        :param str id: (optional)
        :param int issue_count: (optional)
        :param dict labels: (optional)
        :param str manifest_type: (optional)
        :param str parent_id: (optional)
        :param List[str] repo_digests: (optional)
        :param List[str] repo_tags: (optional)
        :param int size: (optional)
        :param int virtual_size: (optional)
        :param int vulnerability_count: (optional)
        :param str vulnerable: (optional)
        """
        self.configuration_issue_count = configuration_issue_count
        self.created = created
        self.digest_tags = digest_tags
        self.exempt_issue_count = exempt_issue_count
        self.id = id
        self.issue_count = issue_count
        self.labels = labels
        self.manifest_type = manifest_type
        self.parent_id = parent_id
        self.repo_digests = repo_digests
        self.repo_tags = repo_tags
        self.size = size
        self.virtual_size = virtual_size
        self.vulnerability_count = vulnerability_count
        self.vulnerable = vulnerable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RemoteAPIImage':
        """Initialize a RemoteAPIImage object from a json dictionary."""
        args = {}
        if 'ConfigurationIssueCount' in _dict:
            args['configuration_issue_count'] = _dict.get('ConfigurationIssueCount')
        if 'Created' in _dict:
            args['created'] = _dict.get('Created')
        if 'DigestTags' in _dict:
            args['digest_tags'] = _dict.get('DigestTags')
        if 'ExemptIssueCount' in _dict:
            args['exempt_issue_count'] = _dict.get('ExemptIssueCount')
        if 'Id' in _dict:
            args['id'] = _dict.get('Id')
        if 'IssueCount' in _dict:
            args['issue_count'] = _dict.get('IssueCount')
        if 'Labels' in _dict:
            args['labels'] = _dict.get('Labels')
        if 'ManifestType' in _dict:
            args['manifest_type'] = _dict.get('ManifestType')
        if 'ParentId' in _dict:
            args['parent_id'] = _dict.get('ParentId')
        if 'RepoDigests' in _dict:
            args['repo_digests'] = _dict.get('RepoDigests')
        if 'RepoTags' in _dict:
            args['repo_tags'] = _dict.get('RepoTags')
        if 'Size' in _dict:
            args['size'] = _dict.get('Size')
        if 'VirtualSize' in _dict:
            args['virtual_size'] = _dict.get('VirtualSize')
        if 'VulnerabilityCount' in _dict:
            args['vulnerability_count'] = _dict.get('VulnerabilityCount')
        if 'Vulnerable' in _dict:
            args['vulnerable'] = _dict.get('Vulnerable')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RemoteAPIImage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'configuration_issue_count') and self.configuration_issue_count is not None:
            _dict['ConfigurationIssueCount'] = self.configuration_issue_count
        if hasattr(self, 'created') and self.created is not None:
            _dict['Created'] = self.created
        if hasattr(self, 'digest_tags') and self.digest_tags is not None:
            _dict['DigestTags'] = self.digest_tags
        if hasattr(self, 'exempt_issue_count') and self.exempt_issue_count is not None:
            _dict['ExemptIssueCount'] = self.exempt_issue_count
        if hasattr(self, 'id') and self.id is not None:
            _dict['Id'] = self.id
        if hasattr(self, 'issue_count') and self.issue_count is not None:
            _dict['IssueCount'] = self.issue_count
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['Labels'] = self.labels
        if hasattr(self, 'manifest_type') and self.manifest_type is not None:
            _dict['ManifestType'] = self.manifest_type
        if hasattr(self, 'parent_id') and self.parent_id is not None:
            _dict['ParentId'] = self.parent_id
        if hasattr(self, 'repo_digests') and self.repo_digests is not None:
            _dict['RepoDigests'] = self.repo_digests
        if hasattr(self, 'repo_tags') and self.repo_tags is not None:
            _dict['RepoTags'] = self.repo_tags
        if hasattr(self, 'size') and self.size is not None:
            _dict['Size'] = self.size
        if hasattr(self, 'virtual_size') and self.virtual_size is not None:
            _dict['VirtualSize'] = self.virtual_size
        if hasattr(self, 'vulnerability_count') and self.vulnerability_count is not None:
            _dict['VulnerabilityCount'] = self.vulnerability_count
        if hasattr(self, 'vulnerable') and self.vulnerable is not None:
            _dict['Vulnerable'] = self.vulnerable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RemoteAPIImage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RemoteAPIImage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RemoteAPIImage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RestoreResult():
    """
    The result of restoring tags for a digest. In a successful request the digest is
    always restored, and zero or more of its tags may be restored.

    :attr List[str] successful: (optional) Successful is a list of tags that were
          restored.
    :attr List[str] unsuccessful: (optional) Unsuccessful is a list of tags that
          were not restored because of a conflict.
    """

    def __init__(self,
                 *,
                 successful: List[str] = None,
                 unsuccessful: List[str] = None) -> None:
        """
        Initialize a RestoreResult object.

        :param List[str] successful: (optional) Successful is a list of tags that
               were restored.
        :param List[str] unsuccessful: (optional) Unsuccessful is a list of tags
               that were not restored because of a conflict.
        """
        self.successful = successful
        self.unsuccessful = unsuccessful

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RestoreResult':
        """Initialize a RestoreResult object from a json dictionary."""
        args = {}
        if 'successful' in _dict:
            args['successful'] = _dict.get('successful')
        if 'unsuccessful' in _dict:
            args['unsuccessful'] = _dict.get('unsuccessful')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RestoreResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'successful') and self.successful is not None:
            _dict['successful'] = self.successful
        if hasattr(self, 'unsuccessful') and self.unsuccessful is not None:
            _dict['unsuccessful'] = self.unsuccessful
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RestoreResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RestoreResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RestoreResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RetentionPolicy():
    """
    A document that contains the image retention settings for a namespace.

    :attr int images_per_repo: (optional) Determines how many images will be
          retained for each repository when the retention policy is executed. The value -1
          denotes 'Unlimited' (all images are retained).
    :attr str namespace: The namespace to which the retention policy is attached.
    :attr bool retain_untagged: (optional) Determines if untagged images are
          retained when executing the retention policy. This is false by default meaning
          untagged images will be deleted when the policy is executed.
    """

    def __init__(self,
                 namespace: str,
                 *,
                 images_per_repo: int = None,
                 retain_untagged: bool = None) -> None:
        """
        Initialize a RetentionPolicy object.

        :param str namespace: The namespace to which the retention policy is
               attached.
        :param int images_per_repo: (optional) Determines how many images will be
               retained for each repository when the retention policy is executed. The
               value -1 denotes 'Unlimited' (all images are retained).
        :param bool retain_untagged: (optional) Determines if untagged images are
               retained when executing the retention policy. This is false by default
               meaning untagged images will be deleted when the policy is executed.
        """
        self.images_per_repo = images_per_repo
        self.namespace = namespace
        self.retain_untagged = retain_untagged

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RetentionPolicy':
        """Initialize a RetentionPolicy object from a json dictionary."""
        args = {}
        if 'images_per_repo' in _dict:
            args['images_per_repo'] = _dict.get('images_per_repo')
        if 'namespace' in _dict:
            args['namespace'] = _dict.get('namespace')
        else:
            raise ValueError('Required property \'namespace\' not present in RetentionPolicy JSON')
        if 'retain_untagged' in _dict:
            args['retain_untagged'] = _dict.get('retain_untagged')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RetentionPolicy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'images_per_repo') and self.images_per_repo is not None:
            _dict['images_per_repo'] = self.images_per_repo
        if hasattr(self, 'namespace') and self.namespace is not None:
            _dict['namespace'] = self.namespace
        if hasattr(self, 'retain_untagged') and self.retain_untagged is not None:
            _dict['retain_untagged'] = self.retain_untagged
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RetentionPolicy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RetentionPolicy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RetentionPolicy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RootFS():
    """
    RootFS contains information about the root filesystem of a container image.

    :attr str base_layer: (optional) Descriptor for the base layer in the image.
    :attr List[str] layers: (optional) Descriptors for each layer in the image.
    :attr str type: (optional) The type of filesystem.
    """

    def __init__(self,
                 *,
                 base_layer: str = None,
                 layers: List[str] = None,
                 type: str = None) -> None:
        """
        Initialize a RootFS object.

        :param str base_layer: (optional) Descriptor for the base layer in the
               image.
        :param List[str] layers: (optional) Descriptors for each layer in the
               image.
        :param str type: (optional) The type of filesystem.
        """
        self.base_layer = base_layer
        self.layers = layers
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RootFS':
        """Initialize a RootFS object from a json dictionary."""
        args = {}
        if 'BaseLayer' in _dict:
            args['base_layer'] = _dict.get('BaseLayer')
        if 'Layers' in _dict:
            args['layers'] = _dict.get('Layers')
        if 'Type' in _dict:
            args['type'] = _dict.get('Type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RootFS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'base_layer') and self.base_layer is not None:
            _dict['BaseLayer'] = self.base_layer
        if hasattr(self, 'layers') and self.layers is not None:
            _dict['Layers'] = self.layers
        if hasattr(self, 'type') and self.type is not None:
            _dict['Type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RootFS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RootFS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RootFS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Trash():
    """
    Details of the tags and days until expiry.

    :attr int days_until_expiry: (optional)
    :attr List[str] tags: (optional)
    """

    def __init__(self,
                 *,
                 days_until_expiry: int = None,
                 tags: List[str] = None) -> None:
        """
        Initialize a Trash object.

        :param int days_until_expiry: (optional)
        :param List[str] tags: (optional)
        """
        self.days_until_expiry = days_until_expiry
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Trash':
        """Initialize a Trash object from a json dictionary."""
        args = {}
        if 'daysUntilExpiry' in _dict:
            args['days_until_expiry'] = _dict.get('daysUntilExpiry')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Trash object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'days_until_expiry') and self.days_until_expiry is not None:
            _dict['daysUntilExpiry'] = self.days_until_expiry
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Trash object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Trash') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Trash') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class VAReport():
    """
    The VA Report for a given image.

    :attr int configuration_issue_count: (optional) Number of configuration issues
          in the image.
    :attr int exempt_issue_count: (optional) Total number of issues in the image
          that were exempted by an exemption policy.
    :attr int issue_count: (optional) Total number of issues in the image.
    :attr int vulnerability_count: (optional) Number of vulnerabilities in the
          image.
    :attr str vulnerable: (optional) Summary of vulnerability status.
    """

    def __init__(self,
                 *,
                 configuration_issue_count: int = None,
                 exempt_issue_count: int = None,
                 issue_count: int = None,
                 vulnerability_count: int = None,
                 vulnerable: str = None) -> None:
        """
        Initialize a VAReport object.

        :param int configuration_issue_count: (optional) Number of configuration
               issues in the image.
        :param int exempt_issue_count: (optional) Total number of issues in the
               image that were exempted by an exemption policy.
        :param int issue_count: (optional) Total number of issues in the image.
        :param int vulnerability_count: (optional) Number of vulnerabilities in the
               image.
        :param str vulnerable: (optional) Summary of vulnerability status.
        """
        self.configuration_issue_count = configuration_issue_count
        self.exempt_issue_count = exempt_issue_count
        self.issue_count = issue_count
        self.vulnerability_count = vulnerability_count
        self.vulnerable = vulnerable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VAReport':
        """Initialize a VAReport object from a json dictionary."""
        args = {}
        if 'configurationIssueCount' in _dict:
            args['configuration_issue_count'] = _dict.get('configurationIssueCount')
        if 'exemptIssueCount' in _dict:
            args['exempt_issue_count'] = _dict.get('exemptIssueCount')
        if 'issueCount' in _dict:
            args['issue_count'] = _dict.get('issueCount')
        if 'vulnerabilityCount' in _dict:
            args['vulnerability_count'] = _dict.get('vulnerabilityCount')
        if 'vulnerable' in _dict:
            args['vulnerable'] = _dict.get('vulnerable')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VAReport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'configuration_issue_count') and self.configuration_issue_count is not None:
            _dict['configurationIssueCount'] = self.configuration_issue_count
        if hasattr(self, 'exempt_issue_count') and self.exempt_issue_count is not None:
            _dict['exemptIssueCount'] = self.exempt_issue_count
        if hasattr(self, 'issue_count') and self.issue_count is not None:
            _dict['issueCount'] = self.issue_count
        if hasattr(self, 'vulnerability_count') and self.vulnerability_count is not None:
            _dict['vulnerabilityCount'] = self.vulnerability_count
        if hasattr(self, 'vulnerable') and self.vulnerable is not None:
            _dict['vulnerable'] = self.vulnerable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VAReport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VAReport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VAReport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
