# Local Authentication Embedded UI

Present a standard local authentication view icon in a custom authentication view.

## Overview

When you authenticate users with the `Local Authentication` framework, the framework
handles all user interaction by default. If you want to create a custom authentication
user interface, build it around an [`LAAuthenticationView`](/documentation/LocalAuthenticationEmbeddedUI/LAAuthenticationView)
instance. The authentication view displays an icon that users associate with biometric
authentication, like the Touch ID icon, and then modifies that icon over time to
reflect changes in the authentication state. You can add other text, images, or interactive
elements to your custom view as needed.

![A screenshot of a view with the title Access My Transactions above a circular finger print icon, which is in turn above a secure text entry field. The finger print icon is highlighted.](images/com.apple.Local-Authentication-Embedded-UI/localauthenticationembeddedui-1@2x.png)

For all local authentication operations, the system manages the underlying biometric
data, but with a local authentication view, you can customize the authentication
interface to match the design of your app. At the same time, familiar iconography
helps users understand what you are asking from them.

## Topics

### The Local Authentication View

[`LAAuthenticationView`](/documentation/LocalAuthenticationEmbeddedUI/LAAuthenticationView)

A graphical representation of the state of biometric authentication.

### Reference

[Local Authentication Embedded UI Data Types](/documentation/LocalAuthenticationEmbeddedUI/local-authentication-embedded-ui-data-types)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
