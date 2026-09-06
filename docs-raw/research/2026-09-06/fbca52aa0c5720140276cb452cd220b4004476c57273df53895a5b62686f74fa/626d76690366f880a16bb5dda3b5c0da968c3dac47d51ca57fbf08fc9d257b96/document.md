# Audio Queue Hardware Codec Policy

## Topics

### Constants

[`kAudioQueueHardwareCodecPolicy_Default`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_Default)

If the required codec is available in both hardware and software implementations, the audio queue will use a hardware codec if its audio session category permits; it will use a software codec otherwise. If the required codec is available in only one form, that codec implementation is used.

[`kAudioQueueHardwareCodecPolicy_PreferHardware`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_PreferHardware)

The audio queue will use a hardware codec if one is available and if its use permitted by the audio session category that you have set; otherwise, it will use a software codec if one is available.

[`kAudioQueueHardwareCodecPolicy_PreferSoftware`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_PreferSoftware)

The audio queue will use a software codec if one is available; if not, it will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.

[`kAudioQueueHardwareCodecPolicy_UseHardwareOnly`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_UseHardwareOnly)

The audio queue will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.

[`kAudioQueueHardwareCodecPolicy_UseSoftwareOnly`](/documentation/AudioToolbox/kAudioQueueHardwareCodecPolicy_UseSoftwareOnly)

The audio queue will use a software codec if one is available.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
