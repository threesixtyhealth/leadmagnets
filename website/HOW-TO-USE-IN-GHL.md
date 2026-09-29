# Three Sixty Health Website: GHL Build Guide

This folder holds the Three Sixty Health homepage as paste-in code for GoHighLevel. It's built to turn visitors into booked discovery calls. Most sections are a single code block. The two photo areas (hero and About Ash) use GHL's own Image elements, so you can upload and swap photos in the builder without touching code. Open `full-page-preview.html` in your browser to see the whole page. The green dashed boxes there show where your GHL Image elements go.

The design uses the **Soft Earth** brand palette: Moss `#4A5D45`, Butter `#FFF6BF`, Lilac `#E6C8F2`, Linen `#F7F1E8`, Eucalyptus `#C5D1BC` and Terracotta `#D9774A` (buttons only), with Inter throughout.

## Quick option: paste the whole site in one go

`ghl-all-in-one.html` is the entire page in a single file, styles included.

1. Create a blank page, add a full-width section with **0 padding**, add one row and one column (also 0 padding), and drop in a **Custom Code** element.
2. Open `ghl-all-in-one.html`, copy everything, paste it into the Custom Code element and save.
3. Find and replace the placeholders in Step 4 below, plus `PASTE-HERO-PHOTO-URL-HERE` and `PASTE-ASH-PHOTO-URL-HERE` (upload two 4:5 photos to GHL Media and copy their URLs).
4. Clear the yellow tags (Step 5).

This is the fastest route. The trade-off is that photos and copy are edited in code rather than with GHL's visual editor. If you'd rather edit visually, use the section-by-section build below instead.

## Step 1: Global styles

Create a new Website (or Funnel) page and start from a blank page. Open the page's Settings, go to Tracking Code, and paste all of `ghl-blocks/00-global-styles.html` into the Header Code box. Every block depends on it. Add your Meta pixel and your SEO title and description while you're there.

Suggested SEO title: *Three Sixty Health | Functional Nutrition for Women*
Suggested description: *Tired, bloated or hormonal and told your bloods are normal? Functional blood analysis, personalised nutrition protocols and weekly 1:1 support with Ash.*

## Step 2: Build the sections in order

| File | Section | How to build it in GHL |
| --- | --- | --- |
| 01-header.html | Header + mobile "Book" button | Full-width section, 0 padding, one Custom Code element |
| 02-hero-TEXT.html | Hero | Photo section (see Step 3) |
| 03-sound-familiar.html | Sound familiar? (the problem) | Full-width section, 0 padding, one Custom Code element |
| 04-the-360-approach.html | The Three Sixty approach + comparison | Full-width section, 0 padding, one Custom Code element |
| 05-about-ash-TEXT.html | About Ash | Photo section (see Step 3) |
| 06-services.html | Ways to work together | Full-width section, 0 padding, one Custom Code element |
| 07-how-it-works.html | How it works (4 steps) | Full-width section, 0 padding, one Custom Code element |
| 08-outcomes-and-fit.html | What changes + This is for you if | Full-width section, 0 padding, one Custom Code element |
| 09-client-stories.html | Client stories | Full-width section, 0 padding, one Custom Code element |
| 10-faq.html | FAQ | Full-width section, 0 padding, one Custom Code element |
| 11-final-cta-and-footer.html | Final CTA, footer + disclaimer | Full-width section, 0 padding, one Custom Code element |

For the code-only sections, the spacing and backgrounds are built into the code, so set GHL's section and row padding to 0 or it will double up.

## Step 3: The two photo sections

These are the parts you can edit visually. GHL provides the background and spacing here, so these settings matter.

| Section | Section background | Section padding (desktop / mobile) | Row | Left column | Right column |
| --- | --- | --- | --- | --- | --- |
| 02 Hero | #4A5D45 | 112px top, 136px bottom / 84px both | 2 columns, 58% / 42%, vertically centred | Custom Code: 02-hero-TEXT.html | Image element: hero photo |
| 05 About Ash | #F7F1E8 | 128px top and bottom / 84px both | 2 columns, 42% / 58%, vertically centred | Image element: portrait of you | Custom Code: 05-about-ash-TEXT.html |

Set each row's max width to 1120px, with about 72px between the columns.

**Image element settings:** width 100%, border radius 20px, no border or shadow. Crop before uploading: 4:5 portrait (1200 × 1500px) for both. Add alt text to each one. Warm, natural-light lifestyle photos of you work best for a premium feel. To change a photo later, click it in the builder and upload a new one.

## Step 4: Swap in your links

| Placeholder | Replace with |
| --- | --- |
| PASTE-BOOKING-URL-HERE | Your GHL calendar / discovery call booking link (header, mobile button, hero, services, how it works, client stories, FAQ, final CTA) |
| PASTE-BLOOD-ANALYSIS-URL-HERE | Your blood analysis sales page or checkout (services card) |
| PASTE-LOGO-URL-HERE | Your logo's URL from GHL Media (header, final CTA). `assets/logo.png` is included here to upload |
| PASTE-PRIVACY-URL-HERE | Your privacy policy page (footer) |

## Step 5: Clear the yellow placeholders

Search the blocks for `class="tbc"` to find the small yellow tags and replace each one with your final wording:

- **Hero + services:** confirm the discovery call length (currently "20 minutes").
- **About Ash:** add 1–2 lines of your personal story and your qualification.
- **Services:** program length and investment for 1:1 coaching, and the blood analysis price.
- **Client stories:** the three quotes are **sample copy only**. Replace them with real client words (with their permission), and change "Client name" to a first name or initial. Don't publish the sample quotes.
- **FAQ:** how clients get blood tests done, online/in-person options, and pricing (or keep "discussed on your call").

## Editing copy later

All text sits in plain HTML inside each block. Change the words and keep the tags (`<p>`, `<h2>`, `<em>`) in place. The coloured italic accent words in each headline sit inside `<em>`. Styles are scoped under a `tsh` class, so they won't clash with the rest of your site. Menu links jump to each section by its `id` (`#approach`, `#services`, `#about`, `#stories`, `#faq`). Preview on your phone before publishing.

## Updating the preview

After editing any block, run `python3 website/build-preview.py` to rebuild `full-page-preview.html`.
