# Protecting user data with App Sandbox

Guard user data and operating system resources from malicious attacks by limiting your app’s access to files, network connections, and hardware capabilities.

## Discussion

Even if you adopted secure coding practices while developing your app, it may still have vulnerabilities that threaten your users’ security and privacy. App Sandbox — a requirement for distributing your app on the App Store — limits the scope for an attacker to abuse platform features via your app.

When you create a new macOS app in Xcode, it receives the App Sandbox entitlement and a default set of capabilities. If you have an existing app, you can adopt App Sandbox to provide people with additional security.

> Note:
> For information on enabling the App Sandbox capability in Xcode, see <doc://com.apple.documentation/documentation/Xcode/configuring-the-macos-app-sandbox>.

### Review functionality that is incompatible with App Sandbox

Certain activities are forbidden by the operating system when an app runs in a sandbox. Identify whether your app performs these, and remove them or find alternative ways to provide the same functionality. The restricted activities are:

- Use of [Authorization Services](/documentation/Security/authorization-services) API.
- Use of accessibility APIs in assistive apps.
- Sending Apple Events to arbitrary apps.
- Sending <doc://com.apple.documentation/documentation/Foundation/NSNotification/userInfo> dictionaries in distributed notifications to other tasks.
- Loading kernel extensions.
- Simulating user input in Open and Save dialogs.
- Accessing or modifying preferences in other apps.
- Configuring network settings.
- Terminating other running apps.

### Place data files and scripts in standard locations

The operating system creates a container directory when launching your sandboxed app, to which the app has unrestricted read and write access. The sandboxed app doesn’t have unrestricted access to the user’s home folder. Use the <doc://com.apple.documentation/documentation/Foundation/FileManager> method <doc://com.apple.documentation/documentation/Foundation/FileManager/url(for:in:appropriateFor:create:)> to find common directories for user documents, scripts, and supporting files, as it returns a location within the app’s container for a sandboxed app.

If you are enabling App Sandbox for an existing app that already has documents, user scripts, or supporting files in the user’s home folder, refer to [Migrating your app’s files to its App Sandbox container](/documentation/Security/migrating-your-app-s-files-to-its-app-sandbox-container).

### Configure the App Sandbox for an embedded tool

If your macOS app embeds a command-line tool, that tool must inherit the containing app’s sandbox configuration. For more information, see <doc://com.apple.documentation/documentation/Xcode/embedding-a-helper-tool-in-a-sandboxed-app>.

### Verify that your app uses App Sandbox

You can verify if your app uses App Sandbox by looking for the process in Activity Monitor or with the `codesign` command in Terminal.

To verify your app in Activity Monitor:

1. Open Activity Monitor.
2. Choose View > Columns, and choose Sandbox among the list of possible columns to monitor.
3. Launch your app.
4. Find your app in Activity Monitor’s process list, and verify that the value in the Sandbox column is Yes as shown in the figure below.

![A screenshot of Activity Monitor. The row describing an app is highlighted, calling out the value in the Sandbox column.](images/com.apple.security/media-4098973@2x.png)

To verify your app’s App Sandbox configuration in Terminal, use the `codesign` command:

```zsh
% codesign -dvvv --entitlements - <path to your app>
```

If your app has the App Sandbox entitlement, you will see the following in the output:

```console
    [Key] com.apple.security.app-sandbox
    [Value]
        [Bool] true
```

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
