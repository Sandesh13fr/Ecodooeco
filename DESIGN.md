---
name: Ecodoo
description: A calm, light-first command center for traceable ESG operations inside Odoo.
colors:
  ledger-navy: "#0A1628"
  structural-navy: "#123044"
  measured-teal: "#00C9B1"
  measured-teal-hover: "#009B88"
  verified-green: "#22C55E"
  information-cobalt: "#3B82F6"
  governance-gold: "#F59E0B"
  governance-ink: "#92400E"
  quiet-mist: "#F0FAF8"
  canvas: "#FFFFFF"
  evidence-ink: "#1E293B"
  muted-trace: "#64748B"
  critical-red: "#EF4444"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "28px"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.4
rounded:
  control: "8px"
  panel: "12px"
  feature: "16px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.measured-teal}"
    textColor: "{colors.ledger-navy}"
    rounded: "{rounded.control}"
    padding: "10px 20px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.measured-teal-hover}"
    textColor: "{colors.ledger-navy}"
    rounded: "{rounded.control}"
    padding: "10px 20px"
    height: "44px"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ledger-navy}"
    rounded: "{rounded.control}"
    padding: "10px 20px"
    height: "44px"
  panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.evidence-ink}"
    rounded: "{rounded.panel}"
    padding: "24px"
  field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.evidence-ink}"
    rounded: "{rounded.control}"
    padding: "10px 12px"
    height: "44px"
---

# Design System: Ecodoo

## 1. Overview

**Creative North Star: "The Evidence Ledger"**

Ecodoo is a light-first ESG command center where every important number feels attributable, reviewable, and ready for a serious operating decision. It serves ESG managers, employees, and executives who must understand carbon transactions, goals, challenges, governance issues, and reports quickly without losing the evidence behind them.

The visual system is clean, premium, calm, trustworthy, and modern. White and quiet-mist surfaces create working clarity; ledger navy establishes hierarchy; measured teal marks the next action and active evidence path. The interface must never depend on dark mode, glass effects, generic admin density, fake eco imagery, or decorative charts to feel sophisticated.

**Key Characteristics:**

- Light-first operational surfaces with disciplined, readable hierarchy.
- Evidence one click from every material ESG number.
- Restrained accent color used for action, selection, and meaning.
- Familiar, keyboard-reachable controls with explicit states and generous touch targets.
- Calm density: enough information to decide, never a wall of widgets.

## 2. Colors

The palette uses canvas and quiet mist for the working environment, ledger navy for structure, and measured teal as a scarce operational accent.

### Primary

- **Measured Teal:** Primary actions, current selection, active evidence paths, and the environmental pillar. It is never a decorative wash.
- **Ledger Navy:** Headings, navigation, high-emphasis data, and structural anchors on light surfaces.

### Secondary

- **Verified Green:** Verified, resolved, and on-track states; always paired with text or an icon.
- **Information Cobalt:** Informational states and the social pillar when teal would imply an action.

### Tertiary

- **Governance Gold:** Governance context and attention states; never a substitute for critical severity.
- **Critical Red:** Errors and critical severity only, always supported by explicit language and an icon.

### Neutral

- **Canvas:** The default application background and primary content surface.
- **Quiet Mist:** Secondary panels, table grouping, selected neutral rows, and empty-state structure.
- **Evidence Ink:** Body copy and operational data.
- **Muted Trace:** Secondary metadata, timestamps, dividers, and inactive controls while preserving WCAG AA contrast.

### Named Rules

**The Light Workspace Rule.** Product surfaces use canvas or quiet mist. Full-page dark mode is prohibited.

**The Evidence, Not Decoration Rule.** Accent colors communicate action, pillar, or state. They never decorate empty space and should occupy less than 10% of a routine product screen.

**The Paired State Rule.** Status is never communicated by color alone; pair hue with explicit text, an icon, or both.

## 3. Typography

**Display Font:** System sans with Segoe UI fallback
**Body Font:** System sans with Segoe UI fallback
**Label/Mono Font:** System monospace for formulas, units, factor versions, record IDs, and timestamps only

**Character:** Clear, modern, and operational. Sophistication comes from spacing, alignment, and honest hierarchy rather than decorative type.

### Hierarchy

- **Display** (700, 36px, 1.15): Outcome-focused page headings and executive report titles only.
- **Headline** (650, 28px, 1.2): Major dashboard regions and decisive form groups.
- **Title** (600, 20px, 1.3): Panels, records, dialogs, and table groups.
- **Body** (400, 16px, 1.6): Instructions, descriptions, and review content; prose is capped at 65–75 characters per line.
- **Label** (600, 14px, 1.4, normal case): Field labels, states, and metadata. Tiny uppercase tracking is prohibited as a default hierarchy device.

### Named Rules

**The Outcome First Rule.** Headings name the decision or result, not internal ESG jargon.

**The Trace Type Rule.** Monospace identifies evidence artifacts; it never becomes the default interface voice.

## 4. Elevation

Ecodoo is flat by default. Depth comes from canvas-to-mist tonal changes, borders that clarify interaction, and predictable layering. Static panels do not float. Menus, dialogs, and temporary overlays may use one restrained structural shadow with no glow or blur-heavy glass treatment.

### Shadow Vocabulary

- **Temporary overlay** (`0 4px 8px rgba(10, 22, 40, 0.12)`): Menus, dialogs, and popovers only.

### Named Rules

**The Structural Elevation Rule.** Elevation explains hierarchy or temporary overlap. Static cards never receive decorative shadows.

**The No Glass Rule.** Backdrop blur, translucent glass cards, glow, and frosted navigation are prohibited.

**The Immediate Motion Rule.** State transitions last 150–250ms, communicate a change, and become instant when reduced motion is requested.

## 5. Components

### Buttons

- **Shape:** Compact, familiar controls with gently curved corners (8px) and a minimum height of 44px.
- **Primary:** Measured teal with ledger-navy text, reserved for the single clearest next action in a region. This pairing preserves AA contrast at routine control sizes.
- **Hover / Focus:** Darken to the measured-teal hover token while retaining ledger-navy text; show a visible 2px ledger-navy focus outline without layout shift. No glow, bounce, or scale choreography.
- **Secondary / Ghost:** Canvas or transparent surface with ledger-navy text and a quiet structural border.

### Chips

- **Style:** Restrained status or filter labels with 8px corners, explicit text, and an icon where state meaning matters.
- **State:** Selected and unselected treatments remain distinguishable without relying on hue alone.

### Cards / Containers

- **Corner Style:** Modestly curved panels (12px); feature regions may use 16px. Pills are reserved for compact tags and controls.
- **Background:** Canvas and quiet mist establish grouping.
- **Shadow Strategy:** Flat at rest; refer to the Structural Elevation Rule.
- **Border:** Use only when it clarifies grouping or interaction, never as a decorative side stripe.
- **Internal Padding:** 16–24px for routine panels; 32px only for decisive report or empty-state regions.

### Inputs / Fields

- **Style:** Labeled, 44px minimum-height controls with a clear boundary, canvas background, evidence-ink text, and 8px corners.
- **Focus:** High-contrast 2px measured-teal outline without layout shift.
- **Error / Disabled:** Explicit text, icon, and semantic state; disabled controls remain readable and explain unavailable actions when needed.

### Navigation

Use familiar Odoo navigation, breadcrumbs, tabs, and progressive drill-down on light surfaces. Active location is explicit, keyboard reachable, and stable across modules. Mobile navigation collapses structurally; labels and touch targets stay readable.

### Evidence Trace

Every material ESG value exposes its source record, quantity and unit, conversion path, factor and version, calculation timestamp, approval state, and correction history through one consistent drill-down pattern. Graphics clarify this lineage; they never replace the underlying text or data.

## 6. Do's and Don'ts

### Do:

- **Do** make provenance, units, freshness, and approval state visible beside material ESG numbers.
- **Do** use canvas and quiet mist for the working environment, reserving measured teal for actions, selection, and evidence paths.
- **Do** pair every color-coded status with text, an icon, or both.
- **Do** use restrained 150–250ms state transitions and honor reduced-motion preferences.
- **Do** preserve native Odoo patterns, progressive disclosure, keyboard access, and clear loading, empty, error, partial-data, and permission-denied states.
- **Do** use charts only when they answer an operational question, with honest labels, accessible legends, and direct drill-down to evidence.

### Don't:

- **Don't** resemble a generic or reskinned Odoo admin template; hierarchy and ESG evidence must remain deliberate.
- **Don't** use dark mode or navy as the full-page working canvas.
- **Don't** use glassmorphism, backdrop blur, translucent glass cards, glow, or frosted navigation.
- **Don't** reproduce Bloomberg Terminal / SAP GUI density, jargon-heavy screens, or competing widgets.
- **Don't** reproduce Salesforce / HubSpot dashboard clutter with twelve widgets fighting for attention.
- **Don't** use consumer “green” app imagery, cartoon leaves, generic sustainability photography, fake eco imagery, pastel greenwashing, or excessive green.
- **Don't** use purple SaaS gradients, generic green globes, hands holding saplings, leaf-covered dashboards, or greenwashing language.
- **Don't** use playful SaaS illustrations, public leaderboards, streak pressure, confetti, or celebratory effects around ESG, compliance, or employee data.
- **Don't** use crypto / Web3 dashboard language, animated tickers, neon, or “moonshot” energy.
- **Don't** use decorative charts, oversized circular charts, or consultant-style infographic panels in place of traceable data.
- **Don't** use decorative motion, auto-playing carousels, parallax, 3D flips, bounce, elastic easing, flashing, or transitions longer than 500ms.
- **Don't** use tiny text, display fonts in controls, all-caps body copy, color-only meaning, decorative side stripes, gradient text, nested cards, or over-rounded containers.
- **Don't** autoplay audio or make video the only source of essential information.
