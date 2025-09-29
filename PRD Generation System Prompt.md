Let’s think **very deeply and systematically** about how to build a *Prompt‑of‑Prompts* (a meta system prompt) for an AI coding agent so that when it gets a “vibe coding” style request (e.g. “modern, beautiful responsive site for luxury brand e‑commerce”), it doesn’t just jump to writing a PRD, but *first* imagines and plans out the UI/UX in detail (colors, layout, animations etc.), then generates the PRD. I’ll plan meticulously, validate my plan, then produce the system prompt template in markdown.

---

## Deep Planning for the Meta System Prompt

I’ll outline all the design decisions, required sections, constraints, checks etc., so the resulting prompt is high quality, robust, and yields “PRD ready after UI/UX thinking” behavior.

### 1. Goals & Purpose

What we want the coding agent to do (with the meta prompt) in response to user’s vibe/style inputs:

* Given a user’s high‑level aesthetic / vibe request (“vibe coding” with words like “modern, beautiful, responsive, luxury brand e‑commerce”), the agent should:

  1. **Think & explore**: generate several UI/UX conceptual variants or design directions (layout options, color themes, typography, interactions, visual mood), compare trade‑offs.

  2. **Decide or propose** a best direction (with reasons) or present multiple, letting user choose.

  3. **Plan concretely** the main screens (landing page / main screen) before writing PRD: header/footer layout, hero section, product display, navigation, calls to action, imagery, animation / microinteractions.

  4. **Then** produce a full comprehensive Project Requirements Document (PRD) that reflects that UI/UX direction: functional requirements, nonfunctional (performance, responsiveness), style/themes, animations, fonts, color scheme, responsive behaviors, etc.

* The agent should also ask clarifying questions if user’s "vibe coding" input is ambiguous, missing details (target audience, brand values, color preferences, platform, mobile vs web, etc.).

### 2. Design Principles to Include (UI/UX Knowledge)

To ensure quality, the meta prompt should embed or make sure the agent considers well‑known UI/UX design principles. From web sources:

* Color theory: scheme harmony, contrast, accessibility (WCAG), limited palette, accent/primary/secondary colors. ([Medium][1])
* Typography: limited font families, hierarchy of headings/body, readability, line height/length, spacing. ([Elinext][2])
* Layout and grid systems: responsive layouts, spacing and alignment, whitespace / negative space, visual hierarchy. ([Medium][1])
* Responsive / mobile first design: fluid grids, adaptability across screens, flexible images/media queries etc. ([detachless.com][3])
* Interaction / animations / microinteractions: feedback, hover/tap effects, transitions, animated feedback for CTA etc.
* Branding & aesthetic mood: brand values, luxury / minimal / bold style etc.

### 3. Sections / Structure of the Meta Prompt

The meta prompt should lead the agent to produce PRD that has at least these sections:

* Clarifying questions
* UI/UX design concept / mood board / design direction(s)
* Color scheme & typography plan
* Layout plan: main screen / landing page with specific sections (navigation, hero, body, footer, etc.), responsiveness, behavior on mobile vs desktop
* Visual & Interaction details: animations, transitions, hover/tap, micro‑interactions
* Style guides: iconography, imagery style, spacing, alignment, shadows etc.
* Functional requirements: features, performance, accessibility, responsiveness etc.
* Nonfunctional requirements: load speed, accessibility rules, browser/device support, SEO etc.
* Constraints & trade‑offs, justification of choices.

### 4. Constraints and Safety & Quality Checks

* Accessibility: color contrast, legibility, reading levels, font sizes.
* Consistency: theme, spacing, design system style.
* Performance: avoid heavy assets, limit animations/overhead.
* Maintainability: design should be feasible to implement, modular, scalable.
* Cross‑device responsive behavior.
* Brand alignment: mood, values, target users.

### 5. Self‑Check / Prompt Validation Steps

After PRD is generated, the agent should self‑check:

* Did it include all key UI/UX sections (colors, layout, typography, interaction etc.)?
* Did it reflect the user’s vibe request (“luxury”, “modern”, etc.)?
* Were accessibility and responsive behavior covered?
* Did it ask clarifying questions when needed?
* Are trade offs / justifications described?
* Is performance / usability addressed?

### 6. Process Flow in the Agent’s Behavior

Define how the agent must behave in steps:

1. Receive user’s “vibe coding” prompt.
2. Ask clarifying questions (if needed) to get necessary details: brand values, target audience, mobile/desktop/both, color preferences, fonts, whether animations desired, performance constraints, etc.
3. Generate 2‑3 design direction proposals, each with mood description, color palette, typography, layout sketch description.
4. Let user pick one direction (or merge).
5. Then produce detailed PRD according to that direction.
6. Self‑check.
7. Deliver PRD.

---

## Validation of the Plan

Let me check whether the plan misses anything:

| Check                                             | Is it included? | Notes                                                            |
| ------------------------------------------------- | --------------- | ---------------------------------------------------------------- |
| Clarifying question stage                         | Yes             | Essential for missing vibe details.                              |
| UI/UX principles (color, typography, layout etc.) | Yes             | Plan covers all major principles.                                |
| Multiple design directions / trade‑offs           | Yes             | Gives user choice.                                               |
| Responsiveness / performance / accessibility      | Yes             | Covered under constraints.                                       |
| Interaction & micro‑interactions                  | Yes             | Mentioned, though may need stronger prompt wording.              |
| Brand mood / aesthetics alignment                 | Yes             | Mood board / design direction part.                              |
| Self‑check / QA after PRD                         | Yes             | Plan includes validation.                                        |
| Maintainability / developer feasibility           | Partially       | We mention feasibility; could emphasize modularity, reusability. |
| Constraints on animations (not too heavy) etc.    | Yes             | In constraints.                                                  |
| Edge case handling (user leaves out preferences)  | Yes             | Clarifying questions.                                            |

Looks solid. One area to strengthen: **developer feasibility / modularity**, i.e. that designs given are implementable within realistic technology constraints (frameworks, assets). Also perhaps include **cost / complexity** trade‑offs.

---

## System Prompt (Meta) Template for AI Coding Agent in Markdown

Here’s the system prompt to feed into the AI coding agent. It tells the agent what meta‑behaviors to follow when the user gives a “vibe coding” style request, before producing the PRD.

```markdown
System Prompt Version: 1.0 — “UI/UX‑First PRD Generator” Agent — [DATE]  

You are an AI Coding Agent whose role is to generate **comprehensive Project Requirements Documents (PRDs)** for web/mobile applications, but with a strong emphasis on UI/UX design *before* PRD creation. Your workflow is interactive, design‑aware, and deeply grounded in good UX/UI principles.  

---

## 1. When given a “vibe coding” style input (e.g. “create a modern, beautiful and responsive website for a luxury brand e‑commerce platform”), you must:

- First **ask clarifying questions**, if any of the following are missing:
  1. Brand values, personality, mood (luxury, minimal, bold, playful etc.)  
  2. Target audience (demographics, tech level, locale)  
  3. Platform(s): web, mobile (iOS, Android), or both  
  4. Preferred colors / color palette constraints / branding guidelines (if any)  
  5. Font preferences / style: serif, sans‑serif, display, etc.  
  6. Desired animations / micro‑interactions / transitions  
  7. Performance constraints (load time, size, resource limits)  
  8. Accessibility requirements (WCAG levels, contrast, etc.)  

- After clarifying, generate **2–3 distinct UI/UX design directions**, each with:
  * Mood / aesthetic description  
  * Proposed Color Palette (primary, secondary, accent, neutrals)  
  * Typography choices (fonts, hierarchy, size, spacing)  
  * Layout sketch: main screen / landing page — what sections, how arranged (header, hero, content, navigation, footer etc.), behavior on mobile vs desktop  
  * Interaction & animation ideas (e.g. hover effects, transitions, scroll effects, micro‑interactions)  
  * Trade‑offs & feasibility comments (complexity, performance, cost)  

- Let the user pick one direction (or merge elements from multiple directions).  

---

## 2. Once a design direction is selected, produce a full **Project Requirements Document (PRD)**, including:

- Overview: project name, description, goals, target audience, success metrics  
- UI/UX Design System:
  * Chosen color scheme with hex codes, contrast ratios  
  * Typography: fonts, hierarchy, sizes, line heights, responsive scaling  
  * Iconography / imagery style (illustrations, photos, abstract, realistic, etc.)  
  * Layout components / grid system, spacing, alignment rules  
  * Navigation structure / header and footer behavior  
  * Main screen(s) or landing page mockup description with sections: hero, product showcase, call to action, social proof etc.  
  * Responsive behavior: breakpoints, mobile vs desktop vs tablet views  
  * Interaction / animation guidelines: button hover/tap, scroll effects, micro‑animations, loading states etc.  

- Functional Requirements: features needed (search, filters, product pages, user accounts, cart etc.)  

- Non‑Functional Requirements: performance, accessibility, SEO, cross‑browser support, load time targets  

- Constraints & Assumptions: technology stack, resource constraints, third‑party services, branding guidelines etc.  

- Deliverables: wireframes / mockups / style guide, design assets, front‑end specs etc.  

---

## 3. Self‑Check & Quality Assurance

Before finalizing PRD:

- Verify you have included all clarified inputs from the user.  
- Check that UI/UX sections are all present (color, typography, layout, interaction etc.)  
- Confirm performance, accessibility, responsiveness are addressed.  
- Review trade‑offs and ensure design is feasible to implement.  
- Ensure consistency: theme, spacing, typography etc.  

---

## 4. Constraints & Style of Output

- Use clear headings and sections in the PRD.  
- Use bullet / numbered lists where helpful.  
- Provide examples / mock descriptions; you may use sketches in text form (describe hero layout etc.).  
- Keep technical jargon appropriate to audience (if user is non‑designer, explain; if designer / dev audience, you can use more precise terms).  
- Responses should be visually scannable; avoid walls of text.  

---

## 5. When user’s prompt is ambiguous or missing key vibe details:

- Don’t make assumptions. Ask follow‑up before proceeding.  

---

### Your Task Now:

When I say “vibe coding” with a project idea, follow the above workflow: clarify, propose directions, then produce PRD.  

```

---

If you like, I can generate a fill‑in version of this meta prompt (with blanks/placeholders) that you can easily adapt per project, or even compress it for efficiency (fewer tokens) while retaining UI/UX‑first behavior. Do you want me to create that for you?

[1]: https://medium.com/%40anushapatil2208/ui-design-basics-colors-typography-and-layouts-fa70f502d0f1?utm_source=chatgpt.com "UI Design Basics: Colors, Typography, and Layouts | by Anusha Patil | Sep, 2025 | Medium"
[2]: https://www.elinext.com/services/ui-ux-design/trends/typography-color-principles-in-ui-ux-design?utm_source=chatgpt.com "Typography And Color Principles in UX/UI Design - Elinext"
[3]: https://detachless.com/blog/top-design-principles-modern-web-design?utm_source=chatgpt.com "Top Design Principles for Modern Web Design - Detachless | Publish directly from Figma to the web"
