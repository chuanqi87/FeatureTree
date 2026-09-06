# Metal sample code library

Explore the complete set of Metal samples.

## Discussion

Browse the topics below to find samples relevant to a concept you want to learn more about, starting with the basic computation and render workflows. The samples in the lighting and multiple technique sections demonstrate how to take advantage of the unique GPU architecture of Apple silicon.

## Topics

### Compute workflows

[Performing calculations on a GPU](/documentation/Metal/performing-calculations-on-a-gpu)

Use Metal to find GPUs and perform calculations on them.

[Selecting device objects for compute processing](/documentation/Metal/selecting-device-objects-for-compute-processing)

Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.

[Customizing a TensorFlow operation](/documentation/Metal/customizing-a-tensorflow-operation)

Implement a custom operation that uses Metal kernels to accelerate neural-network training performance.

[Customizing a PyTorch operation](/documentation/Metal/customizing-a-pytorch-operation)

Implement a custom operation in PyTorch that uses Metal kernels to improve performance.

### Machine learning workflows

[Running a machine learning model on the GPU timeline](/documentation/Metal/running-a-machine-learning-model-on-the-gpu-timeline)

Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.

[Training a neural network to render irradiance in real time](/documentation/Metal/training-a-neural-network-to-render-irradiance-in-real-time)

Train a small neural network on the GPU to approximate diffuse irradiance, and compare the result against Monte Carlo integration and a pre-trained ML model.

[Running inline ML operations in a shader with Metal 4](/documentation/Metal/running-inline-ml-operations-in-a-shader-with-metal-4)

Multiply matrices across multiple GPU cores with inline tensor operations.

### Render workflows

[Using Metal to draw a view’s contents](/documentation/Metal/using-metal-to-draw-a-view's-contents)

Create a MetalKit view and a render pass to draw the view’s contents.

[Drawing a triangle with Metal 4](/documentation/Metal/drawing-a-triangle-with-metal-4)

Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.

[Selecting device objects for graphics rendering](/documentation/Metal/selecting-device-objects-for-graphics-rendering)

Switch dynamically between multiple GPUs to efficiently render to a display.

[Customizing render pass setup](/documentation/Metal/customizing-render-pass-setup)

Render into an offscreen texture by creating a custom render pass.

[Creating a custom Metal view](/documentation/Metal/creating-a-custom-metal-view)

Implement a lightweight view for Metal rendering that’s customized to your app’s needs.

[Calculating primitive visibility using depth testing](/documentation/Metal/calculating-primitive-visibility-using-depth-testing)

Determine which pixels are visible in a scene by using a depth texture.

[Encoding indirect command buffers on the CPU](/documentation/Metal/encoding-indirect-command-buffers-on-the-cpu)

Reduce CPU overhead and simplify your command execution by reusing commands.

[Implementing order-independent transparency with image blocks](/documentation/Metal/implementing-order-independent-transparency-with-image-blocks)

Draw overlapping, transparent surfaces in any order by using tile shaders and image blocks.

[Loading textures and models using Metal fast resource loading](/documentation/Metal/loading-textures-and-models-using-metal-fast-resource-loading)

Stream texture and buffer data directly from disk into Metal resources using fast resource loading.

[Adjusting the level of detail using Metal mesh shaders](/documentation/Metal/adjusting-the-level-of-detail-using-metal-mesh-shaders)

Choose and render meshes with several levels of detail using object and mesh shaders.

[Creating a 3D application with hydra rendering](/documentation/Metal/creating-a-3d-application-with-hydra-rendering)

Build a 3D application that integrates with Hydra and USD.

[Culling occluded geometry using the visibility result buffer](/documentation/Metal/culling-occluded-geometry-using-the-visibility-result-buffer)

Draw a scene without rendering hidden geometry by checking whether each object in the scene is visible.

[Improving edge-rendering quality with multisample antialiasing (MSAA)](/documentation/Metal/improving-edge-rendering-quality-with-multisample-antialiasing-msaa)

Apply MSAA to enhance the rendering of edges with custom resolve options and immediate and tile-based resolve paths.

[Achieving smooth frame rates with a Metal display link](/documentation/Metal/achieving-smooth-frame-rates-with-a-metal-display-link)

Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.

### Textures

[Combining blit and compute operations in a single pass](/documentation/Metal/combining-blit-and-compute-operations-in-a-single-pass)

Run concurrent blit commands and then a compute dispatch in a single pass with a unified compute encoder.

[Reading pixel data from a drawable texture](/documentation/Metal/reading-pixel-data-from-a-drawable-texture)

Access texture data from the CPU by copying it to a buffer.

[Creating and sampling textures](/documentation/Metal/creating-and-sampling-textures)

Load image data into a texture and apply it to a quadrangle.

[Streaming large images with Metal sparse textures](/documentation/Metal/streaming-large-images-with-metal-sparse-textures)

Limit texture memory usage for large textures by loading or unloading image detail on the basis of MIP and tile region.

### Argument buffers

[Managing groups of resources with argument buffers](/documentation/Metal/managing-groups-of-resources-with-argument-buffers)

Create argument buffers to organize related resources.

[Using argument buffers with resource heaps](/documentation/Metal/using-argument-buffers-with-resource-heaps)

Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.

[Encoding argument buffers on the GPU](/documentation/Metal/encoding-argument-buffers-on-the-gpu)

Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.

[Rendering terrain dynamically with argument buffers](/documentation/Metal/rendering-terrain-dynamically-with-argument-buffers)

Use argument buffers to render terrain in real time with a GPU-driven pipeline.

### Shaders

[Creating a Metal dynamic library](/documentation/Metal/creating-a-metal-dynamic-library)

Compile a library of shaders and write it to a file as a dynamically linked library.

[Using function specialization to build pipeline variants](/documentation/Metal/using-function-specialization-to-build-pipeline-variants)

Create pipelines for different levels of detail from a common shader source.

### Synchronization

[Synchronizing CPU and GPU work](/documentation/Metal/synchronizing-cpu-and-gpu-work)

Avoid stalls between CPU and GPU work by using multiple instances of a resource.

[Implementing a multistage image filter using heaps and events](/documentation/Metal/implementing-a-multistage-image-filter-using-heaps-and-events)

Use events to synchronize access to resources allocated on a heap.

[Implementing a multistage image filter using heaps and fences](/documentation/Metal/implementing-a-multistage-image-filter-using-heaps-and-fences)

Use fences to synchronize access to resources allocated on a heap.

### Lighting techniques

[Rendering a scene with forward plus lighting using tile shaders](/documentation/Metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders)

Implement a forward plus renderer using the latest features on Apple GPUs.

[Rendering a scene with deferred lighting in Objective-C](/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-objective-c)

Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.

[Rendering a scene with deferred lighting in Swift](/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift)

Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.

[Rendering a scene with deferred lighting in C++](/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-c++)

Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.

[Rendering reflections with fewer render passes](/documentation/Metal/rendering-reflections-with-fewer-render-passes)

Use layer selection to reduce the number of render passes needed to generate an environment map.

### Multiple techniques

[Modern rendering with Metal](/documentation/Metal/modern-rendering-with-metal)

Use advanced Metal features such as indirect command buffers, sparse textures, and variable rate rasterization to implement complex rendering techniques.

[Encoding indirect command buffers on the GPU](/documentation/Metal/encoding-indirect-command-buffers-on-the-gpu)

Maximize CPU to GPU parallelization by generating render commands on the GPU.

### Ray tracing

[Rendering reflections in real time using ray tracing](/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing)

Implement realistic real-time lighting by dynamically generating reflection maps
by encoding a ray-tracing compute pass.

[Accelerating ray tracing using Metal](/documentation/Metal/accelerating-ray-tracing-using-metal)

Implement ray-traced rendering using GPU-based parallel processing.

[Control the ray tracing process using intersection queries](/documentation/Metal/control-the-ray-tracing-process-using-intersection-queries)

Explicitly enumerate a ray’s intersections with acceleration structures by creating an intersection query object.

[Accelerating ray tracing and motion blur using Metal](/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal)

Generate ray-traced images with motion blur using GPU-based parallel processing.

[Rendering a curve primitive in a ray tracing scene](/documentation/Metal/rendering-a-curve-primitive-in-a-ray-tracing-scene)

Implement ray traced rendering using GPU-based parallel processing.

### HDR

[Processing HDR images with Metal](/documentation/Metal/processing-hdr-images-with-metal)

Implement a post-processing pipeline using the latest features on Apple GPUs.

### OpenGL

[Migrating OpenGL code to Metal](/documentation/Metal/migrating-opengl-code-to-metal)

Replace your app’s deprecated OpenGL code with Metal.

[Mixing Metal and OpenGL rendering in a view](/documentation/Metal/mixing-metal-and-opengl-rendering-in-a-view)

Draw with Metal and OpenGL in the same view using an interoperable texture.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
