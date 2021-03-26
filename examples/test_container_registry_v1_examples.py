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
Examples for ContainerRegistryV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_container_registry.container_registry_v1 import *

account = 'accountID'

#
# This file provides an example of how to use the Container Registry service.
#
# The following configuration properties are assumed to be defined:
# CONTAINER_REGISTRY_URL=<service base url>
# CONTAINER_REGISTRY_AUTH_TYPE=iam
# CONTAINER_REGISTRY_APIKEY=<IAM apikey>
# CONTAINER_REGISTRY_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'container_registry_v1.env'

container_registry_service = None

config = None

# Variables to hold link values
namespace_link = None


##############################################################################
# Start of Examples for Service: ContainerRegistryV1
##############################################################################
# region
class TestContainerRegistryV1Examples():
    """
    Example Test Class for ContainerRegistryV1
    """

    @classmethod
    def setup_class(cls):
        global container_registry_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            container_registry_service = ContainerRegistryV1.new_instance(
                account=account
            )

            # end-common
            assert container_registry_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ContainerRegistryV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        True, reason="Examples for this SDK are not intended to be runnable, skipping..."
    )

    @needscredentials
    def test_create_namespace_example(self):
        """
        create_namespace request example
        """
        try:
            # begin-create_namespace

            namespace = container_registry_service.create_namespace(
                name='my_example_namespace'
            ).get_result()

            print(json.dumps(namespace, indent=2))

            # end-create_namespace

            global namespace_link
            namespace_link = namespace['namespace']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_auth_example(self):
        """
        get_auth request example
        """
        try:
            # begin-get_auth

            auth_options = container_registry_service.get_auth().get_result()

            print(json.dumps(auth_options, indent=2))

            # end-get_auth

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_auth_example(self):
        """
        update_auth request example
        """
        try:
            # begin-update_auth

            response = container_registry_service.update_auth(
                iam_authz=True
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_auth

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_images_example(self):
        """
        list_images request example
        """
        try:
            # begin-list_images

            list_remote_api_image = container_registry_service.list_images().get_result()

            print(json.dumps(list_remote_api_image, indent=2))

            # end-list_images

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_bulk_delete_images_example(self):
        """
        bulk_delete_images request example
        """
        try:
            # begin-bulk_delete_images

            image_bulk_delete_result = container_registry_service.bulk_delete_images(
                bulk_delete=['image name']
            ).get_result()

            print(json.dumps(image_bulk_delete_result, indent=2))

            # end-bulk_delete_images

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_image_digests_example(self):
        """
        list_image_digests request example
        """
        try:
            # begin-list_image_digests

            list_image_digest = container_registry_service.list_image_digests(
                exclude_tagged=False,
                exclude_va=False,
                include_ibm=False
            ).get_result()

            print(json.dumps(list_image_digest, indent=2))

            # end-list_image_digests

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_tag_image_example(self):
        """
        tag_image request example
        """
        try:
            # begin-tag_image

            response = container_registry_service.tag_image(
                fromimage='from image name',
                toimage='to image name'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-tag_image

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_inspect_image_example(self):
        """
        inspect_image request example
        """
        try:
            # begin-inspect_image

            image_inspection = container_registry_service.inspect_image(
                image='image name'
            ).get_result()

            print(json.dumps(image_inspection, indent=2))

            # end-inspect_image

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_image_manifest_example(self):
        """
        get_image_manifest request example
        """
        try:
            # begin-get_image_manifest

            response = container_registry_service.get_image_manifest(
                image='image name'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-get_image_manifest

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_messages_example(self):
        """
        get_messages request example
        """
        try:
            # begin-get_messages

            get_messages_response = container_registry_service.get_messages().get_result()

            print(json.dumps(get_messages_response, indent=2))

            # end-get_messages

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_namespaces_example(self):
        """
        list_namespaces request example
        """
        try:
            # begin-list_namespaces

            result = container_registry_service.list_namespaces().get_result()

            print(json.dumps(result, indent=2))

            # end-list_namespaces

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_namespace_details_example(self):
        """
        list_namespace_details request example
        """
        try:
            # begin-list_namespace_details

            list_namespace_details = container_registry_service.list_namespace_details().get_result()

            print(json.dumps(list_namespace_details, indent=2))

            # end-list_namespace_details

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_assign_namespace_example(self):
        """
        assign_namespace request example
        """
        try:
            # begin-assign_namespace

            namespace = container_registry_service.assign_namespace(
                x_auth_resource_group='Resource Group ID',
                name=namespace_link
            ).get_result()

            print(json.dumps(namespace, indent=2))

            # end-assign_namespace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_plans_example(self):
        """
        get_plans request example
        """
        try:
            # begin-get_plans

            plan = container_registry_service.get_plans().get_result()

            print(json.dumps(plan, indent=2))

            # end-get_plans

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_plans_example(self):
        """
        update_plans request example
        """
        try:
            # begin-update_plans

            response = container_registry_service.update_plans(
                plan='Standard'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_plans

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_quota_example(self):
        """
        get_quota request example
        """
        try:
            # begin-get_quota

            quota = container_registry_service.get_quota().get_result()

            print(json.dumps(quota, indent=2))

            # end-get_quota

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_quota_example(self):
        """
        update_quota request example
        """
        try:
            # begin-update_quota

            response = container_registry_service.update_quota(
                traffic_megabytes=480
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_quota

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_retention_policies_example(self):
        """
        list_retention_policies request example
        """
        try:
            # begin-list_retention_policies

            dict = container_registry_service.list_retention_policies().get_result()

            print(json.dumps(dict, indent=2))

            # end-list_retention_policies

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_retention_policy_example(self):
        """
        set_retention_policy request example
        """
        try:
            # begin-set_retention_policy

            response = container_registry_service.set_retention_policy(
                namespace=namespace_link,
                images_per_repo=10,
                retain_untagged=False
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-set_retention_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_analyze_retention_policy_example(self):
        """
        analyze_retention_policy request example
        """
        try:
            # begin-analyze_retention_policy

            policy_analysis = container_registry_service.analyze_retention_policy(
                namespace=namespace_link,
                images_per_repo=10,
                retain_untagged=False
            ).get_result()

            print(json.dumps(policy_analysis, indent=2))

            # end-analyze_retention_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_retention_policy_example(self):
        """
        get_retention_policy request example
        """
        try:
            # begin-get_retention_policy

            retention_policy = container_registry_service.get_retention_policy(
                namespace=namespace_link
            ).get_result()

            print(json.dumps(retention_policy, indent=2))

            # end-get_retention_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_settings_example(self):
        """
        get_settings request example
        """
        try:
            # begin-get_settings

            account_settings = container_registry_service.get_settings().get_result()

            print(json.dumps(account_settings, indent=2))

            # end-get_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_settings_example(self):
        """
        update_settings request example
        """
        try:
            # begin-update_settings

            response = container_registry_service.update_settings(
                platform_metrics=True
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deleted_images_example(self):
        """
        list_deleted_images request example
        """
        try:
            # begin-list_deleted_images

            dict = container_registry_service.list_deleted_images().get_result()

            print(json.dumps(dict, indent=2))

            # end-list_deleted_images

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_restore_tags_example(self):
        """
        restore_tags request example
        """
        try:
            # begin-restore_tags

            restore_result = container_registry_service.restore_tags(
                digest='image name' # Fully qualified including digest
            ).get_result()

            print(json.dumps(restore_result, indent=2))

            # end-restore_tags

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_restore_image_example(self):
        """
        restore_image request example
        """
        try:
            # begin-restore_image

            response = container_registry_service.restore_image(
                image='image name'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-restore_image

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_namespace_example(self):
        """
        delete_namespace request example
        """
        try:
            # begin-delete_namespace

            response = container_registry_service.delete_namespace(
                name=namespace_link
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_namespace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_image_tag_example(self):
        """
        delete_image_tag request example
        """
        try:
            # begin-delete_image_tag

            image_delete_result = container_registry_service.delete_image_tag(
                image='image name'
            ).get_result()

            print(json.dumps(image_delete_result, indent=2))

            # end-delete_image_tag

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_image_example(self):
        """
        delete_image request example
        """
        try:
            # begin-delete_image

            image_delete_result = container_registry_service.delete_image(
                image='image name'
            ).get_result()

            print(json.dumps(image_delete_result, indent=2))

            # end-delete_image

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: ContainerRegistryV1
##############################################################################
