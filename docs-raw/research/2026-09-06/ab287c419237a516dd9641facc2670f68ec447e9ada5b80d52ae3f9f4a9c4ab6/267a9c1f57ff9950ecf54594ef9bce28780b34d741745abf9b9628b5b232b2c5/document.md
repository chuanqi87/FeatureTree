# android.telephony

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.telephony

---

[Kotlin](https://developer.android.com/reference/kotlin/android/telephony/package-summary "View this page in Kotlin")
|Java

Provides APIs for monitoring the basic phone information, such as
the network type and connection state, plus utilities
for manipulating phone number strings.

## Interfaces

|  |  |
| --- | --- |
| [CarrierConfigManager.CarrierConfigChangeListener](https://developer.android.com/reference/android/telephony/CarrierConfigManager.CarrierConfigChangeListener) | Listener interface to get a notification when the carrier configurations have changed. |
| [TelephonyCallback.ActiveDataSubscriptionIdListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ActiveDataSubscriptionIdListener) | Interface for active data subscription ID listener. |
| [TelephonyCallback.BarringInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.BarringInfoListener) | Interface for barring information listener. |
| [TelephonyCallback.CallDisconnectCauseListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallDisconnectCauseListener) | Interface for call disconnect cause listener. |
| [TelephonyCallback.CallForwardingIndicatorListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallForwardingIndicatorListener) | Interface for call-forwarding indicator listener. |
| [TelephonyCallback.CallStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallStateListener) | Interface for call state listener. |
| [TelephonyCallback.CarrierNetworkListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CarrierNetworkListener) | Interface for carrier network listener. |
| [TelephonyCallback.CarrierRoamingNtnListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CarrierRoamingNtnListener) | Interface for carrier roaming non-terrestrial network listener. |
| [TelephonyCallback.CellInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CellInfoListener) | Interface for cell info listener. |
| [TelephonyCallback.CellLocationListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CellLocationListener) | Interface for device cell location listener. |
| [TelephonyCallback.DataActivationStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataActivationStateListener) | Interface for SIM data activation state listener. |
| [TelephonyCallback.DataActivityListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataActivityListener) | Interface for data activity state listener. |
| [TelephonyCallback.DataConnectionStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataConnectionStateListener) | Interface for data connection state listener. |
| [TelephonyCallback.DisplayInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DisplayInfoListener) | Interface for display info listener. |
| [TelephonyCallback.EmergencyNumberListListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.EmergencyNumberListListener) | Interface for the current emergency number list listener. |
| [TelephonyCallback.ImsCallDisconnectCauseListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ImsCallDisconnectCauseListener) | Interface for IMS call disconnect cause listener. |
| [TelephonyCallback.MessageWaitingIndicatorListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.MessageWaitingIndicatorListener) | Interface for message waiting indicator listener. |
| [TelephonyCallback.PhysicalChannelConfigListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.PhysicalChannelConfigListener) | Interface for current physical channel configuration listener. |
| [TelephonyCallback.PreciseDataConnectionStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.PreciseDataConnectionStateListener) | Interface for precise data connection state listener. |
| [TelephonyCallback.RegistrationFailedListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.RegistrationFailedListener) | Interface for registration failures listener. |
| [TelephonyCallback.ServiceStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ServiceStateListener) | Interface for service state listener. |
| [TelephonyCallback.SignalStrengthsListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.SignalStrengthsListener) | Interface for network signal strengths listener. |
| [TelephonyCallback.UserMobileDataStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.UserMobileDataStateListener) | Interface for user mobile data state listener. |

## Classes

|  |  |
| --- | --- |
| [AccessNetworkConstants](https://developer.android.com/reference/android/telephony/AccessNetworkConstants) | Contains access network related constants. |
| [AccessNetworkConstants.AccessNetworkType](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.AccessNetworkType) |  |
| [AccessNetworkConstants.EutranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.EutranBand) | Frequency bands for EUTRAN. |
| [AccessNetworkConstants.GeranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.GeranBand) | Frequency bands for GERAN. |
| [AccessNetworkConstants.NgranBands](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.NgranBands) | Frequency bands for NGRAN https://www.etsi.org/deliver/etsi\_ts/138100\_138199/13810101/15.08.02\_60/ts\_13810101v150802p.pdf https://www.etsi.org/deliver/etsi\_ts/138100\_138199/13810102/15.08.00\_60/ts\_13810102v150800p.pdf |
| [AccessNetworkConstants.UtranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.UtranBand) | Frequency bands for UTRAN. |
| [AvailableNetworkInfo](https://developer.android.com/reference/android/telephony/AvailableNetworkInfo) | Defines available network information which includes corresponding subscription id, network plmns and corresponding priority to be used for network selection by Opportunistic Network Service when passed through `TelephonyManager.updateAvailableNetworks` |
| [AvailableNetworkInfo.Builder](https://developer.android.com/reference/android/telephony/AvailableNetworkInfo.Builder) | Provides a convenient way to set the fields of a `AvailableNetworkInfo` when creating a new instance. |
| [BarringInfo](https://developer.android.com/reference/android/telephony/BarringInfo) | Provides the barring configuration for a particular service type. |
| [BarringInfo.BarringServiceInfo](https://developer.android.com/reference/android/telephony/BarringInfo.BarringServiceInfo) | Describe the current barring configuration of a cell |
| [CarrierConfigManager](https://developer.android.com/reference/android/telephony/CarrierConfigManager) | Provides access to telephony configuration values that are carrier-specific. |
| [CarrierConfigManager.Apn](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Apn) | Configs used for APN setup. |
| [CarrierConfigManager.Bsf](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Bsf) | This groups the BSF (BootStrapping Function) related configs. |
| [CarrierConfigManager.Gps](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Gps) | GPS configs. |
| [CarrierConfigManager.Ims](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Ims) | Configs used by the IMS stack. |
| [CarrierConfigManager.ImsEmergency](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsEmergency) | Emergency Call/E911. |
| [CarrierConfigManager.ImsRtt](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsRtt) | IMS RTT configs. |
| [CarrierConfigManager.ImsServiceEntitlement](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsServiceEntitlement) | Configs used by ImsServiceEntitlement. |
| [CarrierConfigManager.ImsSms](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsSms) | IMS SMS configs. |
| [CarrierConfigManager.ImsSs](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsSs) | IMS supplementary services configs. |
| [CarrierConfigManager.ImsVoice](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsVoice) | IMS Voice configs. |
| [CarrierConfigManager.ImsVt](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsVt) | IMS Video Telephony configs. |
| [CarrierConfigManager.ImsWfc](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsWfc) | WiFi Calling. |
| [CarrierConfigManager.Iwlan](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Iwlan) | Configs used for epdg tunnel bring up. |
| [CarrierConfigManager.OpportunisticNetwork](https://developer.android.com/reference/android/telephony/CarrierConfigManager.OpportunisticNetwork) | Carrier configuration keys for opportunistic networks. |
| [CellIdentity](https://developer.android.com/reference/android/telephony/CellIdentity) | CellIdentity represents the identity of a unique cell. |
| [CellIdentityCdma](https://developer.android.com/reference/android/telephony/CellIdentityCdma) | *This class was deprecated in API level 36. Legacy CDMA is unsupported.* |
| [CellIdentityGsm](https://developer.android.com/reference/android/telephony/CellIdentityGsm) | CellIdentity to represent a unique GSM cell |
| [CellIdentityLte](https://developer.android.com/reference/android/telephony/CellIdentityLte) | CellIdentity is to represent a unique LTE cell |
| [CellIdentityNr](https://developer.android.com/reference/android/telephony/CellIdentityNr) | Information to represent a unique NR(New Radio 5G) cell. |
| [CellIdentityTdscdma](https://developer.android.com/reference/android/telephony/CellIdentityTdscdma) | CellIdentity is to represent a unique TD-SCDMA cell |
| [CellIdentityWcdma](https://developer.android.com/reference/android/telephony/CellIdentityWcdma) | CellIdentity to represent a unique UMTS cell |
| [CellInfo](https://developer.android.com/reference/android/telephony/CellInfo) | Immutable cell information from a point in time. |
| [CellInfoCdma](https://developer.android.com/reference/android/telephony/CellInfoCdma) | *This class was deprecated in API level 36. Legacy CDMA is unsupported.* |
| [CellInfoGsm](https://developer.android.com/reference/android/telephony/CellInfoGsm) | A `CellInfo` representing a GSM cell that provides identity and measurement info. |
| [CellInfoLte](https://developer.android.com/reference/android/telephony/CellInfoLte) | A `CellInfo` representing an LTE cell that provides identity and measurement info. |
| [CellInfoNr](https://developer.android.com/reference/android/telephony/CellInfoNr) | A `CellInfo` representing an 5G NR cell that provides identity and measurement info. |
| [CellInfoTdscdma](https://developer.android.com/reference/android/telephony/CellInfoTdscdma) | A `CellInfo` representing a TD-SCDMA cell that provides identity and measurement info. |
| [CellInfoWcdma](https://developer.android.com/reference/android/telephony/CellInfoWcdma) | A `CellInfo` representing a WCDMA cell that provides identity and measurement info. |
| [CellLocation](https://developer.android.com/reference/android/telephony/CellLocation) | *This class was deprecated in API level 31. use `CellIdentity`.* |
| [CellSignalStrength](https://developer.android.com/reference/android/telephony/CellSignalStrength) | Abstract base class for cell phone signal strength related information. |
| [CellSignalStrengthCdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthCdma) | Signal strength related information. |
| [CellSignalStrengthGsm](https://developer.android.com/reference/android/telephony/CellSignalStrengthGsm) | GSM signal strength related information. |
| [CellSignalStrengthLte](https://developer.android.com/reference/android/telephony/CellSignalStrengthLte) | LTE signal strength related information. |
| [CellSignalStrengthNr](https://developer.android.com/reference/android/telephony/CellSignalStrengthNr) | 5G NR signal strength related information. |
| [CellSignalStrengthTdscdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthTdscdma) | Tdscdma signal strength related information. |
| [CellSignalStrengthWcdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthWcdma) | Wcdma signal strength related information. |
| [ClosedSubscriberGroupInfo](https://developer.android.com/reference/android/telephony/ClosedSubscriberGroupInfo) | Information to represent a closed subscriber group. |
| [DataFailCause](https://developer.android.com/reference/android/telephony/DataFailCause) | DataFailCause collects data connection failure causes code from different sources. |
| [DisconnectCause](https://developer.android.com/reference/android/telephony/DisconnectCause) | Describes the cause of a disconnected call. |
| [IccOpenLogicalChannelResponse](https://developer.android.com/reference/android/telephony/IccOpenLogicalChannelResponse) | Response to the `TelephonyManager.iccOpenLogicalChannel` command. |
| [MbmsDownloadSession](https://developer.android.com/reference/android/telephony/MbmsDownloadSession) | This class provides functionality for file download over MBMS. |
| [MbmsGroupCallSession](https://developer.android.com/reference/android/telephony/MbmsGroupCallSession) | This class provides functionality for accessing group call functionality over MBMS. |
| [MbmsStreamingSession](https://developer.android.com/reference/android/telephony/MbmsStreamingSession) | This class provides functionality for streaming media over MBMS. |
| [NeighboringCellInfo](https://developer.android.com/reference/android/telephony/NeighboringCellInfo) | *This class was deprecated in API level 29. This class should not be used by any app targeting `Android Q` or higher. Instead callers should use `CellInfo`.* |
| [NetworkRegistrationInfo](https://developer.android.com/reference/android/telephony/NetworkRegistrationInfo) | Description of a mobile network registration info |
| [NetworkScan](https://developer.android.com/reference/android/telephony/NetworkScan) | The caller of `TelephonyManager.requestNetworkScan(NetworkScanRequest,Executor,NetworkScanCallback)` will receive an instance of `NetworkScan`, which contains a callback method `stopScan()` for stopping the in-progress scan. |
| [NetworkScanRequest](https://developer.android.com/reference/android/telephony/NetworkScanRequest) | Defines a request to perform a network scan. |
| [ParsedPhoneNumber](https://developer.android.com/reference/android/telephony/ParsedPhoneNumber) | Handles the results from PhoneNumberManager by providing Phone number, error code, and is valid number. |
| [PhoneNumberFormattingTextWatcher](https://developer.android.com/reference/android/telephony/PhoneNumberFormattingTextWatcher) | *This class was deprecated in API level 35. This is a thin wrapper on a `libphonenumber` `AsYouTypeFormatter`; it is recommended to use that instead.* |
| [PhoneNumberManager](https://developer.android.com/reference/android/telephony/PhoneNumberManager) | PhoneNumberManager provides APIs for parsing phone numbers from various sources, such as URIs. |
| [PhoneNumberUtils](https://developer.android.com/reference/android/telephony/PhoneNumberUtils) | Various utilities for dealing with phone number strings. |
| [PhoneStateListener](https://developer.android.com/reference/android/telephony/PhoneStateListener) | *This class was deprecated in API level 31. Use `TelephonyCallback` instead.* |
| [PhysicalChannelConfig](https://developer.android.com/reference/android/telephony/PhysicalChannelConfig) | Information describing the physical channel configuration. |
| [PreciseDataConnectionState](https://developer.android.com/reference/android/telephony/PreciseDataConnectionState) | Contains precise data connection state. |
| [RadioAccessSpecifier](https://developer.android.com/reference/android/telephony/RadioAccessSpecifier) | Describes a particular radio access network to be scanned. |
| [ServiceState](https://developer.android.com/reference/android/telephony/ServiceState) | Contains phone state and service related information. |
| [SignalStrength](https://developer.android.com/reference/android/telephony/SignalStrength) | Contains phone signal strength related information. |
| [SignalStrengthUpdateRequest](https://developer.android.com/reference/android/telephony/SignalStrengthUpdateRequest) | Request used to register `SignalThresholdInfo` to be notified when the signal strength breach the specified thresholds. |
| [SignalStrengthUpdateRequest.Builder](https://developer.android.com/reference/android/telephony/SignalStrengthUpdateRequest.Builder) | Builder class to create `SignalStrengthUpdateRequest` object. |
| [SignalThresholdInfo](https://developer.android.com/reference/android/telephony/SignalThresholdInfo) | Defines the threshold value of the signal strength. |
| [SignalThresholdInfo.Builder](https://developer.android.com/reference/android/telephony/SignalThresholdInfo.Builder) | Builder class to create `SignalThresholdInfo` objects. |
| [SmsManager](https://developer.android.com/reference/android/telephony/SmsManager) | Manages SMS operations such as sending data, text, and pdu SMS messages. |
| [SmsManager.FinancialSmsCallback](https://developer.android.com/reference/android/telephony/SmsManager.FinancialSmsCallback) | callback for providing asynchronous sms messages for financial app. |
| [SmsMessage](https://developer.android.com/reference/android/telephony/SmsMessage) | A Short Message Service message. |
| [SmsMessage.SubmitPdu](https://developer.android.com/reference/android/telephony/SmsMessage.SubmitPdu) |  |
| [SubscriptionInfo](https://developer.android.com/reference/android/telephony/SubscriptionInfo) | A Parcelable class for Subscription Information. |
| [SubscriptionManager](https://developer.android.com/reference/android/telephony/SubscriptionManager) | Subscription manager provides the mobile subscription information. |
| [SubscriptionManager.OnOpportunisticSubscriptionsChangedListener](https://developer.android.com/reference/android/telephony/SubscriptionManager.OnOpportunisticSubscriptionsChangedListener) | A listener class for monitoring changes to `SubscriptionInfo` records of opportunistic subscriptions. |
| [SubscriptionManager.OnSubscriptionsChangedListener](https://developer.android.com/reference/android/telephony/SubscriptionManager.OnSubscriptionsChangedListener) | A listener class for monitoring changes to `SubscriptionInfo` records. |
| [SubscriptionPlan](https://developer.android.com/reference/android/telephony/SubscriptionPlan) | Description of a billing relationship plan between a carrier and a specific subscriber. |
| [SubscriptionPlan.Builder](https://developer.android.com/reference/android/telephony/SubscriptionPlan.Builder) | Builder for a `SubscriptionPlan`. |
| [TelephonyCallback](https://developer.android.com/reference/android/telephony/TelephonyCallback) | A callback class for monitoring changes in specific telephony states on the device, including service state, signal strength, message waiting indicator (voicemail), and others. |
| [TelephonyDisplayInfo](https://developer.android.com/reference/android/telephony/TelephonyDisplayInfo) | TelephonyDisplayInfo contains telephony-related information used for display purposes only. |
| [TelephonyManager](https://developer.android.com/reference/android/telephony/TelephonyManager) | Provides access to information about the telephony services on the device. |
| [TelephonyManager.CellInfoCallback](https://developer.android.com/reference/android/telephony/TelephonyManager.CellInfoCallback) | Callback for providing asynchronous `CellInfo` on request |
| [TelephonyManager.UssdResponseCallback](https://developer.android.com/reference/android/telephony/TelephonyManager.UssdResponseCallback) | Used to notify callers of `TelephonyManager.sendUssdRequest(String,UssdResponseCallback,Handler)` when the network either successfully executes a USSD request, or if there was a failure while executing the request. |
| [TelephonyScanManager](https://developer.android.com/reference/android/telephony/TelephonyScanManager) | Manages the radio access network scan requests and callbacks. |
| [TelephonyScanManager.NetworkScanCallback](https://developer.android.com/reference/android/telephony/TelephonyScanManager.NetworkScanCallback) | The caller of `TelephonyManager.requestNetworkScan(NetworkScanRequest,Executor,NetworkScanCallback)` should implement and provide this callback so that the scan results or errors can be returned. |
| [UiccCardInfo](https://developer.android.com/reference/android/telephony/UiccCardInfo) | The UiccCardInfo represents information about a currently inserted UICC or embedded eUICC. |
| [UiccPortInfo](https://developer.android.com/reference/android/telephony/UiccPortInfo) | UiccPortInfo class represents information about a single port contained on `UiccCardInfo`. |
| [VisualVoicemailService](https://developer.android.com/reference/android/telephony/VisualVoicemailService) | This service is implemented by dialer apps that wishes to handle OMTP or similar visual voicemails. |
| [VisualVoicemailService.VisualVoicemailTask](https://developer.android.com/reference/android/telephony/VisualVoicemailService.VisualVoicemailTask) | Represents a visual voicemail event which needs to be handled. |
| [VisualVoicemailSms](https://developer.android.com/reference/android/telephony/VisualVoicemailSms) | Represents the content of a visual voicemail SMS. |
| [VisualVoicemailSmsFilterSettings](https://developer.android.com/reference/android/telephony/VisualVoicemailSmsFilterSettings) | Class to represent various settings for the visual voicemail SMS filter. |
| [VisualVoicemailSmsFilterSettings.Builder](https://developer.android.com/reference/android/telephony/VisualVoicemailSmsFilterSettings.Builder) | Builder class for `VisualVoicemailSmsFilterSettings` objects. |

## Enums

|  |  |
| --- | --- |
| [SmsMessage.MessageClass](https://developer.android.com/reference/android/telephony/SmsMessage.MessageClass) | SMS Class enumeration. |

## Exceptions

|  |  |
| --- | --- |
| [TelephonyManager.CallComposerException](https://developer.android.com/reference/android/telephony/TelephonyManager.CallComposerException) | Exception that may be supplied to the callback in `TelephonyManager.uploadCallComposerPicture(InputStream, String, Executor, OutcomeReceiver)` if something goes awry. |
| [TelephonyManager.ModemErrorException](https://developer.android.com/reference/android/telephony/TelephonyManager.ModemErrorException) | Exception that is supplied to the callback in `TelephonyManager.getNetworkSlicingConfiguration(Executor, OutcomeReceiver)` if the modem returned a failure. |
| [TelephonyManager.NetworkSlicingException](https://developer.android.com/reference/android/telephony/TelephonyManager.NetworkSlicingException) | Exception that may be supplied to the callback in `TelephonyManager.getNetworkSlicingConfiguration(Executor, OutcomeReceiver)` if something goes awry. |
| [TelephonyManager.TimeoutException](https://developer.android.com/reference/android/telephony/TelephonyManager.TimeoutException) | Exception that is supplied to the callback in `TelephonyManager.getNetworkSlicingConfiguration(Executor, OutcomeReceiver)` if the system timed out waiting for a response from the Radio. |

* ## Interfaces

  + [CarrierConfigManager.CarrierConfigChangeListener](https://developer.android.com/reference/android/telephony/CarrierConfigManager.CarrierConfigChangeListener)
  + [TelephonyCallback.ActiveDataSubscriptionIdListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ActiveDataSubscriptionIdListener)
  + [TelephonyCallback.BarringInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.BarringInfoListener)
  + [TelephonyCallback.CallDisconnectCauseListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallDisconnectCauseListener)
  + [TelephonyCallback.CallForwardingIndicatorListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallForwardingIndicatorListener)
  + [TelephonyCallback.CallStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CallStateListener)
  + [TelephonyCallback.CarrierNetworkListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CarrierNetworkListener)
  + [TelephonyCallback.CarrierRoamingNtnListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CarrierRoamingNtnListener)
  + [TelephonyCallback.CellInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CellInfoListener)
  + [TelephonyCallback.CellLocationListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.CellLocationListener)
  + [TelephonyCallback.DataActivationStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataActivationStateListener)
  + [TelephonyCallback.DataActivityListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataActivityListener)
  + [TelephonyCallback.DataConnectionStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DataConnectionStateListener)
  + [TelephonyCallback.DisplayInfoListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.DisplayInfoListener)
  + [TelephonyCallback.EmergencyNumberListListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.EmergencyNumberListListener)
  + [TelephonyCallback.ImsCallDisconnectCauseListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ImsCallDisconnectCauseListener)
  + [TelephonyCallback.MessageWaitingIndicatorListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.MessageWaitingIndicatorListener)
  + [TelephonyCallback.PhysicalChannelConfigListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.PhysicalChannelConfigListener)
  + [TelephonyCallback.PreciseDataConnectionStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.PreciseDataConnectionStateListener)
  + [TelephonyCallback.RegistrationFailedListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.RegistrationFailedListener)
  + [TelephonyCallback.ServiceStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.ServiceStateListener)
  + [TelephonyCallback.SignalStrengthsListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.SignalStrengthsListener)
  + [TelephonyCallback.UserMobileDataStateListener](https://developer.android.com/reference/android/telephony/TelephonyCallback.UserMobileDataStateListener)
* ## Classes

  + [AccessNetworkConstants](https://developer.android.com/reference/android/telephony/AccessNetworkConstants)
  + [AccessNetworkConstants.AccessNetworkType](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.AccessNetworkType)
  + [AccessNetworkConstants.EutranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.EutranBand)
  + [AccessNetworkConstants.GeranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.GeranBand)
  + [AccessNetworkConstants.NgranBands](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.NgranBands)
  + [AccessNetworkConstants.UtranBand](https://developer.android.com/reference/android/telephony/AccessNetworkConstants.UtranBand)
  + [AvailableNetworkInfo](https://developer.android.com/reference/android/telephony/AvailableNetworkInfo)
  + [AvailableNetworkInfo.Builder](https://developer.android.com/reference/android/telephony/AvailableNetworkInfo.Builder)
  + [BarringInfo](https://developer.android.com/reference/android/telephony/BarringInfo)
  + [BarringInfo.BarringServiceInfo](https://developer.android.com/reference/android/telephony/BarringInfo.BarringServiceInfo)
  + [CarrierConfigManager](https://developer.android.com/reference/android/telephony/CarrierConfigManager)
  + [CarrierConfigManager.Apn](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Apn)
  + [CarrierConfigManager.Bsf](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Bsf)
  + [CarrierConfigManager.Gps](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Gps)
  + [CarrierConfigManager.Ims](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Ims)
  + [CarrierConfigManager.ImsEmergency](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsEmergency)
  + [CarrierConfigManager.ImsRtt](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsRtt)
  + [CarrierConfigManager.ImsServiceEntitlement](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsServiceEntitlement)
  + [CarrierConfigManager.ImsSms](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsSms)
  + [CarrierConfigManager.ImsSs](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsSs)
  + [CarrierConfigManager.ImsVoice](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsVoice)
  + [CarrierConfigManager.ImsVt](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsVt)
  + [CarrierConfigManager.ImsWfc](https://developer.android.com/reference/android/telephony/CarrierConfigManager.ImsWfc)
  + [CarrierConfigManager.Iwlan](https://developer.android.com/reference/android/telephony/CarrierConfigManager.Iwlan)
  + [CarrierConfigManager.OpportunisticNetwork](https://developer.android.com/reference/android/telephony/CarrierConfigManager.OpportunisticNetwork)
  + [CellIdentity](https://developer.android.com/reference/android/telephony/CellIdentity)
  + [CellIdentityCdma](https://developer.android.com/reference/android/telephony/CellIdentityCdma)
  + [CellIdentityGsm](https://developer.android.com/reference/android/telephony/CellIdentityGsm)
  + [CellIdentityLte](https://developer.android.com/reference/android/telephony/CellIdentityLte)
  + [CellIdentityNr](https://developer.android.com/reference/android/telephony/CellIdentityNr)
  + [CellIdentityTdscdma](https://developer.android.com/reference/android/telephony/CellIdentityTdscdma)
  + [CellIdentityWcdma](https://developer.android.com/reference/android/telephony/CellIdentityWcdma)
  + [CellInfo](https://developer.android.com/reference/android/telephony/CellInfo)
  + [CellInfoCdma](https://developer.android.com/reference/android/telephony/CellInfoCdma)
  + [CellInfoGsm](https://developer.android.com/reference/android/telephony/CellInfoGsm)
  + [CellInfoLte](https://developer.android.com/reference/android/telephony/CellInfoLte)
  + [CellInfoNr](https://developer.android.com/reference/android/telephony/CellInfoNr)
  + [CellInfoTdscdma](https://developer.android.com/reference/android/telephony/CellInfoTdscdma)
  + [CellInfoWcdma](https://developer.android.com/reference/android/telephony/CellInfoWcdma)
  + [CellLocation](https://developer.android.com/reference/android/telephony/CellLocation)
  + [CellSignalStrength](https://developer.android.com/reference/android/telephony/CellSignalStrength)
  + [CellSignalStrengthCdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthCdma)
  + [CellSignalStrengthGsm](https://developer.android.com/reference/android/telephony/CellSignalStrengthGsm)
  + [CellSignalStrengthLte](https://developer.android.com/reference/android/telephony/CellSignalStrengthLte)
  + [CellSignalStrengthNr](https://developer.android.com/reference/android/telephony/CellSignalStrengthNr)
  + [CellSignalStrengthTdscdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthTdscdma)
  + [CellSignalStrengthWcdma](https://developer.android.com/reference/android/telephony/CellSignalStrengthWcdma)
  + [ClosedSubscriberGroupInfo](https://developer.android.com/reference/android/telephony/ClosedSubscriberGroupInfo)
  + [DataFailCause](https://developer.android.com/reference/android/telephony/DataFailCause)
  + [DisconnectCause](https://developer.android.com/reference/android/telephony/DisconnectCause)
  + [IccOpenLogicalChannelResponse](https://developer.android.com/reference/android/telephony/IccOpenLogicalChannelResponse)
  + [MbmsDownloadSession](https://developer.android.com/reference/android/telephony/MbmsDownloadSession)
  + [MbmsGroupCallSession](https://developer.android.com/reference/android/telephony/MbmsGroupCallSession)
  + [MbmsStreamingSession](https://developer.android.com/reference/android/telephony/MbmsStreamingSession)
  + [NeighboringCellInfo](https://developer.android.com/reference/android/telephony/NeighboringCellInfo)
  + [NetworkRegistrationInfo](https://developer.android.com/reference/android/telephony/NetworkRegistrationInfo)
  + [NetworkScan](https://developer.android.com/reference/android/telephony/NetworkScan)
  + [NetworkScanRequest](https://developer.android.com/reference/android/telephony/NetworkScanRequest)
  + [ParsedPhoneNumber](https://developer.android.com/reference/android/telephony/ParsedPhoneNumber)
  + [PhoneNumberFormattingTextWatcher](https://developer.android.com/reference/android/telephony/PhoneNumberFormattingTextWatcher)
  + [PhoneNumberManager](https://developer.android.com/reference/android/telephony/PhoneNumberManager)
  + [PhoneNumberUtils](https://developer.android.com/reference/android/telephony/PhoneNumberUtils)
  + [PhoneStateListener](https://developer.android.com/reference/android/telephony/PhoneStateListener)
  + [PhysicalChannelConfig](https://developer.android.com/reference/android/telephony/PhysicalChannelConfig)
  + [PreciseDataConnectionState](https://developer.android.com/reference/android/telephony/PreciseDataConnectionState)
  + [RadioAccessSpecifier](https://developer.android.com/reference/android/telephony/RadioAccessSpecifier)
  + [ServiceState](https://developer.android.com/reference/android/telephony/ServiceState)
  + [SignalStrength](https://developer.android.com/reference/android/telephony/SignalStrength)
  + [SignalStrengthUpdateRequest](https://developer.android.com/reference/android/telephony/SignalStrengthUpdateRequest)
  + [SignalStrengthUpdateRequest.Builder](https://developer.android.com/reference/android/telephony/SignalStrengthUpdateRequest.Builder)
  + [SignalThresholdInfo](https://developer.android.com/reference/android/telephony/SignalThresholdInfo)
  + [SignalThresholdInfo.Builder](https://developer.android.com/reference/android/telephony/SignalThresholdInfo.Builder)
  + [SmsManager](https://developer.android.com/reference/android/telephony/SmsManager)
  + [SmsManager.FinancialSmsCallback](https://developer.android.com/reference/android/telephony/SmsManager.FinancialSmsCallback)
  + [SmsMessage](https://developer.android.com/reference/android/telephony/SmsMessage)
  + [SmsMessage.SubmitPdu](https://developer.android.com/reference/android/telephony/SmsMessage.SubmitPdu)
  + [SubscriptionInfo](https://developer.android.com/reference/android/telephony/SubscriptionInfo)
  + [SubscriptionManager](https://developer.android.com/reference/android/telephony/SubscriptionManager)
  + [SubscriptionManager.OnOpportunisticSubscriptionsChangedListener](https://developer.android.com/reference/android/telephony/SubscriptionManager.OnOpportunisticSubscriptionsChangedListener)
  + [SubscriptionManager.OnSubscriptionsChangedListener](https://developer.android.com/reference/android/telephony/SubscriptionManager.OnSubscriptionsChangedListener)
  + [SubscriptionPlan](https://developer.android.com/reference/android/telephony/SubscriptionPlan)
  + [SubscriptionPlan.Builder](https://developer.android.com/reference/android/telephony/SubscriptionPlan.Builder)
  + [TelephonyCallback](https://developer.android.com/reference/android/telephony/TelephonyCallback)
  + [TelephonyDisplayInfo](https://developer.android.com/reference/android/telephony/TelephonyDisplayInfo)
  + [TelephonyManager](https://developer.android.com/reference/android/telephony/TelephonyManager)
  + [TelephonyManager.CellInfoCallback](https://developer.android.com/reference/android/telephony/TelephonyManager.CellInfoCallback)
  + [TelephonyManager.UssdResponseCallback](https://developer.android.com/reference/android/telephony/TelephonyManager.UssdResponseCallback)
  + [TelephonyScanManager](https://developer.android.com/reference/android/telephony/TelephonyScanManager)
  + [TelephonyScanManager.NetworkScanCallback](https://developer.android.com/reference/android/telephony/TelephonyScanManager.NetworkScanCallback)
  + [UiccCardInfo](https://developer.android.com/reference/android/telephony/UiccCardInfo)
  + [UiccPortInfo](https://developer.android.com/reference/android/telephony/UiccPortInfo)
  + [VisualVoicemailService](https://developer.android.com/reference/android/telephony/VisualVoicemailService)
  + [VisualVoicemailService.VisualVoicemailTask](https://developer.android.com/reference/android/telephony/VisualVoicemailService.VisualVoicemailTask)
  + [VisualVoicemailSms](https://developer.android.com/reference/android/telephony/VisualVoicemailSms)
  + [VisualVoicemailSmsFilterSettings](https://developer.android.com/reference/android/telephony/VisualVoicemailSmsFilterSettings)
  + [VisualVoicemailSmsFilterSettings.Builder](https://developer.android.com/reference/android/telephony/VisualVoicemailSmsFilterSettings.Builder)
* ## Enums

  + [SmsMessage.MessageClass](https://developer.android.com/reference/android/telephony/SmsMessage.MessageClass)
* ## Exceptions

  + [TelephonyManager.CallComposerException](https://developer.android.com/reference/android/telephony/TelephonyManager.CallComposerException)
  + [TelephonyManager.ModemErrorException](https://developer.android.com/reference/android/telephony/TelephonyManager.ModemErrorException)
  + [TelephonyManager.NetworkSlicingException](https://developer.android.com/reference/android/telephony/TelephonyManager.NetworkSlicingException)
  + [TelephonyManager.TimeoutException](https://developer.android.com/reference/android/telephony/TelephonyManager.TimeoutException)
