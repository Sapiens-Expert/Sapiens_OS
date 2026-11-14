# Brand and visual production standard

Sapiens OS was developed by **Vladislav (Vlad) Andreev**. © 2026 Vladislav Andreev. All rights reserved. See [RIGHTS.md](../RIGHTS.md). This page guides any AI or human creating a dashboard, report, document, chart, presentation, export or onboarding file from this repository.

## Choose the identity before designing

| Context | Visible name | Mark | Use |
| --- | --- | --- | --- |
| Framework, personal dashboard and method documentation | **Sapiens OS** | Approved O!Sapiens master-brand logo, with “Sapiens OS” as the product/method title | The method sits under the O!Sapiens brand. |
| O!Sapiens coaching, community, campaign or commercial material | **O!Sapiens** | Approved O!Sapiens logo | Public-facing master brand. Credit the framework separately when used. |
| A person's raw private data or machine-readable export | Descriptive file name; no logo required | None | Do not embed branding into portable health data. |

Write **Sapiens OS** with a space in all visible copy, headings, metadata and generated prose. Technical repository names, paths, CSV schema identifiers and URLs may retain their machine spelling. Use **O!Sapiens** exactly, including the exclamation mark. Do not redraw, recolor, stretch or substitute a logo. Do not invent a standalone Sapiens OS symbol. If the approved asset is unavailable in a target format, use the plain text name and flag the missing asset for review. Keep the two identities visibly related, without stacking multiple logos by default.

## Source-based visual tokens

The [Sapiens OS brand strategy](https://docs.google.com/document/d/1ex6aknCaSq0n1yVevhkyPCJ3vf-NgfET-3n9erpfTFw/edit) specifies the O!Sapiens master brand and these colors. Use CSS equivalents or matching document theme values:

| Token | Hex | Role |
| --- | --- | --- |
| O! Blue | `#191795` | Brand primary, headers, prominent actions |
| Soft Sand | `#EACEAC` | Warm accent / OS Foundation |
| Sage Green | `#D4E6D5` | Calm accent / OS Transformation |
| Near White | `#F0F0F0` | Background / OS Reboot |
| Dark Text | `#1A1A2E` | Body text |

The strategy names Montserrat Bold for headings, Montserrat Regular for body/UI, and Palatino for decorative product line names. Use licensed or locally installed fonts when available; otherwise a clear sans-serif fallback for UI and an ordinary serif fallback for decorative display. Do not require a network font for the private offline dashboard. Preserve legible contrast; brand colors are not a substitute for accessible status text. The dashboard's warning color is an accessibility utility, not an additional brand color.

## Logo and layout

The owner's [O!Sapiens asset folder](https://drive.google.com/drive/folders/18qLiK6mJDsizfn-BbfQsEU7ssSC5FJrN) contains original marks, wordmarks and brand reference PDFs. Approved files carried into this repository:

| Asset | Intended use |
| --- | --- |
| [`osapiens-grey-logo.png`](../assets/brand/osapiens-grey-logo.png) | Light wordmark on the dashboard's dark blue header. |
| [`osapiens-blue-logo.svg`](../assets/brand/osapiens-blue-logo.svg) | Blue wordmark on light backgrounds in vector-friendly reports, slides and web pages. |
| [`osapiens-beige-logo.svg`](../assets/brand/osapiens-beige-logo.svg) | Beige wordmark on suitably dark backgrounds, when contrast is adequate. |
| [`o-grey.svg`](../assets/brand/o-grey.svg), [`o-blue.svg`](../assets/brand/o-blue.svg), [`o-beige.svg`](../assets/brand/o-beige.svg), [`o-green.svg`](../assets/brand/o-green.svg) | Standalone O! mark for small spaces or product-line accents, with the brand named in nearby accessible text. |

These are existing owner-provided designs, not generated approximations. Keep their transparent backgrounds, aspect ratios and legibility; do not recolor paths. Check contrast against the final background. Do not use a pale beige or green mark on near-white solely because it is in the palette. The dashboard uses the grey full wordmark; a report on near-white can use the blue full wordmark. This repository does not contain an independent Sapiens OS logo, so pair an O!Sapiens mark with the visible **Sapiens OS** method title. Use alt text “O!Sapiens” for a full logo or “O!Sapiens mark” for the standalone mark; for an adjacent identical heading, use empty alt to avoid duplicate speech. For PDF and slides, use equivalent accessible text and include creator credit where the method is explained. Never use a third-party wearable logo without its brand permission.

Favor generous whitespace, a small number of meaningful charts, visible units and dates, text labels with every status, and tables or plain-language summaries alongside graphs. Support keyboard navigation, zoom, reduced motion, and readable exports. Avoid red/green-only alerts, visual shame, decorative biometric claims, and stock images that imply a universal body or ability.

## Production check for every generated artifact

1. State the intended audience and choose the identity above. Apply the approved mark only where an appropriate asset and contrast are available.
2. Use the five palette values and typography rules, then check text contrast and readable sizes in the actual output medium.
3. Put **Sapiens OS** in visible framework titles and credit Vladislav Andreev. Put the O!Sapiens logo on branded human-readable materials, not raw private exports.
4. Label sources, dates, missing data and uncertainty. Follow [DASHBOARD.md](DASHBOARD.md) and [SAFETY.md](SAFETY.md) for health interpretation.
5. Inspect the exported page or file at mobile/desktop or print size; verify that the logo, captions, focus order and contrast survive export.

The brand strategy is a source of identity guidance, not evidence that the framework or dashboard is clinically validated. Any future brand-book revision or approved logo variant should be incorporated here and traced to its source before replacing these assets.
