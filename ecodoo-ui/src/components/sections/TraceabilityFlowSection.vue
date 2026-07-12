<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import FadeIn from '../motion/FadeIn.vue'

const evidenceLedgerGraphic = '/graphics/evidence-ledger.webp'

const steps = [
  {
    num: '01',
    label: 'Source',
    title: 'PO-2026-0418',
    detail: 'Purchase · 2,400 L diesel',
    icon: '📥',
  },
  {
    num: '02',
    label: 'Factor',
    title: 'SYNTHETIC-FUEL-2026 v1',
    detail: '2.512 kgCO₂e / L',
    icon: '⚗️',
  },
  {
    num: '03',
    label: 'Calculation',
    title: '2,400 × 2.512',
    detail: '6,028.80 kgCO₂e',
    icon: '🧮',
  },
  {
    num: '04',
    label: 'Goal',
    title: 'Fleet intensity FY26',
    detail: 'Counts toward Q2 baseline',
    icon: '🎯',
  },
  {
    num: '05',
    label: 'Report',
    title: 'Management ESG summary',
    detail: 'Trace link retained',
    icon: '📊',
  },
]
</script>

<template>
  <section
    id="traceability"
    class="relative overflow-hidden bg-[#0a1628] py-24 text-white sm:py-32"
  >
    <!-- Background orb -->
    <div class="pointer-events-none absolute inset-0" aria-hidden="true">
      <div
        class="absolute left-1/2 top-0 h-[600px] w-[600px] -translate-x-1/2 -translate-y-1/2 rounded-full opacity-10"
        style="background: radial-gradient(circle, #00c9b1 0%, transparent 65%)"
      ></div>
    </div>

    <PageContainer class="relative">
      <!-- Header -->
      <div class="max-w-3xl">
        <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">Evidence Trail</p>
        <h2 class="text-3xl font-bold text-white sm:text-5xl">
          One evidence trail, from transaction to report.
        </h2>
        <p class="mt-5 text-base leading-7 text-white/60">
          Every result retains the source, quantity, unit, factor version, formula, calculation
          time, and destination needed to reproduce it — without exception.
        </p>
      </div>

      <figure class="mt-10 overflow-hidden rounded-xl bg-navy-mid">
        <img
          :src="evidenceLedgerGraphic"
          alt="An operational record, measurement instrument, and calculation receipt connected as one evidence trail"
          width="1200"
          height="800"
          class="max-h-[30rem] w-full object-cover"
          loading="lazy"
          decoding="async"
        />
        <figcaption class="px-5 py-3 text-sm text-white/70">
          The evidence starts with the operational record—not a disconnected sustainability
          spreadsheet.
        </figcaption>
      </figure>

      <!-- Steps Flow -->
      <FadeIn class="mt-16">
        <p class="mb-6 text-xs font-medium text-white/40">
          Synthetic illustrative demo data — not a published emissions factor
        </p>

        <!-- Steps Grid -->
        <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
          <div
            v-for="(step, index) in steps"
            :key="step.label"
            class="group relative overflow-hidden rounded-2xl border border-white/10 bg-white/5 p-5 backdrop-blur-sm transition-all duration-300 hover:border-teal/30 hover:bg-white/8"
          >
            <!-- Number -->
            <span class="text-xs font-bold text-teal/60">{{ step.num }}</span>
            <!-- Label -->
            <p class="mt-2 text-xs font-semibold uppercase tracking-widest text-teal">
              {{ step.label }}
            </p>
            <!-- Title -->
            <p class="mt-3 font-semibold text-white">{{ step.title }}</p>
            <!-- Detail -->
            <code class="mt-2 block text-xs leading-5 text-white/55">{{ step.detail }}</code>

            <!-- Connector Arrow (not on last) -->
            <div
              v-if="index < steps.length - 1"
              class="absolute -right-3 top-1/2 z-10 hidden -translate-y-1/2 lg:flex h-6 w-6 items-center justify-center rounded-full border border-teal/30 bg-[#0a1628] text-xs text-teal"
            >
              →
            </div>
          </div>
        </div>
      </FadeIn>

      <!-- Calculation Evidence Card -->
      <div class="mt-12 overflow-hidden rounded-2xl border border-white/10 bg-white shadow-2xl">
        <div class="grid lg:grid-cols-[0.85fr_1.15fr]">
          <!-- Left: Source record -->
          <div class="border-b border-[#0a1628]/10 bg-[#f0faf8] p-8 lg:border-b-0 lg:border-r">
            <div class="mb-6 flex items-start justify-between">
              <div>
                <p class="text-xs font-medium text-[#64748b]">Odoo Purchase</p>
                <h3 class="mt-1 text-xl font-bold text-[#0a1628]">Fuel delivery</h3>
              </div>
              <span
                class="rounded-full bg-green-100 px-3 py-1 text-xs font-semibold text-green-700"
              >
                Approved
              </span>
            </div>
            <dl class="grid gap-5 text-sm sm:grid-cols-2">
              <div
                v-for="field in [
                  ['Record', 'PO-2026-0418', true],
                  ['Company', 'Ecodoo Demo Ltd', false],
                  ['Quantity', '2,400 L', true],
                  ['Recorded', '18 Apr 2026', true],
                ]"
                :key="field[0]"
              >
                <dt class="text-xs font-medium text-[#94a3b8]">{{ field[0] }}</dt>
                <dd
                  class="mt-1"
                  :class="field[2] ? 'font-mono text-[#0a1628]' : 'font-medium text-[#0a1628]'"
                >
                  {{ field[1] }}
                </dd>
              </div>
            </dl>
          </div>

          <!-- Right: Calculation detail -->
          <div class="p-8">
            <p class="text-xs font-semibold uppercase tracking-widest text-teal">
              Calculation evidence
            </p>

            <div class="mt-5 flex flex-wrap items-baseline gap-x-3 gap-y-2 font-mono">
              <span class="text-lg text-[#0a1628]">2,400 L</span>
              <span class="text-[#94a3b8]" aria-hidden="true">×</span>
              <span class="text-lg text-[#0a1628]">2.512 kgCO₂e/L</span>
              <span class="text-[#94a3b8]" aria-hidden="true">=</span>
              <strong class="text-2xl font-black leading-tight text-teal"> 6,028.80 kgCO₂e </strong>
            </div>
            <p class="mt-1 text-xs text-[#94a3b8]">illustrative result</p>

            <dl class="mt-8 divide-y divide-[#0a1628]/8 border-y border-[#0a1628]/8 text-sm">
              <div
                v-for="item in [
                  ['Factor version', 'SYNTHETIC-FUEL-2026 · v1', true],
                  ['Calculated', '18 Apr 2026 · 14:32 UTC', true],
                  ['Correction history', 'No corrections', false],
                ]"
                :key="item[0]"
                class="flex flex-wrap justify-between gap-4 py-3"
              >
                <dt class="text-[#94a3b8]">{{ item[0] }}</dt>
                <dd :class="item[2] ? 'font-mono text-[#0a1628]' : 'font-medium text-green-600'">
                  {{ item[1] }}
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
