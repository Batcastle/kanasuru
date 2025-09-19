# KanaSuru (かなする)
Kanasuru is a Japanese learning app for Linux. It leverages touchscreen tech and GTK3+ to help users learn Kana and practice stroke order.

## How does KanaSuru know when strokes are correct?
KanaSuru interally uses a layer system:

### Layer 1: The work layer
This layer is the layer the user draws onto. By default, it is transparent, except for the markings made by the user.

### Layer 2: The refrence layer
This layer displays a PNG, SVG, or WEBM image with a transparent background of the image the user is to trace

### Layer 3: The background layer
This layer is the background, a procedurally generated image stored in memory.

### The process
When a user draws out hiragana, etc. They will be tracing an image. Depending on the difficulty, that image may or may not be visible. The image of the character, the background, and the "ink" the user uses are all three different colors.

To confirm the user didn't miss any strokes, we can compare the number of pixels on screen that are the color of the refrence layer vs the work layer. If we can see a certain amount of the rerence layer, the user may have missed a stroke. This can be improved, to catch small strokes, by splitting the layers into sections.

To confirm the user didn't add strokes, we can compare the amount of the background that is covered by the reference image vs how much of the background is covered by the user's work. Further, we can also tell their accuracy by comparing how much of the refrence image is visible behind the user's work. These three numbers make up our confidence scores. Ideally, the refrence image coverage of the background should be close to, if not the same as, the user's work coverage of the background. And, the user's work coverage of the refrence should be very high.

This method does have the limitation of waiting to give the user feedback until they are done, but also gives us the advantage of allowing users to make mistakes and correct themselves without being penelized, as well as giving them feedback on a rough measure on how readable their writing is.
