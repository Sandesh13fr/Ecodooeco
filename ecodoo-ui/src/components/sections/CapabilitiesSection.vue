<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'

const capabilities = [
  {
    title: 'Carbon transactions',
    desc: 'Create reproducible entries from Odoo activity and immutable factor versions.',
    icon: `<path d="M8 2a6 6 0 100 12A6 6 0 008 2zm0 2v6l4 2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`,
    gradient: 'from-teal/15 to-teal/5',
    border: 'border-teal/20',
    iconColor: 'text-teal',
  },
  {
    title: 'Goals and progress',
    desc: 'Connect each result to a baseline, target, owner, and period — visible at all times.',
    icon: `<path d="M3 10L7 6l3 3 3-5 3 2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M14 4v4h-4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`,
    gradient: 'from-green-500/15 to-green-500/5',
    border: 'border-green-500/20',
    iconColor: 'text-green-400',
  },
  {
    title: 'Governance workflow',
    desc: 'Assign policy acknowledgements, audits, findings, and corrective actions to owners.',
    icon: `<path d="M8 2L3 5v5c0 3.3 2.2 6.1 5 7 2.8-.9 5-3.7 5-7V5L8 2z" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`,
    gradient: 'from-yellow-500/15 to-yellow-500/5',
    border: 'border-yellow-500/20',
    iconColor: 'text-yellow-400',
  },
  {
    title: 'Management reports',
    desc: 'Produce clear summaries with estimates, provenance, and drill-down intact for disclosure.',
    icon: `<path d="M4 3h8v10H4z" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M6 6h4M6 8h4M6 10h2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>`,
    gradient: 'from-blue-500/15 to-blue-500/5',
    border: 'border-blue-500/20',
    iconColor: 'text-blue-400',
  },
]
</script>

<template>
  <section id="capabilities" class="relative overflow-hidden bg-white py-24 sm:py-32">
    <!-- Top gradient fade from dark section -->
    <div class="pointer-events-none absolute inset-x-0 top-0 h-32" style="background: linear-gradient(to bottom, #f0faf8, white)" aria-hidden="true"></div>

    <PageContainer class="relative">
      <div class="text-center">
        <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">Capabilities</p>
        <h2 class="text-3xl font-bold text-[#0a1628] sm:text-5xl">
          From evidence to the next decision.
        </h2>
        <p class="mx-auto mt-5 max-w-[65ch] text-base leading-7 text-[#64748b]">
          Ecodoo keeps measurement, management, and reporting connected without creating a
          parallel system outside Odoo.
        </p>
      </div>

      <!-- Capability Cards Grid -->
      <div class="mt-14 grid gap-6 md:grid-cols-2">
        <article
          v-for="(cap, i) in capabilities"
          :key="cap.title"
          class="group relative overflow-hidden rounded-2xl border p-8 transition-all duration-400 hover:-translate-y-1 hover:shadow-xl"
          :class="[`bg-gradient-to-br ${cap.gradient}`, cap.border]"
          :style="{ transitionDelay: `${i * 50}ms` }"
        >
          <!-- Icon -->
          <div
            class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-xl border bg-white shadow-sm"
            :class="[cap.border, cap.iconColor]"
          >
            <svg class="h-6 w-6" viewBox="0 0 16 16" v-html="cap.icon"></svg>
          </div>

          <h3 class="text-lg font-bold text-[#0a1628]">{{ cap.title }}</h3>
          <p class="mt-3 text-sm leading-6 text-[#64748b]">{{ cap.desc }}</p>

          <!-- Arrow on hover -->
          <div class="mt-5 flex items-center gap-1.5 text-sm font-semibold opacity-0 transition-opacity duration-300 group-hover:opacity-100" :class="cap.iconColor">
            Learn more
            <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 16 16" fill="none">
              <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </article>
      </div>

      <!-- Bottom CTA prompt -->
      <div class="mt-12 rounded-2xl border border-teal/20 bg-gradient-to-r from-teal/5 to-teal/10 p-8 text-center">
        <p class="text-sm font-medium text-[#64748b]">Ready to see how it all works in context?</p>
        <a
          href="/demo"
          class="mt-4 inline-flex items-center gap-2 rounded-xl bg-[#0a1628] px-6 py-3 text-sm font-semibold text-white transition-all hover:bg-navy-mid hover:shadow-lg active:scale-95"
        >
          Open the interactive demo
          <svg class="h-4 w-4" viewBox="0 0 16 16" fill="none">
            <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>
    </PageContainer>
  </section>
</template>
