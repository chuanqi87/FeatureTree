* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/multipeerconnectivity#app-main)

Framework

# Multipeer Connectivity

Support peer-to-peer connectivity and the discovery of nearby devices.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.0+macOS 10.10+tvOS 10.0+visionOS 1.0+

## [Overview](https://developer.apple.com/documentation/multipeerconnectivity\#overview)

The Multipeer Connectivity framework supports the discovery of services provided by nearby devices and supports communicating with those services through message-based data, streaming data, and resources (such as files). In iOS, the framework uses infrastructure Wi-Fi networks, peer-to-peer Wi-Fi, and Bluetooth personal area networks for the underlying transport. In macOS and tvOS, it uses infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Ethernet.

### [Architecture](https://developer.apple.com/documentation/multipeerconnectivity\#Architecture)

When working with the Multipeer Connectivity framework, your app must interact with several types of objects:

- Session objects ( [`MCSession`](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)) support communication between connected peer devices. Your app creates a session and adds peers to it when peers accept an invitation to connect, and it creates a session when invited to connect by another peer. Session objects maintain a set of peer ID objects that represent the peers connected to the session.

- Advertiser objects ( [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)) tell nearby peers that your app is willing to join sessions of a specified type. An advertiser object uses a single local peer object to provide information that identifies the device and its user to other nearby devices.

- Advertiser assistant objects ( [`MCAdvertiserAssistant`](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)) provide the same functionality as advertiser objects, but also provide a standard user interface that allows the user to accept invitations. If you wish to provide your own user interface, or if you wish to exercise additional programmatic control over which invitations are displayed, use an advertiser object directly.

- Browser objects ( [`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)) let your app search programmatically for nearby devices with apps that support sessions of a particular type.

- Browser view controller objects ( [`MCBrowserViewController`](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)) provide a standard user interface that allows the user to choose nearby peers to add to a session.

- Peer IDs ( [`MCPeerID`](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)) uniquely identify an app running on a device to nearby peers.


### [Discovery Phase and Session Phase](https://developer.apple.com/documentation/multipeerconnectivity\#Discovery-Phase-and-Session-Phase)

This framework is used in two phases: the discovery phase and the session phase.

In the discovery phase, your app uses an [`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser) object to browse for nearby peers, optionally using the [`MCBrowserViewController`](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller) object to display a user interface.

The app also uses an [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser) object or an [`MCAdvertiserAssistant`](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant) object to tell nearby peers that it is available, so that apps on other nearby devices can invite it to a session.

During the discovery phase, your app has limited communication with and knowledge of other peers; it has access to the `discoveryInfo` data that other nearby clients provide, and any context data that other peers provide when inviting it to join a session.

After the user chooses which peers to add to a session, the app invites those peers to join the session. Apps running on the nearby devices can choose whether to accept or reject the invitation, and can ask their users for permission.

If the peer accepts the invitation, the browser establishes a connection with the advertiser and the session phase begins. In this phase, your app can perform direct communication to one or more peers within the session. The framework notifies your app through delegate callbacks when peers join the session and when they leave the session.

If the app moves into the background, the framework stops advertising and browsing and disconnects any open sessions. Upon returning to the foreground, the framework automatically resumes advertising and browsing, but the developer must reestablish any closed sessions.

## [Topics](https://developer.apple.com/documentation/multipeerconnectivity\#topics)

### [Classes](https://developer.apple.com/documentation/multipeerconnectivity\#Classes)

[`class MCAdvertiserAssistant`](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)

The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.

[`class MCBrowserViewController`](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)

The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ( [`prepare(for:sender:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/prepare(for:sender:)) and [`performSegue(withIdentifier:sender:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/performsegue(withidentifier:sender:)) for storyboards or [`present(_:animated:completion:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/present(_:animated:completion:)) and [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/dismiss(animated:completion:)) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) and [`dismiss(_:)`](https://developer.apple.com/documentation/appkit/nsviewcontroller/dismiss(_:)-91my5) instead.

[`class MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)

The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.

[`class MCNearbyServiceBrowser`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)

Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).

[`class MCPeerID`](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)

An `MCPeerID` object represents a peer in a multipeer session.

[`class MCSession`](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)

An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.

### [Protocols](https://developer.apple.com/documentation/multipeerconnectivity\#Protocols)

[`protocol MCAdvertiserAssistantDelegate`](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate)

The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.

[`protocol MCBrowserViewControllerDelegate`](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate)

The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.

[`protocol MCNearbyServiceAdvertiserDelegate`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate)

The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.

[`protocol MCNearbyServiceBrowserDelegate`](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)

The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.

[`protocol MCSessionDelegate`](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate)

The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](https://developer.apple.com/documentation/multipeerconnectivity/mcsession).

### [Structures](https://developer.apple.com/documentation/multipeerconnectivity\#Structures)

[`struct MCError`](https://developer.apple.com/documentation/multipeerconnectivity/mcerror)

### [Reference](https://developer.apple.com/documentation/multipeerconnectivity\#Reference)

[API Reference\\
MultipeerConnectivity Enumerations](https://developer.apple.com/documentation/multipeerconnectivity/multipeerconnectivity_enumerations)

[API Reference\\
MultipeerConnectivity Constants](https://developer.apple.com/documentation/multipeerconnectivity/multipeerconnectivity_constants)

Current page is Multipeer Connectivity