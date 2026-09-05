* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/carplay#app-main)

Framework

# CarPlay

Integrate CarPlay in apps related to audio, communication, navigation, parking, EV charging, food ordering, and more.

iOS 12.0+iPadOS 12.0+Mac Catalyst 14.0+

## [Overview](https://developer.apple.com/documentation/carplay\#overview)

Use the CarPlay framework to create an in-car experience for your app. The framework provides templates for building a version of your app’s interface suitable for presentation on a vehicle’s displays. Add the templates you want to your app and customize them to suit your content. You control the content of the templates, but the framework controls certain aspects of the template interface elements, such as the touch target size, font size, font color, and highlights.

CarPlay features run when the current device supports CarPlay and when that device is connected to an appropriately equipped vehicle. CarPlay handles variations in vehicle systems, letting you focus on your content. When a person runs your app from their vehicle, the system generates and hosts your app’s interface for you. If the device doesn’t support CarPlay, the system doesn’t try to access your app’s CarPlay features.

You can use other technologies to drive portions of your app’s CarPlay interface. Messaging apps can include [SiriKit](https://developer.apple.com/documentation/sirikit) support to allow someone to read or send messages. VoIP apps can use [CallKit](https://developer.apple.com/documentation/callkit) to manage incoming and outgoing calls, often in combination with SiriKit call support. Navigation apps can include [MapKit](https://developer.apple.com/documentation/mapkit) support.

## [Topics](https://developer.apple.com/documentation/carplay\#topics)

### [CarPlay Integration](https://developer.apple.com/documentation/carplay\#CarPlay-Integration)

[Requesting CarPlay Entitlements](https://developer.apple.com/documentation/carplay/requesting-carplay-entitlements)

Configure your CarPlay-enabled app with the entitlements it requires.

[Displaying Content in CarPlay](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay)

Use scenes to present your app’s content on the vehicle’s built-in screen.

[Supporting Previous Versions of iOS](https://developer.apple.com/documentation/carplay/supporting-previous-versions-of-ios)

Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.

[Using the CarPlay Simulator](https://developer.apple.com/documentation/carplay/using-the-carplay-simulator)

Configure Simulator to run and debug your CarPlay-enabled app.

[`class CPTemplateApplicationScene`](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene)

A CarPlay scene that controls your app’s user interface.

[`protocol CPTemplateApplicationSceneDelegate`](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate)

The methods for responding to the life cycle events of your app’s scene.

[`class CPSessionConfiguration`](https://developer.apple.com/documentation/carplay/cpsessionconfiguration)

An object that provides vehicle properties and configuration for the CarPlay environment.

### [General Purpose Templates](https://developer.apple.com/documentation/carplay\#General-Purpose-Templates)

Display your app’s content using a variety of templates that provide a consistent CarPlay layout and appearance.

[`class CPListTemplate`](https://developer.apple.com/documentation/carplay/cplisttemplate)

A template that displays and manages a list of items.

[`class CPGridTemplate`](https://developer.apple.com/documentation/carplay/cpgridtemplate)

A template that displays and manages a grid of items.

[`class CPTabBarTemplate`](https://developer.apple.com/documentation/carplay/cptabbartemplate)

A container template that displays and manages other templates, presenting them as tabs.

[`class CPTemplate`](https://developer.apple.com/documentation/carplay/cptemplate)

An abstract base class for interface templates.

[`protocol CPBarButtonProviding`](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding)

The methods that templates use to provide buttons for the navigation bar.

### [Audio](https://developer.apple.com/documentation/carplay\#Audio)

Templates that are available exclusively to apps with the audio entitlement.

[Integrating CarPlay with Your Music App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-music-app)

Configure your music app to work with CarPlay by displaying a custom UI.

[`class CPNowPlayingTemplate`](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate)

A shared system template that displays Now Playing information.

### [Instrument cluster](https://developer.apple.com/documentation/carplay\#Instrument-cluster)

Symbols that are available for managing the instrument cluster.

[`class CPInstrumentClusterController`](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller)

[`protocol CPInstrumentClusterControllerDelegate`](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate)

[`class CPTemplateApplicationInstrumentClusterScene`](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene)

[`protocol CPTemplateApplicationInstrumentClusterSceneDelegate`](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscenedelegate)

### [Navigation](https://developer.apple.com/documentation/carplay\#Navigation)

Symbols that are available exclusively to apps with the navigation entitlement.

[Integrating CarPlay with Your Navigation App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-navigation-app)

Configure your navigation app to work with CarPlay by displaying your custom map and directions.

[`class CPTemplateApplicationDashboardScene`](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene)

A CarPlay scene that controls your app’s dashboard navigation window.

[`protocol CPTemplateApplicationDashboardSceneDelegate`](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate)

The methods for responding to the life-cycle events of your navigation app’s dashboard scene.

[`class CPMapTemplate`](https://developer.apple.com/documentation/carplay/cpmaptemplate)

A template that displays a navigation overlay that your app draws on the map.

[`class CPSearchTemplate`](https://developer.apple.com/documentation/carplay/cpsearchtemplate)

A template that provides the ability to search for a destination and see a list of search results.

[`class CPVoiceControlTemplate`](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate)

A template that displays a voice control indicator during audio input.

### [Location and Information](https://developer.apple.com/documentation/carplay\#Location-and-Information)

Templates that are available exclusively to apps with the parking, EV-charging, or food-ordering entitlements.

[`class CPPointOfInterestTemplate`](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate)

A template that displays a map with selectable points of interest.

[`class CPInformationTemplate`](https://developer.apple.com/documentation/carplay/cpinformationtemplate)

A template that provides information for a point of interest, food order, parking location, or charging location.

[`class CPTextButton`](https://developer.apple.com/documentation/carplay/cptextbutton)

A button that displays a stylized title.

[Integrating CarPlay with your quick-ordering app](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-quick-ordering-app)

Configure your food-ordering app to work with CarPlay.

### [Maneuvers](https://developer.apple.com/documentation/carplay\#Maneuvers)

[`class CPManeuver`](https://developer.apple.com/documentation/carplay/cpmaneuver)

An object that describes a single navigation instruction.

[`enum CPManeuverState`](https://developer.apple.com/documentation/carplay/cpmaneuverstate)

Values that describe the state of a maneuver.

[`enum CPManeuverType`](https://developer.apple.com/documentation/carplay/cpmaneuvertype)

Values that describe types of navigation maneuvers.

### [Routes, lanes and junctions](https://developer.apple.com/documentation/carplay\#Routes-lanes-and-junctions)

[`class CPRouteInformation`](https://developer.apple.com/documentation/carplay/cprouteinformation)

A class that describes the characteristic elements of a route.

[`class CPLane`](https://developer.apple.com/documentation/carplay/cplane)

A class that describes characteristics of a lane on a roadway.

[`class CPLaneGuidance`](https://developer.apple.com/documentation/carplay/cplaneguidance)

A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.

[`enum CPLaneStatus`](https://developer.apple.com/documentation/carplay/cplanestatus)

Values that describe the status or preferability of a lane.

[`enum CPJunctionType`](https://developer.apple.com/documentation/carplay/cpjunctiontype)

Values that represent types of roadway junctions.

### [Communication](https://developer.apple.com/documentation/carplay\#Communication)

Templates that are available exclusively to apps with the communication entitlement.

[`class CPContactTemplate`](https://developer.apple.com/documentation/carplay/cpcontacttemplate)

A template that displays information about a person or a business.

### [Actions and Alerts](https://developer.apple.com/documentation/carplay\#Actions-and-Alerts)

[`class CPActionSheetTemplate`](https://developer.apple.com/documentation/carplay/cpactionsheettemplate)

A template that displays a modal action sheet.

[`class CPAlertTemplate`](https://developer.apple.com/documentation/carplay/cpalerttemplate)

A template that displays a modal alert.

[`class CPAlertAction`](https://developer.apple.com/documentation/carplay/cpalertaction)

An object that encapsulates an action the user can perform on an action sheet or alert.

### [Related Types](https://developer.apple.com/documentation/carplay\#Related-Types)

[`class CPButton`](https://developer.apple.com/documentation/carplay/cpbutton)

A button that displays an image and invokes a handler when the user taps it.

[`class CPImageSet`](https://developer.apple.com/documentation/carplay/cpimageset)

Light and dark representations of an image.

[`let CarPlayErrorDomain: String`](https://developer.apple.com/documentation/carplay/carplayerrordomain)

The domain that CarPlay uses for any errors it provides.

### [Deprecated](https://developer.apple.com/documentation/carplay\#Deprecated)

[API Reference\\
Deprecated Symbols](https://developer.apple.com/documentation/carplay/deprecated-symbols)

Symbols that the CarPlay framework no longer supports.

### [Reference](https://developer.apple.com/documentation/carplay\#Reference)

[API Reference\\
CarPlay Enumerations](https://developer.apple.com/documentation/carplay/carplay-enumerations)

[API Reference\\
CarPlay Constants](https://developer.apple.com/documentation/carplay/carplay-constants)

### [Classes](https://developer.apple.com/documentation/carplay\#Classes)

[`class CPChargingStationConnection`](https://developer.apple.com/documentation/carplay/cpchargingstationconnection) Beta

[`class CPImageOverlay`](https://developer.apple.com/documentation/carplay/cpimageoverlay)

An overlay that displays information over an image.

[`class CPListImageRowItemCardElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement)

[`class CPListImageRowItemCondensedElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement)

[`class CPListImageRowItemElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement)

Abstract superclass for a a row item element object.

[`class CPListImageRowItemGridElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemgridelement)

[`class CPListImageRowItemImageGridElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemimagegridelement)

[`class CPListImageRowItemRowElement`](https://developer.apple.com/documentation/carplay/cplistimagerowitemrowelement)

[`class CPListTemplateDetailsHeader`](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader)

A header for list templates that displays rich media content with action buttons.

[`class CPMapPanel`](https://developer.apple.com/documentation/carplay/cpmappanel) Beta

[`class CPMapPanelButtonConfiguration`](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration) Beta

[`class CPMapPanelItem`](https://developer.apple.com/documentation/carplay/cpmappanelitem) Beta

[`class CPMapPanelSection`](https://developer.apple.com/documentation/carplay/cpmappanelsection) Beta

[`class CPMapTemplateWaypoint`](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint)

CPMapTemplateWaypoint represents a waypoint with associated travel estimates

[`class CPMessageGridItemConfiguration`](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration)

[`class CPMultiStopCardConfiguration`](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration) Beta

[`class CPNavigationWaypoint`](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint)

CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.

[`class CPNowPlayingMode`](https://developer.apple.com/documentation/carplay/cpnowplayingmode)

[`class CPNowPlayingModeSports`](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports)

The sports mode represents a layout for now playing suited to live-streaming or recorded playback of a sporting event that features exactly two teams.

[`class CPNowPlayingSportsClock`](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock)

A representation of the amount of time elapsed so far in this event, for events where the clock counts UP.

[`class CPNowPlayingSportsEventStatus`](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus)

A representation of the status of a sporting event.

[`class CPNowPlayingSportsTeam`](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam)

A representation of a sports team for the now playing screen, in sports that have exactly two teams.

[`class CPNowPlayingSportsTeamLogo`](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo)

A logo image or, if no image is available, an abbreviation or initialism for this team.

[`class CPPanel`](https://developer.apple.com/documentation/carplay/cppanel) Beta

[`class CPPanelButtonConfiguration`](https://developer.apple.com/documentation/carplay/cppanelbuttonconfiguration) Beta

[`class CPPanelItem`](https://developer.apple.com/documentation/carplay/cppanelitem) Beta

[`class CPPlaybackConfiguration`](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration)

[`class CPRouteDetail`](https://developer.apple.com/documentation/carplay/cproutedetail) Beta

[`class CPRouteSegment`](https://developer.apple.com/documentation/carplay/cproutesegment)

CPRouteSegment describes information pertaining to a segment of a route.

[`class CPSportsOverlay`](https://developer.apple.com/documentation/carplay/cpsportsoverlay)

A sports overlay that displays left and right team information.

[`class CPThumbnailImage`](https://developer.apple.com/documentation/carplay/cpthumbnailimage)

### [Protocols](https://developer.apple.com/documentation/carplay\#Protocols)

[`protocol CPPlayableItem`](https://developer.apple.com/documentation/carplay/cpplayableitem)

### [Structures](https://developer.apple.com/documentation/carplay\#Structures)

[`struct CPLocationCoordinate3D`](https://developer.apple.com/documentation/carplay/cplocationcoordinate3d)

CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.

### [Variables](https://developer.apple.com/documentation/carplay\#Variables)

[`let CPMaximumMessageItemLeadingDetailTextImageSize: CGSize`](https://developer.apple.com/documentation/carplay/cpmaximummessageitemleadingdetailtextimagesize)

Maximum size of an image for the detailed text leading image.

### [Functions](https://developer.apple.com/documentation/carplay\#Functions)

[`func NSStringFromCPJunctionType(CPJunctionType) -> String!`](https://developer.apple.com/documentation/carplay/nsstringfromcpjunctiontype(_:))

[`func NSStringFromCPLaneStatus(CPLaneStatus) -> String!`](https://developer.apple.com/documentation/carplay/nsstringfromcplanestatus(_:))

[`func NSStringFromCPManeuverType(CPManeuverType) -> String!`](https://developer.apple.com/documentation/carplay/nsstringfromcpmaneuvertype(_:))

[`func NSStringFromCPRerouteReason(CPRerouteReason) -> String!`](https://developer.apple.com/documentation/carplay/nsstringfromcpreroutereason(_:))

[`func NSStringFromCPTrafficSide(CPTrafficSide) -> String!`](https://developer.apple.com/documentation/carplay/nsstringfromcptrafficside(_:))

### [Enumerations](https://developer.apple.com/documentation/carplay\#Enumerations)

[`enum CPRerouteReason`](https://developer.apple.com/documentation/carplay/cpreroutereason)

Values that represent reasons for navigation rerouting.

[`enum CPRouteSource`](https://developer.apple.com/documentation/carplay/cproutesource)

Current page is CarPlay