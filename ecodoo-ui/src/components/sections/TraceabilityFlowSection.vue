<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
import FadeIn from '../motion/FadeIn.vue'

const steps = [
  ['Source', 'PO-2026-0418', 'Purchase · 2,400 L diesel'],
  ['Factor', 'SYNTHETIC-FUEL-2026 v1', '2.512 kgCO₂e / L'],
  ['Calculation', '2,400 × 2.512', '6,028.80 kgCO₂e'],
  ['Goal', 'Fleet intensity FY26', 'Counts toward Q2 baseline'],
  ['Report', 'Management ESG summary', 'Trace link retained'],
]
</script>
<template>
  <section id="traceability" class="overflow-hidden bg-navy py-24 text-white sm:py-32">
    <PageContainer>
      <SectionHeading
        tone="inverse"
        title="One evidence trail, from transaction to report"
        description="Every result retains the source, quantity, unit, factor version, formula, calculation time, and destination needed to reproduce it."
      />
      <FadeIn class="mt-14">
        <p class="mb-5 text-sm font-semibold text-white/80">
          Synthetic illustrative demo data — not a published emissions factor
        </p>
        <ol class="evidence-ribbon" aria-label="Transaction to report evidence flow">
          <li v-for="(step, index) in steps" :key="step[0]" class="evidence-step">
            <span class="text-sm font-semibold text-teal-light"
              >{{ index + 1 }} · {{ step[0] }}</span
            >
            <strong class="mt-3 block text-base font-semibold text-white">{{ step[1] }}</strong>
            <code class="mt-2 block text-sm leading-6 text-white/75">{{ step[2] }}</code>
          </li>
        </ol>
      </FadeIn>
      <div
        class="mt-14 grid overflow-hidden rounded-xl bg-white text-navy lg:grid-cols-[0.85fr_1.15fr]"
      >
        <div class="bg-mist p-6 sm:p-8">
          <div class="flex items-center justify-between border-b border-navy/15 pb-5">
            <div>
              <p class="text-sm text-muted">Odoo Purchase</p>
              <h3 class="mt-1 text-xl font-semibold">Fuel delivery</h3>
            </div>
            <span class="rounded-full bg-green/15 px-3 py-1 text-sm font-semibold text-green-ink"
              >Approved</span
            >
          </div>
          <dl class="mt-6 grid gap-5 text-sm sm:grid-cols-2">
            <div>
              <dt class="text-muted">Record</dt>
              <dd class="mt-1 font-mono">PO-2026-0418</dd>
            </div>
            <div>
              <dt class="text-muted">Company</dt>
              <dd class="mt-1 font-medium">Ecodoo Demo Ltd</dd>
            </div>
            <div>
              <dt class="text-muted">Quantity</dt>
              <dd class="mt-1 font-mono">2,400 L</dd>
            </div>
            <div>
              <dt class="text-muted">Recorded</dt>
              <dd class="mt-1 font-mono">18 Apr 2026</dd>
            </div>
          </dl>
        </div>
        <div class="p-6 sm:p-8">
          <p class="text-sm font-semibold text-teal">Calculation evidence</p>
          <div class="mt-5 flex flex-wrap items-baseline gap-x-3 gap-y-2 font-mono text-lg">
            <span>2,400 L</span><span aria-hidden="true" class="text-muted">×</span>
            <span>2.512 kgCO₂e/L</span><span aria-hidden="true" class="text-muted">=</span>
            <strong class="text-2xl leading-tight text-navy"
              >6,028.80 kgCO₂e illustrative result</strong
            >
          </div>
          <dl class="mt-8 divide-y divide-navy/10 border-y border-navy/10 text-sm">
            <div class="min-w-0 py-3 sm:flex sm:justify-between sm:gap-4">
              <dt class="text-muted">Factor version</dt>
              <dd class="mt-1 min-w-0 break-words font-mono sm:mt-0">SYNTHETIC-FUEL-2026 · v1</dd>
            </div>
            <div class="min-w-0 py-3 sm:flex sm:justify-between sm:gap-4">
              <dt class="text-muted">Calculated</dt>
              <dd class="mt-1 min-w-0 break-words font-mono sm:mt-0">18 Apr 2026 · 14:32 UTC</dd>
            </div>
            <div class="min-w-0 py-3 sm:flex sm:justify-between sm:gap-4">
              <dt class="text-muted">Correction history</dt>
              <dd class="font-medium">No corrections</dd>
            </div>
          </dl>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
