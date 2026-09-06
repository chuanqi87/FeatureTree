# Accessing and using secure element credentials

Manage and use payment cards and other credentials.

## Discussion

You can use the [`SecureElementCredential`](/documentation/SecureElementCredential) framework to store, manage, and use *credentials*, for example, contactless payment cards, transit passes, and corporate badges, that the system stores in the device’s Secure Element. The person using your app can then authenticate with features like Face ID and Touch ID to use their credentials.

`SecureElementCredential` provides UIKit and SwiftUI APIs to handle user authentication, and to temporarily give your app exclusive use of the device when presenting the credential. You can also receive notifications of credential-handling events. These include events like proximity to an NFC card reader, or the person performing a credential gesture like double tapping the side button of an iPhone.

You or your organization manage credentials and the embedded applet code you create for those credentials through the [Apple Business Register](https://register.apple.com/login) (ABR). This framework allows your iOS app access to use those credentials.

### Create a credential session

The [`CredentialSession`](/documentation/SecureElementCredential/CredentialSession) class is the central access point for working with credentials. To use it, first verify that the device is eligible to use credential sessions, by checking the value of [`isEligible`](/documentation/SecureElementCredential/CredentialSession/isEligible). If eligible, create a session with [`startSession()`](/documentation/SecureElementCredential/CredentialSession/startSession()). Then, fetch the available credentials with [`listCredentials()`](/documentation/SecureElementCredential/CredentialSession/listCredentials()). If the credential you expect to use isn’t in the array returned by `listCredentials()`, call [`provisionCredential(configurationUUID:name:)`](/documentation/SecureElementCredential/CredentialSession/provisionCredential(configurationUUID:name:)) to install the applet bundle that you submitted to ABR into the Secure Element, then list the credentials again.

The following example shows how to create a credential session in the context of a SwiftUI view that lists the available credentials. After the view instantiates and before it appears:

- The `.task` view modifier spawns a <doc://com.apple.documentation/documentation/Swift/Task> that calls a private `kickOff()` helper method.
- `kickOff()` makes the asynchronous calls to create the session and fetch an array of credentials from the Secure Element. This array can then populate a <doc://com.apple.documentation/documentation/SwiftUI/List>.

```swift
struct MyCredentialsView: View {
    @State private var activeSession: CredentialSession
    @State private var credentials: [Credential]
    
    var body: some View {
        // Display a list of credentials.
        List(credentials, id: \.identifier) { credential in
            MyCredentialListItem(credential: credential)
        }
        .task {
            do {
                try await kickOff()
            } catch {
                // Handle error from kickOff().
            }
        }
    }
    
    private func kickOff() async throws {
        guard CredentialSession.isEligible else {
            throw CredentialSession.ErrorCode.ineligible
        }
        self.activeSession = try await CredentialSession.startSession()
        self.credentials = try await activeSession.listCredentials()
    }
}
```

When you first start the credential session, it’s in the default state, [`CredentialSession.State.management`](/documentation/SecureElementCredential/CredentialSession/State-swift.enum/management). In this state, you can perform the following actions:

- List credentials (as shown in the above example) with [`listCredentials()`](/documentation/SecureElementCredential/CredentialSession/listCredentials()).
- Provision new credentials with [`provisionCredential(configurationUUID:name:)`](/documentation/SecureElementCredential/CredentialSession/provisionCredential(configurationUUID:name:)).
- Delete a credential with [`deleteCredential(_:)`](/documentation/SecureElementCredential/CredentialSession/deleteCredential(_:))

Beyond the management state, there are two other credential session states:

- Wired state, for communicating directly with a credential stored in the Secure Element.
- Card emulation state, for using the credential with an NFC card reader.

### Obtain exclusive use of the user interface

Prior to presenting a credential for use with an NFC reader or performing transactions, your app can get exclusive use of the credential user interface. This exclusivity prevents interruptions from another app chosen as the default for contactless transactions, any other apps using the `SecureElementCredential` framework, and Wallet.

To gain exclusive use of the credential UI, obtain an instance of the [`CredentialSession.PresentmentIntentAssertion`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion) class. Hold on to this object until you finish using the credential. The following example shows an overview of this process:

```swift
private var activeSession: CredentialSession = CredentialSession()
private var assertion: CredentialSession.PresentmentIntentAssertion?

func useAssertion() async throws {
    do {
        assertion = try await activeSession.acquirePresentmentAssertion()
        // Perform UI tasks with a credential.
    } catch {
        // Retry tasks if necessary.
    }
    
    try await assertion?.relinquish() // After completing UI tasks.
}
```

The assertion expires when the object deinitializes, you call [`relinquish()`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion/relinquish()), or after a 15-second timeout, whichever occurs first.

> Note: You can acquire a maximum of two instances of ``doc://SecureElementCredential/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion`` in one 80-second period.

### Enter wired mode

After obtaining a [`CredentialSession.Credential`](/documentation/SecureElementCredential/CredentialSession/Credential), many tasks require changing the [`state`](/documentation/SecureElementCredential/CredentialSession/state-swift.property) before you perform them. For example, you might need to maintain a credential by directly interacting with it in the Secure Element, which you can only do in the [`CredentialSession.State.wired(credential:)`](/documentation/SecureElementCredential/CredentialSession/State-swift.enum/wired(credential:)) state. Credential maintenance tasks include exchanging keys and certificates with an installed credential.

> Tip: Be aware that you can only perform these kinds of maintenance tasks if your app has owner-level access to the credential.

You can perform credential maintenance by transitioning the session state to [`CredentialSession.State.wired(credential:)`](/documentation/SecureElementCredential/CredentialSession/State-swift.enum/wired(credential:)). Next, you send Application Protocol Data Unit (APDU) commands, as defined by [ISO 7816-4](https://www.iso.org/obp/ui/#iso:std:iso-iec:7816:-4:ed-4:v1:en), to the credential with the session’s [`transceive(_:)`](/documentation/SecureElementCredential/CredentialSession/transceive(_:)) method. See the integration guide in the [Apple Business Register](https://register.apple.com) for more information about the payloads for these calls.

Here’s how you enter wired mode and perform maintenance on a credential:

```swift
// For simplicity, this example just uses the first credential discovered.
guard let selectedCredential = credentialList.first else {
    return
}
try await activeSession.enterWiredMode(using: selectedCredential)
let credentialResponse = try await activeSession.transceive(transceiveData)

// Perform additional transceive(_:) calls here if your task
// requires multiple round trips.

try await activeSession.endWiredMode() // Transition back to management mode when done.
```

### Use wired mode in a UIKit app

You can also go into wired mode to get user authorization for using the credential, which authenticates with a passcode or biometric features like Face ID. This approach is useful for tasks like using the credential to perform web payments.

The following example shows how a UIKit-based app can get authorization and perform a transaction in wired mode. After getting the [`CredentialSession.PresentmentIntentAssertion`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion) as described above, it verifies that the selected credential is installed, and gets the first installed instance’s unique identifier. Using this unique identifier, it calls [`performWiredTransaction(using:over:instanceAID:)`](/documentation/SecureElementCredential/CredentialSession/performWiredTransaction(using:over:instanceAID:)) to present an authentication interface over the current <doc://com.apple.documentation/documentation/UIKit/UIScene>. This call puts the session into wired mode, at which point the app can interact with the credential by calling [`transceive(_:)`](/documentation/SecureElementCredential/CredentialSession/transceive(_:)).

For a web payment, an app might receive a token from a web service, and then ingest it by sending the token as the APDU payload of a `transceive(_:)` call. The credential then provides an APDU as the return value. It might take several exchanges to complete the transaction, after which the app exits wired mode by calling [`endWiredMode()`](/documentation/SecureElementCredential/CredentialSession/endWiredMode()) and relinquishes the [`CredentialSession.PresentmentIntentAssertion`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion).

```swift
@IBAction func performWebTransaction() {
    Task {
        do {
            let assertion = try await self.activeSession.acquirePresentmentAssertion()
            guard case let .installed(instances) = selectedCredential.state,
                let instanceAID = instances.first?.instanceAID,
                let scene = self.view.window?.windowScene else {
              return // Handle error.
            }
            try await assertion.relinquish()
             
            try await activeSession.performWiredTransaction(using: selectedCredential,
                                                            over: scene,
                                                            instanceAID: instanceAID)

            // Perform proprietary tasks here by calling activeSession.transcieve(_:)
            // to exchange APDUs with the credential.

            // If you have cleanup tasks after transceiving, reacquire the
            // PresentmentIntentAssertion, perform those tasks, and relinquish
            // the assertion.

            try await activeSession.endWiredMode() 
        } catch {
            // Handle error.
        }
    }
}
```

The example above calls [`relinquish()`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion/relinquish()) before making the `performWiredTransaction(using:over:scene:)` call. This is because all methods that perform transactions acquire an internal instance of the presentment intent assertion on your behalf and automatically relinquish it. If you need to perform clean-up work after a transaction, acquire another assertion, subject to the limit of two assertions in an 80-second span.

### Use wired mode in a SwiftUI app

The flow is different when you use a SwiftUI <doc://com.apple.documentation/documentation/SwiftUI/View> instead of a UIKit <doc://com.apple.documentation/documentation/UIKit/UIViewController>, but the result is the same. The following example shows a SwiftUI view that presents the UI for performing a wired transaction. This example assumes you already acquired the [`CredentialSession.PresentmentIntentAssertion`](/documentation/SecureElementCredential/CredentialSession/PresentmentIntentAssertion), and passed a [`CredentialSession`](/documentation/SecureElementCredential/CredentialSession) and a [`CredentialSession.Credential`](/documentation/SecureElementCredential/CredentialSession/Credential) to the view.

Before the view appears, the closure associated with the `View.task(priority:_:)` view modifier executes. This code fetches the current [`CredentialTransaction.Configuration`](/documentation/SecureElementCredential/CredentialTransaction/Configuration) and stores it in a state property. Next, the `View.transactionTask(_:action:)` closure runs. This closure gets the current credential, and from that, gets the unique identifier of the credential’s first instance. With instance ID, it can enter wired mode by calling [`performTransactionInWiredMode(using:instanceAID:)`](/documentation/SecureElementCredential/CredentialTransaction/performTransactionInWiredMode(using:instanceAID:)) on the [`CredentialTransaction`](/documentation/SecureElementCredential/CredentialTransaction) that the closure receives.

At this point, the SwiftUI sample is in the same state as the earlier UIKit example — you can make [`transceive(_:)`](/documentation/SecureElementCredential/CredentialSession/transceive(_:)) calls to exchange APDUs with the installed credential to process the web transaction. When done, invalidate the configuration to exit wired mode and return to management mode.

```swift
struct TransactView: View {
    @State var session: CredentialSession
    @State private var assertion: CredentialSession.PresentmentIntentAssertion? // Acquire this prior to showing view.
    @State var credential: CredentialSession.Credential
    @State var activeConfiguration: CredentialTransaction.Configuration?
    
    var body: some View {
        VStack {
            // Subviews to represent the credential, such as
            // an image of a card.
        }
        .task {
            do {
                self.activeConfiguration = try await session.configuration()
            } catch {
                // Present alert for error.
            }
        }
        .transactionTask(activeConfiguration) { transaction in 
            do {
                guard let credential = try await session.listCredentials().first(where: { $0.identifier == credential.identifier }) else {
                    // Present alert for error.
                    return
                }
                
                guard case let .installed(instances: instances) = credential.state,
                let firstInstance = instances.first else {
                    return // Handle error.
                }
                
                assertion?.relinquish()
                try await transaction.performTransactionInWiredMode(using: credential,
                                                                    instanceAID: firstInstance.instanceAID)

                // Perform proprietary tasks here by reacquiring
                // PresentmentIntentAssertion, then calling
                // activeSession.transcieve(_:) to exchange APDUs with the credential.
                // Relinquish the assertion when done.

                activeConfiguration?.invalidate() // Invalidate the session when you're done.
            } catch {
                // Present alert for error.
            }
        }
    }
}
```

### Perform card emulation

You can also use credentials for contactless transactions with NFC card readers. Implement the [`CredentialSessionWindowSceneDelegate`](/documentation/SecureElementCredential/CredentialSessionWindowSceneDelegate) protocol in your app to receive [`CredentialSessionWindowSceneEvent`](/documentation/SecureElementCredential/CredentialSessionWindowSceneEvent) instances that describe NFC-related events. These events can occur when the device comes within range of an NFC card reader. Your app also gets an event when the person using the app performs a gesture to present an NFC display, like double-pressing the Home button or Side button.

To perform a contactless transaction, select an installed credential and then put the session into card emulation mode. In UIKit, you do this by calling [`performTransaction(using:over:options:)`](/documentation/SecureElementCredential/CredentialSession/performTransaction(using:over:options:)). In the following example, the `performNFCTransaction()` method gets exclusive use of the contactless UI with  [`acquirePresentmentAssertion()`](/documentation/SecureElementCredential/CredentialSession/acquirePresentmentAssertion()). Next, it verifies that the selected credential is installed and unwraps the current <doc://com.apple.documentation/documentation/UIKit/UIScene>  into a local variable. With these parameters, it calls `performTransaction(using:over:)` to begin the contactless transaction with the NFC reader.

The `performTransaction(using:over:)` method implicitly changes the session state to [`CredentialSession.State.cardEmulation(credential:)`](/documentation/SecureElementCredential/CredentialSession/State-swift.enum/cardEmulation(credential:)). When the transaction completes, the example returns to management mode by calling [`endCardEmulation()`](/documentation/SecureElementCredential/CredentialSession/endCardEmulation()), and relinquishes the contactless UI.

```swift
@IBAction func performNFCTransaction() {
    Task {
        do {
            let assertion = try await activeSession.acquirePresentmentAssertion()
            guard case let .installed(instances) = selectedCredential.state,
            let scene = self.view.window?.windowScene else {
                return // Handle error.
            }
            try await assertion.relinquish()

            try await activeSession.performTransaction(using: selectedCredential,
                                                       over: scene)

            // Perform other tasks, if necessary.

            // If you have cleanup tasks after transceiving, reacquire the
            // PresentmentIntentAssertion, perform those tasks, and relinquish
            // the assertion.

            try await activeSession.endCardEmulation()
        } catch {
            // Handle error.
        }
    }
}
```

The SwiftUI equivalent uses the `transactionTask(_:action:)` view modifier to receive a [`CredentialTransaction`](/documentation/SecureElementCredential/CredentialTransaction) from the view. Using this parameter, it calls [`performTransaction(using:options:)`](/documentation/SecureElementCredential/CredentialTransaction/performTransaction(using:options:)) to enter card emulation mode.

```swift
struct CredentialView: View {
    @State private var configuration: CredentialTransaction.Configuration?
    @State private var assertion: CredentialSession.PresentmentIntentAssertion? // aAquire prior to showing view.
    private var activeSession: CredentialSession
    private var selectedCredential: CredentialSession.Credential

    var body: some View {
        VStack {
            // Subviews to represent the credential, such as
            // an image of a card.
            }
            .task {
                self.configuration = await activeSession.configuration()
            }
            .transactionTask(configuration) { transaction in
                do {
                    guard case .installed(_) = selectedCredential.state else {
                        // Handle error.
                        return
                    }
                    assertion?.relinquish()
                    try await transaction.performTransaction(using: selectedCredential)
                } catch {
                    // Handle error.
                }
                await configuration?.invalidate() // Transition back to management state.
            }
        }
    }
}
```

### Performing wired actions and card emulation

The previous example assumes the credential is already installed and ready to use. It’s also possible to perform maintenance on a credential immediately before using it with an NFC reader. The following example shows how to do this. The `presentCredential()` method checks an internal `firstUse` flag to determine if it needs to perform up-front maintenance work. If so, it calls a private `personalizeCredentialInformation()` method to enter wired mode and perform the maintenance with one or more calls to [`transceive(_:)`](/documentation/SecureElementCredential/CredentialSession/transceive(_:)).

After this method returns, the session has a current credential — the one it entered wired mode with — so it can enter card emulation mode with a call to [`performCardEmulationTransactionWithCurrentCredential(over:options:)`](/documentation/SecureElementCredential/CredentialSession/performCardEmulationTransactionWithCurrentCredential(over:options:)). On the other hand, if `presentCredential()` didn’t need to perform card maintenance, it calls [`performTransaction(using:over:options:)`](/documentation/SecureElementCredential/CredentialSession/performTransaction(using:over:options:)) as before. In either case, the contactless transaction with the NFC reader proceeds, and the example calls [`endCardEmulation()`](/documentation/SecureElementCredential/CredentialSession/endCardEmulation()) when done.

```swift
class TransactionViewController: UIViewController {
    private var activeSession: CredentialSession
    private var selectedCredential: CredentialSession.Credential
    private var assertion: CredentialSession.PresentmentIntentAssertion
    private var firstUse: Bool

    // The card maintenance method.
    private func personalizeCredentialInformation() async throws {
        try await activeSession.enterWiredMode(using: selectedCredential)
        let credentialResponse = try await activeSession.transceive( generatePersonalizationAPDU() )
        // Perform additional transceive(_:) calls here if your task
        // requires multiple round trips.
    }

    func presentCredential() async throws {
        guard case let .installed(instances) = selectedCredential.state,
        let scene = self.view.window?.windowScene else {
            return // Handle error.
        }
        
        if firstUse {
            try await personalizeCredentialInformation()
            try await activeSession.performCardEmulationTransactionWithCurrentCredential(over: scene)

        } else {
            try await activeSession.performTransaction(using: selectedCredential, over: scene)
        }

        // Perform other tasks, if necessary.

        try await activeSession.endCardEmulation()
    }
}
```

In SwiftUI, the main difference is that the `transactionTask(_:action:)` view modifier provides a [`CredentialTransaction`](/documentation/SecureElementCredential/CredentialTransaction) parameter when it executes your closure, so you call transaction-performing methods on this object.

In the following example, the code checks the `isFirstUse` flag in the closure passed to the `.transactionTask(_:action:)` view modifier and then performs any needed maintenance on the credential in wired mode. From there, the first-use case calls [`performCardEmulationTransactionWithCurrentCredential(options:)`](/documentation/SecureElementCredential/CredentialTransaction/performCardEmulationTransactionWithCurrentCredential(options:)) to enter card emulation mode with this credential.
If the credential doesn’t require maintenance, which means the session is in management mode, the code calls [`performTransaction(using:options:)`](/documentation/SecureElementCredential/CredentialTransaction/performTransaction(using:options:)), passing in the credential to use for the NFC transaction.

```swift
struct TransactionView: View {
    @State private var configuration: CredentialTransaction.Configuration?
    @State private var assertion: CredentialSession.PresentmentIntentAssertion? // acquire prior to showing view
    private var activeSession: CredentialSession
    private var selectedCredential: CredentialSession.Credential
    private var isFirstUse: Bool

    var body: some View {
        VStack {
            // Subviews to represent the credential, such as
            // an image of a card.
            }
            .task {
                self.configuration = await activeSession.configuration()
            }
            .transactionTask(configuration) { transaction in
                do {
                    guard case .installed(_) = selectedCredential.state else  {
                        // Handle error.
                        return
                    }
                    if isFirstUse {
                        do {
                            guard case let .installed(instances: instances) = selectedCredential.state,
                            let firstInstance = instances.first else {
                                // Handle error.
                                return
                            }
                            try await session.enterWiredMode()
                            // Perform proprietary tasks here by calling activeSession.transcieve(_:)
                            // to exchange APDUs with the credential.
                        } catch {
                            // Handle error.
                        }
                        assertion?.relinquish()
                        try await transaction.performCardEmulationTransactionWithCurrentCredential()
                    } else {
                        assertion?.relinquish()
                        try await transaction.performTransaction(using: selectedCredential)
                    }

                    // Perform other tasks, if necessary. Reacquire a 
                    // PresentmentIntentAssertion prior to any "perform" calls,
                    // and relinquish() the assertion when done.

                } catch {
                    // Handle error.
                }
                await configuration?.invalidate() // Transition the session back to management state.
            }
        }
    }
```

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
