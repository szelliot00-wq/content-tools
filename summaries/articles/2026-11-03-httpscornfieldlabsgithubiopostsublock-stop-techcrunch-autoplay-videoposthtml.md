# uBlock Origin filter to block autoplay videos in TechCrunch

Source: https://cornfieldlabs.github.io/posts/ublock-stop-techcrunch-autoplay-video/post.html

## Summary
This is a short technical post from the "cornfieldlabs" blog sharing a custom uBlock Origin filter list to block autoplay videos on TechCrunch. It provides specific filter rules targeting the JW Player and Connatix ad/video scripts that TechCrunch uses, along with CSS selectors to hide the embedded player elements.

## Key takeaways
- TechCrunch uses JW Player (via `jwplatform.com` and `jwpcdn.com`) and Connatix for autoplay video embeds.
- The filter blocks the player scripts at the network level, preventing them from loading entirely.
- Two cosmetic filters (`##`) hide the player container elements from the page layout.
- The rules are scoped to `domain=techcrunch.com` so they won't affect other sites.