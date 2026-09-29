"""Stitch the GHL blocks into full-page-preview.html so the whole site can be viewed in a browser.

Run from anywhere:  python3 website/build-preview.py
The grey boxes stand in for the GHL Image elements in the two photo sections.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
BLOCKS = ROOT / "ghl-blocks"


def block(name):
    return (BLOCKS / name).read_text()


def photo_box(label, ratio="4 / 5"):
    return (
        f'<div class="pv-photo" style="aspect-ratio:{ratio}">'
        f"<span>GHL Image element<br><b>{label}</b></span></div>"
    )


def photo_section(bg, pad_top, pad_bottom, left, right, cols):
    return f"""
<section class="pv-photo-sec" style="background:{bg};--pt:{pad_top}px;--pb:{pad_bottom}px">
  <div class="pv-row" style="grid-template-columns:{cols}">
    <div class="pv-col">{left}</div>
    <div class="pv-col">{right}</div>
  </div>
</section>"""


logo = base64.b64encode((ROOT / "assets" / "logo.png").read_bytes()).decode()

body = "\n".join(
    [
        block("01-header.html"),
        photo_section("#4A5D45", 112, 136, block("02-hero-TEXT.html"),
                      photo_box("Hero photo, 4:5 (1200 &times; 1500px)"), "58fr 42fr"),
        block("03-sound-familiar.html"),
        block("04-the-360-approach.html"),
        photo_section("#F7F1E8", 128, 128, photo_box("Portrait of Ash, 4:5 (1200 &times; 1500px)"),
                      block("05-about-ash-TEXT.html"), "42fr 58fr"),
        block("06-services.html"),
        block("07-how-it-works.html"),
        block("08-outcomes-and-fit.html"),
        block("09-client-stories.html"),
        block("10-faq.html"),
        block("11-final-cta-and-footer.html"),
    ]
)
body = body.replace("PASTE-LOGO-URL-HERE", f"data:image/png;base64,{logo}")
for placeholder in ("PASTE-BOOKING-URL-HERE", "PASTE-BLOOD-ANALYSIS-URL-HERE", "PASTE-PRIVACY-URL-HERE"):
    body = body.replace(placeholder, "#")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Three Sixty Health</title>
<meta name="description" content="Functional nutrition for women. Functional blood analysis, personalised protocols and weekly 1:1 support.">
{block("00-global-styles.html")}
<style>
body{{margin:0;background:#F7F1E8}}
/* Emulates GHL section/row/column settings for the photo sections */
.pv-photo-sec{{padding:var(--pt) 24px var(--pb)}}
.pv-row{{max-width:1120px;margin:0 auto;display:grid;gap:72px;align-items:center}}
.pv-photo{{width:100%;border-radius:20px;background:#C5D1BC;display:flex;align-items:center;justify-content:center;text-align:center;font:14px/1.5 Inter,Arial,sans-serif;color:#4A5D45;border:2px dashed rgba(74,93,69,.35)}}
@media (max-width:767px){{
  .pv-photo-sec{{padding:84px 20px}}
  .pv-row{{grid-template-columns:1fr!important;gap:44px}}
}}
</style>
</head>
<body>
{body}
</body>
</html>
"""

(ROOT / "full-page-preview.html").write_text(page)
print("Wrote", ROOT / "full-page-preview.html")


# All-in-one version: paste into ONE GHL Custom Code element (full-width section, 0 padding).
# Photos become <img> tags pointing at PASTE-HERO-PHOTO-URL-HERE / PASTE-ASH-PHOTO-URL-HERE.
def photo_img(url, alt):
    return f'<img class="tsh-photo" src="{url}" alt="{alt}">'


def code_photo_section(bg, left, right, cols, cls):
    return f"""
<div class="tsh"><section class="tsh-photo-sec {cls}" style="background:{bg}">
  <div class="tsh-photo-row" style="grid-template-columns:{cols}">
    <div>{left}</div>
    <div>{right}</div>
  </div>
</section></div>"""


single_css = """<style>
.tsh-photo-sec{padding:112px 24px 136px}
.tsh-photo-sec.tsh-about-sec{padding:128px 24px}
.tsh-photo-row{max-width:1120px;margin:0 auto;display:grid;gap:72px;align-items:center}
.tsh-photo{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:20px;background:#C5D1BC}
@media (max-width:767px){
  .tsh-photo-sec,.tsh-photo-sec.tsh-about-sec{padding:84px 20px}
  .tsh-photo-row{grid-template-columns:1fr!important;gap:44px}
}
</style>"""

single = "\n".join(
    [
        "<!-- Three Sixty Health website: ALL-IN-ONE. Paste into one Custom Code element. -->",
        block("00-global-styles.html"),
        single_css,
        block("01-header.html"),
        code_photo_section("#4A5D45", block("02-hero-TEXT.html"),
                           photo_img("PASTE-HERO-PHOTO-URL-HERE", "Ash, functional nutritionist"),
                           "58fr 42fr", ""),
        block("03-sound-familiar.html"),
        block("04-the-360-approach.html"),
        code_photo_section("#F7F1E8",
                           photo_img("PASTE-ASH-PHOTO-URL-HERE", "Portrait of Ash"),
                           block("05-about-ash-TEXT.html"), "42fr 58fr", "tsh-about-sec"),
        block("06-services.html"),
        block("07-how-it-works.html"),
        block("08-outcomes-and-fit.html"),
        block("09-client-stories.html"),
        block("10-faq.html"),
        block("11-final-cta-and-footer.html"),
    ]
)
(ROOT / "ghl-all-in-one.html").write_text(single)
print("Wrote", ROOT / "ghl-all-in-one.html")
