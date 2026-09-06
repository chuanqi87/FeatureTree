# Document Type Definition

Document Type Definition (DTD) for the latest Final Cut Pro XML interchange format.

## Discussion

The following DTD applies to Final Cut Pro XML (FCPXML) Interchange Format 1.10. Find a downloadable version of the FCPXML DTD version 1.10 at the Final Cut Pro XML DTDs section on the [Final Cut Pro Support page](https://support.apple.com/final-cut-pro).

> Note:
> Even though an imported FCPXML document matches this DTD, import errors may still occur due to invalid data. If the document does not match the DTD, Final Cut Pro rejects the import operation completely.

```swift








<!ENTITY % time "CDATA">

<!ENTITY % collection_item "collection-folder | keyword-collection | smart-collection">

<!ENTITY % event_item "clip | audition | mc-clip | ref-clip | sync-clip | asset-clip | %collection_item; | project">


<!ELEMENT fcpxml (import-options?, resources?, (library | event* | (%event_item;)*))>
<!ATTLIST fcpxml version CDATA #FIXED "1.10">



<!ELEMENT import-options (option*)>

<!ELEMENT option EMPTY>
<!ATTLIST option key CDATA #REQUIRED>
<!ATTLIST option value CDATA #REQUIRED>


<!ELEMENT library (event | smart-collection)*>
<!ATTLIST library location CDATA #IMPLIED>
<!ATTLIST library colorProcessing (standard | wide | wide-hdr) #IMPLIED>


<!ELEMENT event (%event_item;)*>
<!ATTLIST event name CDATA #IMPLIED>
<!ATTLIST event uid CDATA #IMPLIED>


<!ELEMENT project (sequence)>
<!ATTLIST project name CDATA #IMPLIED>
<!ATTLIST project uid CDATA #IMPLIED>
<!ATTLIST project id ID #IMPLIED>
<!ATTLIST project modDate CDATA #IMPLIED>





<!ELEMENT resources (asset | effect | format | media | locator)*>




<!ELEMENT media (multicam | sequence)?>
<!ATTLIST media id ID #REQUIRED>
<!ATTLIST media name CDATA #IMPLIED>
<!ATTLIST media uid CDATA #IMPLIED>
<!ATTLIST media projectRef IDREF #IMPLIED>
<!ATTLIST media modDate CDATA #IMPLIED>


<!ELEMENT format EMPTY>
<!ATTLIST format id ID #REQUIRED>
<!ATTLIST format name CDATA #IMPLIED>
<!ATTLIST format frameDuration %time; #IMPLIED>
<!ATTLIST format fieldOrder CDATA #IMPLIED>
<!ATTLIST format width CDATA #IMPLIED>
<!ATTLIST format height CDATA #IMPLIED>
<!ATTLIST format paspH CDATA #IMPLIED>
<!ATTLIST format paspV CDATA #IMPLIED>
<!ATTLIST format colorSpace CDATA #IMPLIED>




<!ATTLIST format projection CDATA #IMPLIED>
<!ATTLIST format stereoscopic CDATA #IMPLIED>




<!ELEMENT asset (media-rep+, metadata?)>
<!ATTLIST asset id ID #REQUIRED>
<!ATTLIST asset name CDATA #IMPLIED>
<!ATTLIST asset uid CDATA #IMPLIED>
<!ATTLIST asset start %time; #IMPLIED>
<!ATTLIST asset duration %time; #IMPLIED>
<!ATTLIST asset hasVideo CDATA #IMPLIED>
<!ATTLIST asset format IDREF #IMPLIED>
<!ATTLIST asset hasAudio CDATA #IMPLIED>
<!ATTLIST asset videoSources CDATA #IMPLIED>
<!ATTLIST asset audioSources CDATA #IMPLIED>
<!ATTLIST asset audioChannels CDATA #IMPLIED>
<!ATTLIST asset audioRate CDATA #IMPLIED>
<!ATTLIST asset customLUTOverride CDATA #IMPLIED>




<!ATTLIST asset colorSpaceOverride CDATA #IMPLIED>


<!ATTLIST asset projectionOverride CDATA #IMPLIED>
<!ATTLIST asset stereoscopicOverride CDATA #IMPLIED>
<!ATTLIST asset auxVideoFlags CDATA #IMPLIED>

<!ELEMENT media-rep (bookmark?)>
<!ATTLIST media-rep kind (original-media | proxy-media) "original-media">
<!ATTLIST media-rep sig CDATA #IMPLIED>
<!ATTLIST media-rep src CDATA #REQUIRED>
<!ATTLIST media-rep suggestedFilename CDATA #IMPLIED>

<!ENTITY % md-type "( string | boolean | integer | float | date | timecode )">

<!ELEMENT metadata (md*)>

<!ELEMENT md (array?)>
<!ATTLIST md key CDATA #REQUIRED>
<!ATTLIST md value CDATA #IMPLIED>
<!ATTLIST md editable (0 | 1) "0">
<!ATTLIST md type %md-type; #IMPLIED>
<!ATTLIST md displayName CDATA #IMPLIED>
<!ATTLIST md description CDATA #IMPLIED>
<!ATTLIST md source CDATA #IMPLIED>


<!ELEMENT effect EMPTY>
<!ATTLIST effect id ID #REQUIRED>
<!ATTLIST effect name CDATA #IMPLIED>
<!ATTLIST effect uid CDATA #REQUIRED>
<!ATTLIST effect src CDATA #IMPLIED>

<!ELEMENT locator (bookmark?)>
<!ATTLIST locator id ID #REQUIRED>
<!ATTLIST locator url CDATA #REQUIRED>









<!ENTITY % ao_attrs "
lane CDATA #IMPLIED
offset %time; #IMPLIED
">




<!ENTITY % clip_attrs "
%ao_attrs;
name CDATA #IMPLIED
start %time; #IMPLIED
duration %time; #REQUIRED
enabled (0 | 1) '1'
">


<!ENTITY % clip_attrs_with_optional_duration "
%ao_attrs;
name CDATA #IMPLIED
start %time; #IMPLIED
duration %time; #IMPLIED
enabled (0 | 1) '1'
">

<!ENTITY % audioHz "( 32k | 44.1k | 48k | 88.2k | 96k | 176.4k | 192k )">





<!ENTITY % media_attrs "
format IDREF #REQUIRED
duration %time; #IMPLIED
tcStart %time; #IMPLIED
tcFormat (DF | NDF) #IMPLIED
">

<!ENTITY % fadeType "(linear | easeIn | easeOut | easeInOut)">


<!ELEMENT fadeIn EMPTY>
<!ATTLIST fadeIn type %fadeType; #IMPLIED>
<!ATTLIST fadeIn duration %time; #REQUIRED>


<!ELEMENT fadeOut EMPTY>
<!ATTLIST fadeOut type %fadeType; #IMPLIED>
<!ATTLIST fadeOut duration %time; #REQUIRED>


<!ELEMENT keyframeAnimation (keyframe*)>


<!ELEMENT keyframe EMPTY>
<!ATTLIST keyframe time %time; #REQUIRED>
<!ATTLIST keyframe value CDATA #REQUIRED>
<!ATTLIST keyframe interp (linear | ease | easeIn | easeOut) "linear"> 
<!ATTLIST keyframe curve (linear | smooth) "smooth"> 


<!ELEMENT mute (fadeIn?, fadeOut?)>
<!ATTLIST mute start %time; #IMPLIED>
<!ATTLIST mute duration %time; #IMPLIED>



<!ELEMENT param (fadeIn?, fadeOut?, keyframeAnimation?, param*)>
<!ATTLIST param name CDATA #REQUIRED>
<!ATTLIST param key CDATA #IMPLIED>

<!ATTLIST param value CDATA #IMPLIED>
<!ATTLIST param enabled (0 | 1) "1">


<!ELEMENT data (#PCDATA)>
<!ATTLIST data key CDATA #IMPLIED>


<!ELEMENT crop-rect (param*)>
<!ATTLIST crop-rect left CDATA "0">
<!ATTLIST crop-rect top CDATA "0">
<!ATTLIST crop-rect right CDATA "0">
<!ATTLIST crop-rect bottom CDATA "0">


<!ELEMENT trim-rect (param*)>
<!ATTLIST trim-rect left CDATA "0">
<!ATTLIST trim-rect top CDATA "0">
<!ATTLIST trim-rect right CDATA "0">
<!ATTLIST trim-rect bottom CDATA "0">



<!ELEMENT pan-rect EMPTY>
<!ATTLIST pan-rect left CDATA "0">
<!ATTLIST pan-rect top CDATA "0">
<!ATTLIST pan-rect right CDATA "0">
<!ATTLIST pan-rect bottom CDATA "0">







 
<!ELEMENT adjust-crop (crop-rect?, trim-rect?, (pan-rect, pan-rect)?)>
<!ATTLIST adjust-crop mode (trim | crop | pan) #REQUIRED>
<!ATTLIST adjust-crop enabled (0 | 1) "1">

<!ELEMENT adjust-corners (param*)>
<!ATTLIST adjust-corners enabled (0 | 1) "1">
<!ATTLIST adjust-corners botLeft CDATA "0 0">
<!ATTLIST adjust-corners topLeft CDATA "0 0">
<!ATTLIST adjust-corners topRight CDATA "0 0">
<!ATTLIST adjust-corners botRight CDATA "0 0">


<!ELEMENT adjust-conform EMPTY>
<!ATTLIST adjust-conform type (fit | fill | none) "fit">

<!ELEMENT adjust-transform (param*)>
<!ATTLIST adjust-transform enabled (0 | 1) "1">
<!ATTLIST adjust-transform position CDATA "0 0">
<!ATTLIST adjust-transform scale CDATA "1 1">
<!ATTLIST adjust-transform rotation CDATA "0">
<!ATTLIST adjust-transform anchor CDATA "0 0">
<!ATTLIST adjust-transform tracking IDREF #IMPLIED>

<!ELEMENT adjust-blend (param*, reserved?)>
<!ATTLIST adjust-blend amount CDATA "1.0">
<!ATTLIST adjust-blend mode CDATA #IMPLIED>

<!ELEMENT adjust-stabilization (param*)>
<!ATTLIST adjust-stabilization enabled (0 | 1) "1">
<!ATTLIST adjust-stabilization type (automatic | inertiaCam | smoothCam) "automatic">

<!ELEMENT adjust-rollingShutter EMPTY>
<!ATTLIST adjust-rollingShutter enabled (0 | 1) "1">
<!ATTLIST adjust-rollingShutter amount (none | low | medium | high | extraHigh) "none">

<!ELEMENT adjust-360-transform (param*)>
<!ATTLIST adjust-360-transform enabled (0 | 1) "1">
<!ATTLIST adjust-360-transform coordinates (spherical | cartesian) #REQUIRED>
<!ATTLIST adjust-360-transform latitude CDATA "0">
<!ATTLIST adjust-360-transform longitude CDATA "0">
<!ATTLIST adjust-360-transform distance CDATA #IMPLIED>
<!ATTLIST adjust-360-transform xPosition CDATA "0">
<!ATTLIST adjust-360-transform yPosition CDATA "0">
<!ATTLIST adjust-360-transform zPosition CDATA #IMPLIED>
<!ATTLIST adjust-360-transform xOrientation CDATA "0">
<!ATTLIST adjust-360-transform yOrientation CDATA "0">
<!ATTLIST adjust-360-transform zOrientation CDATA "0">
<!ATTLIST adjust-360-transform autoOrient (0 | 1) "1">
<!ATTLIST adjust-360-transform convergence CDATA "0">
<!ATTLIST adjust-360-transform interaxial CDATA #IMPLIED>
<!ATTLIST adjust-360-transform scale CDATA "1 1">

<!ELEMENT adjust-reorient (param*)>
<!ATTLIST adjust-reorient enabled (0 | 1) "1">
<!ATTLIST adjust-reorient tilt CDATA "0">
<!ATTLIST adjust-reorient pan CDATA "0">
<!ATTLIST adjust-reorient roll CDATA "0">
<!ATTLIST adjust-reorient convergence CDATA "0">

<!ELEMENT adjust-orientation (param*)>
<!ATTLIST adjust-orientation enabled (0 | 1) "1">
<!ATTLIST adjust-orientation tilt CDATA "0">
<!ATTLIST adjust-orientation pan CDATA "0">
<!ATTLIST adjust-orientation roll CDATA "0">
<!ATTLIST adjust-orientation fieldOfView CDATA #IMPLIED>
<!ATTLIST adjust-orientation mapping (normal | tinyPlanet) "normal">

<!ELEMENT adjust-cinematic (param*)>
<!ATTLIST adjust-cinematic enabled (0 | 1) "1">
<!ATTLIST adjust-cinematic dataLocator IDREF #IMPLIED>
<!ATTLIST adjust-cinematic aperture CDATA #IMPLIED>

<!ELEMENT adjust-loudness EMPTY>
<!ATTLIST adjust-loudness amount CDATA #REQUIRED>
<!ATTLIST adjust-loudness uniformity CDATA #REQUIRED>

<!ELEMENT adjust-noiseReduction EMPTY>
<!ATTLIST adjust-noiseReduction amount CDATA #REQUIRED>

<!ELEMENT adjust-humReduction EMPTY>
<!ATTLIST adjust-humReduction frequency (50 | 60) #REQUIRED>

<!ELEMENT adjust-EQ (param*)>
<!ATTLIST adjust-EQ mode (flat | voice_enhance | music_enhance | loudness | hum_reduction | bass_boost | bass_reduce | treble_boost | treble_reduce) #REQUIRED>

<!ELEMENT adjust-matchEQ (data)>


<!ENTITY % adjust-audio-enhancements "(adjust-loudness?, adjust-noiseReduction?, adjust-humReduction?, (adjust-EQ | adjust-matchEQ)?)">

<!ELEMENT adjust-volume (param*)>
<!ATTLIST adjust-volume amount CDATA "0dB">

<!ELEMENT adjust-panner (param*)>
<!ATTLIST adjust-panner mode CDATA #IMPLIED>
<!ATTLIST adjust-panner amount CDATA "0">
<!ATTLIST adjust-panner original_decoded_mix CDATA #IMPLIED>
<!ATTLIST adjust-panner ambient_direct_mix CDATA #IMPLIED>
<!ATTLIST adjust-panner surround_width CDATA #IMPLIED>
<!ATTLIST adjust-panner left_right_mix CDATA #IMPLIED> 
<!ATTLIST adjust-panner front_back_mix CDATA #IMPLIED> 
<!ATTLIST adjust-panner LFE_balance CDATA #IMPLIED>
<!ATTLIST adjust-panner rotation CDATA #IMPLIED>
<!ATTLIST adjust-panner stereo_spread CDATA #IMPLIED>
<!ATTLIST adjust-panner attenuate_collapse_mix CDATA #IMPLIED>
<!ATTLIST adjust-panner center_balance CDATA #IMPLIED>

<!ELEMENT tracking-shape EMPTY>
<!ATTLIST tracking-shape id ID #REQUIRED>
<!ATTLIST tracking-shape name CDATA #IMPLIED>
<!ATTLIST tracking-shape offsetEnabled (0 | 1) "0">
<!ATTLIST tracking-shape analysisMethod (automatic | combined | machineLearning | pointCloud) "automatic">
<!ATTLIST tracking-shape dataLocator IDREF #IMPLIED>

<!ELEMENT object-tracker (tracking-shape+)>


<!ENTITY % intrinsic-params-video "(object-tracker?, adjust-crop?, adjust-corners?, adjust-conform?, adjust-transform?, adjust-blend?, adjust-stabilization?, adjust-rollingShutter?, adjust-360-transform?, adjust-reorient?, adjust-orientation?, adjust-cinematic?)">
<!ENTITY % intrinsic-params-audio "(adjust-volume?, adjust-panner?)">
<!ENTITY % intrinsic-params "(%intrinsic-params-video;, %intrinsic-params-audio;)">


<!ENTITY % timing-params "(conform-rate?, timeMap?)">



<!ENTITY % anchor_item "audio | video | clip | title | caption | mc-clip | ref-clip | sync-clip | asset-clip | audition | spine">


<!ENTITY % clip_item "audio | video | clip | title | mc-clip | ref-clip | sync-clip | asset-clip | audition | gap">

<!ENTITY % marker_item "(marker | chapter-marker | rating | keyword | analysis-marker)">

<!ENTITY % video_filter_item "(filter-video | filter-video-mask)">



<!ELEMENT audio-channel-source (%adjust-audio-enhancements;, %intrinsic-params-audio;, filter-audio*, mute*)>
<!ATTLIST audio-channel-source srcCh CDATA #REQUIRED>
<!ATTLIST audio-channel-source outCh CDATA #IMPLIED>
<!ATTLIST audio-channel-source role CDATA #IMPLIED>
<!ATTLIST audio-channel-source start %time; #IMPLIED>
<!ATTLIST audio-channel-source duration %time; #IMPLIED>
<!ATTLIST audio-channel-source enabled (0 | 1) '1'>
<!ATTLIST audio-channel-source active (0 | 1) '1'>


<!ELEMENT audio-role-source (%adjust-audio-enhancements;, %intrinsic-params-audio;, filter-audio*, mute*)>
<!ATTLIST audio-role-source role CDATA #REQUIRED>
<!ATTLIST audio-role-source start %time; #IMPLIED>
<!ATTLIST audio-role-source duration %time; #IMPLIED>
<!ATTLIST audio-role-source enabled (0 | 1) '1'>
<!ATTLIST audio-role-source active (0 | 1) '1'>


<!ELEMENT audition (audio | video | title | ref-clip | asset-clip | clip | sync-clip)+ >
<!ATTLIST audition %ao_attrs;>
<!ATTLIST audition modDate CDATA #IMPLIED>



<!ELEMENT spine (%clip_item; | transition)* >
<!ATTLIST spine%ao_attrs;>
<!ATTLIST spine name CDATA #IMPLIED>
<!ATTLIST spine format IDREF #IMPLIED>


<!ELEMENT sequence (note?, spine, metadata?)>
<!ATTLIST sequence %media_attrs;>
<!ATTLIST sequence audioLayout (mono | stereo | surround) #IMPLIED>
<!ATTLIST sequence audioRate %audioHz; #IMPLIED>
<!ATTLIST sequence renderFormat CDATA #IMPLIED>
<!ATTLIST sequence keywords CDATA #IMPLIED>


<!ELEMENT multicam (mc-angle*, metadata?)>
<!ATTLIST multicam %media_attrs;>
<!ATTLIST multicam renderFormat CDATA #IMPLIED>



<!ELEMENT mc-angle ((%clip_item; | transition)*) >
<!ATTLIST mc-angle name CDATA #IMPLIED>
<!ATTLIST mc-angle angleID CDATA #REQUIRED>


<!ELEMENT mc-clip (note?, %timing-params;, %intrinsic-params-audio;, mc-source*, (%anchor_item;)*, (%marker_item;)*, filter-audio*, metadata?)>
<!ATTLIST mc-clip ref IDREF #REQUIRED>
<!ATTLIST mc-clip %clip_attrs;>
<!ATTLIST mc-clip srcEnable (all | audio | video) "all">
<!ATTLIST mc-clip audioStart %time; #IMPLIED>
<!ATTLIST mc-clip audioDuration %time; #IMPLIED>
<!ATTLIST mc-clip modDate CDATA #IMPLIED>


<!ELEMENT mc-source (audio-role-source*, %intrinsic-params-video;, (%video_filter_item;)*)>
<!ATTLIST mc-source angleID CDATA #REQUIRED>
<!ATTLIST mc-source srcEnable (all | audio | video | none) "all">




<!ELEMENT clip (note?, %timing-params;, %intrinsic-params;, (spine | (%clip_item;) | caption)*, (%marker_item;)*, audio-channel-source*, (%video_filter_item;)*, filter-audio*, metadata?)>
<!ATTLIST clip %clip_attrs;>
<!ATTLIST clip format IDREF #IMPLIED>
<!ATTLIST clip audioStart %time; #IMPLIED>
<!ATTLIST clip audioDuration %time; #IMPLIED>
<!ATTLIST clip tcStart %time; #IMPLIED>
<!ATTLIST clip tcFormat (DF | NDF) #IMPLIED>
<!ATTLIST clip modDate CDATA #IMPLIED>




<!ELEMENT ref-clip (note?, %timing-params;, %intrinsic-params;, (%anchor_item;)*, (%marker_item;)*, audio-role-source*, (%video_filter_item;)*, filter-audio*, metadata?)>
<!ATTLIST ref-clip ref IDREF #REQUIRED>
<!ATTLIST ref-clip %clip_attrs;>
<!ATTLIST ref-clip srcEnable (all | audio | video) "all">
<!ATTLIST ref-clip audioStart %time; #IMPLIED>
<!ATTLIST ref-clip audioDuration %time; #IMPLIED>
<!ATTLIST ref-clip useAudioSubroles (0 | 1) '0'>
<!ATTLIST ref-clip modDate CDATA #IMPLIED>



<!ELEMENT sync-clip (note?, %timing-params;, %intrinsic-params;, (spine | (%clip_item;) | caption)*, (%marker_item;)*, sync-source*, (%video_filter_item;)*, filter-audio*, metadata?)>
<!ATTLIST sync-clip %clip_attrs;>
<!ATTLIST sync-clip format IDREF #IMPLIED>
<!ATTLIST sync-clip audioStart %time; #IMPLIED>
<!ATTLIST sync-clip audioDuration %time; #IMPLIED>
<!ATTLIST sync-clip tcStart %time; #IMPLIED>
<!ATTLIST sync-clip tcFormat (DF | NDF) #IMPLIED>
<!ATTLIST sync-clip modDate CDATA #IMPLIED>


<!ELEMENT sync-source (audio-role-source*)>
<!ATTLIST sync-source sourceID (storyline | connected) #REQUIRED>





<!ELEMENT asset-clip (note?, %timing-params;, %intrinsic-params;, (%anchor_item;)*, (%marker_item;)*, audio-channel-source*, (%video_filter_item;)*, filter-audio*, metadata?)>
<!ATTLIST asset-clip ref IDREF #REQUIRED>
<!ATTLIST asset-clip %clip_attrs_with_optional_duration;>
<!ATTLIST asset-clip srcEnable (all | audio | video) "all">
<!ATTLIST asset-clip audioStart %time; #IMPLIED>
<!ATTLIST asset-clip audioDuration %time; #IMPLIED>
<!ATTLIST asset-clip format IDREF #IMPLIED>
<!ATTLIST asset-clip tcStart %time; #IMPLIED>
<!ATTLIST asset-clip tcFormat (DF | NDF) #IMPLIED>
<!ATTLIST asset-clip modDate CDATA #IMPLIED>
<!ATTLIST asset-clip audioRole CDATA #IMPLIED>
<!ATTLIST asset-clip videoRole CDATA #IMPLIED>


<!ELEMENT audio (note?, %timing-params;, adjust-volume?, (%anchor_item;)*, (%marker_item;)*, filter-audio*)>
<!ATTLIST audio ref IDREF #REQUIRED>
<!ATTLIST audio %clip_attrs;>
<!ATTLIST audio srcID CDATA #IMPLIED>
<!ATTLIST audio role CDATA #IMPLIED>
<!ATTLIST audio srcCh CDATA #IMPLIED>
<!ATTLIST audio outCh CDATA #IMPLIED>


<!ELEMENT video (param*, note?, %timing-params;, %intrinsic-params-video;, (%anchor_item;)*, (%marker_item;)*, (%video_filter_item;)*, reserved?)>
<!ATTLIST video ref IDREF #REQUIRED>
<!ATTLIST video %clip_attrs;>
<!ATTLIST video srcID CDATA #IMPLIED>
<!ATTLIST video role CDATA #IMPLIED>


<!ELEMENT caption (text*, text-style-def*, note?)>
<!ATTLIST caption %clip_attrs;>
<!ATTLIST caption role CDATA #IMPLIED>



<!ELEMENT gap (note?, (%anchor_item;)*, (%marker_item;)*, metadata?)>
<!ATTLIST gap name CDATA #IMPLIED>
<!ATTLIST gap offset %time; #IMPLIED>
<!ATTLIST gap start %time; #IMPLIED>
<!ATTLIST gap duration %time; #REQUIRED>
<!ATTLIST gap enabled (0 | 1) "1">


<!ELEMENT title (param*, text*, text-style-def*, note?, %intrinsic-params-video;, (%anchor_item;)*, (%marker_item;)*, (%video_filter_item;)*, metadata?)>
<!ATTLIST title ref IDREF #REQUIRED>
<!ATTLIST title %clip_attrs;>
<!ATTLIST title role CDATA #IMPLIED>


<!ELEMENT text (#PCDATA | text-style)*>

<!ATTLIST text display-style (pop-on | paint-on | roll-up) #IMPLIED>
<!ATTLIST text roll-up-height CDATA #IMPLIED>
<!ATTLIST text position CDATA #IMPLIED>
<!ATTLIST text placement (left | right | top | bottom) #IMPLIED>
<!ATTLIST text alignment (left | center | right ) #IMPLIED>

<!ELEMENT text-style-def (text-style)>
<!ATTLIST text-style-def id ID #REQUIRED>
<!ATTLIST text-style-def name CDATA #IMPLIED>


<!ELEMENT text-style (#PCDATA | param)*>
<!ATTLIST text-style ref IDREF #IMPLIED>
<!ATTLIST text-style font CDATA #IMPLIED>
<!ATTLIST text-style fontSize CDATA #IMPLIED>
<!ATTLIST text-style fontFace CDATA #IMPLIED>
<!ATTLIST text-style fontColor CDATA #IMPLIED>
<!ATTLIST text-style backgroundColor CDATA #IMPLIED>
<!ATTLIST text-style bold (0 | 1) #IMPLIED>
<!ATTLIST text-style italic (0 | 1) #IMPLIED>
<!ATTLIST text-style strokeColor CDATA #IMPLIED>
<!ATTLIST text-style strokeWidth CDATA #IMPLIED>
<!ATTLIST text-style baseline CDATA #IMPLIED>
<!ATTLIST text-style shadowColor CDATA #IMPLIED>
<!ATTLIST text-style shadowOffset CDATA #IMPLIED>
<!ATTLIST text-style shadowBlurRadius CDATA #IMPLIED>
<!ATTLIST text-style kerning CDATA #IMPLIED>
<!ATTLIST text-style alignment (left | center | right | justified) #IMPLIED>
<!ATTLIST text-style lineSpacing CDATA #IMPLIED>
<!ATTLIST text-style tabStops CDATA #IMPLIED>
<!ATTLIST text-style baselineOffset CDATA #IMPLIED>
<!ATTLIST text-style underline (0 | 1) #IMPLIED>



<!ELEMENT transition (filter-video?, filter-audio?, (%marker_item;)*, metadata?, reserved?)>
<!ATTLIST transition name CDATA #IMPLIED>
<!ATTLIST transition offset %time; #IMPLIED>
<!ATTLIST transition duration %time; #REQUIRED>





<!ELEMENT filter-video (data*, param*)>
<!ATTLIST filter-video ref IDREF #REQUIRED>
<!ATTLIST filter-video name CDATA #IMPLIED>
<!ATTLIST filter-video enabled (0 | 1) "1">

<!ENTITY % mask_item "(mask-shape | mask-isolation)">






<!ELEMENT filter-video-mask ((%mask_item;)+, (filter-video, filter-video?))>
<!ATTLIST filter-video-mask enabled (0 | 1) "1">
<!ATTLIST filter-video-mask inverted (0 | 1) "0">


<!ELEMENT mask-shape (param*)>
<!ATTLIST mask-shape name CDATA #IMPLIED>
<!ATTLIST mask-shape enabled (0 | 1) "1">
<!ATTLIST mask-shape blendMode (add | subtract | multiply) "add">
<!ATTLIST mask-shape tracking IDREF #IMPLIED>


<!ELEMENT mask-isolation (data, param*)>
<!ATTLIST mask-isolation name CDATA #IMPLIED>
<!ATTLIST mask-isolation enabled (0 | 1) "1">
<!ATTLIST mask-isolation blendMode (add | subtract | multiply) "multiply">
<!ATTLIST mask-isolation type (3D | HSL) "3D">



<!ELEMENT filter-audio (data?, param*)>
<!ATTLIST filter-audio ref IDREF #REQUIRED>
<!ATTLIST filter-audio name CDATA #IMPLIED>
<!ATTLIST filter-audio enabled (0 | 1) "1">
<!ATTLIST filter-audio presetID CDATA #IMPLIED>


<!ELEMENT conform-rate EMPTY>
<!ATTLIST conform-rate scaleEnabled (0 | 1) "1">
<!ATTLIST conform-rate srcFrameRate (23.98 | 24 | 25 | 29.97 | 30 | 60 | 47.95 | 48 | 50 | 59.94) #IMPLIED>
<!ATTLIST conform-rate frameSampling (floor | nearest-neighbor | frame-blending | optical-flow-classic | optical-flow) "floor">




<!ELEMENT timeMap (timept)*>
<!ATTLIST timeMap frameSampling (floor | nearest-neighbor | frame-blending | optical-flow-classic | optical-flow) "floor">
<!ATTLIST timeMap preservesPitch (0 | 1) "1">


<!ELEMENT timept EMPTY>
<!ATTLIST timept time %time; #REQUIRED>
<!ATTLIST timept value CDATA #REQUIRED>
<!ATTLIST timept interp (smooth2 | linear | smooth) "smooth2"> 
<!ATTLIST timept inTime %time; #IMPLIED>
<!ATTLIST timept outTime %time; #IMPLIED>




<!ELEMENT marker EMPTY>
<!ATTLIST marker start %time; #REQUIRED>
<!ATTLIST marker duration %time; #IMPLIED>
<!ATTLIST marker value CDATA #REQUIRED>
<!ATTLIST marker completed CDATA #IMPLIED>
<!ATTLIST marker note CDATA #IMPLIED>

<!ELEMENT rating EMPTY>
<!ATTLIST rating name CDATA #IMPLIED>
<!ATTLIST rating start %time; #IMPLIED>
<!ATTLIST rating duration %time; #IMPLIED>
<!ATTLIST rating value (favorite | reject) #REQUIRED>
<!ATTLIST rating note CDATA #IMPLIED>

<!ELEMENT keyword EMPTY>
<!ATTLIST keyword start %time; #IMPLIED>
<!ATTLIST keyword duration %time; #IMPLIED>
<!ATTLIST keyword value CDATA #REQUIRED>
<!ATTLIST keyword note CDATA #IMPLIED>

<!ELEMENT analysis-marker (shot-type | stabilization-type)+>
<!ATTLIST analysis-marker start %time; #IMPLIED>
<!ATTLIST analysis-marker duration %time; #IMPLIED>

<!ELEMENT keyword-collection EMPTY>
<!ATTLIST keyword-collection name CDATA #REQUIRED>

<!ELEMENT collection-folder (%collection_item;)*>
<!ATTLIST collection-folder name CDATA #REQUIRED>


<!ELEMENT smart-collection ((match-text | match-ratings | match-media | match-clip | match-stabilization | match-keywords | match-shot | match-property | match-time | match-timeRange | match-roles | match-usage | match-representation | match-markers)*)>
<!ATTLIST smart-collection name CDATA #REQUIRED>
<!ATTLIST smart-collection match (any | all) #REQUIRED>

<!ELEMENT match-text EMPTY>
<!ATTLIST match-text enabled (0 | 1) "1">
<!ATTLIST match-text rule (includes | doesNotInclude | is | isNot) "includes">
<!ATTLIST match-text value CDATA #REQUIRED>
<!ATTLIST match-text scope (all | notes | names | markers) "all">

<!ELEMENT match-ratings EMPTY>
<!ATTLIST match-ratings enabled (0 | 1) "1">
<!ATTLIST match-ratings value (favorites | rejected) #REQUIRED>

<!ELEMENT match-media EMPTY>
<!ATTLIST match-media enabled (0 | 1) "1">
<!ATTLIST match-media rule (is | isNot) "is">
<!ATTLIST match-media type (videoWithAudio | videoOnly | audioOnly | stills) #REQUIRED>

<!ELEMENT match-clip EMPTY>
<!ATTLIST match-clip enabled (0 | 1) "1">
<!ATTLIST match-clip rule (is | isNot) "is">
<!ATTLIST match-clip type (audition | synchronized | compound | multicam | layeredGraphic | project) #REQUIRED>

<!ELEMENT match-stabilization (stabilization-type*)>
<!ATTLIST match-stabilization enabled (0 | 1) "1">
<!ATTLIST match-stabilization rule (includesAny | includesAll | doesNotIncludeAny | doesNotIncludeAll) "includesAny">

<!ELEMENT match-keywords (keyword-name*)>
<!ATTLIST match-keywords enabled (0 | 1) "1">
<!ATTLIST match-keywords rule (includesAny | includesAll | doesNotIncludeAny | doesNotIncludeAll) "includesAny">

<!ELEMENT keyword-name EMPTY>
<!ATTLIST keyword-name value CDATA #REQUIRED>

<!ELEMENT match-shot (shot-type*)>
<!ATTLIST match-shot enabled (0 | 1) "1">
<!ATTLIST match-shot rule (includesAny | includesAll | doesNotIncludeAny | doesNotIncludeAll) "includesAny">

<!ELEMENT shot-type EMPTY>
<!ATTLIST shot-type value (onePerson | twoPersons | group | closeUp | mediumShot | wideShot) #REQUIRED>

<!ELEMENT stabilization-type EMPTY>
<!ATTLIST stabilization-type value (excessiveShake) #REQUIRED>

<!ELEMENT match-property EMPTY>
<!ATTLIST match-property enabled (0 | 1) "1">
<!ATTLIST match-property key (reel | scene | take | audioOutputChannels | frameSize | videoFrameRate | audioSampleRate | cameraName | cameraAngle | projection | stereoscopic | cinematic) #REQUIRED>
<!ATTLIST match-property rule (includes | doesNotInclude | is | isNot | isSet | isNotSet) "includes">
<!ATTLIST match-property value CDATA #IMPLIED>



<!ELEMENT match-time EMPTY>
<!ATTLIST match-time enabled (0 | 1) "1">
<!ATTLIST match-time type (contentCreated | dateImported) #REQUIRED>
<!ATTLIST match-time rule (is | isBefore | isAfter) #REQUIRED>
<!ATTLIST match-time value CDATA #REQUIRED>

<!ELEMENT match-timeRange EMPTY>
<!ATTLIST match-timeRange enabled (0 | 1) "1">
<!ATTLIST match-timeRange type (contentCreated | dateImported) #REQUIRED>
<!ATTLIST match-timeRange rule (isInLast | isNotInLast) #REQUIRED>
<!ATTLIST match-timeRange value CDATA #REQUIRED>
<!ATTLIST match-timeRange units (hour | day | week | month | year) #IMPLIED>

<!ELEMENT match-roles (role*)>
<!ATTLIST match-roles enabled (0 | 1) "1">
<!ATTLIST match-roles rule (includesAny | includesAll | doesNotIncludeAny | doesNotIncludeAll) "includesAny">

<!ELEMENT role EMPTY>
<!ATTLIST role name CDATA #REQUIRED>

<!ELEMENT match-usage EMPTY>
<!ATTLIST match-usage enabled (0 | 1) "1">
<!ATTLIST match-usage rule (used | unused) "used">

<!ELEMENT match-representation EMPTY>
<!ATTLIST match-representation enabled (0 | 1) "1">
<!ATTLIST match-representation type (original | optimized | proxy) #REQUIRED>
<!ATTLIST match-representation rule (isAvailable | isMissing) "isAvailable">

<!ELEMENT match-markers EMPTY>
<!ATTLIST match-markers enabled (0 | 1) "1">
<!ATTLIST match-markers type (all | standard | allTodo | complete | incomplete) "all">

<!ELEMENT chapter-marker EMPTY>
<!ATTLIST chapter-marker start %time; #REQUIRED>
<!ATTLIST chapter-marker duration %time; #IMPLIED>
<!ATTLIST chapter-marker value CDATA #REQUIRED>
<!ATTLIST chapter-marker note CDATA #IMPLIED>
<!ATTLIST chapter-marker posterOffset %time; #IMPLIED>

<!ELEMENT note (#PCDATA)>

<!ELEMENT bookmark (#PCDATA)>
<!ELEMENT reserved (#PCDATA)>

<!ELEMENT array (string*)>
<!ELEMENT string (#PCDATA)>
```

### Legacy FCPXML DTDs

For earlier versions (v1.5 - v1.9) of the FCPXML DTDs, see Final Cut Pro XML DTDs section on the [Final Cut Pro Support page](https://support.apple.com/final-cut-pro).

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
