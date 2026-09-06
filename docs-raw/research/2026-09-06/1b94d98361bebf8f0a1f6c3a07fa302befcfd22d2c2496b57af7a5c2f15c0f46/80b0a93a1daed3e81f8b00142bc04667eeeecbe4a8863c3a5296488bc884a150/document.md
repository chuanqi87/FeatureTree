# Profile-specific payload keys

Apply settings to devices using configuration profiles.

## Discussion

In addition to the standard payload keys (described in [Define a profile](/documentation/DeviceManagement/configuring-multiple-devices-using-profiles#Define-a-profile)) each payload can contain keys specific to a payload type. These payload specific keys are described in detail, below.

For profiles that use paths, consider them to be case sensitive.

## Topics

### General

[`TopLevel`](/documentation/DeviceManagement/TopLevel)

The top-level payload properties for all profiles.

[`CommonPayloadKeys`](/documentation/DeviceManagement/CommonPayloadKeys)

The properties common to all payloads.

### Accounts

[`Accounts`](/documentation/DeviceManagement/Accounts)

The payload that configures guest accounts.

[`CalDAV`](/documentation/DeviceManagement/CalDAV)

The payload that configures a Calendar account.

[`CardDAV`](/documentation/DeviceManagement/CardDAV)

The payload that configures a Contacts account.

[`GoogleAccount`](/documentation/DeviceManagement/GoogleAccount)

The payload that configures a Google account.

[`LDAP`](/documentation/DeviceManagement/LDAP)

The payload that configures a Lightweight Directory Access Protocol (LDAP) account.

[`MobileAccounts`](/documentation/DeviceManagement/MobileAccounts)

The payload that configures mobile accounts on the device.

[`SubscribedCalendars`](/documentation/DeviceManagement/SubscribedCalendars)

The payload that configures subscribed calendars.

### AirPlay

[`AirPlay`](/documentation/DeviceManagement/AirPlay)

The payload that configures AirPlay settings.

[`AirPlaySecurity`](/documentation/DeviceManagement/AirPlaySecurity)

The payload that configures Apple TV for a particular style of AirPlay security.

### App management

[`AppLock`](/documentation/DeviceManagement/AppLock)

The payload that configures a device to run a single app.

[`AssociatedDomains`](/documentation/DeviceManagement/AssociatedDomains)

The payload that configures associated domains.

[`AutonomousSingleAppMode`](/documentation/DeviceManagement/AutonomousSingleAppMode)

The payload that configures Autonomous Single App mode.

[`NSExtensionManagement`](/documentation/DeviceManagement/NSExtensionManagement)

The payload that configures the extensions that the system allows or disallows to run on the device.

### App Store

[`AppStore`](/documentation/DeviceManagement/AppStore)

The payload that configures macOS App Store restrictions.

### Apple TV

[`ConferenceRoomDisplay`](/documentation/DeviceManagement/ConferenceRoomDisplay)

The payload that configures Conference Room Display mode for Apple TV.

[`TVRemote`](/documentation/DeviceManagement/TVRemote)

The payload that configures the Apple TV remote.

### Authentication

[`DirectoryService`](/documentation/DeviceManagement/DirectoryService)

The payload that configures an Active Directory (AD) domain.

[`ExtensibleSingleSignOn`](/documentation/DeviceManagement/ExtensibleSingleSignOn)

The payload that configures an app extension that performs single sign-on (SSO).

[`ExtensibleSingleSignOnKerberos`](/documentation/DeviceManagement/ExtensibleSingleSignOnKerberos)

The payload that configures an app extension that performs single sign-on with the Kerberos extension.

[`Identification`](/documentation/DeviceManagement/Identification)

The payload that configures the names of the account user.

[`IdentityPreference`](/documentation/DeviceManagement/IdentityPreference)

The payload that configures the user’s identity on the device.

[`SingleSignOn`](/documentation/DeviceManagement/SingleSignOn)

The payload that configures single sign-on (SSO).

### Certificates

[`ACMECertificate`](/documentation/DeviceManagement/ACMECertificate)

The payload that configures Automated Certificate Management Environment (ACME) settings.

[`ActiveDirectoryCertificate`](/documentation/DeviceManagement/ActiveDirectoryCertificate)

The payload that configures Active Directory Certificate settings.

[`CertificatePEM`](/documentation/DeviceManagement/CertificatePEM)

The payload that configures a PEM-formatted certificate.

[`CertificatePKCS1`](/documentation/DeviceManagement/CertificatePKCS1)

The payload that configures a PKCS #1-formatted certificate.

[`CertificatePKCS12`](/documentation/DeviceManagement/CertificatePKCS12)

The payload that configures a PKCS #12-formatted certificate.

[`CertificateRoot`](/documentation/DeviceManagement/CertificateRoot)

The payload that configures a root certificate.

[`CertificatePreference`](/documentation/DeviceManagement/CertificatePreference)

The payload that configures a certificate preference.

[`CertificateRevocation`](/documentation/DeviceManagement/CertificateRevocation)

The payload that configures certificate revocation checking.

[`CertificateTransparency`](/documentation/DeviceManagement/CertificateTransparency)

The payload that configures certificate transparency enforcement.

[`SCEP`](/documentation/DeviceManagement/SCEP)

The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.

### Ethernet

[`8021XGlobalEthernet`](/documentation/DeviceManagement/8021XGlobalEthernet)

The payload that configures the default fallback global Ethernet interface.

[`8021XFirstActiveEthernet`](/documentation/DeviceManagement/8021XFirstActiveEthernet)

The payload that configures the first wired, active Ethernet interface.

[`8021XFirstEthernet`](/documentation/DeviceManagement/8021XFirstEthernet)

The payload that configures the first wired Ethernet interface.

[`8021XSecondActiveEthernet`](/documentation/DeviceManagement/8021XSecondActiveEthernet)

The payload that configures the second wired, active Ethernet interface.

[`8021XSecondEthernet`](/documentation/DeviceManagement/8021XSecondEthernet)

The payload that configures the second wired Ethernet interface.

[`8021XThirdActiveEthernet`](/documentation/DeviceManagement/8021XThirdActiveEthernet)

The payload that configures the third wired, active Ethernet interface.

[`8021XThirdEthernet`](/documentation/DeviceManagement/8021XThirdEthernet)

The payload that configures the third wired Ethernet interface.

### FileVault

[`FDEFileVault`](/documentation/DeviceManagement/FDEFileVault)

The payload that configures FileVault.

[`FDEFileVaultOptions`](/documentation/DeviceManagement/FDEFileVaultOptions)

The payload that configures FileVault options.

[`FDERecoveryKeyEscrow`](/documentation/DeviceManagement/FDERecoveryKeyEscrow)

The payload that configures FileVault recovery key escrow.

### Login

[`LoginItemsManagedItems`](/documentation/DeviceManagement/LoginItemsManagedItems)

The payload that configures a device’s login items.

[`LoginWindowLoginItems`](/documentation/DeviceManagement/LoginWindowLoginItems)

The payload that configures login behavior.

[`LoginWindow`](/documentation/DeviceManagement/LoginWindow)

The payload that configures Login Window behavior.

[`LoginWindowScripts`](/documentation/DeviceManagement/LoginWindowScripts)

The payload that configures scripts to run at login and logout.

[`ServiceManagementManagedLoginItems`](/documentation/DeviceManagement/ServiceManagementManagedLoginItems)

This payload that configures managed login items, which auto-enables and auto-allows matched items.

### Mail

[`ExchangeActiveSync`](/documentation/DeviceManagement/ExchangeActiveSync)

The payload that configures Exchange ActiveSync accounts.

[`ExchangeWebServices`](/documentation/DeviceManagement/ExchangeWebServices)

The payload that configures an Exchange Web Services accounts.

[`Mail`](/documentation/DeviceManagement/Mail)

The payload that configures a Mail account.

### Managed devices

[`EducationConfiguration`](/documentation/DeviceManagement/EducationConfiguration)

The payload that configures the users, groups, and departments within an educational organization.

[`LightsOutManagementLOM`](/documentation/DeviceManagement/LightsOutManagementLOM)

The payload that configures lights-out management (LOM) settings.

[`ManagedPreferences`](/documentation/DeviceManagement/ManagedPreferences)

The payload that configures managed preferences.

[`MDM`](/documentation/DeviceManagement/MDM)

The payload that configures mobile device management (MDM) settings.

[`ProfileRemovalPassword`](/documentation/DeviceManagement/ProfileRemovalPassword)

The payload that configures profile removal.

### Media management

[`MediaManagementDiscBurning`](/documentation/DeviceManagement/MediaManagementDiscBurning)

The payload that configures disc-burning settings.

### Networking

[`Cellular`](/documentation/DeviceManagement/Cellular)

The payload that configures cellular settings.

[`CellularPrivateNetwork`](/documentation/DeviceManagement/CellularPrivateNetwork)

The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.

[`ContentCachingService`](/documentation/DeviceManagement/ContentCachingService)

The payload that configures the Content Caching service.

[`DNSSettings`](/documentation/DeviceManagement/DNSSettings)

The payload that configures encrypted DNS settings.

[`Domains`](/documentation/DeviceManagement/Domains)

The payload that configures the domains under an organization’s management.

[`Firewall`](/documentation/DeviceManagement/Firewall)

The payload that configures the firewall.

[`NetworkUsageRules`](/documentation/DeviceManagement/NetworkUsageRules)

The payload that configures network-usage rules.

[`Relay`](/documentation/DeviceManagement/Relay)

The payload that configures relay settings.

[`WiFi`](/documentation/DeviceManagement/WiFi)

The payload that configures Wi-Fi settings.

[`WiFiManagedSettings`](/documentation/DeviceManagement/WiFiManagedSettings)

The payload that configures managed Wi-Fi settings.

### Parental controls

[`ParentalControlsApplicationRestrictions`](/documentation/DeviceManagement/ParentalControlsApplicationRestrictions)

The payload that configures parental controls for apps.

[`ParentalControlsContentFilter`](/documentation/DeviceManagement/ParentalControlsContentFilter)

The payload that configures the parental control web content filters.

[`ParentalControlsDictionary`](/documentation/DeviceManagement/ParentalControlsDictionary)

The payload that configures parental control dictionary restrictions.

[`ParentalControlsGameCenter`](/documentation/DeviceManagement/ParentalControlsGameCenter)

The payload that configures Game Center parental controls.

[`ParentalControlsTimeLimits`](/documentation/DeviceManagement/ParentalControlsTimeLimits)

The payload that configures parental control time limits.

### Preferences

[`GlobalPreferences`](/documentation/DeviceManagement/GlobalPreferences)

The payload to configure global preferences.

[`UserPreferences`](/documentation/DeviceManagement/UserPreferences)

The payload that configures iCloud password preferences.

### Printing

[`AirPrint`](/documentation/DeviceManagement/AirPrint)

The payload that configures AirPrint printer discoverability in the user’s printer list.

[`Printing`](/documentation/DeviceManagement/Printing)

The payload that configures printers.

### Privacy

[`PrivacyPreferencesPolicyControl`](/documentation/DeviceManagement/PrivacyPreferencesPolicyControl)

The payload that configures privacy preferences.

### Proxies

[`DNSProxy`](/documentation/DeviceManagement/DNSProxy)

The payload that configures DNS proxies.

[`GlobalHTTPProxy`](/documentation/DeviceManagement/GlobalHTTPProxy)

The payload that configures a global HTTP proxy.

[`NetworkProxyConfiguration`](/documentation/DeviceManagement/NetworkProxyConfiguration)

The payload that configures network proxies for a device.

### Restrictions

[`Restrictions`](/documentation/DeviceManagement/Restrictions)

The payload that configures restrictions on a device.

### Security

[`Passcode`](/documentation/DeviceManagement/Passcode)

The payload that configures a passcode policy.

[`SecurityPreferences`](/documentation/DeviceManagement/SecurityPreferences)

The payload that configures security preferences.

[`SmartCard`](/documentation/DeviceManagement/SmartCard)

The payload that configures a smart card.

### System configuration

[`Declarations`](/documentation/DeviceManagement/Declarations)

The payload that applies a set of declarations to the device through the Settings app.

[`EnergySaver`](/documentation/DeviceManagement/EnergySaver)

The payload that configures Energy Saver settings.

[`FileProvider`](/documentation/DeviceManagement/FileProvider)

The payload that configures file provider settings.

[`Font`](/documentation/DeviceManagement/Font)

The payload that configures fonts.

[`LockScreenMessage`](/documentation/DeviceManagement/LockScreenMessage)

The payload that configures a Lock Screen message.

[`Screensaver`](/documentation/DeviceManagement/Screensaver)

The payload that configures the screen saver.

[`SystemExtensions`](/documentation/DeviceManagement/SystemExtensions)

The payload that configures system extensions.

[`SystemLogging`](/documentation/DeviceManagement/SystemLogging)

The payload that configures system logging.

[`TimeServer`](/documentation/DeviceManagement/TimeServer)

The payload that configures the time server.

### System policy

[`SystemPolicyControl`](/documentation/DeviceManagement/SystemPolicyControl)

The payload that configures the system policy for assessments.

[`SystemPolicyKernelExtensions`](/documentation/DeviceManagement/SystemPolicyKernelExtensions)

The payload that configures the kernel extension policies.

[`SystemPolicyManaged`](/documentation/DeviceManagement/SystemPolicyManaged)

The payload that configures the Finder’s contextual menu to bypass the system policy.

[`SystemPolicyRule`](/documentation/DeviceManagement/SystemPolicyRule)

The payload that configures the system policy.

### System migration

[`SystemMigration`](/documentation/DeviceManagement/SystemMigration)

The payload that configures system migration.

### User experience

[`Accessibility`](/documentation/DeviceManagement/Accessibility)

The payload that configures the accessibility features of the device.

[`Desktop`](/documentation/DeviceManagement/Desktop)

The payload that configures the desktop wallpaper.

[`Dock`](/documentation/DeviceManagement/Dock)

The payload that configures the Dock.

[`Finder`](/documentation/DeviceManagement/Finder)

The payload that configures Finder settings.

[`HomeScreenLayout`](/documentation/DeviceManagement/HomeScreenLayout)

The payload that configures the Home Screen layout.

[`ManagedMenuExtras`](/documentation/DeviceManagement/ManagedMenuExtras)

The payload that configures menu extras.

[`Notifications`](/documentation/DeviceManagement/Notifications)

The payload that configures notifications.

[`ScreensaverUser`](/documentation/DeviceManagement/ScreensaverUser)

The payload that configures a user’s screen saver settings.

[`SetupAssistant`](/documentation/DeviceManagement/SetupAssistant)

The payload that configures Setup Assistant settings.

[`TimeMachine`](/documentation/DeviceManagement/TimeMachine)

The payload that configures Time Machine.

### VPN

[`AppLayerVPN`](/documentation/DeviceManagement/AppLayerVPN)

The payload that configures a per-app VPN.

[`AppToAppLayerVPNMapping`](/documentation/DeviceManagement/AppToAppLayerVPNMapping)

The payload that configures per-app VPN settings.

[`VPN`](/documentation/DeviceManagement/VPN)

The payload that configures a VPN.

### Web

[`WebClip`](/documentation/DeviceManagement/WebClip)

The profile that configures web clips on the device.

[`WebContentFilter`](/documentation/DeviceManagement/WebContentFilter)

The payload that configures web content filters.

### Xsan

[`Xsan`](/documentation/DeviceManagement/Xsan)

The payload that configures an Xsan client system.

[`XsanPreferences`](/documentation/DeviceManagement/XsanPreferences)

The payload that configures the Xsan preferences that define the volumes that automatically mount at startup.

### Deprecated

[`APN`](/documentation/DeviceManagement/APN)

The payload that configures access point names.

[`FDERecoveryKeyRedirection`](/documentation/DeviceManagement/FDERecoveryKeyRedirection)

The payload that configures FileVault recovery key redirection.

[`MediaManagementAllowedMedia`](/documentation/DeviceManagement/MediaManagementAllowedMedia)

The payload that configures media management.

[`ParentalControlDictationAndProfanity`](/documentation/DeviceManagement/ParentalControlDictationAndProfanity)

The payload that configures parental control for dictation and profanity.

[`ShareKit`](/documentation/DeviceManagement/ShareKit)

The payload that configures ShareKit.

[`SystemPreferences`](/documentation/DeviceManagement/SystemPreferences)

The payload that configures the preference panes.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
