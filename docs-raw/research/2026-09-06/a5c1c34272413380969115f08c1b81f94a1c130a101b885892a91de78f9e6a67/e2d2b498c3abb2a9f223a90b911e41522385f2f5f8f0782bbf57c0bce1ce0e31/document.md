# Audio Engine

Perform advanced real-time and offline audio processing, implement 3D spatialization, and work with MIDI and samplers.

## Discussion

The audio engine provides a powerful, feature-rich API to simplify audio generation, processing, and input/output tasks. The engine contains a group of nodes that connect to form an audio signal processing chain. These nodes perform a variety of tasks on a signal before rendering to an output destination.

Audio Engine helps you achieve simple, as well as complex, audio processing tasks. With Audio Engine, your apps can:

- Play audio using files and buffers
- Capture audio at any point during the processing chain
- Add built-in effects like reverb, delay, distortion, and your custom effects
- Perform stereo and 3D mixing
- Provide MIDI playback and control over sampler instruments

## Topics

### Essentials

[`AVAudioEngine`](/documentation/AVFAudio/AVAudioEngine)

An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.

### Nodes

[`AVAudioNode`](/documentation/AVFAudio/AVAudioNode)

An object you use for audio generation, processing, or an I/O block.

[`AVAudioInputNode`](/documentation/AVFAudio/AVAudioInputNode)

An object that connects to the system’s audio input.

[`AVAudioOutputNode`](/documentation/AVFAudio/AVAudioOutputNode)

An object that connects to the system’s audio output.

[`AVAudioIONode`](/documentation/AVFAudio/AVAudioIONode)

An object that performs audio input or output in the engine.

[`AVAudioIONodeInputBlockRealtimeSafe`](/documentation/AVFAudio/AVAudioIONodeInputBlockRealtimeSafe)

### Playback

[Building an audio sequencer to arrange and play clips](/documentation/AVFAudio/building-an-audio-sequencer-to-arrange-and-play-clips)

Synchronize audio loops with a main tempo by creating a real-time clip launcher.

[Playing custom audio with your own player](/documentation/AVFAudio/playing-custom-audio-with-your-own-player)

Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.

[Using voice processing](/documentation/AVFAudio/using-voice-processing)

Add voice-processing capabilities to your app by using audio engine.

[`AVAudioPlayerNode`](/documentation/AVFAudio/AVAudioPlayerNode)

An object for scheduling the playback of buffers or segments of audio files.

### MIDI

[`AVAudioSequencer`](/documentation/AVFAudio/AVAudioSequencer)

An object that plays audio from a collection of MIDI events the system organizes into music tracks.

[`AVAudioUnitSampler`](/documentation/AVFAudio/AVAudioUnitSampler)

An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.

[`AVMIDIEventListBlock`](/documentation/AVFAudio/AVMIDIEventListBlock)

### Mixing

[`AVAudioMixerNode`](/documentation/AVFAudio/AVAudioMixerNode)

An object that takes any number of inputs and converts them into a single output.

[`AVAudioMixing`](/documentation/AVFAudio/AVAudioMixing)

A collection of properties that are applicable to the input bus of a mixer node.

### Effects

[Creating custom audio effects](/documentation/AVFAudio/creating-custom-audio-effects)

Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.

[Audio Units](/documentation/AVFAudio/audio-units)

The data type for a plug-in component that provides audio processing or audio data generation.

### Rendering

[Building a signal generator](/documentation/AVFAudio/building-a-signal-generator)

Generate audio signals using an audio source node and a custom render callback.

[Performing offline audio processing](/documentation/AVFAudio/performing-offline-audio-processing)

Add offline audio processing features to your app by enabling offline manual rendering mode.

[`AVAudioSourceNode`](/documentation/AVFAudio/AVAudioSourceNode)

An object that supplies audio data.

[`AVAudioSourceNodeRenderBlockRealtimeSafe`](/documentation/AVFAudio/AVAudioSourceNodeRenderBlockRealtimeSafe)

[`AVAudioSinkNode`](/documentation/AVFAudio/AVAudioSinkNode)

An object that receives audio data.

[`AVAudioSinkNodeReceiverBlockRealtimeSafe`](/documentation/AVFAudio/AVAudioSinkNodeReceiverBlockRealtimeSafe)

### Conversion

[`AVAudioConverter`](/documentation/AVFAudio/AVAudioConverter)

An object that converts streams of audio between formats.

### Spatial audio

[`AVAudioEnvironmentNode`](/documentation/AVFAudio/AVAudioEnvironmentNode)

An object that simulates a 3D audio environment.

[`AVAudioEnvironmentDistanceAttenuationParameters`](/documentation/AVFAudio/AVAudioEnvironmentDistanceAttenuationParameters)

An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.

[`AVAudioEnvironmentReverbParameters`](/documentation/AVFAudio/AVAudioEnvironmentReverbParameters)

A class that encapsulates the parameters that you use to control the reverb of the environment node class.

[`AVAudio3DMixing`](/documentation/AVFAudio/AVAudio3DMixing)

A collection of properties that define 3D mixing properties.

[`AVAudio3DPoint`](/documentation/AVFAudio/AVAudio3DPoint)

A structure that represents a point in 3D space.

[`AVAudio3DVectorOrientation`](/documentation/AVFAudio/AVAudio3DVectorOrientation)

A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.

[`AVAudio3DAngularOrientation`](/documentation/AVFAudio/AVAudio3DAngularOrientation)

A structure that represents the angular orientation of the listener in 3D space.

[`AVAudio3DMixingSourceMode`](/documentation/AVFAudio/AVAudio3DMixingSourceMode)

The source modes for the input bus of the audio environment node.

[`AVAudio3DMixingRenderingAlgorithm`](/documentation/AVFAudio/AVAudio3DMixingRenderingAlgorithm)

The types of rendering algorithms available per input bus of the environment node.

[`AVAudioEnvironmentOutputType`](/documentation/AVFAudio/AVAudioEnvironmentOutputType)

The output types for using with the automatic 3D mixing rendering algorithm.

[`AVAudio3DMixingPointSourceInHeadMode`](/documentation/AVFAudio/AVAudio3DMixingPointSourceInHeadMode)

The in-head modes for a point source.

[`AVAudio3DVector`](/documentation/AVFAudio/AVAudio3DVector)

A structure that represents a vector in 3D space, in degrees.

### Supporting data types

[`AVAudioBuffer`](/documentation/AVFAudio/AVAudioBuffer)

An object that represents a buffer of audio data with a format.

[`AVAudioPCMBuffer`](/documentation/AVFAudio/AVAudioPCMBuffer)

An object that represents an audio buffer you use with PCM audio formats.

[`AVReadOnlyAudioPCMBuffer`](/documentation/AVFAudio/AVReadOnlyAudioPCMBuffer)

A read-only, Sendable audio buffer for safe concurrent access.

[`AVAudioFile`](/documentation/AVFAudio/AVAudioFile)

An object that represents an audio file that the system can open for reading or writing.

[`AVAudioTime`](/documentation/AVFAudio/AVAudioTime)

An object you use to represent a moment in time.

[Audio settings](/documentation/AVFAudio/audio-settings)

Configure audio processing settings using standard key and value constants.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
