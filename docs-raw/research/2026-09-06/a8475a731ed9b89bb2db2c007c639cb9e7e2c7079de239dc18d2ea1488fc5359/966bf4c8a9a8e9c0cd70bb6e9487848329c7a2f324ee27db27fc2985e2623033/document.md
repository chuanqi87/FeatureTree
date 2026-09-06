# Audio Session Category Route Overrides

Specifies whether the default audio route for the `PlayAndRecord` category should be overridden.

## Discussion

The `kAudioSessionCategory_PlayAndRecord` category supports simultaneous input and output. You could use this category, for example, to add an effect to audio coming into the device’s microphone. By default, output audio for this category goes to the receiver—the speaker you hold to your ear when on a phone call. The `kAudioSessionOverrideAudioRoute_Speaker` constant lets you direct the output audio to the speaker situated at the bottom of the phone.

## Topics

### Constants

[`kAudioSessionOverrideAudioRoute_None`](/documentation/AudioToolbox/kAudioSessionOverrideAudioRoute_None)

Specifies, for the [`kAudioSessionCategory_PlayAndRecord`](/documentation/AudioToolbox/kAudioSessionCategory_PlayAndRecord) category, that output audio should go to the receiver. This is the default output audio route for this category.

[`kAudioSessionOverrideAudioRoute_Speaker`](/documentation/AudioToolbox/kAudioSessionOverrideAudioRoute_Speaker)

Specifies, for the [`kAudioSessionCategory_PlayAndRecord`](/documentation/AudioToolbox/kAudioSessionCategory_PlayAndRecord) category,  that output audio should go to the speaker, not the receiver.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
