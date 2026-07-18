# Regressive JPEGs

Source: https://maurycyz.com/projects/bad_jpeg/

## Summary
The article explores a technique for embedding multiple images (or even a short video) inside a single progressive JPEG file by exploiting the multi-scan structure of the format. Progressive JPEGs load low-frequency data first, then refine quality in subsequent scans — and with careful manipulation, later scans can overwrite earlier rendered image data, creating a switching or animation effect. The author walks through the technical details of JPEG scans, DCT bins, and color channels, then demonstrates practical tricks including a cat photo that switches between two images and a "video" of a walking cat, all encoded as one JPEG file.

## Key takeaways
- Progressive JPEGs store image data across multiple "scans," each adding detail (DC then AC frequency components), which normally allows low-resolution previews before full download completes.
- By concatenating multiple JPEGs and stripping certain markers (start-of-image, start-of-frame, end-of-image), later scans can overwrite already-rendered image data, making a single file visually switch between images as it loads.
- To maximize frames, using DC-only scans (no AC data) is the most compact option; this results in 1/16th resolution previews per frame but avoids ghosting artifacts.
- Chrome handles around 90 frames before stopping; most browsers tolerate a 90-scan image, making ~90 frames the practical limit for broad compatibility.
- Color data (Cb/Cr chrominance channels) is stored at half resolution in YCbCr space, so full color data weighs roughly half as much as luminance — explaining why color scans can come before luminance scans without violating quality priorities.
- Playback timing cannot be controlled (no metadata for that exists in the format), so the "animation" speed depends entirely on network delay, making this a curiosity rather than a practical video format.
- The technique enables novelties like pure-HTML "video" using `<dialog>` tags and even interactive single-page apps with no CSS or JavaScript.