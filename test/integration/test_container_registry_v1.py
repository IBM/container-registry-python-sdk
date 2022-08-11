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
Integration Tests for ContainerRegistryV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_container_registry.container_registry_v1 import *

# Config file name
config_file = 'container_registry_v1.env'

# Variables to hold link values
namespace_link = None

class TestContainerRegistryV1():
    """
    Integration Test Class for ContainerRegistryV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.config = read_external_sources(
                ContainerRegistryV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.container_registry_service = ContainerRegistryV1.new_instance(
                account=cls.config["ACCOUNT_ID"]
                )
            assert cls.container_registry_service is not None

            cls.dns_name = cls.config["URL"]
            assert cls.dns_name is not None
            if cls.dns_name.startswith("https://"):
                cls.dns_name = cls.dns_name[len("https://"):]

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_namespace(self):

        create_namespace_response = self.container_registry_service.create_namespace(
            name=self.config["NAMESPACE"]
        )

        assert (create_namespace_response.get_status_code() == 200) or (create_namespace_response.get_status_code() == 201)
        namespace = create_namespace_response.get_result()
        assert namespace is not None

        # Store namespace_link value for later test cases
        global namespace_link
        namespace_link = namespace['namespace']

    @needscredentials
    def test_get_auth(self):

        get_auth_response = self.container_registry_service.get_auth()

        assert get_auth_response.get_status_code() == 200
        auth_options = get_auth_response.get_result()
        assert auth_options is not None

    @needscredentials
    def test_update_auth(self):

        update_auth_response = self.container_registry_service.update_auth(
            iam_authz=True
        )

        assert update_auth_response.get_status_code() == 204
    
    @needscredentials
    def test_tag_image(self):

        seed_image=self.config["SEED_IMAGE"]

        tag_image_response = self.container_registry_service.tag_image(
            fromimage=self.dns_name+"/"+seed_image,
            toimage=self.dns_name+"/"+namespace_link+"/sdktest:1"
        )

        assert tag_image_response.get_status_code() == 201

    @needscredentials
    def test_list_images(self):

        list_images_response = self.container_registry_service.list_images(
            namespace=namespace_link,
            include_ibm=True,
            include_private=True,
            include_manifest_lists=True,
            vulnerabilities=False
        )

        assert list_images_response.get_status_code() == 200
        list_remote_api_image = list_images_response.get_result()
        assert list_remote_api_image is not None

    @needscredentials
    def test_bulk_delete_images(self):

        bulk_delete_images_response = self.container_registry_service.bulk_delete_images(
            bulk_delete=[self.dns_name+"/"+namespace_link+"/notexist:1"]
        )

        assert bulk_delete_images_response.get_status_code() == 200
        image_bulk_delete_result = bulk_delete_images_response.get_result()
        assert image_bulk_delete_result is not None

    @needscredentials
    def test_list_image_digests(self):

        list_image_digests_response = self.container_registry_service.list_image_digests(
            exclude_tagged=False,
            exclude_va=False,
            include_ibm=False
        )

        assert list_image_digests_response.get_status_code() == 200
        list_image_digest = list_image_digests_response.get_result()
        assert list_image_digest is not None
        repo = self.dns_name+"/"+namespace_link+"/sdktest"
        found = False
        for result_item in list_image_digest:
            item = ImageDigest.from_dict(result_item)
            got_tags = item.repo_tags.get(repo)
            if got_tags:
                found = True
                report = got_tags.get('1')
                va_report = VAReport.from_dict(report)
                assert va_report.configuration_issue_count is 0
        assert found is True

    @needscredentials
    def test_inspect_image(self):

        inspect_image_response = self.container_registry_service.inspect_image(
            image=self.dns_name+"/"+namespace_link+"/sdktest:1"
        )

        assert inspect_image_response.get_status_code() == 200
        image_inspection = inspect_image_response.get_result()
        assert image_inspection is not None

    @needscredentials
    def test_get_image_manifest(self):

        get_image_manifest_response = self.container_registry_service.get_image_manifest(
            image=self.dns_name+"/"+namespace_link+"/sdktest:1"
        )

        assert get_image_manifest_response.get_status_code() == 200
        image_manifest = get_image_manifest_response.get_result()
        assert image_manifest.get("schemaVersion") == 2

    @needscredentials
    def test_get_messages(self):

        get_messages_response = self.container_registry_service.get_messages()

        assert (get_messages_response.get_status_code() == 200) or (get_messages_response.get_status_code() == 204)
        result = get_messages_response.get_result()

    @needscredentials
    def test_list_namespaces(self):

        list_namespaces_response = self.container_registry_service.list_namespaces()

        assert list_namespaces_response.get_status_code() == 200
        result = list_namespaces_response.get_result()
        assert result is not None
        assert namespace_link in result

    @needscredentials
    def test_list_namespace_details(self):

        list_namespace_details_response = self.container_registry_service.list_namespace_details()

        assert list_namespace_details_response.get_status_code() == 200
        list_namespace_details = list_namespace_details_response.get_result()
        assert list_namespace_details is not None

    @needscredentials
    def test_assign_namespace(self):

        assign_namespace_response = self.container_registry_service.assign_namespace(
            x_auth_resource_group=self.config["RESOURCE_GROUP_ID"],
            name=namespace_link
        )

        assert assign_namespace_response.get_status_code() == 200
        namespace = assign_namespace_response.get_result()
        assert namespace is not None

    @needscredentials
    def test_get_plans(self):

        get_plans_response = self.container_registry_service.get_plans()

        assert get_plans_response.get_status_code() == 200
        plan = get_plans_response.get_result()
        assert plan is not None

    # @needscredentials
    # def test_update_plans(self):

    #     update_plans_response = self.container_registry_service.update_plans(
    #         plan='Standard'
    #     )

    #     assert update_plans_response.get_status_code() == 200

    @needscredentials
    def test_update_quota(self):

        update_quota_response = self.container_registry_service.update_quota(
            storage_megabytes=500,
            traffic_megabytes=4900
        )

        assert update_quota_response.get_status_code() == 200

    @needscredentials
    def test_get_quota(self):

        get_quota_response = self.container_registry_service.get_quota()

        assert get_quota_response.get_status_code() == 200
        quota = get_quota_response.get_result()
        assert quota is not None
        assert quota['limit']['storage_bytes'] == 524288000

    @needscredentials
    def test_list_retention_policies(self):

        list_retention_policies_response = self.container_registry_service.list_retention_policies()

        assert list_retention_policies_response.get_status_code() == 200
        dict = list_retention_policies_response.get_result()
        assert dict is not None

    @needscredentials
    def test_set_retention_policy(self):

        set_retention_policy_response = self.container_registry_service.set_retention_policy(
            namespace=namespace_link,
            images_per_repo=10,
            retain_untagged=False
        )

        assert (set_retention_policy_response.get_status_code() == 201) or (set_retention_policy_response.get_status_code() == 200)

    @needscredentials
    def test_analyze_retention_policy(self):

        analyze_retention_policy_response = self.container_registry_service.analyze_retention_policy(
            namespace=namespace_link,
            images_per_repo=10,
            retain_untagged=False
        )

        assert analyze_retention_policy_response.get_status_code() == 200
        result = analyze_retention_policy_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_retention_policy(self):

        get_retention_policy_response = self.container_registry_service.get_retention_policy(
            namespace=namespace_link
        )

        assert get_retention_policy_response.get_status_code() == 200
        retention_policy = get_retention_policy_response.get_result()
        assert retention_policy is not None
        assert retention_policy['images_per_repo'] == 10

    @needscredentials
    def test_get_settings(self):

        get_settings_response = self.container_registry_service.get_settings()

        assert get_settings_response.get_status_code() == 200
        account_settings = get_settings_response.get_result()
        assert account_settings is not None

    @needscredentials
    def test_update_settings(self):

        update_settings_response = self.container_registry_service.update_settings(
            platform_metrics=False
        )

        assert update_settings_response.get_status_code() == 204
    
    @needscredentials
    def test_delete_image_tag(self):

        delete_image_tag_response = self.container_registry_service.delete_image_tag(
            image=self.dns_name+"/"+namespace_link+"/sdktest:1"
        )

        assert delete_image_tag_response.get_status_code() == 200
        image_delete_result = delete_image_tag_response.get_result()
        assert image_delete_result is not None

    @needscredentials
    def test_delete_image(self):

        delete_image_response = self.container_registry_service.delete_image(
            image=self.dns_name+"/"+namespace_link+"/sdktest@"+self.config['SEED_DIGEST']
        )

        assert delete_image_response.get_status_code() == 200
        image_delete_result = delete_image_response.get_result()
        assert image_delete_result is not None

    @needscredentials
    def test_list_deleted_images(self):

        list_deleted_images_response = self.container_registry_service.list_deleted_images(
            namespace=namespace_link
        )
        deleted_image = self.dns_name+"/"+namespace_link+"/sdktest@"+self.config['SEED_DIGEST']

        assert list_deleted_images_response.get_status_code() == 200
        deleted_images = list_deleted_images_response.get_result()
        assert deleted_images is not None
        assert deleted_image in deleted_images

    @needscredentials
    def test_restore_tags(self):

        restore_tags_response = self.container_registry_service.restore_tags(
            digest=self.dns_name+"/"+namespace_link+"/sdktest@"+self.config['SEED_DIGEST']
        )

        assert restore_tags_response.get_status_code() == 200
        restore_result = restore_tags_response.get_result()
        assert restore_result is not None

    @needscredentials
    def test_restore_image(self):

        check_code = 0
        try:
            self.container_registry_service.restore_image(
                image=self.dns_name+"/"+namespace_link+"/sdktest:nope"
            )

        except ApiException as e_api:
            check_code = e_api.code

        assert check_code == 404

    @needscredentials
    def test_delete_namespace(self):

        delete_namespace_response = self.container_registry_service.delete_namespace(
            name=namespace_link
        )

        assert delete_namespace_response.get_status_code() == 204
