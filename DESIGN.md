---
name: Ecodoo
description: A calm, audit-ready interface for traceable ESG operations inside Odoo.
---

<!-- SEED: re-run $impeccable document once there's code to capture the actual tokens and components. -->

# Design System: Ecodoo

## 1. Overview

**Creative North Star: "The Evidence Ledger"**

Ecodoo is a calm, technical, regenerative operational workspace where every ESG result feels attributable, reviewable, and fit for a CFO's attention. It serves Odoo hackathon judges, implementation partners, SME founders, operations managers, finance controllers, and ESG leaders. It occupies the middle ground between Bloomberg-level density and Asana-style cheerfulness: restrained like Linear, editorially structured like Stripe, and clear like Apple's environmental reporting.

The interface uses generous spacing, disciplined hierarchy, and familiar Odoo interaction patterns. Environmental themes appear through measured teal accents and visible provenance, never decorative leaves, optimistic imagery, or generic green styling. Motion is restrained and responsive; it explains state and then disappears.

**Key Characteristics:**

- Audit-ready hierarchy with evidence one click from every material number.
- Restrained navy-led surfaces with deliberate pillar and semantic colors.
- Familiar, keyboard-reachable controls and progressively disclosed detail.
- Explicit units, factor versions, timestamps, approvals, and data-quality states.
- Calm density: enough information to decide, never a wall of widgets.

## 2. Colors

The palette is structured around deep navy and mist, with low-saturation accents assigned to stable product meanings.

### Primary

- **Measured Teal** ([to be resolved during implementation]): Primary actions, active calculation paths, selection, and the environmental pillar.
- **Ledger Navy** ([to be resolved during implementation]): Navigation, headings, audit panels, and structural emphasis.

### Secondary

- **Verified Green** ([to be resolved during implementation]): Positive progress, verified records, and on-track states; always paired with text or an icon.
- **Information Cobalt** ([to be resolved during implementation]): Informational states and the social pillar.

### Tertiary

- **Governance Gold** ([to be resolved during implementation]): Governance context, attention states, and restrained highlights; never a substitute for critical severity.
- **Critical Red** ([to be resolved during implementation]): Errors and critical severity only, always supported by text and an icon.

### Neutral

- **Quiet Mist** ([to be resolved during implementation]): Main canvas, quiet panels, and negative space.
- **Evidence Ink** ([to be resolved during implementation]): Body copy and dense operational data.
- **Muted Trace** ([to be resolved during implementation]): Secondary metadata, separators, and inactive controls while preserving WCAG AA contrast.

### Named Rules

**The Evidence, Not Decoration Rule.** Accent colors communicate action, pillar, or state. They never decorate empty space.

**The Paired State Rule.** Status is never communicated by color alone; pair hue with explicit text, an icon, or both.

**The No Greenwashing Rule.** Gradients, neon, pastel greenwashing, and decorative environmental imagery are prohibited.

## 3. Typography

**Display Font:** Inter or system sans (with `-apple-system`, BlinkMacSystemFont, `Segoe UI`, and Roboto fallbacks)
**Body Font:** Inter or system sans for product UI; Source Sans 3 for reports and long-form guidance
**Label/Mono Font:** IBM Plex Mono for formulas, units, factor versions, record IDs, and timestamps

**Character:** Clear, modern, and operational. Sophistication comes from spacing, consistent alignment, and honest hierarchy rather than decorative typography.

### Hierarchy

- **Display** (medium, 28–36px, tight but readable): Outcome-focused page headings and decisive report titles only.
- **Headline** (semibold, 22–28px, compact): Major dashboard regions and form groups.
- **Title** (semibold, 17–20px, compact): Panels, records, dialogs, and table groups.
- **Body** (regular, 15–16px, comfortable): Instructions, descriptions, and review content; prose is capped at 65–75 characters per line.
- **Label** (medium, 13–14px, normal case): Field labels, states, and metadata; mono is reserved for trace data rather than general interface copy.

### Named Rules

**The Outcome First Rule.** Headings name the decision or result, not internal ESG jargon.

**The Trace Type Rule.** Monospace identifies evidence artifacts; it never becomes the default interface voice.

## 4. Elevation

Ecodoo is flat by default. Depth comes from tonal surface changes, containment, and predictable layering rather than decorative shadows. Dialogs, menus, and temporary overlays may use restrained structural elevation once implementation defines the exact vocabulary.

### Named Rules

**The Structural Elevation Rule.** Elevation explains hierarchy or temporary overlap. Static cards do not float merely to look important.

**The Immediate Motion Rule.** State transitions last 200–300ms with restrained ease-in-out timing; reduced-motion preferences make them instant or use a simple crossfade.

## 5. Components

Components are not yet implemented. New UI must begin with native Odoo controls and views, then add custom Owl components only where interaction or visualization materially requires them.

### Buttons

- **Shape:** Familiar, compact, and consistent across screens; exact radius and spacing will be resolved during implementation.
- **Primary:** Measured teal, reserved for the single clearest next action in a region.
- **Hover / Focus:** Visible keyboard focus and a short state transition; no bounce, glow, or celebratory response.
- **Secondary / Ghost:** Navy or neutral treatments for supporting actions; destructive actions remain explicit and separate.

### Chips

- **Style:** Restrained status or filter labels with text plus an icon where state meaning matters.
- **State:** Selected and unselected treatments remain distinguishable without relying on hue alone.

### Cards / Containers

- **Corner Style:** Modestly curved, never pill-like or over-rounded.
- **Background:** Quiet mist and neutral surface layers establish grouping.
- **Shadow Strategy:** Flat at rest; refer to the Structural Elevation Rule.
- **Border:** Use only when it clarifies grouping or interaction, never as decorative side stripes.
- **Internal Padding:** Generous enough for scanning while preserving useful operational density.

### Inputs / Fields

- **Style:** Standard, labeled Odoo controls with clear boundaries and predictable affordances.
- **Focus:** High-contrast visible focus without layout shift.
- **Error / Disabled:** Explicit text, icon, and semantic state; disabled controls remain readable and explain unavailable actions when needed.

### Navigation

Use familiar Odoo navigation, breadcrumbs, tabs, and progressive drill-down. Active location is explicit, keyboard reachable, and stable across modules. Dense destinations may collapse structurally on narrow screens; typography does not scale fluidly.

### Evidence Trace

Every material ESG value exposes its source record, quantity and unit, conversion path, factor and version, calculation timestamp, approval state, and correction history through a consistent drill-down pattern.

## 6. Do's and Don'ts

### Do:

- **Do** make provenance, units, freshness, and approval state visible beside material ESG numbers.
- **Do** use navy and mist for structure, reserving accent color for actions, pillars, and semantic states.
- **Do** pair every color-coded status with text, an icon, or both.
- **Do** use restrained 200–300ms state transitions and honor reduced-motion preferences.
- **Do** favor native Odoo patterns, progressive disclosure, keyboard access, and clear empty, loading, error, partial-data, and permission-denied states.
- **Do** use honest chart labels, accessible legends, and direct drill-down from aggregates to evidence.

### Don't:

- **Don't** resemble a reskinned Odoo admin panel; keep hierarchy deliberate and ESG evidence legible.
- **Don't** reproduce Bloomberg Terminal / SAP GUI density, jargon-heavy screens, competing widgets, or expert-only complexity.
- **Don't** reproduce Salesforce / HubSpot dashboard clutter with twelve widgets fighting for attention.
- **Don't** use consumer "green" app imagery, cartoon leaves, generic sustainability photography, pastel greenwashing, gradients, or neon.
- **Don't** use purple SaaS gradients, generic green globes, hands holding saplings, leaf-covered dashboards, or greenwashing language.
- **Don't** use gamified fitness-app patterns such as public leaderboards, streak pressure, confetti, unicorns, or celebratory completion effects around ESG, compliance, or employee data.
- **Don't** borrow Asana's colorful project-view energy: pastel task cards and competing bright tags undermine audit credibility.
- **Don't** use crypto / Web3 dashboard language, animated tickers, glow, glassmorphism, or "moonshot" energy.
- **Don't** mimic consultant-style infographic PDFs with oversized circular charts, pastel gradients, or stock photography standing in for traceable data.
- **Don't** use decorative motion, auto-playing carousels, parallax, 3D flips, bounce or elastic easing, flashing, or transitions longer than 500ms.
- **Don't** use display fonts in controls, all-caps body copy, condensed faces, color-only meaning, decorative side stripes, gradient text, nested cards, or over-rounded containers.
- **Don't** autoplay audio or make video the only source of essential information.
