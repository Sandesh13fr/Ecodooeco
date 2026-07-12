# Ecodoo Frontend MVP Handoff

## Run

```bash
cd ecodoo-ui
npm install
npm run dev
```

Open `/app` for the judge-ready MVP surface. The landing page CTA routes there.

## Demo path

1. `/app` — Command Center
2. `/app/transactions` — carbon transaction and calculation trace
3. `/app/goals` — Logistics target status
4. `/app/challenges` and `/app/participation` — challenge and participation slice
5. `/app/policies` or `/app/issues` — governance slice
6. `/app/summary` — printable ESG summary

Append `?role=employee`, `?role=manager`, or `?role=executive` to show role-scoped presentation states.

## Demo/fallback data

The MVP uses deterministic local fallback data in `src/data/demoMvp.ts`. It includes:

- `120.000 L x 2.680000 kg CO2e/L = 321.600 kg CO2e`
- `DIESEL-DEMO v1.0`
- E/S/G/overall demonstration management scores
- one challenge, one badge, policy acknowledgement status, and two compliance issues

## Backend contract assumptions

No live API is wired in this pass. A future API adapter should map backend dashboard data into the same visible contract used by `src/data/demoMvp.ts` and keep server authorization authoritative.

## Validation

```bash
npm run lint
npm run test:unit -- --run
npm run build
```

All passed during handoff. Vitest prints jsdom `window.scrollTo()` warnings from router scrolling; the tests still pass.

## Limitations

- Fixtures only; live backend integration not verified.
- Print layout is CSS-supported but browser print preview was not manually checked.
- Screenshots were not captured in this environment.
- The ESG summary is for internal demo/management only, not assurance, certification, or proof of regulatory compliance.
