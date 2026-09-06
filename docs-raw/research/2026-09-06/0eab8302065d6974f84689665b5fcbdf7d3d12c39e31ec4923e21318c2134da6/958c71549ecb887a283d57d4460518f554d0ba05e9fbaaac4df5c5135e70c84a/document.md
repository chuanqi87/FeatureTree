# Hardware Codec Policy Keys

Indicates how an audio queue should choose between hardware and software implementations of a codec.

## Discussion

If the designated codec implementation is not available, or if a hardware codec is chosen and the audio session category does not permit use of hardware codecs, your attempts to call the [`AudioQueuePrime(_:_:_:)`](/documentation/AudioToolbox/AudioQueuePrime(_:_:_:)) or [`AudioQueueStart(_:_:)`](/documentation/AudioToolbox/AudioQueueStart(_:_:)) functions will fail.

Use the [`kAudioFormatProperty_Encoders`](/documentation/AudioToolbox/kAudioFormatProperty_Encoders) or [`kAudioFormatProperty_Decoders`](/documentation/AudioToolbox/kAudioFormatProperty_Decoders) properties to determine whether the codec you are interested in using is available in hardware form, software, or both. See the discussion for [`kAudioFormatProperty_HardwareCodecCapabilities`](/documentation/AudioToolbox/kAudioFormatProperty_HardwareCodecCapabilities).

The system does not permit you to change the value associated with the [`kAudioQueueProperty_HardwareCodecPolicy`](/documentation/AudioToolbox/kAudioQueueProperty_HardwareCodecPolicy) key while the audio queue is primed or running. Changing the value at other times may cause codec settings to be lost.

## Topics

### Constants

[`kAudioQueueProperty_HardwareCodecPolicy`](/documentation/AudioToolbox/kAudioQueueProperty_HardwareCodecPolicy)

The preferred codec implementation type—hardware or software—for an audio queue. Possible values for this constant are the remaining constants described in this section.

[`kAudioQueueHardwareCodecPolicy_Default`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_Default)

If the required codec is available in both hardware and software implementations, the audio queue will use a hardware codec if its audio session category permits; it will use a software codec otherwise. If the required codec is available in only one form, that codec implementation is used.

[`kAudioQueueHardwareCodecPolicy_UseSoftwareOnly`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_UseSoftwareOnly)

The audio queue will use a software codec if one is available.

[`kAudioQueueHardwareCodecPolicy_UseHardwareOnly`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_UseHardwareOnly)

The audio queue will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.

[`kAudioQueueHardwareCodecPolicy_PreferSoftware`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_PreferSoftware)

The audio queue will use a software codec if one is available; if not, it will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.

[`kAudioQueueHardwareCodecPolicy_PreferHardware`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_PreferHardware)

The audio queue will use a hardware codec if one is available and if its use permitted by the audio session category that you have set; otherwise, it will use a software codec if one is available.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
