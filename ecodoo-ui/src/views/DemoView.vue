<script setup lang="ts">
import PageContainer from '../components/layout/PageContainer.vue'
import BaseButton from '../components/ui/BaseButton.vue'
</script>
<template>
  <main class="min-h-screen bg-mist py-10 sm:py-14">
    <PageContainer>
      <nav class="flex flex-wrap items-center justify-between gap-4" aria-label="Demo navigation">
        <RouterLink to="/" class="inline-flex min-h-11 items-center font-semibold text-teal"
          >← Ecodoo home</RouterLink
        >
        <BaseButton href="/#traceability" variant="secondary" size="compact"
          >Evidence trail</BaseButton
        >
      </nav>

      <section class="mt-10 grid gap-8 lg:grid-cols-[0.8fr_1.2fr]">
        <div>
          <p class="text-sm font-semibold text-teal">Synthetic demo</p>
          <h1 class="mt-4 max-w-[14ch] text-4xl font-semibold sm:text-5xl">
            Trace an approved purchase to its ESG result.
          </h1>
          <p class="mt-5 max-w-[65ch] text-lg leading-8 text-ink">
            This walkthrough uses illustrative data to show the product shape: source record, factor
            version, calculation evidence, target impact, and reporting limits.
          </p>
          <p class="mt-4 max-w-[65ch] leading-7 text-muted">
            It is not a regulatory, audit, or carbon-neutrality certification.
          </p>
        </div>

        <div class="overflow-hidden rounded-xl bg-white text-navy">
          <div
            class="flex flex-wrap items-center justify-between gap-3 bg-navy px-5 py-4 text-white"
          >
            <div>
              <p class="font-semibold">Purchase record</p>
              <p class="mt-1 text-sm text-white/75">PO-2026-0418 · Fuel delivery</p>
            </div>
            <span class="rounded-full bg-green/15 px-3 py-1 text-sm font-semibold text-teal-light"
              >Approved</span
            >
          </div>

          <div class="grid gap-px bg-navy/10 sm:grid-cols-3">
            <div
              v-for="item in [
                ['Source quantity', '2,400 L diesel'],
                ['Factor version', 'SYNTHETIC-FUEL-2026 · v1'],
                ['Calculated result', '6,028.80 kgCO₂e'],
              ]"
              :key="item[0]"
              class="bg-white p-5"
            >
              <p class="text-sm text-muted">{{ item[0] }}</p>
              <p class="mt-2 font-mono text-base font-semibold text-navy">{{ item[1] }}</p>
            </div>
          </div>

          <dl class="divide-y divide-navy/10 px-5 py-2">
            <div
              v-for="item in [
                ['Conversion path', 'litres diesel × kgCO₂e per litre'],
                ['Calculation time', '18 Apr 2026 · 14:32 UTC'],
                ['Goal impact', 'Counts toward Fleet intensity FY26 baseline'],
                ['Report treatment', 'Displayed as an estimate with provenance retained'],
              ]"
              :key="item[0]"
              class="grid gap-2 py-4 text-sm sm:grid-cols-[11rem_1fr]"
            >
              <dt class="font-semibold text-navy">{{ item[0] }}</dt>
              <dd class="text-muted">{{ item[1] }}</dd>
            </div>
          </dl>
        </div>
      </section>
    </PageContainer>
  </main>
</template>
