# Metal

Render advanced 3D graphics and compute data in parallel with graphics processors.

## Overview

The Metal framework gives your app direct access to a device’s graphics processing unit (GPU). With Metal, apps can leverage a GPU to quickly render complex scenes and run computational tasks in parallel. For example, apps in these categories use Metal to maximize their performance:

- Games that render sophisticated 2D or 3D environments
- Video processing apps, like Final Cut Pro
- Scientific research apps that analyze and process large datasets
- Fully immersive visionOS apps

Metal works hand-in-hand with other frameworks that supplement its capability. For example, <doc://com.apple.documentation/documentation/MetalFX> upscales your renderings in less time than rendering them natively, and <doc://com.apple.documentation/documentation/MetalKit> simplifies the tasks that display your Metal content onscreen. The <doc://com.apple.documentation/documentation/MetalPerformanceShaders> framework provides a large library of optimized compute and rendering shaders that take advantage of each GPU’s unique hardware. In visionOS, create fully immersive stereoscopic content with the help of the <doc://com.apple.documentation/documentation/CompositorServices> framework.

Many high-level Apple frameworks leverage the performance of Metal, including <doc://com.apple.documentation/documentation/RealityKit>, <doc://com.apple.documentation/documentation/SpriteKit>, and <doc://com.apple.documentation/documentation/CoreImage>. These high-level frameworks implement the GPU programming details for you. However, you can typically get better performance by writing your own custom Metal and shader code. See the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for shader implementation details.

## Topics

### Essentials

Begin with the Metal fundamentals.

[Understanding the Metal 4 core API](/documentation/Metal/understanding-the-metal-4-core-api)

Discover the features and functionality in the Metal 4 foundational APIs.

[Drawing a triangle with Metal 4](/documentation/Metal/drawing-a-triangle-with-metal-4)

Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.

[Performing calculations on a GPU](/documentation/Metal/performing-calculations-on-a-gpu)

Use Metal to find GPUs and perform calculations on them.

[Using Metal to draw a view’s contents](/documentation/Metal/using-metal-to-draw-a-view's-contents)

Create a MetalKit view and a render pass to draw the view’s contents.

### Samples

Discover graphics techniques and Metal features through sample code projects.

[Metal sample code library](/documentation/Metal/metal-sample-code-library)

Explore the complete set of Metal samples.

### GPU devices

Start with a Metal device instance to begin working with the GPU it represents.

[GPU devices and work submission](/documentation/Metal/gpu-devices-and-work-submission)

Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

### Command encoders

Send work to a GPU by issuing commands and configuring the pipeline states for those commands.

[Render passes](/documentation/Metal/render-passes)

Encode a render pass to draw graphics into an image.

[Compute passes](/documentation/Metal/compute-passes)

Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.

[Machine learning passes](/documentation/Metal/machine-learning-passes)

Add machine learning model inference to your Metal app’s GPU workflow.

[Blit passes](/documentation/Metal/blit-passes)

Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.

[Indirect command encoding](/documentation/Metal/indirect-command-encoding)

Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.

[Ray tracing with acceleration structures](/documentation/Metal/ray-tracing-with-acceleration-structures)

Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.

### Resources

Store data in buffers and textures, and optionally manage the underlying GPU memory yourself.

[Resource fundamentals](/documentation/Metal/resource-fundamentals)

Control the common attributes of all Metal memory resources, including buffers and textures,
and how to configure their underlying memory.

[Buffers](/documentation/Metal/buffers)

Create and manage untyped data your app uses to exchange information with its shader functions.

[Textures](/documentation/Metal/textures)

Create and manage typed data your app uses to exchange information with its shader functions.

[Memory heaps](/documentation/Metal/memory-heaps)

Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.

[Resource loading](/documentation/Metal/resource-loading)

Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.

[Resource synchronization](/documentation/Metal/resource-synchronization)

Prevent multiple commands that can access the same resources simultaneously by
coordinating those reads and writes with barriers, fences, or events.

### Shader compilation and libraries

Compile and organize shaders, the GPU functions that run on a Metal device’s execution units.

[Writing reusable GPU functions with generic pointers](/documentation/Metal/writing-reusable-gpu-functions-with-generic-pointers)

Define utility functions once for multiple address spaces, and share types with your app’s main code.

[Using the Metal 4 compilation API](/documentation/Metal/using-the-metal-4-compilation-api)

Control when and how you compile an app’s shaders.

[Shader libraries](/documentation/Metal/shader-libraries)

Manage and load your app’s Metal shaders.

[Using function specialization to build pipeline variants](/documentation/Metal/using-function-specialization-to-build-pipeline-variants)

Create pipelines for different levels of detail from a common shader source.

### Presentation

Display standard or high-dynamic-range content on a device’s display with
<doc://com.apple.documentation/documentation/QuartzCore> or
<doc://com.apple.documentation/documentation/MetalKit>, in standard or high dynamic range.

[Managing your game window for Metal in macOS](/documentation/Metal/managing-your-game-window-for-metal-in-macos)

Set up a window and view for optimally displaying your Metal content.

[Managing your Metal app window in iPadOS](/documentation/Metal/managing-your-metal-app-window-in-ipados)

Set up a window that handles dynamically resizing your Metal content.

[Adapting your game interface for smaller screens](/documentation/Metal/adapting-your-game-interface-for-smaller-screens)

Make text legible on all devices the player chooses to run your game on.

[Onscreen presentation](/documentation/Metal/onscreen-presentation)

Show the output from a GPU’s rendering pass to the user in your app.

[HDR content](/documentation/Metal/hdr-content)

Take advantage of high dynamic range to present more vibrant colors in your apps and games.

### Developer tools

Identify and fix issues with your app’s Metal API calls, shader code, resources, and performance during development by using Metal Debugger.

[Supporting Simulator in a Metal app](/documentation/Metal/supporting-simulator-in-a-metal-app)

Configure alternative render paths in your Metal app to enable running your app in Simulator.

[Capturing Metal commands programmatically](/documentation/Metal/capturing-metal-commands-programmatically)

Invoke a Metal frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.

[Logging shader debug messages](/documentation/Metal/logging-shader-debug-messages)

Print debugging messages that a shader generates using shader logging.

[Developing Metal apps that run in Simulator](/documentation/Metal/developing-metal-apps-that-run-in-simulator)

Prototype and test your Metal apps in Simulator.

[Improving your game’s graphics performance and settings](/documentation/Metal/improving-your-games-graphics-performance-and-settings)

Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.

  <doc://com.apple.documentation/documentation/Xcode/Metal-debugger>

  <doc://com.apple.documentation/documentation/Xcode/Metal-developer-workflows>

[GPU counters and counter sample buffers](/documentation/Metal/gpu-counters-and-counter-sample-buffers)

Retrieve runtime data from a GPU device by sampling one or more of its counters.

[Metal debugging types](/documentation/Metal/metal-debugging-types)

Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.

### Apple silicon

Take advantage of the unique architecture of Apple silicon GPUs.

  <doc://com.apple.documentation/documentation/Apple-Silicon/porting-your-metal-code-to-apple-silicon>

[Tailor your apps for Apple GPUs and tile-based deferred rendering](/documentation/Metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering)

Learn about characteristic Apple GPU features, including imageblocks, tile shaders, and raster order groups.

### Reference

[Metal structures](/documentation/Metal/metal-structures)

[Metal enumerations](/documentation/Metal/metal-enumerations)

[Metal constants](/documentation/Metal/metal-constants)

[Metal data types](/documentation/Metal/metal-data-types)

[Metal variables](/documentation/Metal/metal-variables)

### Reference

[Metal structures](/documentation/Metal/metal-structures)

[Metal enumerations](/documentation/Metal/metal-enumerations)

[Metal constants](/documentation/Metal/metal-constants)

[Metal functions](/documentation/Metal/metal-functions)

[Metal data types](/documentation/Metal/metal-data-types)

[Metal variables](/documentation/Metal/metal-variables)

[Metal macros](/documentation/Metal/metal-macros)

## See Also

  [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

  [Metal Best Practices Guide](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/index.html#//apple_ref/doc/uid/TP40016642)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
