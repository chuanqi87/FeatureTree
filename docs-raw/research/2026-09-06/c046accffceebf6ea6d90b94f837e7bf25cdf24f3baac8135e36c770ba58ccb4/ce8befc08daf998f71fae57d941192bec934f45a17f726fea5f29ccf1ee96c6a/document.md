# Release notes

**Key Point:** Some features may take several weeks to roll out to all users.

This page summarizes all changes (new features, bug fixes, updates) to the
Android Management API and [Android Device Policy](https://play.google.com/store/apps/details?id=com.google.android.apps.work.clouddpc) each month.

[**Join the Android Management API mailing list**](https://groups.google.com/forum/#!forum/android-management-api/join) to receive monthly updates
and service advisories directly to your inbox.

---



## July 2026

### Android Management API

* Support for Android 6.0 is now deprecated, consistent with [Google
  Play services](https://support.google.com/googleplay/answer/9037938) support for Android 7.0 and later. Devices running
  Android 6.0 won't receive updates to Android Management API. This does not
  block devices from enrolling into management.
* Version 1.8.2 of the AMAPI SDK was released. See [Android
  Management SDK Release Notes](https://developers.google.com/android/management/sdk-release-notes#version-1.8.2) for details.
* Fixed an issue where consumer Factory Reset Protection (FRP) could
  unexpectedly trigger on company-owned devices after a factory reset, even
  when no FRP admin emails were specified in the device policy.
* Documentation items have also been updated:
  + We added guidance to explain how to [enforce
    Google authentication on enrollment](https://developers.google.com/android/management/provision-device#enforce_google_authentication_on_enrollment).
  + The [`persistentPreferredActivities`
    policy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.persistent_preferred_activities) now includes a warning to avoid configuring this policy and
    [`defaultApplicationSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.default_application_settings)
    for the same intent domain to avoid unpredictable behavior. We also
    updated [the
    corresponding guide](https://developers.google.com/android/management/default-application-settings).
  + We clarified in [the
    documentation](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ManagedConfigurationTemplate.FIELDS.template_id) that the `templateId` parameter of a
    managed configurations template must be a numeric string containing
    only digits.
  + The [Quickstart guide](https://developers.google.com/android/management/quickstart) now
    includes instructions for generating your own OAuth client when
    setting up the Android Management API.

## June 2026

### Android Management API

* We've added policies for [`nearbyNotificationStreaming`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#CrossDevicePolicies.FIELDS.nearby_notification_streaming)
  and [`nearbyAppStreaming`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#CrossDevicePolicies.FIELDS.nearby_app_streaming)
  to control whether users can stream app content and notifications to
  nearby devices. These mirror two existing platform APIs: [`setNearbyNotificationStreamingPolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNearbyNotificationStreamingPolicy(int))
  and [`setNearbyAppStreamingPolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNearbyAppStreamingPolicy(int)).
* IT administrators can now configure `googleAuthenticationOptions`
  within [`SigninDetail`](https://developers.google.com/android/management/reference/rest/v1/enterprises#SigninDetail.FIELDS.google_authentication_options)
  and [`EnrollmentToken`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens#EnrollmentToken.FIELDS.google_authentication_options)
  to specify whether users must authenticate with Google during enrollment.
* Version 1.8.1 of the AMAPI SDK was released. See [Android
  Management SDK Release Notes](https://developers.google.com/android/management/sdk-release-notes#version-1.8.1) for details.
* Documentation items have also been updated:
  + [We
    clarified](https://developers.google.com/android/management/app-roles#add_the_required_metadata_to_the_apps_manifest) that the `NotificationReceiverService` base
    class automatically handles security protections (see the "note" at
    the bottom of the linked section).
  + Updated guidance on [configuring
    an MCP client](https://developers.google.com/android/management/use-android-management-mcp#configure-client) to use the Android Management API MCP server.

## May 2026

### Android Management API

* AMAPI now reports SHA-256 hashes for [signing certificates](https://developers.google.com/android/management/reference/rest/v1/ApplicationSigningKeyCert) in [application reporting](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#ApplicationReport.FIELDS.signing_key_certs), providing improved security over the
  now-deprecated SHA-1 hash field. This aligns with the latest Android
  Ecosystem [best practices](https://support.google.com/googleplay/android-developer/answer/16641489).
* AMAPI improves Factory Reset Protection (FRP) policy handling on COPE
  devices by explicitly disabling FRP and clearing account lists when no [admin emails](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.frp_admin_emails) are configured, preventing unexpected lockouts after
  device resets.

## April 2026

### Android Management API

* AMAPI added [a new policy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#autofillpolicy)
  to allow the IT admin to disable the autofill service. The
  `AutofillPolicy` complements other [credential
  policies](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#credentialproviderpolicydefault) in disabling credential storing.
* Version 1.8.0 of the AMAPI SDK was released. See
  [Android Management SDK Release Notes](https://developers.google.com/android/management/sdk-release-notes#version-1.8.0) for details.
* Documentation items have also been updated:
  + [We
    clarified](https://developers.google.com/android/management/provision-device#sign-in_url) that the `provisioningInfo` object is available
    for up to 24 hours after device provisioning.
  + We noted that the [application
    roles](https://developers.google.com/android/management/app-roles) feature replaces the [`extensionConfig`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ExtensionConfig)
    field in `ApplicationPolicy`.

## XR device management

### Android Management API

* AMAPI now supports Android XR. Learn more about
  [XR device management](https://developers.google.com/android/work/xr-management).

## March 2026

### Android Management API

* As documented in
   [October 2025](https://developers.google.com/android/management/release-notes#oct-2025) and communicated in the following
  [service announcement](https://www.androidenterprise.dev/s/article/Upcoming-change-to-default-Enterprise-display-name-visibility-policy-default-in-AM-API), the default value for the
  [`enterpriseDisplayNameVisibility`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.enterprise_display_name_visibility) policy is now
  [`ENTERPRISE_DISPLAY_NAME_VISIBLE`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#EnterpriseDisplayNameVisibility.ENUM_VALUES.ENTERPRISE_DISPLAY_NAME_VISIBLE). This policy controls
  whether the
  [`enterpriseDisplayName`](https://developers.google.com/android/management/reference/rest/v1/enterprises#Enterprise.FIELDS.enterprise_display_name) is shown on devices, such as on the
  lock screen of company-owned devices. To hide the enterprise name,
  explicitly set the policy to
  [`ENTERPRISE_DISPLAY_NAME_HIDDEN`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#EnterpriseDisplayNameVisibility.ENUM_VALUES.ENTERPRISE_DISPLAY_NAME_HIDDEN).
* The EAP configuration within
  [Open Network Configuration](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.open_network_configuration) has been updated, adding support for
  EAP-PWD as an EAP outer method. See the
  [documentation](https://developers.google.com/android/management/configure-networks#supported_features) for the complete list of supported features.
* We've updated the documentation for:
  + [`networkResetDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.network_reset_disabled) to clarify that this policy only
    applies to fully managed devices.
  + [`installType.KIOSK`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#InstallType.ENUM_VALUES.KIOSK) and the
    [`RoleType.KIOSK`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#RoleType.ENUM_VALUES.KIOSK) to clarify that, on Android 11+, user
    control is disallowed for all apps.
  + [`screenCaptureDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.screen_capture_disabled) and
    [`personalUsagePolicies.screenCaptureDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.screen_capture_disabled) to
    mention that this setting also blocks
    [Circle to Search](https://support.google.com/android/answer/14508957).

## February 2026

### Android Management API

* On company-owned devices with Android 10 and later, IT Admins can now
  manage Private DNS using the new
  [`privateDnsSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#privatednssettings) field within
  [`Policy.DeviceConnectivityManagement`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceconnectivitymanagement). Available modes in
  [`PrivateDnsSettings.privateDnsMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#privatednsmode) include: user choice,
  automatic, and specified host (fully managed devices only).
* AMAPI now supports a preview of integration with the Model Context
  Protocol (MCP). This provides the foundation for EMMs to build AI-driven
  conversational interfaces using read-only tools. See the
  [documentation](https://developers.google.com/android/management/reference/mcp) for more details.
* Updated
  [`NetworkInfo.TelephonyInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#telephonyinfo) documentation to clarify
  support across device types:
  + General telephony information is available for all SIM cards on fully
    managed devices (Android 6+).
  + For admin-added eSIMs, telephony information is available across all
    management modes on Android 15+.
  + The fields `activationState` and `configMode`
    are applicable only to eSIMs on devices running Android 15 and above.

## January 2026

### Android Management API

* We've added a new policy to control user-initiated eSIM addition. The
  [`userInitiatedAddEsimSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#userinitiatedaddesimsettings) field within
  [`DeviceRadioState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceradiostate) allows administrators to specify whether
  the user is allowed to add eSIM profiles on company-owned devices running
  Android 15 and higher.
* The documentation for the
  [`WIPE_ESIMS`](https://developers.google.com/android/management/reference/rest/v1/WipeDataFlag) flag, used within
  [`Policy.wipeDataFlags`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wipedataflag) and
  [`DeleteDeviceRequest.wipeDataFlags`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete#body.request_body.FIELDS.wipe_data_flags), has been updated to
  clarify that for devices running on Android 16 or higher, managed eSIMs
  are always wiped when a work profile is removed from a personally-owned
  device, regardless of whether this flag is set.
* Version 1.7.1 of the AMAPI SDK was released. This version adds more
  detailed logging for the device trust signal APIs to help in diagnosing
  issues. See
  [Android Management SDK Release Notes](https://developers.google.com/android/management/sdk-release-notes#version-1.7.1) for details.
* The [AMAPI Terms
  of Service](https://www.android.com/enterprise/apis/terms/) have been updated to explicitly cover the AMAPI SDK and to
  add to the definition of "Customers" the Original Equipment Manufacturers
  (OEMs) of Android devices.
* The [permissible usage
  guidelines](https://developers.google.com/android/management/permissible-usage) now specifically prohibit the use of the `Advertising
  ID` when accessing the device trust signals.

## November 2025

### Android Management API

* Effective Nov 1, 2025 Android Management API device enrollment requires
  Android Enterprise registration and approval. Developers can initiate this
  process by completing the
  [request form](https://docs.google.com/forms/d/1wraSQCpGsUYoPD6KSAv4OzJpA-UUAEeHzrDMqz9FgMU).
* The documentation for the
  [`CUSTOM`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#InstallType.ENUM_VALUES.CUSTOM) value in
  [`ApplicationPolicy.InstallType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype) has been updated to clarify
  its usage. This includes more details on the requirements for
  [`ApplicationPolicy.signingKeyCerts`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#applicationsigningkeycert) and the expected
  behavior when changing an application's `installType` to or
  from `CUSTOM`.
* The descriptions for the existing policies
  [`setUserIconDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.set_user_icon_disabled) and
  [`shareLocationDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.share_location_disabled) have been refined for better
  clarity.

### Android Management API SDK

* Version 1.7.0 of the AMAPI SDK was released in November. This SDK release
  includes support for the
  [`REQUEST_DEVICE_INFO`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.REQUEST_DEVICE_INFO) command. Refer to the
  [AMAPI SDK Release Notes](https://developers.google.com/android/management/sdk-release-notes#version-1.7.0) for complete details.

## October 2025

### Android Management API

* We've added a new policy to manage [default applications](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.default_application_settings) on devices. Admins can configure a prioritized
  list of applications for each app type, and the first installed and
  qualified app on the device will be set as the default. Once configured,
  this policy prevents users from changing the default application settings,
  maintaining compliance with corporate policies. See [this guide](https://developers.google.com/android/management/default-application-settings) for more details.
* We introduced in [May](https://developers.google.com/android/management/release-notes#may-2025) a policy to configure the
  [`enterpriseDisplayNameVisibility`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.enterprise_display_name_visibility) setting, allowing
  administrators to control visibility of the
  [`enterpriseDisplayName`](https://developers.google.com/android/management/reference/rest/v1/enterprises#Enterprise.FIELDS.enterprise_display_name) on the device, such as on the lock
  screen of company-owned devices. In that announcement, we mentioned we
  will soon set the default for that policy setting to be
  [`ENTERPRISE_DISPLAY_NAME_VISIBLE`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#EnterpriseDisplayNameVisibility.ENUM_VALUES.ENTERPRISE_DISPLAY_NAME_VISIBLE). That change is expected
  to go live in **January 2026**.
* Documentation items have also been updated:
  + We clarified behavior of the [`LOCK`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.LOCK) command on devices with work profiles.
  + We added information about `nonComplianceDetails` for changes
    to the [`mte_policy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#AdvancedSecurityOverrides.FIELDS.mte_policy) on devices pending a reboot.

## September 2025

### Android Management API

* We've introduced the concept of [application roles](https://developers.google.com/android/management/app-roles). This includes:
  + [`COMPANION_APP`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#RoleType.ENUM_VALUES.COMPANION_APP) for offline interaction with Android
    Device Policy
  + [`KIOSK`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#RoleType.ENUM_VALUES.KIOSK) for dedicated device experiences to be used with
    apps that have [`InstallType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype) configured as [`REQUIRED_FOR_SETUP`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#InstallType.ENUM_VALUES.REQUIRED_FOR_SETUP) or [`CUSTOM`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#InstallType.ENUM_VALUES.CUSTOM)
  + [`MOBILE_THREAT_DEFENSE_ENDPOINT_DETECTION_RESPONSE`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#RoleType.ENUM_VALUES.MOBILE_THREAT_DEFENSE_ENDPOINT_DETECTION_RESPONSE)
    (MTD/EDR) and [`SYSTEM_HEALTH_MONITORING`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#RoleType.ENUM_VALUES.SYSTEM_HEALTH_MONITORING) apps.These types of apps are exempt from power and background execution
  restrictions, suspension and hibernation on Android 14 and later. User
  control is disallowed by default on Android 11 and later. See the
  documentation for [`ApplicationPolicy.roles`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.roles) and [`RoleType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#roletype) for more details.
* A new stable release and a release candidate of the AMAPI SDK are
  available. See the [Release notes](https://developers.google.com/android/management/sdk-release-notes) for the details of what is included in these versions.

## August 2025

### Android Management API

* We are now supporting installation of applications using AMAPI SDK
  1.6.0-rc01 and later. To install an application, add it to the
  [`application policy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#applicationpolicy) with [`installType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype) `CUSTOM` and the application's
  signing key certificates are specified in the [`signingKeyCerts`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#applicationsigningkeycert) list. Using AMAPI SDK, issue [`installCustomApp`](https://developers.google.com/android/management/reference/amapi/com/google/android/managementapi/commands/model/IssueCommandRequest.InstallCustomApp) and [`uninstallCustomApp`](https://developers.google.com/android/management/reference/amapi/com/google/android/managementapi/commands/model/IssueCommandRequest.UninstallCustomApp) commands to install and uninstall the
  custom applications. See the [documentation](https://developers.google.com/android/management/manage-custom-apps) for more details
* We've added [`ApplicationPolicy.signingKeyCerts`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.signing_key_certs) replacing the usage of
  [`ExtensionConfig.signingKeyFingerprintsSha256`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ExtensionConfig.FIELDS.signing_key_fingerprints_sha256), which is
  now deprecated. `ApplicationPolicy.signingKeyCerts` must be set
  when the app has [`installType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.install_type) set to `CUSTOM`
  (i.e. a custom app) or when the app has [`extensionConfig`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.extension_config) set (i.e. an extension app) and is not on
  the Play Store. See the [documentation](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.signing_key_certs) for more details.
* For the AMAPI SDK, we have released:
  + An updated stable release [v1.5.0](https://developers.google.com/android/management/sdk-release-notes#version-1.5.0)
  + A new release candidate [v1.6.0-rc01](https://developers.google.com/android/management/sdk-release-notes#version-1.6.0-rc01) that introduces the functionality to manage custom apps.

## July 2025

### Android Management API

* We've updated the [`PasswordRequirements`](https://developers.google.com/android/management/reference/rest/v1/PasswordRequirements) to allow complexity-based
  requirements on work profile scope. A new [guide](https://developers.google.com/android/management/password-policies-quality) has been published to explain interaction of complexity-based
  and non-complexity-based password settings.

## June 2025

### Android Management API

* For Android 16 and later, IT admins can now use the
  [`appFunctions`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.app_functions) policy setting to control whether apps on
  the device for fully managed devices or in the work profile for devices
  with work profiles are allowed to expose app functions.
  [`crossProfileAppFunctions`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#CrossProfilePolicies.FIELDS.cross_profile_app_functions)can be used to control whether
  personal profile apps can invoke app functions exposed by apps in the work
  profile.
* We've added to the Android Management API two new methods:
  [`modifyPolicyApplications`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies/modifyPolicyApplications) and
  [`removePolicyApplications`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies/removePolicyApplications). These methods allow creating,
  updating, and removing subsets of applications in the Policy applications
  field, without having to fetch and supply to
  [`policies.patch`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies/patch) all the applications that remain
  unchanged.
* A new
  [`WIPE`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.WIPE) command is being introduced as an alternative to
  [`devices.delete`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete), and can be triggered using
  [`devices.issueCommand`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand). This method triggers company-owned
  devices to factory reset and personally-owned devices to delete the work
  profile. After the wipe or deletion, the device record will also be
  deleted.
    
  We have published a new [guide](https://developers.google.com/android/management/deprovision-device) to explain the various methods for deprovisioning a device.
* We've updated the Android Management API SDK (AMAPI SDK) to include the
  [`Device.WorkProfileState`](https://developers.google.com/android/management/reference/amapi/com/google/android/managementapi/device/model/Device.WorkProfileState) signal to identify the device
  management state.
    
  See the
  [AMAPI SDK Release notes](https://developers.google.com/android/management/sdk-release-notes#version-1.4.0) for further details.

## May 2025

### Android Management API

* We've added a new policy restriction
  [`apnPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#apnpolicy) to
  [`DeviceConnectivityManagement`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceconnectivitymanagement) to enable IT admins to
  configure Access Point Names (APNs) on devices. The APNs enforced by the
  policy will override any other APNs configured by users.
* A new policy restriction
  [`preferentialNetworkServiceSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PreferentialNetworkServiceSettings) has been implemented
  in
  [`DeviceConnectivityManagement`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceconnectivitymanagement) to enable IT admins to
  configure preferential networks. The
  [`preferentialNetworkId`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.preferential_network_id) field in the
  [Application](https://developers.google.com/android/management/reference/rest/v1/enterprises.applications) can be used to choose a preferential network for each
  individual application. More information can be found on our
  [5G network slicing](https://developers.google.com/android/management/5g-network-slicing)
  guide and on AOSP
  [5G
  network slicing](https://source.android.com/docs/core/connect/5g-slicing) docs.
* This release provides IT admins with enhanced eSIM management, enabling
  them to
  [add](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.ADD_ESIM),
  [remove](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.REMOVE_ESIM) and
  [view](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#telephonyinfo) managed eSIMs across all devices. From now, admins can define
  policies for managed eSIMs, specifying their behaviour if a device is
  wiped or a work profile becomes non-compliant, ensuring control and
  compliance with organizational policies.
* The new
  [`enterpriseDisplayNameVisibility`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.enterprise_display_name_visibility) policy setting allows
  administrators to control visibility of the
  [`enterpriseDisplayName`](https://developers.google.com/android/management/reference/rest/v1/enterprises#Enterprise.FIELDS.enterprise_display_name) on the device, such as on the lock
  screen of company-owned devices. While it now defaults showing the
  enterprise name configured during initial device setup, this will change
  in six months (November 2025), at which point the default will be
  [`ENTERPRISE_DISPLAY_NAME_VISIBLE`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#EnterpriseDisplayNameVisibility.ENUM_VALUES.ENTERPRISE_DISPLAY_NAME_VISIBLE).

## April 2025

### Android Management API

* We've added a new policy restriction [`bluetoothSharing`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.bluetooth_sharing) to [`PersonalUsagePolicies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#personalusagepolicies)
  and [`DeviceConnectivityManagement`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceconnectivitymanagement)
  to enable IT admins to allow or disallow sharing of files using Bluetooth.
* A new [security log event](https://developers.google.com/android/management/reference/rest/v1/BackupServiceToggledEvent) is generated and notified using Pub/Sub
  notification in AMAPI when [`BackupServiceState`](https://developers.google.com/android/management/reference/rest/v1/BackupServiceState) field is enabled or disabled by the
  admin.
* We've added a new field [`EuiccChipInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#euiccchipinfo) in [`HardwareInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#hardwareinfo) to read
  EID for corporate-owned devices and a new command [`REQUEST_DEVICE_INFO`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#requestdeviceinfoparams) has been added to read EID from
  personally-owned devices.
* Documentation items have also been updated:
  + We've updated the Android Management API SDK (AMAPI SDK) to include the
    stable release of Device Trust from Android Enterprise. Release notes are
    available at <https://developers.google.com/android/management/sdk-release-notes>

## March 2025

### Android Management API

* The Enterprise resource now includes more details in the [enterprise type](https://developers.google.com/android/management/reference/rest/v1/enterprises#enterprisetype) field. They specify whether the
  enterprise uses [Managed Google Play Accounts](https://developers.google.com/android/management/reference/rest/v1/enterprises#managedgoogleplayaccountsenterprisetype) (and if it's customer-owned
  or EMM-owned) or if it's a [managed Google domain](https://developers.google.com/android/management/reference/rest/v1/enterprises#managedgoogledomaintype) (either DNS-verified or
  an email-verified team). This information helps EMMs prepare for an
  upcoming feature that allows enterprises to upgrade from Managed Google
  Play Accounts to managed Google domains, allowing them to adapt the IT
  admin console based on the enterprise type.

## February 2025

### Android Management API

* We added [the guide](https://developers.google.com/android/management/work-profile-detection) on how to detect work profiles managed by the Android
  Device policy app.
* We've updated the Android Management API SDK (AMAPI SDK) to include the
  first release candidate for the device trust signal APIs.
  See [AMAPI SDK release notes](https://developers.google.com/android/management/sdk-release-notes#version-1.3.0-rc01) to know what is the latest version available.

## January 2025

### Android Management API

* EMMs can now limit the IT admin to sign up using an email from an
  [allowlist of domain names](https://developers.google.com/android/management/reference/rest/v1/signupUrls/create#query-parameters).
* Documentation items have also been updated:
  + The [web apps guide](https://developers.google.com/android/management/web-apps#display-mode) has been updated to clarify how the user's chosen
    default browser interacts with display settings like fullscreen or
    minimal UI. The browser may or may not support these attributes.
    IT administrators are responsible for testing the browser's compatibility
    with web app settings before deploying it to users.

## December 2024

### Android Management API

* For Android 15 and later, IT admins can now use the [`privateSpacePolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.private_space_policy) to allow or disallow the creation of a
  [Private Space](https://source.android.com/docs/security/features/private-space).
* For Android 15 and later, we introduced [`WifiRoamingMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifiroamingmode) in [`WifiRoamingPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifiroamingpolicy), allowing IT admins to disable Wi-Fi
  roaming for specific SSIDs on fully managed devices and on work profiles
  on company-owned devices.
* Various items of our documentation have been updated:
  + The description of the [`keyguardDisable`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.keyguard_disabled) field now includes
    information about management mode.
  + The [`securityPosture`](https://developers.google.com/android/management/understanding-security-posture) documentation now includes a [table](https://developers.google.com/android/management/understanding-security-posture#android_management_api_to_play_integrity_api_mappings) that shows the equivalent Play Integrity API verdict for each
    AM API verdict.

## November 2024

### Android Management API

* We now prevent users from changing their email address during customers
  signup. We also introduced validation for [`admin_email`](https://developers.google.com/android/management/reference/rest/v1/signupUrls/create#body.QUERY_PARAMETERS.admin_email)
  when creating a signup URL.
* Various items of our documentation have been updated:
  + We updated the description for the [`addUserDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.add_user_disabled)
    policy. For devices where [`managementMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#Device.FIELDS.management_mode) is
    [`DEVICE_OWNER`](https://developers.google.com/android/management/reference/rest/v1/ManagementMode#ENUM_VALUES.DEVICE_OWNER) this field is ignored and
    the user is never allowed to add or remove users.
  + We updated the [`ExtensionConfig`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#extensionconfig)
    to clarify that exempt from battery restrictions applies to Android 11
    and above.
  + We updated the description of the [`PermissionPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PermissionPolicy.ENUM_VALUES.GRANT)
    .
  + We clarified to how many applications a scope can be delegated in the
    [`DelegatedScope`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#delegatedscope) enum.

## October 2024

### Android Management API

* We updated the behavior of the
  [`CommonCriteriaMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#commoncriteriamode) policy.  
  `COMMON_CRITERIA_MODE_ENABLED` will now enable cryptographic
  policy integrity check and additional network certificate validation. The
  result of the policy integrity check is set to
  [`PolicySignatureVerificationStatus`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#policysignatureverificationstatus) if
  [`statusReportingSettings.commonCriteriaModeEnabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#StatusReportingSettings.FIELDS.common_criteria_mode_enabled) is set
  to `true`.  
  There are no changes to the behaviour of the default value
  (`COMMON_CRITERIA_MODE_UNSPECIFIED`) or when explicitly
  disabling it with `COMMON_CRITERIA_MODE_DISABLED`.
* We updated the documentation for
  [`PERSONAL_USAGE_DISALLOWED_USERLESS`](https://developers.google.com/android/management/reference/rest/v1/AllowPersonalUsage#ENUM_VALUES.PERSONAL_USAGE_DISALLOWED_USERLESS) to remind developers
  that this change is necessary before January 2025. If this change is
  omitted, users may encounter an *"Authenticate with Google"* prompt
  during enrollment, when their IT admin has this feature enabled.  
  The complete timeline for this feature is published on the Android
  Enterprise partner portal:
  [Feature Timeline: Improved sign-up flow, device enrollment, and on-device
  experiences.](https://emm.androidenterprise.dev/s/article/Feature-Timeline-for-Better-Together-Enterprise)
* We updated the documentation for
  [`CrossProfileDataSharing`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#CrossProfileDataSharing) to include details of simple data
  sharing via intents.

## September 2024

### Android Management API

The Android Management API now supports the following Android 15 features:

* For Android 15 and above a new policy has been added to control Wi-Fi
  roaming settings. IT Admins can use
  [`WifiRoamingPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifiroamingpolicy) to select the desired
  [`WifiRoamingMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifiroamingmode). Supported on fully managed devices and
  work profiles on company-owned devices.

## Android 15 release

### Android Management API

The Android Management API now supports the following Android 15 features:

* Android 15 introduces a new policy to control
  [*Circle to Search*](https://support.google.com/android/answer/14508957). IT admins can use
  [`AssistContentPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#assistcontentpolicy) to control this feature.
* Android 15 introduces a new policy to control Phishing Detection of apps.
  IT admins can use
  [`ContentProtectionPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#contentprotectionpolicy) to control whether the app is
  scanned by **On Device Abuse Detection** (ODAD) for phishing
  malware.
  **Note:** Users are not able to see this control from settings on
  devices with a work profile. This will be fixed in a later platform
  release.
* Android 15 expands the support of
  [screen brightness](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#screenbrightnesssettings) and [screen timeout](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#screentimeoutsettings) settings using the [`DisplaySettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#displaysettings) policy to company-owned devices with a work
  profile. This setting was previously available only on fully managed devices.

## August 2024

### Android Management API

* On Android 13+, IT ​​Admins can now query the
  [`ICCID`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#TelephonyInfo.FIELDS.icc_id) associated with the SIM card of the
  [`TelephonyInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#telephonyinfo) included in a
  [`NetworkInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#networkinfo). This is supported on fully managed devices
  when the
  [`networkInfoEnabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#StatusReportingSettings.FIELDS.network_info_enabled) field in
  [`statusReportingSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#statusreportingsettings) is set to `true`.
* Various items of our documentation have been updated:
  + We updated the
    [documentation for the Common Criteria Mode](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#commoncriteriamode) to clarify that it is
    only supported on company-owned devices running Android 11 or above.
  + We documented the optional field
    [`DefaultStatus`](https://developers.google.com/android/management/reference/rest/v1/enterprises#SigninDetail.FIELDS.default_status) in
    [`SigninDetail`](https://developers.google.com/android/management/reference/rest/v1/enterprises#SigninDetail).

## July 2024

### Android Management API

* Various items of our documentation have been updated:
  + We removed the note in the documentation for
    [`enrollmentToket.create`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens/create) about not being able to
    retrieve the token content anymore as it is possible getting the
    enrollment token value using
    [`enrollmentTokens.get`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens/get).
  + We clarified
    [`NonComplianceReason`](https://developers.google.com/android/management/reference/rest/v1/NonComplianceReason) documentation.

## June 2024

### Android Management API

* IT admins can now control the [screen brightness](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#screenbrightnesssettings) and [screen timeout](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#screentimeoutsettings) settings using the [`DisplaySettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#displaysettings) policy. Supported on fully managed devices, on Android 9 and above.
* We've updated our documentation to explain that, even when using
  [`AUTO_UPDATE_HIGH_PRIORITY`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#AutoUpdateMode.ENUM_VALUES.AUTO_UPDATE_HIGH_PRIORITY), updates to apps with larger
  deployments across Android's ecosystem can take up to 24h.
* We've updated the Android Management API SDK (AMAPI SDK) to explain
  the different use cases that this library (originally known as
  Extensibility SDK) now supports. The updated documentation covers:
  + [How to integrate the library](https://developers.google.com/android/management/extensibility-sdk-integration)
  + [Extension apps and local commands](https://developers.google.com/android/management/sdk-local-commands)
  + [DPC migration](https://developers.google.com/android/management/dpc-migration)

  See [AMAPI SDK release notes](https://developers.google.com/android/management/sdk-release-notes) to know what is the latest version available.

## May 2024

### Android Management API

* The [`get`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens/get) and [`list`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens/list) methods for [`enrollmentTokens`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens) now return populated [`value`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens#EnrollmentToken.FIELDS.value), [`qrCode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens#EnrollmentToken.FIELDS.qr_code), and [`allowPersonalUsage`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens#EnrollmentToken.FIELDS.allow_personal_usage) fields.
* For fully managed devices, the
  [`AllowPersonalUsage`](https://developers.google.com/android/management/reference/rest/v1/AllowPersonalUsage) setting now
  supports the
  [`PERSONAL_USAGE_DISALLOWED_USERLESS`](https://developers.google.com/android/management/reference/rest/v1/AllowPersonalUsage#ENUM_VALUES.PERSONAL_USAGE_DISALLOWED_USERLESS).
* On Android 11+ the new
  [`UserControlSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#usercontrolsettings) policy
  allows to specify whether user control is permitted for a given app.
  `UserControlSettings` includes user actions like force-stopping
  and clearing app data.
* Version 1.1.5 of the AMAPI SDK is now available. Additional
  information is available on the [release notes page](https://developers.google.com/android/management/sdk-release-notes).

  **Note:** We strongly recommend to always use the latest
  available version of the library to benefit from the available bug fixes
  and improvements.

## April 2024

### Android Management API

* On Android 13+, for company-owned devices, we added controls over
  which WiFi SSIDs devices can connect to. Using
  [`WifiSsidPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifissidpolicy) IT Admins can specify a list of SSIDs to
  be added to an allowlist (
  [`WIFI_SSID_ALLOWLIST`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#WifiSsidPolicyType.ENUM_VALUES.WIFI_SSID_ALLOWLIST)) or to a denylist (
  [`WIFI_SSID_DENYLIST`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#WifiSsidPolicyType.ENUM_VALUES.WIFI_SSID_DENYLIST)).
* For corporate-owned devices, we added hardware identifiers (IMEI,
  MEID, and serial number) to
  [`ProvisioningInfo`](https://developers.google.com/android/management/reference/rest/v1/provisioningInfo#ProvisioningInfo) that EMMs can now access during device
  setup using the
  [sign-in](https://developers.google.com/android/management/provision-device#sign-in_url) URL.

## March 2024

### Android Management API

* We added additional controls over app installation using
  [`InstallConstraint`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installconstraint),
  IT admins can restrict app installation based on specific criteria.  
  By setting
  [`installPriority`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy.FIELDS.install_priority),
  IT admins can ensure that critical apps are installed first.
* On Android 10+, AMAPI supports configuring enterprise 192 bit networks
  in
  [openNetworkConfiguration](https://developers.google.com/android/management/configure-networks#eap_authentication)
  by passing Security value WPA3-Enterprise\_192.  
  On Android 13+, in the
  [`MinimumWifiSecurityLevel`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#minimumwifisecuritylevel)
  policy, we now support
  [`ENTERPRISE_BIT192_NETWORK_SECURITY`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#MinimumWifiSecurityLevel.ENUM_VALUES.ENTERPRISE_BIT192_NETWORK_SECURITY),
  which can be used to ensure that devices do not connect to Wi-Fi networks
  below this security level.
* We have updated the
  [`UsbDataAccess`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#usbdataaccess)
  setting so that the
  [`USB_DATA_ACCESS_UNSPECIFIED`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#UsbDataAccess.ENUM_VALUES.USB_DATA_ACCESS_UNSPECIFIED)
  value defaults to
  [`DISALLOW_USB_FILE_TRANSFER`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#UsbDataAccess.ENUM_VALUES.DISALLOW_USB_DATA_TRANSFER).

## February 2024

### Android Management API

* On Android 9+, IT admins can now control whether printing is allowed
  using the
  [`printingPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#printingpolicy)
  field.
* For Android 14+, a new policy is added to control
  [CredentialProvider](https://developer.android.com/reference/androidx/credentials/CredentialProvider)
  apps. IT admins can use the
  [`credentialProviderPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#credentialproviderpolicy)
  field to control whether the app is allowed to act as a credential
  provider.
* A new policy is added to control
  [Arm Memory Tagging Extension](https://source.android.com/docs/security/test/memory-safety/arm-mte) (MTE) on the device. The
  [`MtePolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#MtePolicy)
  field is supported on fully managed devices and work profiles on
  company-owned devices with Android 14 and above.
* We have updated how AM API receives errors related to installs that
  are triggered by IT admins. As a result of this migration, the
  [`InstallationFailureReason`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#installationfailurereason) field now also includes client
  errors (in addition to the server errors).
* For Android 12+, IT admins can use a key pair installed on the device
  for enterprise Wi-Fi authentication. See the new
  [`ClientCertKeyPairAlias`](https://chromium.googlesource.com/chromium/src/+/main/components/onc/docs/onc_spec.md#:~:text=ClientCertKeyPairAlias) field in Open Network
  Configuration (ONC) and
  [our network configuration guide](https://developers.google.com/android/management/configure-networks#eap_authentication) for more information.

## January 2024

### Android Management API

* Devices managed by your custom DPC can now be seamlessly
  [migrated](https://developers.google.com/android/management/dpc-migration)
  to use Android Management API.

## December 2023

### Android Management API

* Added
  [`MinimumWifiSecurityLevel`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#MinimumWifiSecurityLevel)
  to define the different minimum security levels required to connect to
  Wi-Fi networks. Supported on fully managed devices and work profiles on
  company-owned devices with Android 13 and above.

## November 2023

### Android Management API

* Android 12+ now supports passwordless enterprise Wi-Fi network
  configuration using `Identity` and `Password`
  fields in
  [Open Network Configuration](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/onc/docs/onc_spec.md#eap-configurations).
  This was already supported prior to Android 12.

  **Note:** On Android 12+, for Wi-Fi networks with EAP
  username/password authentication, if the user password is not provided and
  `AutoConnect` is set to `true`, the device might
  try to connect to the network with a randomly generated placeholder
  password. To avoid this when the user’s password is not provided, set
  `AutoConnect` to `false`.
* Local device events that occur in quick succession are batched and
  reported in a single [Pub/Sub message](https://developers.google.com/android/management/notifications) to EMMs.

  | **Event type** | **Expected latency between on-device event and corresponding EMM notification1** | |
  | --- | --- | --- |
  | **Previous behavior** | **New behavior** |
  | High priority [keyed app states](https://developers.google.com/android/management/app-feedback) | Immediate, at most one report per minute | Immediate, at most one report per minute |
  | Standard priority [keyed app states](https://developers.google.com/android/management/app-feedback) | Schedule-based | Within one minute |
  | Application-related events *during* provisioning, for apps with install states defined by the IT admin2 | Integrated into other provisioning-related events | Within one minute on top of other related provisioning events |
  | Application-related events *after* provisioning, for apps with install states defined by the IT admin2 | Schedule-based | Within 5 minutes |
  | Application-related events both *during* and *after* provisioning, for apps with install states defined by the employee3 | Schedule-based | Within 60 minutes |
  | Other on-device app events | Schedule-based | Within 60 minutes |

  1
  Best effort targets based on controlled circumstances. Actual latency
  may vary according to a variety of device and environmental factors.  
  2
  [`InstallType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype)
  of apps enforced in the policy: `FORCE_INSTALLED`,
  `BLOCKED`, `REQUIRED_FOR_SETUP`,
  `PREINSTALLED` and `KIOSK`.  
  3
  [`InstallType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype)
  of available apps: `AVAILABLE`,
  `INSTALL_TYPE_UNSPECIFIED`.

## October 2023

### Android Management API

* Apps launched as [`SetupAction`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#setupaction)
  can now cancel enrollment. This will reset a company-owned
  device or deletes the work profile on a personally-owned device.

## Android 14 release

### Android Management API

With the [release of Android 14](https://blog.google/products/android-enterprise/Android-14-for-business/), the Android Management API now supports the
following Android 14 features:

* Restricting work profile contacts access
  to system applications and personal apps specified in
  [`exemptionsToShowWorkContactsInPersonalProfile`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#CrossProfilePolicies.FIELDS.exemptions_to_show_work_contacts_in_personal_profile).
  Now access to work profile contacts can be enabled for all personal
  apps, select personal apps, or no personal apps.

  For convenience, the new [`SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_DISALLOWED_EXCEPT_SYSTEM`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ShowWorkContactsInPersonalProfile.ENUM_VALUES.SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_DISALLOWED_EXCEPT_SYSTEM)
  option in [`showWorkContactsInPersonalProfile`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#showworkcontactsinpersonalprofile) ensures that the only
  personal apps to access work contacts are the device default Dialer,
  Messages, and Contacts apps. In this case, neither user-configured Dialer,
  Messages, and Contacts apps, nor any other system or user-installed
  personal apps, will be able to query work contacts.
* Disable use of the ultra wideband
  radio on the device. This can be achieved using the new
  [`deviceRadioState.ultraWidebandState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#DeviceRadioState.FIELDS.ultra_wideband_state) policy.
* Block the use of cellular 2G,
  improving network security. This is offered through the new
  [`deviceRadioState.cellularTwoGState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#DeviceRadioState.FIELDS.cellular_two_g_state) policy.
* Android 14 introduces [customizable lock screen shortcuts](https://blog.google/products/android/android-14/).

  The [lock screen features admin control](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#keyguarddisabledfeature), which includes camera,
  fingerprint unlock, face unlock, etc, has been extended
  to also disable lockscreen shortcuts using the new
  [`SHORTCUTS`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#KeyguardDisabledFeature.ENUM_VALUES.SHORTCUTS) option.

## September 2023

### Android Management API

* Device and provisioning information can now be optionally retrieved
  during setup, allowing developers to create more targeted policies during
  setup or filter devices according to the supplied attributes. The [sign-in url](https://developers.google.com/android/management/provision-device#sign-in_url)
  will now include a [`provisioningInfo`](https://developers.google.com/android/management/reference/rest/v1/provisioningInfo)
  parameter which can be exchanged for the corresponding device details
  using the new [provisioningInfo get](https://developers.google.com/android/management/reference/rest/v1/provisioningInfo/get)
  method.
* [`SigninDetails`](https://developers.google.com/android/management/reference/rest/v1/enterprises#signindetail)
  can now be distinguished from one another with a customizable [`tokenTag`](https://developers.google.com/android/management/reference/rest/v1/enterprises#SigninDetail.FIELDS.token_tag)
  value.

## August 2023

### Android Management API

* Introduced [Lost Mode](https://developers.google.com/android/management/lost-mode)
  for company-owned devices. Lost mode enables employers to remotely lock
  and secure a lost device and optionally to display a message on the device
  screen with contact information to facilitate asset recovery.
* Added support for certificate selection delegation which grants an app
  access to selection of KeyChain certificates on behalf of requesting apps.
  See [`DelegatedScope.CERT_SELECTION`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#DelegatedScope.ENUM_VALUES.CERT_SELECTION)
  for more details.
* Added additional WiFi management policies:
  + [`configureWifi`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#configurewifi)
    - Admins can now disable adding or configuring WiFi networks.
    [`wifiConfigDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.wifi_config_disabled)
    is now deprecated.
  + [`wifiDirectSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifidirectsettings)
    - This policy can be used to disable configuring WiFi direct.
  + [`tetheringSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#tetheringsettings)
    - This policy can be used to disable WiFi tethering or all forms of
    tethering. [`tetheringConfigDisabled`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.tethering_config_disabled)
    is now deprecated.
  + [`wifiState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wifistate)
    - This policy can be used to force enable/disable WiFi in a user's device.
* Sharing of admin configured WiFi networks will be disabled from Android 13 and above

## July 2023

### Android Management API

* Added [`userFacingType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#ApplicationReport.FIELDS.user_facing_type) field to
  [`ApplicationReport`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#ApplicationReport) to signal
  whether an app is user facing.
* Added [`ONC_WIFI_INVALID_ENTERPRISE_CONFIG`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#SpecificNonComplianceReason.ENUM_VALUES.ONC_WIFI_INVALID_ENTERPRISE_CONFIG)
  specific non-compliance reason.   
  Non-compliance with reason
  [`INVALID_VALUE`](https://developers.google.com/android/management/reference/rest/v1/NonComplianceReason#ENUM_VALUES.INVALID_VALUE)
  and specific reason `ONC_WIFI_INVALID_ENTERPRISE_CONFIG` is
  reported if enterprise Wi-Fi network does not have
  [`DomainSuffixMatch`](https://chromium.googlesource.com/chromium/src/+/main/components/onc/docs/onc_spec.md#eap-type)
  set.
* New Pub/Sub notification `EnrollmentCompleteEvent` added,
  as a type of
  [`UsageLogEvent`](https://developers.google.com/android/management/reference/rest/v1/BatchUsageLogEvents#usagelogevent)
  that is published when the device finishes the enrollment.
* Added [`airplaneModeState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#airplanemodestate)
  in
  [`deviceRadioState`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#deviceradiostate)
  to control the current state of airplane mode and whether the user can
  toggle it on or off. By default, the user is allowed to toggle airplane
  mode on or off. Supported on fully managed devices and work profiles on
  company-owned devices, on Android 9 and above.

## June 2023

### Android Management API

* Added support for the `DomainSuffixMatch` field in
  [Open
  Network Configuration](https://chromium.googlesource.com/chromium/src/+/main/components/onc/docs/onc_spec.md#eap-configurations) to configure enterprise WiFi networks for
  Android 6+. Enterprise WiFi configurations without `DomainSuffixMatch`
  are considered insecure and
  [will
  be rejected by the platform](https://developer.android.com/guide/topics/connectivity/wifi-enterprise).
* Added
  [`UsbDataAccess`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#usbdataaccess)
  policy setting that allows admins to fully disable USB data transferring.
  `usbFileTransferDisabled` is now deprecated, please use `UsbDataAccess`.

## December 2022

### Android Management API

* Management capabilities over Work Profile Widgets have been improved with the addition of two new API fields: [`workProfileWidgets`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#workprofilewidgets) on the application level and [`workProfileWidgetsDefault`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#crossprofilepolicies) on the device level. These allow greater control over whether an application running in the work profile can create widgets on the parent profile e.g. the home screen. This functionality is disallowed by default, but can be set to allowed using `workProfileWidgets` and `workProfileWidgetsDefault`, and is only supported for work profiles.
* We have added [support](https://developers.google.com/android/management/configure-networks) to set [MAC address randomization settings](https://source.android.com/docs/core/connect/wifi-mac-randomization-behavior#types) while configuring WiFi networks. Admins can now specify whether `MACAddressRandomizationMode` is set to `Hardware` or `Automatic` while configuring WiFi networks which takes effect on devices with OS version Android 13 and above and is applicable on all management modes. If set to `Hardware` the factory MAC address will be configured to the WiFi network, whereas `Automatic` the MAC address will be random.
* Various items of our documentation have been updated:

+ [Understanding Security Posture](https://developers.google.com/android/management/understanding-security-posture) has been created to provide clarity on the potential responses from [`devicePosture`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#deviceposture) and [`securityRisk`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#securityrisk) evaluations.
+ [`autoUpdateMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#autoupdatemode) has been provided for  [`autoUpdatePolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#appautoupdatepolicy) as a recommended alternative due to greater flexibility with update frequency.
+ We have provided clarification that [`BlockAction`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#blockaction) and [`WipeAction`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#wipeaction) are restricted to company-owned devices.
+ The  [Pub/Sub notifications page](https://developers.google.com/android/management/notifications#message_format) has been updated to accurately reflect the resource types for different notification types.
+ For Android 13+, [extension apps](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#extensionconfig) are exempt from battery restrictions so will not be placed into the [restricted App Standby Bucket.](https://developer.android.com/topic/performance/appstandby#restricted-bucket)

## October 2022

### Android Management API

* Various items of our documentation have been updated:

+ We recommend having one [policy](https://developers.google.com/android/management/create-policy) per device, to enable granular device-level management capabilities.
+ In order for [FreezePeriods](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#freezeperiod) to work as expected, system update policy cannot be set as [SYSTEM\_UPDATE\_TYPE\_UNSPECIFIED.](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#systemupdatetype)
+ Additional suggestions have been provided for policy updates regarding visibility of password steps during company-owned [device provisioning.](https://developers.google.com/android/management/provision-device#company-owned_devices_for_work_use_only)
+ [shareLocationDisabled](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#shareLocationDisabled) is supported for fully managed devices and personally owned work profiles.
+ We have provided an updated description on the usage of [enterprises.devices.delete](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete) and its effects on device visibility.
+ Maximum enrollment token [duration](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens#EnrollmentToken.FIELDS.duration) is now 10,000 years, where it was previously 90 days.

## July 12 2022

### Android Management API

* Added [NETWORK\_ACTIVITY\_LOGS](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#DelegatedScope.ENUM_VALUES.NETWORK_ACTIVITY_LOGS) and [SECURITY\_LOGS](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#DelegatedScope.ENUM_VALUES.SECURITY_LOGS) values to the [DelegatedScope](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#delegatedscope) to grant device policy applications access to the corresponding logs.

## June 14 2022

### Android Management API

* Added [specificNonComplianceReason](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#SpecificNonComplianceReason) and [specificNonComplianceContext](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#specificnoncompliancecontext) to [NonComplianceDetail](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#noncompliancedetail) to provide detailed context for policy application errors.

## June 6 2022

### Android Management API

* Added a [command](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand#CommandType.ENUM_VALUES.CLEAR_APP_DATA) to allow the admin to remotely clear the application data of an app.
* Enrollment tokens can now be [created](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens/create) with a longer [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration) than the previous maximum of 90 days, up to approximately 10,000 years. Enrollment tokens that last longer than 90 days will have a length of 24 characters, while tokens that last 90 days or less will continue to have 20 characters.

## May 24 2022

### Android Management API

* Hardware-backed security features such as [key attestation](https://developer.android.com/training/articles/security-key-attestation) will now be used in device integrity evaluations, when supported by the device. This provides a strong guarantee of system integrity. Devices that fail these evaluations or do not support such hardware-backed security features will report the new HARDWARE\_BACKED\_EVALUATION\_FAILED [SecurityRisk](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#SecurityRisk).

## May 16 2022

### Android Management API

* Added [unifiedLockSettings](https://developers.google.com/android/management/reference/rest/v1/PasswordRequirements#UnifiedLockSettings) in [PasswordPolicies](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.password_policies) to allow the admin to configure if the work profile needs a separate lock.

## March 25 2022

### Android Management API

* Added [alwaysOnVpnLockdownExemption](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#AlwaysOnVpnLockdownExemption) to specify which apps should be exempt from the
  [AlwaysOnVpnPackage](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#alwaysonvpnpackage) setting.
* Added all available fields from the Play EMM API [Products](https://developers.google.com/android/work/play/emm-api/v1/products) resource to the [Application](https://developers.google.com/android/management/reference/rest/v1/enterprises.applications) resource.

## February 22 2022

### Android Management API

* Added [cameraAccess](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.camera_access) to control the use of camera and camera toggle,
  and [microphoneAccess](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.microphone_access), to control the use of microphone and microphone toggle.
  These fields replace newly deprecated
  [cameraDisabled](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.camera_disabled) and
  [unmuteMicrophoneDisabled](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Policy.FIELDS.unmute_microphone_disabled), respectively.

## February 15 2022

### AMAPI SDK

* Minor bug fixes. See [Google's Maven Repository](https://maven.google.com/web/index.html#com.google.android.libraries.enterprise.amapi:amapi:1.0.1) for more details.

## November 15 2021

### Android Device Policy

* Apps that are marked as unavailable in
  [`personalApplications`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.personal_applications)
  will now be uninstalled from the personal profile of company-owned devices if already installed, as they are in the
  [ApplicationPolicy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ApplicationPolicy) for work profile and fully managed devices.

## September 17 2021

### Android Management API

* You can now designate an app as an extension app using [`ExtensionConfig`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#applicationpolicy). Extension apps can communicate directly with Android Device Policy and in future will be able to interact with the complete set of management features offered in the Android Management API, enabling a local interface for managing the device that does not require server connectivity.
  + This initial release includes support for local execution of [`Commands`](https://developers.google.com/android/management/reference/amapi/com/google/android/managementapi/commands/package-summary), and currently only the `ClearAppData` command. See the [extensibility integration guide](https://developers.google.com/android/management/extensibility-sdk-integration) for more details.
  + The remaining commands will be added over time, as well as additional extension app features designed to expose the breadth of device management features to the extension app.

## June 30 2021

### Android Device Policy

* Minor bug fixes

## June 2 2021

### Android Device Policy

* Minor bug fixes

## May 5 2021

### Android Device Policy

* Minor bug fixes

## April 6 2021

### Android Device Policy

* Minor bug fixes

## March 2021

### Android Management API

* Added two new [`AdvancedSecurityOverrides`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#advancedsecurityoverrides). These policies enable
  Android Enterprise security best practices by default, while allowing
  organizations to override the default values for advanced use cases.

+ `googlePlayProtectVerifyApps` enables
  [Google Play's app verification](https://developers.google.com/android/play-protect/client-protections)
  by default.
+ `developerSettings` prevents users from accessing
  [developer options](https://developer.android.com/studio/debug/dev-options)
  and safe mode by default, capabilities that would otherwise
  introduce risk of corporate data exfiltration.
To facilitate migration to the new
default behaviors, the default values for these policies are not
enforced for existing API users (Google Cloud projects with Android
Management API enabled as of April 15, 2021) until October
2021. Until then, existing API users must explicitly set a desired
value to use the new policies.
* [`ChoosePrivateKeyRule`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ChoosePrivateKeyRule)
  now supports the direct grant of specific KeyChain keys to managed
  apps.

+ This allows the target app(s) to access specified keys by calling
  [`getCertificateChain()`](https://developer.android.com/reference/android/security/KeyChain#getCertificateChain(android.content.Context,%20java.lang.String))
  and
  [`getPrivateKey()`](https://developer.android.com/reference/android/security/KeyChain#getPrivateKey(android.content.Context,%20java.lang.String))
  without having to first call
  [`choosePrivateKeyAlias()`](https://developer.android.com/reference/android/security/KeyChain#choosePrivateKeyAlias(android.app.Activity,%20android.security.KeyChainAliasCallback,%20java.lang.String%5B%5D,%20java.security.Principal%5B%5D,%20java.lang.String,%20int,%20java.lang.String)).
+ Android Management API defaults to granting direct
  access to the keys specified in policy, but otherwise falls back to
  granting access after the specified app has called
  [`choosePrivateKeyAlias()`](https://developer.android.com/reference/android/security/KeyChain#choosePrivateKeyAlias(android.app.Activity,%20android.security.KeyChainAliasCallback,%20java.lang.String%5B%5D,%20java.security.Principal%5B%5D,%20java.lang.String,%20int,%20java.lang.String)).
  See
  [`ChoosePrivateKeyRule`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ChoosePrivateKeyRule)
  for more details.

### Deprecations

* `ensureVerifyAppsEnabled` is now deprecated. Use the
  `googlePlayProtectVerifyApps` [`AdvancedSecurityOverrides`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#advancedsecurityoverrides) instead.

+ Existing API users (Google Cloud projects with Android Management
  API enabled as of April 15, 2021) can continue to use
  `ensureVerifyAppsEnabled`
  until October 2021, but are encouraged to migrate to
  [`AdvancedSecurityOverrides`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#advancedsecurityoverrides) as soon
  as possible. In October `ensureVerifyAppsEnabled` will no
  longer function.

* `debuggingFeaturesAllowed` and
  `safeBootDisabled` are now deprecated. Use the
  `developerSettings` [`AdvancedSecurityOverrides`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#advancedsecurityoverrides) instead.

+ Existing API users (Google Cloud projects with Android Management
  API enabled as of April 15, 2021) can continue to use
  `debuggingFeaturesAllowed` and
  `safeBootDisabled`
  until October 2021, but are encouraged to use
  [`AdvancedSecurityOverrides`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#advancedsecurityoverrides)
  as soon as possible. In October
  `debuggingFeaturesAllowed` and
  `safeBootDisabled` will no longer function.

## February 2021

### Android Management API

* Added [`personalApplications`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.personal_applications) support for company-owned
  devices starting from Android 8. The feature is now supported on all
  company-owned devices with a work profile.
* Device phone number is now reported on Fully Managed Devices as part
  of the [`Device`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#telephonyinfo) resource.

## January 2021

### Android Device Policy

* Minor bug fixes

## December 2020

### Android Management API

* Added [`personalApplications`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalUsagePolicies.FIELDS.personal_applications) to
  `PersonalUsagePolicies`. On company-owned devices, IT can
  specify an allow or blocklist of applications in the personal profile.
  This feature is currently available only on Android 11 devices, but
  will be backported to Android 8 in a future release.

### Android Device Policy

* Minor updates to the provisioning UI

  ![Provisioning UI](/static/android/management/images/provisioning.png)

## November 2020

### Android Management API

* Added [`AutoDateAndTimeZone`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#autodateandtimezone), replacing the deprecated
  `autoTimeRequired`, to control auto date, time, and time
  zone configuration on a company-owned device.
* Starting in Android 11, users can no longer clear app data or force
  stop applications when the device is configured as a kiosk (that is,
  when the `InstallType` of one application in
  `ApplicationPolicy` is set to `KIOSK`).
* Added new [`LocationMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#locationmode) controls to replace deprecated location
  detection method controls. On company-owned devices, IT can now choose
  between enforcing location, disabling location, or allowing users to
  toggle location on and off.
* Added support for [`CommonCriteriaMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#commoncriteriamode), a
  [new feature in Android 11](https://developer.android.com/work/versions/android-11#common). Can be enabled to address specific
  [Common Criteria Mobile
  Device Fundamentals Protection Profile](https://www.commoncriteriaportal.org/) (MDFPP) requirements.

### Deprecations

* `autoTimeRequired` is now deprecated, following the
  [deprecation of specific auto time controls](https://developer.android.com/work/versions/android-11#deprecations) in Android 11. Use
  [`AutoDateAndTimeZone`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#autodateandtimezone) instead.
* The following [`LocationMode`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#locationmode) options are now deprecated, following
  their [deprecation in Android 9](https://developer.android.com/reference/android/provider/Settings.Secure#LOCATION_MODE):
  `HIGH_ACCURACY`, `SENSORS_ONLY`,
  `BATTERY_SAVING`, and `OFF`. Use
  `LOCATION_ENFORCED`, `LOCATION_DISABLED`,
  and `LOCATION_USER_CHOICE` instead.

## October 2020

### Android Device Policy

* Added `RELINQUISH_OWNERSHIP` as a new type of
  [device command](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand).
  When deploying work profile, admins can relinquish ownership of
  company-owned devices to employees, wiping the work profile and
  resetting any device policies to factory state, while leaving personal
  data intact. In doing so, IT loses claim to the ownership of the
  device now and in the future and should not expect the device to
  re-enroll. To factory reset a device while maintaining ownership, use
  the [`devices.delete`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete) method instead.

## August 2020

### Android Management API

* Improvements to the work profile experience on company-owned
  devices were announced in the [Android 11 developer preview](https://developer.android.com/preview/work#work_profile_enhancements_for_company-owned_devices). Android Management API adds support for these
  improvements for devices running **Android 8.0+** or higher.
  Enterprises can now designate work profile devices as company-owned,
  allowing management of a device's work profile, personal usage policies,
  and certain device-wide settings while still maintaining privacy in the
  personal profile.

  + For a high-level overview of enhancement to the work profile
    experience, see [Work profile: the new standard for employee privacy](https://blog.google/products/android-enterprise/work-profile-new-standard-employee-privacy/).
  + See [Company-owned devices for work and personal use](https://developers.google.com/android/management/provision-device#company-owned_devices_for_work_and_personal_use) to learn how to set up a work profile on a company-owned device.
  + An example policy for a company-owned device with a work profile
    is available in [Devices with work profiles](https://developers.google.com/android/management/policies/work-profile#company-owned_devices).
  + Added [`blockScope`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#blockscope)
    to `blockAction`. Use `blockScope` to specify
    whether a block action applies to an entire company-owned device or
    to its work profile only.
* Added [`connectedWorkAndPersonalApp`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#connectedworkandpersonalapp)
  to `applicationPolicy`. Starting in Android 11, some core apps
  can connect across a device's work and personal profiles. Connecting an app
  across profiles can provide a more unified experience for users. For
  example, by connecting a calendar app, users could view their work and
  personal events displayed together.

  Some apps (for example, Google Search) may be connected on devices by
  default. A list of connected apps on a device is available in
  **Settings** > **Privacy** > **Connected work & personal apps**.

  Use [`connectedWorkAndPersonalApp`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#connectedworkandpersonalapp)
  to allow or disallow connected apps. Allowing an app to connect
  cross-profile only gives the user the *option* to connect the app.
  Users can disconnect apps at any time.
* Added [`systemUpdateInfo`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#systemupdateinfo)
  to `devices` to report information on pending system updates.

## July 2020

### Android Device Policy

* [July 23] Minor bug fixes

## June 2020

### Android Device Policy

* [June 17] Minor bug fixes.

## May 2020

### Android Device Policy

* [May 12] Minor bug fixes.

## April 2020

### Android Device Policy

* [April 14] Minor bug fixes.

## March 2020

### Android Device Policy

* [March 16] Minor bug fixes.

## February 2020

### Android Device Policy

* [Feb 24] Minor bug fixes.

## January 2020

### Android Device Policy

* [Jan 15] Minor bug fixes.

## December 2019

### Android Management API

* A new policy for blocking untrusted apps (apps from unknown sources) is
  available. Use [`advancedSecurityOverrides.untrustedAppsPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#UntrustedAppsPolicy) to:
  + Block untrusted app installs device-wide (including work profiles).
  + Block untrusted app installs in a work profile only.
  + Allow untrusted app installed device-wide.
  `advancedSecurityOverrides.untrustedAppsPolicy` replaces `installUnknownSourcesAllowed`,
  which is now deprecated. For more details, see the **Deprecations** section
  below.
* A timeout period for allowing non-strong screen lock methods (e.g.
  fingerprint and face unlock) can now be enforced on a device or work
  profile using [`requirePasswordUnlock`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#requirepasswordunlock).
  After the timeout period expires, a user must use a strong form of
  authentication (password, PIN, pattern) to unlock a device or work profile.
* Added [`kioskCustomization`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#kioskcustomization)
  to support the ability to enable or disable the following system UI features in
  [kiosk mode](https://developers.google.com/android/management/policies/dedicated-devices#kiosk-mode) devices:
  + Global actions launched from the power button (see `powerButtonActions`).
  + System info and notifications (see `statusBar`).
  + Home and overview buttons (see `systemNavigation`).
  + Status bar (see `statusBar`).
  + Error dialogs for crashed or unresponsive apps (see `systemErrorWarnings`).
* Added [`freezePeriod`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#freezeperiod)
  policy to support blocking system updates annually over a specified freeze
  period.
* A new parameter is available in [`devices.delete`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete): `wipeReasonMessage` lets you specify a short message to display to a
  user before wiping the work profile from their personal device.

### Deprecations

`installUnknownSourcesAllowed` is now marked as deprecated.
Support for the policy will continue until Q2 2020 for users who enabled
Android Management API **before 2:00pm GMT on December 19, 2019**.
The policy is not supported for users who enabled the API after this date.

[`advancedSecurityOverrides.untrustedAppsPolicy`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#UntrustedAppsPolicy) replaces `installUnknownSourcesAllowed`.
The table below provides a mapping between the two policies. Developers should
update their solutions with the new policy as soon as possible\*.

| installUnknownSourcesAllowed | advancedSecurityOverrides.untrustedAppsPolicy |
| --- | --- |
| `TRUE` | `ALLOW_INSTALL_DEVICE_WIDE` |
| `FALSE` | `ALLOW_INSTALL_IN_PERSONAL_PROFILE_ONLY`  **Note:** Applied to all device types (work profiles and fully managed). Because fully managed devices don't have a personal profile, untrusted apps are blocked across the entire device. To block untrusted apps across an entire device with a work profile, use `DISALLOW_INSTALL` instead. |

\*For users who enabled Android Management API before 2:00pm GMT on
December 19, 2019: The default value of
`untrustedAppsPolicy` (`DISALLOW_INSTALL`) is
**not applied** if `untrustedAppsPolicy` is set to
`UNTRUSTED_APPS_POLICY_UNSPECIFIED` or if the policy is left
unspecified. To block untrusted apps across an entire device, you must
explicitly set the policy to `DISALLOW_INSTALL`.

## November 2019

### Android Device Policy

* [Nov 27] Minor bug fixes.

## October 2019

### Android Management API

* New [`IframeFeature`](https://developers.google.com/android/management/reference/rest/v1/enterprises.webTokens#iframefeature) options allow you to specify which [Managed Google Play iframe](https://developers.google.com/android/management/apps#managed_google_play_iframe) features to enable/disable in your console.

### Android Device Policy

* [Oct 16] Minor bug fixes and performance optimization.

## September 04, 2019

### Features

* The [`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies)
  resource is now capable of distributing closed app releases (closed app
  tracks), allowing organizations to test pre-release versions of apps. For
  details, see [Distribute apps for closed testing](https://developers.google.com/android/management/apps#distribute_apps_for_closed_testing).
* Added `permittedAccessibilityServices` to
  [`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies),
  which can be used to:
  + disallow all non-system accessibility services on a device, or
  + only allow specified apps access to these services.

## August 6, 2019

### Features

* The Android Management API now evaluates the security of a device and
  reports findings in [device reports](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices)
  (under `securityPosture`). `securityPosture` returns
  the security posture status of a device (`POSTURE_UNSPECIFIED`,
  `SECURE`, `AT_RISK`, or
  `POTENTIALLY_COMPROMISED`), as evaluated by
  [SafetyNet](https://developer.android.com/training/safetynet/attestation.html)
  and other checks, along with details of any identified security risks for
  you to share with customers through your management console.

  To enable this feature for a device, ensure its policy has least one field
  from [`statusReportingSettings`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#statusreportingsettings) enabled.

## July 02, 2019

### Features

* To distinguish that an app is launched from `launchApp` in
  [`setupActions`](https://developers.google.com/android/management/provision-device#launch_an_app_during_setup), the activity that's first launched as
  part of the app now contains the boolean intent extra
  `com.google.android.apps.work.clouddpc.EXTRA_LAUNCHED_AS_SETUP_ACTION`
  (set to `true`). This extra allows you to customize your app
  based on whether it's launched from `launchApp` or by a user.

## May 31, 2019

### Maintenance release

* Minor bug fixes and performance optimization.

## May 7, 2019

[`complianceRules`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#compliancerule)
is now deprecated, though it will continue to be supported until late Q2/early
Q3 2019 to allow EMMs to update their policies. To avoid disruption to your
implementation, replace policies containing
[`complianceRules`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#compliancerule)
with [`policyEnforcementRules`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#policyenforcementrule)
using the new compliance logic described in [Policy compliance](https://developers.google.com/android/management/create-policy#policy_compliance).


### Features

* Added [`policyEnforcementRules`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#policyenforcementrule)
  to replace [`complianceRules`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#compliancerule),
  which has been deprecated. See the deprecation notice above for more
  information.
* Added new APIs to create and edit web apps. For more details, see
  [Support web apps](https://developers.google.com/android/management/web-apps).

### User experience

**Android Device Policy:** The app’s icon is no longer
visible on devices. Users can still view the policy page previously
launched by the icon:

* Fully managed devices: Settings > Google > Device Policy
* Devices with work profiles: Settings > Google > Work > Device Policy
* All devices: Google Play Store app > Android Device Policy

## April 16, 2019

* Android Device Policy is now available in South Korea.

## March 21, 2019

### Features

* Added new metadata, including alternate serial numbers, to
  [`devices`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices).
* The number of apps with
  [`installType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype)
  `REQUIRED_FOR_SETUP` is now limited to five per policy. This is
  to ensure the best possible user experience during device and work profile
  provisioning.

## February 12, 2019

### User experience

* **Android Device Policy:** Added improved [non-compliance](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#compliancerule)
  messaging to help users return their devices to a compliant state or inform
  them when it isn’t possible.
* **Android Device Policy:** After an enrollment token is registered, a
  new setup experience guides users through the steps required by their policy
  to complete their device or work profile configuration.

  ![dark-mode](/static/android/management/images/device-setup.png)


  **Figure 1.** Guided setup experience.

### Features

* Added new field to [`installType`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#installtype)
  + `REQUIRED_FOR_SETUP`: If true, the app must be installed
    before the device or work profile setup completes. **Note:** If the
    app isn't installed for any reason (e.g. incompatibility,
    geo-availability, poor network connection), setup won't complete.
* Added [`SetupAction`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#setupaction) to `policies`. With `SetupAction`, you can specify an app to launch during setup, allowing a user to further configure their device. See [Launch an app during setup](https://developers.google.com/android/management/provision-device#launch_an_app_during_setup) for more details.
* For enterprises with [status
  reports enabled](https://developers.google.com/android/management/notifications), new device reports are now issued immediately following
  any failed attempt to unlock a device or work profile.

### Deprecations

* In [`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies), `wifiConfigsLockdownEnabled` has been deprecated. WiFi networks
  specified is policy are now non-modifiable by default. To make them
  modifiable, set `wifiConfigDisabled` to false.

## December 10, 2018

### Features

* Added support for work profile devices to the [sign-in URL](https://developers.google.com/android/management/provision-device#sign-in_url)
  provisioning method. Work profile device owners can now sign in with their
  corporate credentials to complete provisioning.

### User experience

* Added support for dark mode in Android Device Policy. Dark mode is a
  display theme available in Android 9 Pie, which can be enabled in
  **Settings** > **Display** > **Advanced** > **Device theme** >
  **Dark**.

  ![dark-mode](/static/android/management/images/dark-mode.jpg)


  **Figure 1.** (L) Normal display mode (R) Dark mode

## November 2, 2018

### Features

* A new [enrollment
  method](https://developers.google.com/android/management/provision-device#sign-in_url) is available for fully managed devices. The method uses a
  sign-in URL to prompt users to enter their credentials, allowing you to
  assign a policy and provision users' devices based on their identity.
* Added support for the [managed configurations iframe](https://developers.google.com/android/management/managed-configurations-iframe),
  a UI you can add to your console for IT admins to set and save managed
  configurations. The iframe returns a unique `mcmId` for each
  saved configuration, which you can add to
  `policies`.
* Added `passwordPolicies` and `PasswordPolicyScope` to `policies`:
  + `passwordPolicies` sets the password requirements for the
    specified scope (device or work profile).
  + If `PasswordPolicyScope` isn't specified, the default scope is `SCOPE_PROFILE`
    for work profile devices, and `SCOPE_DEVICE` for fully
    managed or dedicated devices.
  + `passwordPolicies` overrides `passwordRequirements`
    if `PasswordPolicyScope` is unspecified (default), or
    `PasswordPolicyScope` is set to the same scope as
    `passwordRequirements`

## September 20, 2018

### Bug fixes

* Fixed issue that made kiosk devices incorrectly appear out of compliance
  following provisioning, for a subset of policy configurations

## August 28, 2018

With this release, Android Management API now supports the
[work profile](https://developers.google.com/android/work/requirements/work-profile)
and [fully managed
device](https://developers.google.com/android/work/requirements/fully-managed-device) solution sets. For more information about solution sets, see
[develop
your solution](https://developers.google.com/android/work/release-solution#2_develop_your_solution).



### Features

*Updates to support work profile and fully managed device
provisioning and management:*

* New provisioning methods are available for work profiles:
  + Provide users with an [enrollment token link](https://developers.google.com/android/management/provision-device#%0Aenrollment_token_link).
  + Go to [**Settings** > **Google** >
    **Set up work profile**](https://developers.google.com/android/management/provision-device#add_work_profile%0A_from_settings).
* Added new fields to `enrollmentTokens`.
  + `oneTimeOnly`: If true, the enrollment token will expire after it's
    first used.
  + `userAccountIdentifier`: Identifies a specific
    [managed
    Google Play Account](https://developers.google.com/android/work/terminology#managed_google_play_account).
    - If not specified: The API silently creates a new account each
      time a device is enrolled with the token.
    - If specified: The API uses the specified account each time a
      device is enrolled with the token. You can specify the same
      account across multiple tokens. See [Specify a user](https://developers.google.com/android/management/p%0Arovision-device#specify_a_user) for more information.
* Added `managementMode` (read-only) to `devices`.
  + Devices with work profiles: `managementMode` is set to
    `PROFILE_OWNER`.
  + Dedicated devices and fully managed devices:
    `managementMode` is set to `DEVICE_OWNER`.

*Updates to the `policies` resource to improve app management
capabilities:*

* Added new field `playStoreMode`.
  + `WHITELIST` (default): Only apps added to policy are
    available in the work profile or on the managed device. Any app
    not in policy is unavailable, and uninstalled if previously
    installed.
  + `BLACKLIST`: Apps added to policy are unavailable.
    All other apps listed in Google Play are available.
* Added `BLOCKED` as an [InstallType](https://developers.google.com/android/management/refere%0Ance/rest/v1/enterprises.policies#installtype) option, which
  makes an app unavailable to install. If the app is already installed,
  it will be uninstalled.
  + You can use installType `BLOCKED` together with
    `playStoreMode` `BLACKLIST` to prevent a
    managed device or work profile from installing specific apps.

### User experience

* Updated Android Device Policy settings to match device settings.

## July 12, 2018

### User experience

* Merged the status and device details pages in Android Device Policy into
  a single page.
* Improved setup UI consistency with Android setup wizard.

### Features

* Added [PermissionGrants](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#%0Apermissiongrant) at the policy level. You can now control
  runtime permissions at four levels:
  + **Global, across all apps:** set defaultPermissionPolicy at the policy
    level.
  + **Per permission, across all apps:** set permissionGrant at the policy
    level.
  + **Per app, across all permissions:** set defaultPermissionPolicy within
    [ApplicationPolicy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Applicat%0AionPolicy).
  + **Per app, per permission:** set permissionGrant within
    [ApplicationPolicy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Applicat%0AionPolicy).
* When factory resetting a device, the new [WipeDataFlag](https://developers.google.com/android/management/refe%0Arence/rest/v1/enterprises.devices/delete#wipedataflag) allows
  you to:
  + `WIPE_EXTERNAL_STORAGE`: wipe the device's external storage
    (e.g. SD cards).
  + `PRESERVE_RESET_PROTECTION_DATA`: preserve the factory
    reset protection data on the device. This flag ensures that only an
    authorized user can recover a device if, for instance, the device is
    lost. **Note:** Only enable this feature if you've set
    `frpAdminEmails[]` in [policy](https://developers.google.com/android/management/reference/%0Arest/v1/enterprises.policies).

### Bug fixes

* Fixed issue with Android Device Policy exiting lock task mode when
  updating in the foreground.

## May 25, 2018

### User experience

* Instead of hiding disabled apps from the launcher, Android 7.0+ devices
  now display icons for disabled apps in gray:  

  ![Disabled apps](/static/android/management/images/disabled-apps.png)

### Features

* Updated [`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policie%0As) to support the following certificate management
  capabilities:
  + [Automatic granting of certificate access to apps.](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#ch%0Aooseprivatekeyrule)
  + [Delegating all certificate management features](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#de%0Alegatedscope) supported by
    Android Device Policy to another app (see `CERT_INSTALL`).
* Individual apps can now be disabled in [ApplicationPolicy](https://developers.google.com/android/management/refere%0Ance/rest/v1/enterprises.policies#applicationpolicy) (set
  `disabled` to `true`), independent of [compliance
  rules.](https://developers.google.com/androi%0Ad/management/reference/rest/v1/enterprises.policies#compliancerule)
* It's now possible to disable system apps.
* Added [application reports](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#a%0Applicationreport) to [`devices`](https://developers.google.com/android/management/refere%0Ance/rest/v1/enterprises.devices). For each managed app
  installed on a device, the report returns the app's package name, version,
  install source, and other detailed information. To enable, set
  `applicationReportsEnabled` to `true` in the
  device's [policy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies).
* Updated [`enterprises`](https://developers.google.com/android/management/reference/rest/v1/enterprises) to include [terms and conditions](https://developers.google.com/android/management/reference%0A/rest/v1/enterprises#termsandconditions). An
  enterprise's terms and conditions are displayed on devices during
  provisioning.

### Bug fixes

* Updated provisioning flow to disable access to settings, except when
  access is required to complete setup (e.g. creating a passcode).

## April 3, 2018

### User experience

* Updated the design of Android Device Policy and the device
  provisioning flow to improve overall user experience.

### Features

* Added support for [Direct Boot](https://developer.android.com/training/articles/direct-boot.html), allowing you to
  [remotely wipe](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete) Android 7.0+ devices that haven't been unlocked since
  they were last rebooted.
* Added a [location mode](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#%0Alocationmode) setting to the
  [`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies) resource, allowing you to configure the location
  accuracy mode on a managed device.
* Added an error response field to the
  [`Command`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueComm%0Aand#Command) resource.

### Bug fixes

* Provisioning performance has been improved.
* Compliance reports are now generated immediately after a device is
  provisioned. To configure an enterprise to receive compliance reports, see
  [Receive non-compliance detail notifications](https://developers.google.com/android/management/create-policy#receive_non-compliance_detail_notif%0Aications).

### Known issues

* Lock Screen Settings crashes on Android 8.0+ LG devices (e.g. LG V30)
  managed by Android Device Policy.

## February 14, 2018

### User experience

* Updated the validation text for the "code" field, which is displayed if a
  user chooses to manually enter a QR code to enroll a device.

### Features

* You can now set a policy to trigger force-installed apps to auto-update if
  they don't meet a specified minimum app version. In
  [ApplicationPolicy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#Applicatio%0AnPolicy):
  + Set `installType` to `FORCE_INSTALLED`
  + Specify a `minimumVersionCode`.
* Updated the
  [Devices](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices)
  resource with new fields containing information that may be useful to IT
  admins, such as the device's carrier name (see
  [NetworkInfo](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#NetworkInfo) for more details), whether the device is encrypted, and
  whether Verify Apps is enabled (see [DeviceSettings](https://developers.google.com/android/management/reference/res%0At/v1/enterprises.devices#DeviceSettings) for more details).

### Bug fixes

* The `RESET_PASSWORD` and `LOCK`
  [commands](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand) now work with Android 8.0 Oreo devices.
* Fixed issue with
  [DeviceSettings](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices#DeviceSettings) not being populated.
* Fixed issue with `stayOnPluggedModes` policy handling.

## December 12, 2017

### Features

* Android Device Policy now supports a basic
  [kiosk launcher](https://developers.google.com/android/management/create-policy#kiosk-launcher), which can be enabled via policy. The launcher locks down a device to a
  set of predefined apps and blocks user access to device settings. The
  specified apps appear on a single page in alphabetical order. To report a
  bug or request a feature, tap the feedback icon on the launcher.
* Updated device setup with new retry logic. If a device is rebooted during
  setup, the provisioning process now continues where it left off.
* The following new policies are now available. See the
  [API
  reference](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies) for full details:

  |  |  |
  | --- | --- |
  | `keyguardDisabledFeatures` | `accountTypesWithManagementDisabled` |
  | `installAppsDisabled` | `mountPhysicalMediaDisabled` |
  | `uninstallAppsDisabled` | `bluetoothContactSharingDisabled` |
  | `shortSupportMessage` | `longSupportMessage` |
  | `bluetoothConfigDisabled` | `cellBroadcastsConfigDisabled` |
  | `credentialsConfigDisabled` | `mobileNetworksConfigDisabled` |
  | `tetheringConfigDisabled` | `vpnConfigDisabled` |
  | `createWindowsDisabled` | `networkResetDisabled` |
  | `outgoingBeamDisabled` | `outgoingCallsDisabled` |
   `smsDisabled` | `usbFileTransferDisabled` || `ensureVerifyAppsEnabled` | `permittedInputMethods` |
  | `recommendedGlobalProxy` | `setUserIconDisabled` |
  | `setWallpaperDisabled` | `alwaysOnVpnPackage` |
  | `dataRoamingDisabled` | `bluetoothDisabled` |
* Updated Android Device Policy's target SDK to
  [Android 8.0
  Oreo](https://source.android.com/setup/build-numbers).

### Bug Fixes

* It's now possible to skip the network picker display if a connection can't
  be made at boot. To enable the network picker on boot, use the
  `networkEscapeHatchEnabled` policy.
