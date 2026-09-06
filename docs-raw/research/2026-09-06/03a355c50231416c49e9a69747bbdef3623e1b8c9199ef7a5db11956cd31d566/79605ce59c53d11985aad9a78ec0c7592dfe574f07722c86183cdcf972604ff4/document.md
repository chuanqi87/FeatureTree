# Discovering peers with Multipeer Connectivity

Exchange discovery tokens over the local network.

## Discussion

To start an interaction session with a nearby device, an app checks for nearby peer devices. When the app finds a peer, it creates an [`NISession`](/documentation/NearbyInteraction/NISession) and sends the session’s [`discoveryToken`](/documentation/NearbyInteraction/NISession/discoveryToken) to the peer using the network technology on which they have agreed. An app can use <doc://com.apple.documentation/documentation/MultipeerConnectivity> to find nearby peers and exchange discovery tokens over the local network.

For an example app that find peer devices using Multipeer Connectivity, see [Implementing interactions between users in close proximity](/documentation/NearbyInteraction/implementing-interactions-between-users-in-close-proximity).

### Add Bonjour Services Plist Keys

To use the local network on iOS and iPadOS 14, your app requires the <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSBonjourServices> key present in its `Info.plist`. The value of the key adheres to the following convention, including `.tcp` and `.udp` extensions.

```swift
<key>NSBonjourServices</key>
<array>
    <string>_myAppName._tcp</string>
    <string>_myAppName._udp</string>
</array>
```

In addition, the system prompts users to grant the app explicit permission to use the local network. To control the messaging of this prompt, your app can include the `NSLocalNetworkUsageDescription` key.

### Check for a Nearby Peer

To broadcast a device’s ability to communicate through Multipeer Connectivity, your app creates an <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser>. The app creates an <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceBrowser> to find other devices advertising with the same technology. When the browser finds another device, it calls <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceBrowserDelegate/browser(_:foundPeer:withDiscoveryInfo:)> and invites the peer to exchange tokens by calling <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceBrowser/invitePeer(_:to:withContext:timeout:)>.

After the other device receives the invitation, <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser> calls <doc://com.apple.documentation/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiserDelegate/advertiser(_:didReceiveInvitationFromPeer:withContext:invitationHandler:)>, in which the apps can begin sharing their discovery tokens.

> Important:
> This process invites any nearby device to interact, but depending on the level of security an app requires, the app can more precisely control broadcasting, invitation, and acceptance behavior. For more information, see <doc://com.apple.documentation/documentation/MultipeerConnectivity>.

### Exchange Discovery Tokens

To respond to the invitation, the app sends its NI session’s [`discoveryToken`](/documentation/NearbyInteraction/NINearbyObject/discoveryToken) to the peer. Because Multipeer Connectivity requires serialization of the data it transmits, the app archives it first.

```swift
let data = try! NSKeyedArchiver.archivedData(withRootObject: niSession.discoverToken, requiringSecureCoding: true)
```

When the receiving peer accepts data from the Multipeer Connectivity session, the app unarchives the data to deserialize the peer’s discovery token.

```swift
let peerDiscoverToken = try! NSKeyedUnarchiver.unarchivedObject(ofClass: NIDiscoverToken, from: data) 
```

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
