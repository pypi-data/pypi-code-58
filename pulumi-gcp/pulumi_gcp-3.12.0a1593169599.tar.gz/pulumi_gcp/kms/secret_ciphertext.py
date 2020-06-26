# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class SecretCiphertext(pulumi.CustomResource):
    additional_authenticated_data: pulumi.Output[str]
    """
    The additional authenticated data used for integrity checks during encryption and decryption.  **Note**: This property is sensitive and will not be displayed in the plan.
    """
    ciphertext: pulumi.Output[str]
    """
    Contains the result of encrypting the provided plaintext, encoded in base64.
    """
    crypto_key: pulumi.Output[str]
    """
    The full name of the CryptoKey that will be used to encrypt the provided plaintext.
    Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
    """
    plaintext: pulumi.Output[str]
    """
    The plaintext to be encrypted.  **Note**: This property is sensitive and will not be displayed in the plan.
    """
    def __init__(__self__, resource_name, opts=None, additional_authenticated_data=None, crypto_key=None, plaintext=None, __props__=None, __name__=None, __opts__=None):
        """
        Encrypts secret data with Google Cloud KMS and provides access to the ciphertext.

        > **NOTE**: Using this resource will allow you to conceal secret data within your
        resource definitions, but it does not take care of protecting that data in the
        logging output, plan output, or state output.  Please take care to secure your secret
        data outside of resource definitions.

        To get more information about SecretCiphertext, see:

        * [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt)
        * How-to Guides
            * [Encrypting and decrypting data with a symmetric key](https://cloud.google.com/kms/docs/encrypt-decrypt)

        > **Warning:** All arguments including `plaintext` and `additional_authenticated_data` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage
        ### Kms Secret Ciphertext Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        keyring = gcp.kms.KeyRing("keyring", location="global")
        cryptokey = gcp.kms.CryptoKey("cryptokey",
            key_ring=keyring.id,
            rotation_period="100000s")
        my_password = gcp.kms.SecretCiphertext("myPassword",
            crypto_key=cryptokey.id,
            plaintext="my-secret-password")
        instance = gcp.compute.Instance("instance",
            machine_type="n1-standard-1",
            zone="us-central1-a",
            boot_disk={
                "initialize_params": {
                    "image": "debian-cloud/debian-9",
                },
            },
            network_interface=[{
                "network": "default",
                "access_config": [{}],
            }],
            metadata={
                "password": my_password.ciphertext,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.  **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.  **Note**: This property is sensitive and will not be displayed in the plan.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['additional_authenticated_data'] = additional_authenticated_data
            if crypto_key is None:
                raise TypeError("Missing required property 'crypto_key'")
            __props__['crypto_key'] = crypto_key
            if plaintext is None:
                raise TypeError("Missing required property 'plaintext'")
            __props__['plaintext'] = plaintext
            __props__['ciphertext'] = None
        super(SecretCiphertext, __self__).__init__(
            'gcp:kms/secretCiphertext:SecretCiphertext',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, additional_authenticated_data=None, ciphertext=None, crypto_key=None, plaintext=None):
        """
        Get an existing SecretCiphertext resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.  **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] ciphertext: Contains the result of encrypting the provided plaintext, encoded in base64.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.  **Note**: This property is sensitive and will not be displayed in the plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["additional_authenticated_data"] = additional_authenticated_data
        __props__["ciphertext"] = ciphertext
        __props__["crypto_key"] = crypto_key
        __props__["plaintext"] = plaintext
        return SecretCiphertext(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
