[![Build Status](https://travis-ci.com/IBM/container-registry-python-sdk.svg?branch=main)](https://travis-ci.com/IBM/container-registry-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud Container Registry Python SDK

Python client library to interact with the [IBM Cloud Container Registry API](https://cloud.ibm.com/apidocs/container-registry), and [IBM Cloud Container Registry Vulnerability Advisor API](https://cloud.ibm.com/apidocs/container-registry/va-v4)


## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Container Registry Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[Container Registry image management API](https://cloud.ibm.com/apidocs/container-registry) | ibm_container_registry.container_registry_v1
[Container Registry Vulnerability Advisor API](https://cloud.ibm.com/apidocs/container-registry/va-v4) | ibm_container_registry.vulnerability_advisor_v4

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.7 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-container-registry>=1.1.4"
```

or

```bash
easy_install --upgrade "ibm-container-registry>=1.1.4"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/container-registry-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.com/IBM/container-registry-python-sdk/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/container-registry-python-sdk/blob/main/LICENSE).
